import sublime
import sublime_plugin
import os
import re

###
# Note: The original version of this plugin can be found at:
#     https://github.com/STealthy-and-haSTy/SublimeScraps/
#
# This version may not be up to date with any enhancements or changes that may
# have been made since this version was forked for use in this repository.
#
# Plugin by: Terence Martin <https://github.com/OdatNurd>
#            Keith Hall <https://github.com/keith-hall>
###


st_ver = int(sublime.version())
HandlerBase = sublime_plugin.ListInputHandler if st_ver >= 3154 else object


def _syntax_name(syntax_res):
    syntax_file = os.path.basename(syntax_res)
    name, ext = os.path.splitext(syntax_file)

    if ext == '.sublime-syntax':
        contents = sublime.load_resource(syntax_res)
        # read the name from the YAML - not worth having a dependency on a full YAML parser for this...
        match = re.search(r'^name:\s+([^\r\n]+|\'[^\']+\')$', contents, re.MULTILINE)
        if match:
            name = match.group(1)

    return name


class SyntaxListInputHandler(HandlerBase):
    """
    Input handler for the syntax argument of the scratch_buffer command; allows
    for the selection of one of the available syntaxes.
    """
    def name(self):
        return "syntax"

    def placeholder(self):
        return "Buffer Syntax"

    def parse(self, langs, resource_spec):
        for syntax in sublime.find_resources(resource_spec):
            langs[_syntax_name(syntax)] = syntax

    def preview(self, value):
        return sublime.Html("<strong>{}</strong>: <em>{}</em>".format(
            value.split("/")[1],
            os.path.basename(value)))

    def list_items(self):
        langs = {}

        self.parse(langs, "*.tmLanguage")
        self.parse(langs, "*.sublime-syntax")

        return [(syntax, langs[syntax]) for syntax in sorted(langs.keys())]


class ScratchBufferCommand(sublime_plugin.WindowCommand):
    """
    Create a scratch view with the provided syntax already set. If syntax is
    None, you get prompted to select a syntax first.
    """
    def run(self, syntax=None):
        if syntax is None:
            return self.query_syntax()

        view = self.window.new_file()
        view.set_name("Scratch: {}".format(_syntax_name(syntax)))

        view.set_scratch(True)
        view.assign_syntax(syntax)
        view.settings().set("is_temp_scratch", True)

    def input(self, args):
        if args.get("syntax", None) is None:
            return SyntaxListInputHandler()

    def input_description(self):
        return "Scratch Buffer"

    def query_syntax(self):
        items = [list(val) for val in SyntaxListInputHandler().list_items()]

        def pick(idx):
            if idx != -1:
                syntax = items[idx][1]
                self.window.run_command("scratch_buffer", {"syntax": syntax})

        self.window.show_quick_panel(
            items,
            on_select=lambda idx: pick(idx))


class ScratchBufferListener(sublime_plugin.EventListener):
    """
    When a scratch buffer is saved, turn off the scratch setting so that further
    changes do not get lost on accidental close.
    """
    def on_post_save(self, view):
        if view.is_scratch() and view.settings().get("is_temp_scratch", True):
            view.set_scratch(False)

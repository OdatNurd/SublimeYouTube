import sublime
import sublime_plugin

import re

_tag_line_regex = r"^[ \t]*((#\w+)\s*){1,}"
_tag_regex = r"#\w+"


def _find_tags(view):
    tags = set()
    tag_lines = view.find_all(_tag_line_regex)

    for region in tag_lines:
        line = view.substr(region)
        tags.update(re.findall(_tag_regex, line))

    if not tags:
        sublime.status_message("This file contains no tags!")

    return list(sorted(tags))


class TagToTopCommand(sublime_plugin.TextCommand):
    def run(self, edit, tag=None):
        if tag is None:
            return self.prompt_tag()

        tag_lines = self.view.find_all(_tag_line_regex)
        matched = []
        eof = sublime.Region(self.view.size())

        for idx, line in enumerate(tag_lines):
            end = tag_lines[idx + 1] if idx + 1 < len(tag_lines) else eof
            if tag in re.findall(_tag_regex, self.view.substr(line)):
                matched.append(sublime.Region(line.a, end.a))

        # self.view.add_regions("tags", matched, "storage")
        text = []
        if matched:
            for region in reversed(matched):
                # grab the text of this region
                text.append(self.view.substr(region))

                # delete the contents of this region
                self.view.replace(edit, region, '')

            self.view.insert(edit, 0, ''.join(reversed(text)))

        else:
            sublime.status_message("'%s' not found in this file" % tag)

    def prompt_tag(self):
        items = _find_tags(self.view)

        def pick(idx):
            if idx != -1:
                self.view.run_command("tag_to_top", {"tag": items[idx]})

        self.view.window().show_quick_panel(
            items,
            lambda idx: pick(idx))


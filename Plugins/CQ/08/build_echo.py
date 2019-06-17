import sublime
import sublime_plugin

from json import dumps


class BuildEchoCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        view = self.window.create_output_panel("build echo")

        view.settings().set("line_numbers", False)
        view.settings().set("gutter", False)
        view.settings().set("scroll_past_end", False)

        view.run_command("append", {"characters": dumps(kwargs, indent=4)})
        self.window.run_command("show_panel", {"panel": "output.build echo"})

import sublime
import sublime_plugin


class ConfirmExecCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        caption = kwargs.pop("caption", "Start the Build?")

        variables = self.window.extract_variables()
        caption = sublime.expand_variables(caption, variables)

        kill = kwargs.get("kill", False)

        if kill or sublime.yes_no_cancel_dialog(caption) == sublime.DIALOG_YES:
            self.window.run_command("exec", kwargs)

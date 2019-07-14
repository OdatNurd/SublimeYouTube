import sublime
import sublime_plugin

from Default.exec import ExecCommand


class ConfirmExecCommand(ExecCommand):
    def run(self, **kwargs):
        caption = kwargs.pop("caption", "Run the Build?")

        variables = self.window.extract_variables()
        caption = sublime.expand_variables(caption, variables)

        kill = kwargs.get("kill", False)
        if kill:
            super().run(kill=True)
            sublime.message_dialog("Build Cancelled")
            return

        if sublime.yes_no_cancel_dialog(caption) == sublime.DIALOG_YES:
            super().run(**kwargs)

    def finish(self, proc):
        super().finish(proc)

        exit_code = proc.exit_code()
        if exit_code == 0 or exit_code is None:
            sublime.message_dialog("Build succeeded")
        else:
            sublime.message_dialog("Build failed with code %d" % exit_code)

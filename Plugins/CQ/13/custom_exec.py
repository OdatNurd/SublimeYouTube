import sublime
import sublime_plugin

import os
import tempfile

from Default.exec import ExecCommand


class OverridePanelExecCommand(ExecCommand):
    def run(self, **kwargs):
        settings = sublime.load_settings("Preferences.sublime-settings")
        show_panel = settings.get("show_panel_on_build")

        override = kwargs.pop("override_panel", False)

        if override:
            settings.set("show_panel_on_build", not show_panel)

        super().run(**kwargs)

        if override:
            settings.set("show_panel_on_build", show_panel)


class GrabSelectionExecCommand(ExecCommand):
    def run(self, **kwargs):
        variables = self.window.extract_variables()

        view = self.window.active_view()

        if not view.sel()[0].empty():
            variables["selection"] = view.substr(view.sel()[0])

        kwargs = sublime.expand_variables(kwargs, variables)

        super().run(**kwargs)

class ExecuteSelectionExecCommand(ExecCommand):
    def run(self, **kwargs):
        view = self.window.active_view()
        if view.sel()[0].empty():
            return self.window.status_message("Cannot build; no selection")

        self.tmp_file = self.get_selection(view)

        variables = {"selection": self.tmp_file}
        kwargs = sublime.expand_variables(kwargs, variables)

        super().run(**kwargs)

    def get_selection(self, view):
        handle, name = tempfile.mkstemp(text=True)
        handle = os.fdopen(handle, mode="wt", encoding="utf-8")

        handle.write(view.substr(view.sel()[0]))

        handle.close()
        return name

    def finish(self, proc):
        super().finish(proc)

        try:
            os.remove(self.tmp_file)
        finally:
            self.tmp_file = None

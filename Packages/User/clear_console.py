import sublime
import sublime_plugin


class ClearConsoleCommand(sublime_plugin.WindowCommand):
    def run(self):
        print("\n" * 100)

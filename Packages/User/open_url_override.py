import sublime, sublime_plugin, webbrowser

# There exists an open_url command already, but under Linux it seems to select
# the wrong browser.
class OpenUrlCommand(sublime_plugin.WindowCommand):
    def run(self, url):
        webbrowser.open_new_tab (url)

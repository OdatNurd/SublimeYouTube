import sublime
import sublime_plugin


def _find_tags(view):
    tags = set()

    for region in view.find_by_selector("entity.name.tag"):
        tags.add(view.substr(region))

    if not tags:
        sublime.status_message("This file contains no tags!")

    return list(sorted(tags))


class TagToTopCommand(sublime_plugin.TextCommand):
    def run(self, edit, tag=None):
        if tag is None:
            return self.prompt_tag()

        tag_lines = self.view.find_by_selector("meta.notes.tag_line")
        matched = []
        eof = sublime.Region(self.view.size())

        tag_regions = list(filter(lambda r: self.view.substr(r) == tag,
                           self.view.find_by_selector("entity.name.tag")))

        for idx, line in enumerate(tag_lines):
            end = tag_lines[idx + 1] if idx + 1 < len(tag_lines) else eof
            if any(line.contains(r) for r in tag_regions):
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

    def is_enabled(self, tag=None):
        return self.view.match_selector(0, "text.plain.notes")


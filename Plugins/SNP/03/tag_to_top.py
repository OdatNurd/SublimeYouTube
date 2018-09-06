import sublime
import sublime_plugin


def _find_tags(view):
    tags = set()

    for region in view.find_by_selector("entity.name.tag"):
        tags.add(view.substr(region))

    if not tags:
        sublime.status_message("This file contains no tags!")

    return list(sorted(tags))


def _tag_under_cursor(view):
    if len(view.sel()) == 1:
        if not view.sel()[0].empty():
            return view.substr(view.sel()[0])

        pt = view.sel()[0].begin()
        ex_class = sublime.CLASS_WORD_START | sublime.CLASS_WORD_END

        if view.match_selector(pt, "entity.name.tag"):
            tag_region = view.expand_by_class(pt, ex_class, " \t")
            return view.substr(tag_region).strip()

    return None


class TagToTopCommand(sublime_plugin.TextCommand):
    def run(self, edit, tag=None):
        tag = tag or _tag_under_cursor(self.view)
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

            top = tag_lines[0].begin()
            self.view.insert(edit, top, ''.join(reversed(text)))

            self.view.sel().clear()
            self.view.sel().add(sublime.Region(top))
            self.view.show(top)

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


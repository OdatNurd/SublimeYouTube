import sublime
import sublime_plugin

import textwrap
from Default.new_templates import reformat


class BuzzwordIpsumCommand(sublime_plugin.TextCommand):
    def __init__(self, view):
        super().__init__(view)
        self.index = -1

    def run(self, edit):
        # Get the last word of the line the cursor is on, then discard the word
        # "lorem" from the start, leaving the remainder
        point = self.view.sel()[0].b
        line = self.view.substr(self.view.line(point))
        word = line.split()[-1][5:]
        repeats = int(word if word != "" else "1")

        # Remove the trigger word
        self.view.replace(edit, sublime.Region(point, point - 5 - len(word)), "")


        for _ in range(repeats):
            self.view.run_command("insert", {"characters": self.text()})
            if _ + 1 < repeats:
                self.view.run_command("insert", {"characters": "\n\n"})


    def text(self):
        point = self.view.sel()[0].b
        col = self.view.rowcol(point)[1]
        width = next(iter(self.view.settings().get('rulers', [])), 72) - col

        self.index += 1
        if self.index == len(_paragraphs):
            self.index = 0

        return textwrap.fill(_paragraphs[self.index], 10 if width < 10 else width)


_paragraphs = [
    reformat("""
    Leverage agile frameworks to provide a robust synopsis for high level overviews.
    Iterative approaches to corporate strategy foster collaborative thinking to
    further the overall value proposition. Organically grow the holistic world view
    of disruptive innovation via workplace diversity and empowerment.
    """),

    reformat("""
    Bring to the table win-win survival strategies to ensure proactive domination.
    At the end of the day, going forward, a new normal that has evolved from
    generation X is on the runway heading towards a streamlined cloud solution. User
    generated content in real-time will have multiple touchpoints for offshoring.
    """),

    reformat("""
    Capitalize on low hanging fruit to identify a ballpark value added activity to
    beta test. Override the digital divide with additional clickthroughs from
    DevOps. Nanotechnology immersion along the information highway will close the
    loop on focusing solely on the bottom line.
    """),

    reformat("""
    Podcasting operational change management inside of workflows to establish a
    framework. Taking seamless key performance indicators offline to maximise the
    long tail. Keeping your eye on the ball while performing a deep dive on the
    start-up mentality to derive convergence on cross-platform integration.
    """),

    reformat("""
    Collaboratively administrate empowered markets via plug-and-play networks.
    Dynamically procrastinate B2C users after installed base benefits. Dramatically
    visualize customer directed convergence without revolutionary ROI.
    """)
]

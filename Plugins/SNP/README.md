Simple Notes Plugin
-------------------

The videos in this series are for illustrating a simple notes plugin, which is
itself based on the code in my answer on [this SO question][1].

The original asker uses Sublime Text to store notes which are marked up with
hash tags to indicate relative topics and wanted a plugin that could move all
of the notes tagged with a given tag to the top of the file for easier reading.

The first video in the series creates an initial plugin that does this, going
over the logical steps taken along the way. We then proceed into adding some
enhancements to the plugin as a vector for explaining how various plugin topics
work and how to integrate with Sublime.

The videos in this series are coded `"Live"`; they were streamed and posted
directly without any editing of any kind. This makes them both longer than a
video of this kind would usually be as well as a good "real world" example of
the top to bottom process of creating a plugin in Sublime.

* [01](01) \[[Video][2]]: The initial version of the plugin. This includes a
  simple syntax definition and a command that performs the core functionality
  of the plugin.

* [02](02) \[[Video][3]]: The plugin is enhanced to leverage the syntax for
  determining where the tags and tag lines are in favour of duplicating the
  regular expressions needed.

* [03](03) \[[Video][4]]: The usability of the plugin is enhanced by making it
  easier to navigate within a notes files and select the tags that are moved to
  the top.

* [04](04) \[[Video][5]]: We add our own simple auto completion facility to the
  plugin to make it easier to create a notes file from scratch.

* [05](05) \[[Video][6]]: We finish up our plugin by adding a settings file and
  converting it into a full package, complete with integration with Sublime to
  give a more professional appearance.


[1]: https://stackoverflow.com/questions/52060923/how-to-group-or-display-paragraphs-with-same-tag-with-sublime-text
[2]: https://youtu.be/KN-EJ5JQ_fk
[3]: https://youtu.be/_xhmN5-D_Ls
[4]: https://youtu.be/5ZZIssKXIcU
[5]: https://youtu.be/pNs92C6Y3iI
[6]: https://youtu.be/yTN-OLfYtHY

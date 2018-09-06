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

[1]: https://stackoverflow.com/questions/52060923/how-to-group-or-display-paragraphs-with-same-tag-with-sublime-text
[2]: https://youtu.be/KN-EJ5JQ_fk
[3]: https://youtu.be/_xhmN5-D_Ls

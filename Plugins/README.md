Sublime Plugin Code
-------------------

This directory contains the code and other related package resources for all
videos on the [YouTube channel](https://www.youtube.com/user/nurdz).

The directory structure is laid out similarly to the production codes that
you'll find in the title of each video, allowing you to easily find exactly the
files that go with a particular video.

For example, for the video title ***Sublime Text Plugin: [SNP01] Simple Notes
Plugin Part 1***, the production code is ***[SNP01]***, so the files related to
that particular video are in ***SNP/01***.

I've chosen to lay out the files in this manner rather than just changing them
as time goes on to make it easier to see the progression of the code as the
videos progress, particularly for those that want to pick and choose the videos
that they watch.

The code samples for videos will be added to the repository on the same day
that the video drops (or thereabouts).

### [Common Questions](CQ/)

The files in this folder associate with the various Common Questions videos on
the channel and generally relate to things like sample files that you may want
to play with without having to manually transcribe them yourself.

### [Simple Notes Plugin](SNP/)

This illustrates a simple notes plugin that works with a file which contains
paragraphs annotated with hash tags. A simple syntax is included to make the
tags visually distinct and a command is implemented that modifies the file by
allowing you to easily shift all paragraphs with a given tag to the top of the
file while maintaining their relative ordering.

This is an illustration on how one might modify the contents of the buffer,
including removing text, replacing text with other text and shifting the
location of text from one place to another.

The videos in this series are coded `"Live"`; that is, in one take with no
edits for content or brevity. As such they are longer than usual videos but
they provide a good real world example of slowly building up functionality a
step at a time in order to make the task more manageable.

> **Note:** The code for this plugin is based on code written for an answer
> on [this SO question][1], but through the video series the capabilities
> of the code are expanded beyond what is available in that answer.


[1]: https://stackoverflow.com/questions/52060923/how-to-group-or-display-paragraphs-with-same-tag-with-sublime-text
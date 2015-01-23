This application is build to create [Jekyll][0] posts from a [Ghost 0.5.8][1] export file.

It reads the JSON contents of the export file and creates posts and drafts for *Jekyll*. You can then move the files into your jekyll directory and generate your blog.

The post template is included in *import.py*, so if you need any special output, you have to modify the script. The template is using the datastructure of the JSON, there are only exceptions for the *isodate* and the *tags* variables.

[0]: http://jekyllrb.com/
[1]: https://ghost.org/


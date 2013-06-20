This is a pygments lexer for pry sessions.

### Installation

`pip install pry_lexer`

### Usage

Copy your pry session into your clipboard, then pygmentize it:

```
pygmentize <(xclip -o)  # linux
pygmentize <(pbpaste)   # mac
```

Or use a file called `*.pry`:

```
pygmentize session.pry
```

If it's not working, try specifying `pygmentize -l pry`, but that shouldn't be needed.

### Why?

Because I'm fed up of people syntax highlighting pry sessions as though they were ruby. 

#### Wrong:

![Alt text](http://jelzo.com/stuff/pry-before.png)

#### Right:

![Alt text](http://jelzo.com/stuff/pry-after.png)

Meta-fu
=======

Licensed under the MIT license (see LICENSE.MIT), bug-reports and pull-requests welcome.

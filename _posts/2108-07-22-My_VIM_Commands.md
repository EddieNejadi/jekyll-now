---
layout: post
title: My vim commands
date: 2018-07-22
category: note
tags: [vim]
summary: My vim commands, shortcuts 
---

## My useful vim commands

### Macro
#### Record a macro and run it
I like to make macro to add a new line `print("number n+1") to the following python code:
```
#! /usr/bin/env python
from __future__ import print_function

if __name__ == "__main__":
    print ("DONE!!!")
    print("number 1")
    print("number 2")

```
I start recording my macro with qa under normal mode in vim. q means to start recording and a is the name of macro. Then, I strok the following keys:
```
gg      # go to first line in the page 
G       # go to last line the page
:       # command 
?print("number # search from button up '''print("number'''
yy      # yank the current line
p       # paste it
$       # move the curser to end of the current line
hh      # move curser 2 char left
<Ctl>a  # plus one the current number
q       # end the macro recording
        #  ggG?print("number^Myyp$<80>kl<80>kl^A
```
To run this macro, I run @a which a is the name of macro. If I like to run it more, I run 10@a to execute the macro for 10 times and result is:
```
#! /usr/bin/env python
from __future__ import print_function

if __name__ == "__main__":
    print ("DONE!!!")
    print("number 1")
    print("number 2")
    print("number 3")
    print("number 4")
    print("number 5")
    print("number 6")
    print("number 7")
    print("number 8")
    print("number 9")
    print("number 10")
    print("number 11")
    print("number 12")
```

## Shorcuts
Grep all lines ended by 0:
```
:vimgrep /0$/ example.txt
:vimgrep/0$/%
```
Search and change with confirmation:
```
:%s/foo/bar/gci # Change each 'foo' (case insensitive due to the i flag) to 'bar'; ask for confirmation.
```
Map systemcall output
```
:map <c-j>d <c-r>=system('/tmp/x.py')<cr> # map system call out put
```
Execute current file
```
nnoremap <F9> :!%:p # execute the current file
```
Commands:
===

Basic
---
* pwd
* cd
* ls -- -a | -l | [path]

* less # read text file
* file # list file type

- cp
- mv
- rm
- mkdir

+ ln # link

- ls -a > io.sh # standard input # standard means no format, like in line etc.
- pwd >> io.sh # append input
- sort < io.sh # standard output 

- telnet | ssh # remote connect machine

Pipes
---
- ls -l | less
- ls -lt | head # display 10 newest files in current directory
- du | sort -nr # display directories and space
- find . type f -print | wc -l # display total numbers of files and subdirectories

Filter
---
- sort
- uniq # unique line
- grep # match pattern
- fmt # format
- pr # split to pages with page format
- head # first lines
- tail # last lines
- tr # translate characters
- sed # stream editor # more power than tr
- awk # programming language for constructing filters

- lpr # printing
cat poorly_formatted_report.txt | fmt | pr | lpr
cat unsorted_list_with_dupes.txt | sort | uniq | pr | lpr

- tar # .tar.gz/.tgz tar/gzip
tar tzvf name.tar.gz | less

Permissions
---
- chmod # modify file access rights
- su # superuser
- chown # file ownership
- chgrp # files group ownership

chomd 750 somefile.txt # - rwx r-x --- === - 111 101 000

chomd 654 dic/ # d rw- r-x r-- ===  d 110 101 100

- rwx = 111 in binary = 7
- rw- = 110 in binary = 6
- r-x = 101 in binary = 5
- r-- = 100 in binary = 4

- 777 755 700 666 644 600 # file settings
- 777 755 700 # directory settings

Jobs Control
---
- ps
- kill # 1 SIGHUP | 2 SIGINT | 15 SIGTERM | 9 SIGKILL
- jobs
- bg
- fg

$ xload &  $ jobs  $ kill %1  $ xload &  $ ps  $ kill pid



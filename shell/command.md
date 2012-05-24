Commands:
===
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

Pipes
---
- ls -l | less
- ls -lt | head # display 10 newest files in current directory
- du | sort -nr # display directories and space
- find . type f -print | wc -l # display total numbers of files and subdirectories

Filter
---


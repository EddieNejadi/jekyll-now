---
layout: post
title: My bash commands
permalink: note/My-Bash-Commands
date: 2020-12-13
category: note
tags: [linux, bash ]
summary: My bash commands, configuration, shortcuts and aliases
---

## My useful bash commands

### Bash history

Add the following configuration to ~/.bashrc

```bash
# Bash history setting
shopt -s histappend # add time stamp to history
HISTFILESIZE=1000000 # history file size
HISTSIZE=1000000 # number of history entry
HISTCONTROL=ignoreboth # ingnore  duplicate command 
HISTIGNORE='bg:fg:history' # ignore unimportant command
HISTTIMEFORMAT='%F %T ' # time stamp format
shopt -s cmdhist # save multiline commands to one line
PROMPT_COMMAND='history -a' # store history immediately 
```

### SSH

#### known host finger print error

```bash
# This option disables the prompt and automatically adds the host key to the ~/.ssh/known_hosts file
ssh -o "StrictHostKeyChecking=no" user@host
ssh -o "UserKnownHostsFile=/dev/null" -o "StrictHostKeyChecking=no" user@host # More extreme cases
```

Make sure that you check ~/.ssh/config file and **StrictHostKeyChecking=yes**

### Add your key to host

```bash
ssh-copy-id user@host
# Alternative  
cat ~/.ssh/id_rsa.pub | ssh hiq@HOSTNAME-HOSTIP -T "cat >> ~/.ssh/authorized_keys"
```

#### Git

##### ssh setting

add this configuration to your ~/.ssh/config file for have git ssh on port 443 (Enable ssh connection over https)

```config
Host github.com
  Hostname ssh.github.com
  Port 443
```

##### https credentials

Save git credentials:

```bash
cd <GIT_REPO>
git config --global credential.helper store
git pull
# Provide user name and password
```

To update or change password remove ~/.git-credentials

#### Sync file or directory

```bash
rsync -a source destination
```

"-a" is combination of options which equals -rlptgoD (no -H,-A,-X). It stands for archive, syncs recursively, preserves symbolic links, special, device files, modification times, group, owner, and permissions.

### USER

#### get full username

```bash
getent passwd username
```

## FILE

Make symbolic link

```bash
ln -s {target-filename} {symbolic-filename}
```

### GREP

Binary file -a

```bash
tail -f some.log | grep --line-buffered "MYERROR"  # On streams
```

### FIND

#### By name

-iname

#### By type

-type

#### By date

-time -min

### Network

chcek open port in tcp and udp

```bash
netstat -tupln
```

Check if connection is possible

```bash
nc -vz host_name port_number
# the package is missing try to install by yum install nmap
```

### COMMAND

#### Argument

!$ gets the last element of the previous command line argument

```bash
!^      # first argument
!$      # last argument
!*      # all arguments
!:2     # second argument

!:2-3   # second to third arguments
!:2-$   # second to last arguments
!:2*    # second to last arguments
!:2-    # second to next to last arguments
!:0     # command
```

### Date parser

There is need to have date parser

```bash
date "+%s" -d "FORMATTED LOG DATE" # convert Mon, 17 Oct 2016 11:18:42 to 1476695922 seconds
date "%s" # give up current time in second 
DURATION=$(expr date "+%s" - date "+%s" -d "FORMATTED LOG DATE") # give time elapse from now in second
```

### TEXT

#### Append test to file

```bash
sed -i '1itask goes here' text.txt # Added a line to first line a txt file
sed -i '1s/^/task goes here\n/' #  Added a line to first line a txt file
echo "last line" >> text.txt
```

### LINK

#### Softlink

modify a existing link

```bash
ln -s /location/to/link linkname
ln -s /location/to/link2 newlink
mv -T newlink linkname
```

### Xargs

#### List user open files

```bash
ps aux | grep bash | grep -v root | grep -v grep | grep $USER | tr -s ' ' | cut -d ' ' -f 2| xargs -I proc /bin/bash -c "lsof -p proc && echo 'lineeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'"
```

### CRONTAB

#### Manage crontab

you might consider mail alert by directing CMD output to /dev/null

```bash
# -------------- minute (0 - 59)
# |------------- hour (0 - 23)
# |  | --------- day of month (1 - 31)
# |  | | ------- month (1 - 12)
# |  | | | ----- day of week (0 - 6) (Sunday=0)
# |  | | | |
# *  * * * * command to be executed

# * * * * * CMD > /dev/null 2>&1 || true # Example of disable mail alert 
crontab -l # list the current user cronjobs
crontab -e # edit the current user cronjobs
```

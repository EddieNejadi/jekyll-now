---
layout: post
title: Introduction to Ansible
date: 2018-03-18
category: Dev
version: 1.1
tags: [ansible, devops, tool]
summary: A short introduction to Ansible for beginners
---

## INTRODUCTION TO ANSIBLE

## DEVOPS

[DevOps](https://en.wikipedia.org/wiki/DevOps) (a clipped compound of "development" and "operations") is a software engineering practice that aims at unifying software development (Dev) and software operation (Ops). The main characteristic of the DevOps movement is to strongly advocate automation and monitoring at all steps of software construction, from integration, testing, releasing to deployment and infrastructure management.
Devops is term that shows the development team should work with operation team to increase throughput. We need to facilitate and ease the process of development, integration, testing, and deployment in a way that all developers on dev team should be able to deploy their code hassle-free and regardless of environment.
There are some tools to automates such tasks like:

* Ansible (rely on python/ssh) backed by Readhat
* Puppet (written by Ruby)
* Chef (written by Ruby, Erlang)
* Salt (written by python)

I have chosen Ansible for my projects since:

1. no need to install any aget (based on python)
2. supported by Redhat
3. learning curve is lower than others

### Devopts is not only tools but to me is more mentality of working

* Be critic to the way working
* Ask questions
* Share your knowledge

## ANSIBLE

Working machine is the machine that we ran our ansible commands/playbooks (need to be a Linux machine)
On our development environment, we have Ansible installed on devapp01,devapp02, devgw01 (Preferably try to run it on devapp02)

### Set up

#### ssh key

```bash
ssh-keygen -t ecdsa -b 521 # Generate your ssh key default location ~/.shh/
ssh-copy-id user@host  # Add your key to One host in each environment (Dev, Test, Prod)
# Option 1: Add ssh agent to your terminal like
eval `ssh-agent` && ssh-add
# Option 2: Add the following function to your ~/.bashrc file and run each time you like
# I have borrowed this function from brilliant reply in stackoverflow.com
function assh { # Feel free to rename the functions
  export SSH_AUTH_SOCK=$(find /tmp/ssh-* -user `whoami` -name agent\* -printf '%T@ %p\n' 2>/dev/null | sort -k 1nr | sed 's/^[^ ]* //' | head -n 1)
  if ssh-add -l 2&>1 > /dev/null; then
    echo Found working SSH Agent:
    ssh-add -l
    return
  fi
  eval `ssh-agent` && ssh-add
} 
```

#### inventory

Simply a list of host that you want to work with in python ini format; occasionally is good idea to have specific list of host as your inventory. An example would be:

```ini
[devgateway]
devgw.example.com       ansible_user=root

[devbd]
devdb1.example.com      ansible_user=dba

[devapp]
devapp1.example.com     ansible_user=admin
devapp2.example.com     ansible_user=admin


[dev:children]
devgw.example.com
devdb.example.com
devapp.example.com

[sastest:vars]
myapp=/opt/myapp
```

#### ansible.cfg

Ansible configuration helper file which can be very useful to activate some Ansible features on the specified playbooks and set default inventory file location, etc.
Example is:

```ini
[defaults]
callback_whitelist = profile_tasks
inventory = hosts
```

### Ansible command line

User can use Ansible for redirecting their commands, queries, and etc to the respective machines and get their result. Example is:

```bash
ansible dev -m ping
ansible dev -m shell -a "date"
```

### Ansible playbook

Ansible playbook is list of commands and instruction to archive a specific goal. For example, a play book to deploy to test environment. Example is:

```yaml
- hosts: dev
  tasks:
    - name: Ping the host
      ping:

    - name: Get user name from shell
      shell: "whoami"
      args:
        executable: /bin/bash
      register: whoami_result

    - name: Print the whoami_result
      debug:
        msg: "{{ whoami_result.stdout }}"
```

***

#### Roles

Ansilbe role is set of task that can be ran to achieve a specific goal like install and configure apache server. So, Apache role would contains steps like install apache, modify apache configuration with roles default variables, and restart handler.

#### Handlers

Ansible handler is a set of actions that need to be played after specific change or action. For example, after a change in server configuration, we like to handler to restart web server; after that we like to update web application and then again we need to restart web server and so on. BY default, handlers will run at the end of play when they are triggered by 'notify' keyword.

#### Vars

List of necessary variables that will be used by Ansible playbooks, roles, and handlers.

#### Template

It simple template solution which is powered by python Jinja2. For example, a config file that need to be updated/overloaded with new variable.

### Writing Ansible playbook

***

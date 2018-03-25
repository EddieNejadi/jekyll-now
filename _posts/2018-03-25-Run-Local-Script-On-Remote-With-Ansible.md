---
layout: post
title: Ansible script module to run local script on remote machine
date: 2018-03-25
category: Dev
tags: [ansible, script, devops]
summary: Using Ansible script module to run local scripts on the remote machine
---

Running a script on a remove host is always a tedious job specially if user have to send the local to remote machine before executing it. Ansible script module is the tool to facilitate this task in secure and convenient way.

I have python script that I like to run on my production machine and here is the code:
{% gist EddieNejadi/e1f531cca5803e1a994a40c21b3e3942 sys_info.py %}
{% gist EddieNejadi/33cea03bfe960ddd5d1393e7b7b520ae Ansible_script_module.yml %}

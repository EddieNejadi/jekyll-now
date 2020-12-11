---
layout: post
title: Python Time out Function Call
date: 2017-07-22
category: Dev
tags: [python, multi-threading, timeout_call]
summary: Using multi-threading to have function call with time out
---

During writing python scripts, I have come to situation that I needed a function call with time out. So. I used python multi-threading library to do the job.

## Python multi-threading

{% gist EddieNejadi/e1f531cca5803e1a994a40c21b3e3942 my_timeout_function.py %}
---
layout: post
title: Log rotation in Linux
date: 2018-09-15
author: Mahdi Abdinejadi
category: Dev
tags: [linux, logging]
summary: Log rotation in Linux
---

### Log rotation in Linux

#### Configuration

- log rotation configuration is located on /etc/logrotate.d/
- configuration would be like:

```bash
###### Path to log files
/var/mytmp/logfiles/*post.log {
    weekly
    rotate 4
    missingok
    notifempty
    compress
    create 0660 MYUSER MYGROUP

}
```

- weekly, daily, monthly, yearly: logging rotation trigger time.
- rotate N: N number of rotation should be kept.
- size NK, NM, NG: on N size logging rotation will be triggered.
- compress/nocompress: will/willnot gzip the log files
- delaycompress:
- notifempty:
- missingok:
- create 0660 MYUSER MYGROUP:

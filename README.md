##Table of Contents##
- [A. Description](#a-description)
- [B. Installation](#b-installation)
    - [B.1. Prerequisites](#b1-prerequisites)
    - [B.2. Install](#b2-install)
- [C. Configuration](#c-configuration)
- [D. Running notifmail](#d-running-notifmail)
- [E. notifmail 'home' directory](#e-notifmail-home-directory)
    - [E.1. notifmail.conf](#e1-notifmailconf)
    - [E.2. notifmail.log](#e2-notifmaillog)
    - [E.3. notifmail.lock](#e3-notifmaillock)


A. Description
==============
notifmail is an email daemon checker which notifies system about new emails on
configured IMAP servers.


B. Installation
===============

B.1. Prerequisites
------------------
Have python and other prerequisites on host:

* python
* python-notify2
* openssl
* python-daemon

Example - Fedora:

    $ sudo yum install python openssl python-daemon python-pip
    $ sudo pip install notify2

Example - Ubuntu:

    $ sudo apt-get install python python-notify2 openssl python-daemon

B.2. Install
------------
    $ cd <notifmail git clone directory>
    $ sudo ./setup.py install


C. Configuration
================
notifmail uses a configuration for connection to IMAP server and for other
configurations. A sample file one is packaged in the sources as
"notifmail.conf.sample". To get started copy this file in ~/.notifmail:

    $ mkdir ~/.notifmail
    $ cp ./notifmail.conf.sample ~/.notifmail/notifmail.conf

Edit ~/.notifmail/notifmail.conf.sample with your configuration.


D. Running notifmail
====================

To start notifmail:

    $ notifmail

For more info about notifmail's command line parameters:

    $ notifmail -h

E. notifmail 'home' directory
==========================
notifmail's 'home' directory is located in $HOME/.notifmail and contains:

E.1. notifmail.conf
-------------------
This file contains the IMAP accounts configuration to be used by notifmail.
Can contain multiple accounts but each account must include:

* `imap_server`
* `imap_user`
* `imap_password`

There are two optional variables:

* `all`: Used to define mailboxes for which notifmail should trigger a
notification with every new email. Multiple mailboxes must be separated by
semicolon.
* `summary`: Used to define mailboxes for which notifmail should trigger one
summary notification. Multiple mailboxes must be separated by semicolon.
See C. Configuration also.

E.2. notifmail.log
------------------
This is the logging file. By default notifmail runs as daemon so all messages go
to this file. If you run daemon in foreground, log messages will be duplicated
between logfile and stdout. For more info run:

    $ notifmail -h

E.3. notifmail.lock
-------------------
This is a lock file to avoid having multiple notifmail instances.

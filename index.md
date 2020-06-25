---
layout: default
---

**ISPAPI Tool Documentation**

**Contents**
* TOC
{:toc}

# Introduction

This site provide documentation for the ispapicli tool. Here you will find documentation for installing on different operation systems, namely windows, mac, and ubuntu. 

In general, this tool consist of two major parts: Graphical User Interface (GUI) and Shell (or so-called command line interpreter).

# What Does This Tool Offer?

This tool enable you to connect to our back-end API and manage your account through GUI or Command Line Interface.


# Tool Features/Commands

This section provides you with a quick introduction to all the features included in this tool.

## Login/logout and session management

*   Login/logout management instead of sending your login credentials everytime you requrest a command
*   Each login session is valid for 60 minutes
*   Accessible from GUI and Shell

## Graphical User Interface

The graphical user interface has many features:

# How to use it?

Basically this tool can be used in two ways: The GUI and Shell

## Run it via Shell

Once you have the tool, you may run the following command:

```
(python) ispapi --help
```

This will show the following:

![Octocat](/assets/doc_img/help.png)

From this point on, you can follow the notes and run your desired command.
However, here are few important notes for you:

-   Note that you can either use the equal sign '=' e.g. --command = querydomainlist, or
-   You can use spaces as a separator e.g. --command querydomainlist 
-   You may also use shortcuts, e.g. -c instead of --command, refer to the tool help command for more information about other commands
-   You must login first in order to requrest a command, you can login by running the command:

```
    -u = <your user id> -p = <your password> -e = {ote,live}
```

## Run it via GUI

# Download and Installation

## Windows

## Mac OS

## Ubuntu

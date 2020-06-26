---
layout: default
---

**ISPAPI Tool Documentation**

**Contents**
* TOC
{:toc}

# Introduction

This site provide documentation for the ispapicli tool. Here you will find documentation for installing on different operation systems, namely windows, mac, and ubuntu. 

This tool enable you to connect to our back-end API and manage your account through GUI or Command Line Interface.

In general, this tool consist of two major parts: Graphical User Interface (GUI) and Shell (or so-called command line interpreter).

# Tool Features

This section provides you with a quick introduction to all the features included in this tool.

## Manage Your Account Remotely

* You can execute any command of the back-end API, for more info see: https://github.com/hexonet/hexonet-api-documentation

* Tip: for quick view of the command use the command: - -list

* To view how to use a specific command, run the command: - -help querydomainlist

## Login/logout and Session Management

* Login/logout management instead of sending your login credentials everytime you requrest a command
* Each login session is valid for 60 minutes
* Accessible from GUI and Shell

## Graphical User Interface

The graphical user interface has many features:

### Save the Command to a File

This feature enables you to save the command and the results into a text file.

### Command auto-complete

Once you start typing the command, a dropdown list will be displayed to show all possible matches.

### Minimum Parameters

Some commands requires a minimum number of parameters, this tool display all min parameters once you have typed a command. 

### Copy the Results

You can copy the command and the results using the shortcut ctr+c, or use the copy button in the GUI

# How to use it?

Basically this tool can be used in two ways: The GUI and Shell

## Run it via Shell

Once you have the tool, you can run it from your Shell.

First, you may run the following command from your Shell:

```
ispapi --help
```

This will show you how to use the tool:

![Octocat](/assets/doc_img/help.png)

From this point on, you can follow the notes and run your desired command.
However, here are few important notes for you:

-   Note that you can either use the equal sign "=" e.g. "- -command = querydomainlist", or
-   You can use spaces as a separator e.g. "- -command querydomainlist"
-   You may also use shortcuts, e.g. "-c" instead of "- -command", refer to the tool help command for more information about other commands
-   You must login first in order to requrest a command, you can login by running the command:

```
    -u = <your user id> -p = <your password> -e = {ote,live}
```

## Run it via GUI

There two ways to start the GUI:

1.  From the Shell, then run the command:

```
    ispapi -g OR ispapi --gui
```

2.  From the executable/portable file by simply openning it

# Download and Installation

There three options for donwload here:

*  Portable file

*  Executable file, must be installed via the wizzard

*  Download it from pypi using pip
    * You must have python ^3.8 
    * It is recommended that you create virtual environment and run the tool in it


## Windows

## Mac OS

## Ubuntu

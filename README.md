Utility Scripts
===============

This repository contains utility scripts to simplify development workflow and frequently repeated activities.

Feature Support
---------------

Currently available scripts
-   repo organizer

Installation
------------
Pre-requisites:
Python 3.7+ should be available as python3 at system level
``` {.sourceCode .bash}
$ which python3
This should point to system level python 3
$ pip3 install parse==1.11.1
```

To install scripts:

``` {.sourceCode .bash}
$ echo "export REPO_HOME=~/code" >> ~/.zshrc
$ mkdir -p $REPO_HOME/github.com/codespider/scripts
$ git clone https://github.com/codespider/scripts.git $REPO_HOME/github.com/codespider/scripts
$ make install
$ echo "alias rcd='cd \$(repo ls | fzf --height 10 --border)'\n" >> ~/.zshrc 

```

Usage
-----

To clone a new repo

``` {.sourceCode .bash}
$ repo clone <git url>
```

To list current repos

``` {.sourceCode .bash}
$ repo ls
```

To navigate to a repo

``` {.sourceCode .bash}
$ rcd
```


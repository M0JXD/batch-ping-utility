# Batch Ping Utility
A simple GUI python program to ping IP addresses.

## About

A friend of mine needed a way to ping a group of IP addresses easily to check some old equipment that operates over CAN. These pieces of equipment are notorious for "forgetting" their static IP, but usually respond to another if you can find it. <br />
Of course using Powershell/Bash is the usual solution, but I said I'd make him a little GUI utility to make his life that little bit easier.

## Usage guide

Fairly simple, enter the desired start and end IPv4 addresses and hit "Start". You can optionally set timeout, but leaving it blank will default it to 1 second. <br />
Any good pings will be recorded in the noted box. Current pings being tried (and failures as they occur) will be noted with the text area.

## Running the code

Install the latest Python if you don't have it (3.12). <br />
Note on Linux you may need to use "python3" instead of "python" in the commands.
Install ping3 and FreeSimpleGUI via pip:
```
python -m pip install ping3
python -m pip install FreeSimpleGUI
```

Then run. In most cases you can just double-click or right-click->execute the .pyw file from your file manager:

Alternatively from a Terminal:
Windows:
```
python .\batch_ping_util.pyw
```

*nix:
```
python ./batch_ping_util.pyw
```

This software originally used PySimpleGUI, however the license changes are unacceptable to me.
Please read more here: https://freesimplegui.readthedocs.io/en/latest/#background-why-freesimplegui-came-to-be
The program now uses the fork of the last LGPL version, FreeSimpleGUI.

Should it be installed, please run this to remove the old library please run:
```
python -m pip uninstall PySimpleGUI
```

## Creating an Executable

Install PyInstaller via pip:
```
pip install -U pyinstaller
```
Run from terminal/cmd/shell:
```
pyinstaller batch_ping_util.pyw -F
```
(The -F signifies to create an all-in-one executable, as opposed to a distribution with lots of library files etc.)

An executable is provided for Windows in releases. 
As most Linux distros have Python pre-installed, and it is only a small program, I see no point in making a 
binary for Linux.
I have no Apple devices so Mac users are on their own.

## Ideas For Improvement

Allow selection/specification of other ping options <br />
Clear button for output box <br />
Extra line for displaying previous fail as it goes by too quickly to read <br />
Check IPv6 compatibility <br />
More Theme Options <br />
Make an Icon

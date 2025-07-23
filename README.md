# Batch Ping Utility
A simple GUI python program to ping IP addresses.

## About

A friend of mine needed a way to ping a group of IP addresses easily to check some old equipment that operates over CAN. These pieces of equipment are notorious for "forgetting" their static IP, but may respond to another if you can find it. <br />
Of course using Powershell/Bash is the usual solution, but I said I'd make him a little GUI utility to make his life that little bit easier.

At the moment the Ping library does not seem to work on Windows.

## Usage guide

Fairly simple, enter the desired start and end IPv4 addresses and hit "Start". You can optionally set timeout, but leaving it blank will default it to 1 second. <br />
Any good pings will be recorded in the noted box. Current pings being tried (and failures as they occur) will be noted with the text area.

## Running the code

Install the latest Python if you don't have it (3.12). <br />

There is one dependency, ping3. On Windows, it's easiest to install via pip:
```
python -m pip install ping3
```
On linux, you might be able to find ping3 available as a system package. E.g. on Debian based distros the package is `python3-ping3`
Then the code should run. You may need to run as root (SHOCK! HORROR!) for the pings to work. 

Example run commands:  <br />
Windows:
```Powershell
python .\batch_ping_util.pyw
```

Linux:
```bash
python3 batch_ping_util.pyw
```

This software originally used PySimpleGUI, however the license changes were unacceptable to me. <br />
I initially ported to FreeSimpleGUI, but now have changed again to tkinter, which also provides the benefit of only needing one dependency, even if it's a bit uglier <br />
Please read more here: https://freesimplegui.readthedocs.io/en/latest/#background-why-freesimplegui-came-to-be <br />

Should it be installed, please remove the old library, e.g. on Windows:
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

An executable is provided for Windows in releases. <br />
As most Linux distros have Python pre-installed, and it is only a small program, there's little point making a 
binary for Linux. <br />
I have no Apple devices so Mac users are on their own.

## Ideas For Improvement

Allow selection/specification of other ping options <br />
Extra line for displaying previous fail as it goes by too quickly to read <br />
IPv6 compatibility <br />

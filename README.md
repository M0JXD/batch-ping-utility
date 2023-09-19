# Batch Ping Utility
A simple GUI python program to ping IP addresses.

## About

A friend of mine needed a way to ping a group of IP addresses easily to check some old equipment that operates over CAN. These pieces of equipment are notorious for "forgetting" their static IP, but usually respond to another if you can find it. <br />
Of course using Powershell/Bash is the usual solution but I said I'd make him a little GUI utility to make his life that little bit easier.

## Usage guide

Fairly simple, enter the desired start and end IPv4 addresses and hit "Start". You can optionally set timeout, but leaving it blank will default it to 1 second. <br />
Any good pings will be recorded in the noted box. Current pings being tried (and failures as they occur) will be noted with the text area.

## Running the code

Install the latest Python if you don't have it (3.11). <br />
Install ping3 and PySimpleGUI via pip.

## Creating an Executable

Install PyInstaller via pip. <br />
Using Terminal, Powershell or Command Prompt, change to the directory and run the command "pyinstaller batch_ping_util.pyw -F". <br />
(The -F signifies to create an all in one executable, as oppose to a distribution with lots of .dll files etc.)

## Ideas For Improvement

Allow selection/specification of other ping options <br />
Clear button for output box <br />
Extra line for displaying previous fail as it goes by too quickly to read <br />
Check IPv6 compatibility <br />
More Theme Options <br />
Make an Icon

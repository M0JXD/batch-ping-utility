# Simple GUI Batch Ping Utility
# 06/09/2023 Jamie Drinkell
# Free for any use, provided 'as is' with no guarantees or warranties etc.
# IPv4 Only
# Thanks to https://www.abstractapi.com/guides/validate-ip-address-python for the IP checker

from ping3 import ping
import PySimpleGUI as gui
import ipaddress

# Globals #
marker_mid_pings = False
start_address = ''
end_address = ''
old_address = ''
timeout = ''


def validate_ip_address(ip_string):
    try:
        ip_object = ipaddress.ip_address(ip_string)
        # window["-INFO-TEXT-"].update("The IP address " + ip_string + " is valid.")
        return True
    except ValueError:
        window["-INFO-TEXT-"].update("The address " + ip_string + " is not valid")
        return False


def calculate_next_address(address):
    if address == end_address:
        return "PING_END_ADDRESS"

    to_ping_by_parts = address.split('.')

    for y in range(3, 0, -1):
        if int(to_ping_by_parts[y]) >= 255:
            if y == 0:
                print("Can't go up from 255.255.255.255 !")
                return
            else:
                # This needs set to zero because we increment the higher part in the next loop
                to_ping_by_parts[y] = '0'
                continue

        else:
            to_ping_by_parts[y] = str(int(to_ping_by_parts[y]) + 1)
            break

    address_to_ping = '.'.join(str(e) for e in to_ping_by_parts)

    return address_to_ping


def do_ping(address, timeout):
    window["-INFO-TEXT-"].update("Pinging address " + str(address))
    window.Refresh()

    response = ping(address, timeout=timeout)

    if response is None or False:
        window["-INFO-TEXT-"].update("Failed to reach " + str(address))
        window.Refresh()
    else:
        window["-INFO-TEXT-"].update("Pinged " + str(address) + " in " + str(response))
        print("Pinged " + str(address) + " in " + str(response))
        window.Refresh()


# MAIN #

gui.theme('DarkAmber')

layout = [[gui.Text("Enter First Address:", size=(27, 1)), gui.InputText()],
          [gui.Text("Enter Last Address:", size=(27, 1)), gui.InputText()],
          [gui.Text("Enter Timeout (Default = 1s):", size=(27, 1)), gui.InputText()],
          [gui.Text("Current ping info displayed here.", key="-INFO-TEXT-", size=(27, 1)), gui.Output(size=(43, 8))],
          [gui.Button("Start", key="-START-BUTTON-"), gui.Button("Cancel", key="-CANCEL-BUTTON-", disabled=True)]]

window = gui.Window('Batch Ping Utility', layout, finalize=True)
print("Good pings will be recorded here.")

while True:
    event, values = window.read(timeout=15)

    if event == gui.WIN_CLOSED:
        break

    elif event == "-CANCEL-BUTTON-":
        window["-INFO-TEXT-"].update("Cancelling")
        marker_mid_pings = False
        start_address = ''
        end_address = ''
        timeout = ''
        window["-INFO-TEXT-"].update("Cancelled")
        window["-START-BUTTON-"].update(disabled=False)
        window["-CANCEL-BUTTON-"].update(disabled=True)

    elif marker_mid_pings:

        next_address = calculate_next_address(old_address)

        if next_address == "PING_END_ADDRESS":
            do_ping(end_address, timeout)
            marker_mid_pings = False
            start_address = ''
            end_address = ''
            timeout = ''
            window["-START-BUTTON-"].update(disabled=False)
            window["-CANCEL-BUTTON-"].update(disabled=True)

        else:
            do_ping(next_address, timeout)
            old_address = next_address

    elif event == "-START-BUTTON-":
        start_address = values[0]
        end_address = values[1]
        timeout = values[2]

        if start_address == '':
            window["-INFO-TEXT-"].update("Please enter valid start address!")
            window.Refresh()
            continue

        if end_address == '':
            window["-INFO-TEXT-"].update("Please enter a valid end address!")
            window.Refresh()
            continue

        if not validate_ip_address(start_address):
            continue

        if not validate_ip_address(end_address):
            continue

        if timeout == '':
            window["-INFO-TEXT-"].update("NB: Timeout is now 1s")
            timeout = 1
            window.Refresh()

        window["-START-BUTTON-"].update(disabled=True)
        window["-CANCEL-BUTTON-"].update(disabled=False)

        if start_address == end_address:
            marker_mid_pings = False
            do_ping(start_address, timeout)
            window["-START-BUTTON-"].update(disabled=False)
            window["-CANCEL-BUTTON-"].update(disabled=True)
        else:
            marker_mid_pings = True
            do_ping(start_address, timeout)
            old_address = start_address

        window.Refresh()

window.close()

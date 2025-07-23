# Simple GUI Batch Ping Utility
# 27/06/24 Jamie Drinkell
# Thanks to https://www.abstractapi.com/guides/validate-ip-address-python for the IP checker
# Converted to tkinter 23/07/25

from ping3 import ping
import tkinter as tk
import tkinter.scrolledtext as st
import ipaddress

# Globals #
start_address = ''
end_address = ''
old_address = ''
timeout = 1
keep_pinging_canceller = ''

# GUI #
root = tk.Tk()
root.title("Batch Ping Utility")
root.minsize(600, 220)
root.maxsize(600, 220)

tk_start_address    = tk.StringVar()
tk_end_address      = tk.StringVar()
tk_timeout          = tk.StringVar()
first_address_label = tk.Label(root, text="Enter First Address:")
first_address_entry = tk.Entry(root, textvariable=tk_start_address, width=45)
last_address_label  = tk.Label(root, text="Enter Last Address:")
last_address_entry  = tk.Entry(root, textvariable=tk_end_address, width=45)
timeout_label       = tk.Label(root, text="Enter Timeout (Default = 1s):")
timeout_entry       = tk.Entry(root, textvariable=tk_timeout, width=45)
ping_info_label     = tk.Label(root, text="Current ping info displayed here -> ")
ping_info_box       = st.ScrolledText(root, bg="white", height=6, width=44)
ping_info_box.insert(tk.INSERT, "Good Pings are recorded here :)\n")
ping_info_box.see(tk.END)
ping_info_box.config(state = "disabled")

# Functions #

def print_to_box(message):
    ping_info_box.config(state = "normal")
    ping_info_box.insert(tk.INSERT, message + "\n")
    ping_info_box.see(tk.END)
    ping_info_box.config(state = "disabled")


def validate_ip_address(ip_string):
    try:
        ipaddress.ip_address(ip_string)
        print_to_box("The IP address " + ip_string + " is valid.")
        return True
    except ValueError:
        print_to_box("The address " + ip_string + " is not valid")
        return False


def calculate_next_address(address):
    to_ping_by_parts = address.split('.')
    for y in range(3, 0, -1):
        if int(to_ping_by_parts[y]) >= 255:
            if y == 0:
                print_to_box("Can't go up from 255.255.255.255")
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


def do_ping(address):
    global timeout
    print_to_box("Pinging address " + str(address))
    response = ping(address, timeout=timeout)
    if response is None or False:
        print_to_box("Failed to reach " + str(address))
    else:
        print_to_box("Pinged " + str(address) + " in " + str(f"{response:.9f}"))


def keep_pinging():
    global end_address, old_address, keep_pinging_canceller, timeout
    global start_button, cancel_button
    if old_address == end_address:
        start_button.config(state='normal')
        cancel_button.config(state='disabled')
        print_to_box("Finished pings!")
        root.after_cancel(keep_pinging_canceller)
    else:
        next_address = calculate_next_address(old_address)
        do_ping(next_address)
        old_address = next_address
        keep_pinging_canceller = root.after(10, keep_pinging)


def on_start():
    global start_address, end_address, timeout, old_address, keep_pinging_canceller
    global start_button, cancel_button, tk_start_address, tk_end_address, tk_timeout
    start_address = tk_start_address.get()
    end_address = tk_end_address.get()
    timeout = tk_timeout.get()

    if start_address == '':
        print_to_box("Please enter a valid start address!")
        return

    if end_address == '':
        print_to_box("Please enter a valid end address!")
        return

    if not validate_ip_address(start_address):
        return

    if not validate_ip_address(end_address):
        return

    if timeout == '':
        print_to_box("No timeout set, timeout is now 1s")
        timeout = 1
    else:
        try:
            timeout = int(timeout)
        except:
            print_to_box("Please enter a valid timeout value!")
            return
        print_to_box("Timeout is set to " + str(timeout) + "s")


    print_to_box("Beginning pings!")
    do_ping(start_address)
    if (start_address == end_address): 
        print_to_box("Finished pings!")
        return

    start_button.config(state='disabled')
    cancel_button.config(state='normal')
    old_address = start_address
    keep_pinging_canceller = root.after(ms=10, func=keep_pinging)


def on_cancel():
    global keep_pinging_canceller, start_button, cancel_button, root
    global start_address, end_address, timeout
    root.after_cancel(keep_pinging_canceller)
    start_address = ''
    end_address = ''
    timeout = ''
    print_to_box("Pinging cancelled")
    start_button.config(state='normal')
    cancel_button.config(state='disabled')

start_button = tk.Button(root, text="Start", command=on_start)
cancel_button = tk.Button(root, text="Cancel", command=on_cancel)
cancel_button.config(state='disabled')

# Apply widgets to grid
first_address_label.grid(row=0, column=0, sticky=tk.W)
first_address_entry.grid(row=0, column=1)
last_address_label.grid(row=1, column=0, sticky=tk.W)
last_address_entry.grid(row=1, column=1)
timeout_label.grid(row=2, column=0, sticky=tk.W)
timeout_entry.grid(row=2, column=1)
ping_info_label.grid(row=3, column=0, sticky=tk.W)
ping_info_box.grid(row=3, column=1)
start_button.grid(row=4, column=0)
cancel_button.grid(row=4, column=1)
root.mainloop()

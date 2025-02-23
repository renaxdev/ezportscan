"""
Created by Maximilian Körner
https://mkoerner.dev
"""

from tkinter import messagebox, simpledialog, Tk
import pyfiglet
import sys
import socket
from datetime import datetime
   
root = Tk()
root.withdraw()

target = simpledialog.askstring("Target IP", "Enter Target IP")

ascii_banner = pyfiglet.figlet_format("ezPortscan")
print(ascii_banner)
print("\nby Renax")
  
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)
messagebox.showinfo("Scanning...", "Scanning Target: " + target)
   
try:     
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
          
        result = s.connect_ex((target,port))
        if result ==0:     
            print("Port {} is open".format(port))
            messagebox.showinfo("Open Port", "Port {} is open".format(port))
        s.close()
          
except KeyboardInterrupt:
        print("\n Exiting Program ")
        sys.exit()
except socket.gaierror:
        messagebox.showerror("Error", "Hostname could not be resolved!")
        print("\n Hostname Could Not Be Resolved!")
        sys.exit()
except socket.error:
        messagebox.showerror("Error", "Server not responding!")
        print("\n Server not responding!")
        sys.exit()

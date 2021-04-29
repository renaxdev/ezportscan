#-----Libraries-----#
import pyfiglet # For Text to Ascii (install with pip pyfiglet)
import sys
import socket
from datetime import datetime
   

#Start Banner
ascii_banner = pyfiglet.figlet_format("ezPortscan")
print(ascii_banner)
print("\nby Renax")
   

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Hostname to IPv4
else:
    print("Invalid amount of Arguments")
  
#Simple Banner
print("-" * 50)
print("Scanning Target: " + target)
print("Started at:" + str(datetime.now()))
print("-" * 50)
   
try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
          
        result = s.connect_ex((target,port))
        if result ==0:
            print("Port {} is open".format(port))
        s.close()
          

        sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved!")
        sys.exit()
except socket.error:
        print("\n Server is not responding!")
        sys.exit()

except KeyboardInterrupt:
        print("\n Exiting Program!")
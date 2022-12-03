#The EnDa Port Scanner's main function

#Import the module
try:
    from Tools.Base import *
except:
    print("Please install all needed modules!")
    time.sleep(10)

#Create a start-up
clearConsole()
if os.name in ("dos","nt"):
    os.system("title EnDa Port Scanner ^| EnDaTeam ^| Checked : 0 ^| Opened : 0")
morebanner(random.randint(1,7))
enter()
slowPrint(Fore.CYAN + "[$] Welcome to EnDa Port Scanner made by EnDaTeam!" + Fore.RESET,times=0.08)
enter()
checked = 0
opened = 0
while True:
    tip("Please enter the hostname!",option=1)
    enter()
    host = input(Fore.YELLOW + "[+] Host >> " + Fore.CYAN)
    ports = input(Fore.YELLOW + "[+] Port limit >> " + Fore.MAGENTA)
    speed = input(Fore.YELLOW + "[+] Speed (seconds) >> " + Fore.GREEN)
    enter()
    if hostname_resolves(host):
        break
    else:
        error("The inputed host does not exist!",option=1)
        enter()
        time.sleep(2)
    try:
        int(ports)
    except:
        error("The inputed port limit is not avaible!",option=1)
        enter()
        time.sleep(2)
    try:
        float(speed)
    except:
        error("The inputed speed is not avaible!",option=1)
        enter()
        time.sleep(2)
target = socket.gethostbyname(host) 
print(Colorate.Horizontal(Colors.white_to_green,f"[!] Starting the scan >> {datetime.today()}",2))
print(Colorate.Horizontal(Colors.white_to_blue,f"[!] Starting the scan >> {target}",2))
enter()
try:
    for port in range(1,int(ports) + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(float(speed))
        result = s.connect_ex((target,port))
        if result == 0:
            print(Fore.GREEN + f"[+] Port {port} is open" + Fore.RESET)
            opened = opened + 1
        #else:
        #    print(Fore.RED + f"[-] Port {port} is closed" + Fore.RESET)
        checked = checked + 1
        if os.name in ("dos","nt"):
            os.system(f"title EnDa Port Scanner ^| EnDaTeam ^| Checked : {checked} ^| Opened : {opened}")
        s.close()
    if opened == 0:
        print(Fore.RED + f"[-] The host [{target}] does not have any opened port!" + Fore.RESET)
    time.sleep(5)
    exit()
except KeyboardInterrupt:
        enter()
        error("Exiting Program by Shortcut CTRL-C!",option=1)
        time.sleep(3)
        exit()
except socket.gaierror:
        enter()
        error(f"Hostname [{target}] Could Not Be Resolved !",option=1)
        time.sleep(3)
        exit()
except socket.error:
        enter()
        error(f"Server [{target}] not responding {404}!",option=1)
        exit()

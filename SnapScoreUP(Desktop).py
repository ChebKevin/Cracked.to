import pyautogui
import keyboard
import time
import os
import ctypes
import platform
from colorama import Fore

ascii_text = """\033[38;5;94m
 ____                      ____                       _   _ ____  
/ ___| _ __   __ _ _ __   / ___|  ___ ___  _ __ ___  | | | |  _ \ 
\___ \| '_ \ / _` | '_ \  \___ \ / __/ _ \| '__/ _ \ | | | | |_) |
 ___) | | | | (_| | |_) |  ___) | (_| (_) | | |  __/ | |_| |  __/ 
|____/|_| |_|\__,_| .__/  |____/ \___\___/|_|  \___|  \___/|_|    
                  |_|                                              (Desktop)
\033[0m

\033[38;5;94mBy @Moonveil on Cracked.io / @DiningTable0 on Github\033[0m
"""

import pyautogui
import keyboard
import time
import os
import ctypes
import platform
from colorama import Fore

class SnapchatBot:

    def __init__(self):
        self.sent_snaps = 0
        self.delay = 1.3

    def print_console(self, arg, status="Console"):
        print(f"\n       {Fore.WHITE}[{Fore.YELLOW}{status}{Fore.WHITE}] {arg}")

    def wait_for_key_press(self, key):
        """Wait for a single press of the key and debounce it."""
        pressed = False
        while not pressed:
            if keyboard.is_pressed(key):
                pressed = True
                # Delay to debounce
                time.sleep(0.5)
            time.sleep(0.1)  # Slight delay to reduce CPU usage

    def get_positions(self):
        self.print_console("Position your cursor over the take picture button and then press the 'C' key to continue.")
        self.wait_for_key_press("c")
        self.take_picture = pyautogui.position()
        time.sleep(0.5)

        self.print_console("Position your cursor over the Send To button, and then press the 'C' key.")
        self.wait_for_key_press("c")
        self.send_to = pyautogui.position()
        time.sleep(0.5)

        self.print_console("Position your cursor over your shortcut, and then press the 'C' key.")
        self.wait_for_key_press("c")
        self.shortcut = pyautogui.position()
        time.sleep(0.5)

        self.print_console("Move your mouse to the Send Snap button, and then press the 'C' key.")
        self.wait_for_key_press("c")
        self.send_snap_button = pyautogui.position()

    def send_snap(self, shortcut_users):
        self.update_title(shortcut_users)
        pyautogui.moveTo(self.take_picture)
        for i in range(1):
            pyautogui.click()
            time.sleep(self.delay)
        pyautogui.moveTo(self.send_to)
        pyautogui.click()
        time.sleep(self.delay)
        pyautogui.moveTo(self.shortcut)
        pyautogui.click()
        time.sleep(self.delay)
        pyautogui.moveTo(self.send_snap_button)
        pyautogui.click()
        self.sent_snaps += 1
        self.update_title(shortcut_users)

    def update_title(self, shortcut_users):
        now = time.time()
        elapsed = str(now - self.started_time).split(".")[0]
        sent_snaps = self.sent_snaps * shortcut_users
        if platform.system() == "Windows":
            ctypes.windll.kernel32.SetConsoleTitleW(f"SnapScore UP (Desktop) | Sent Snaps: {sent_snaps} | Elapsed: {elapsed}s | Developed by @DiningTable on Github \ @Moonveil on Cracked.io")

    def main(self):
        if platform.system() == "Windows":
            os.system("cls")
            ctypes.windll.kernel32.SetConsoleTitleW("SnapScore UP (Desktop) | Developed by @DiningTable on Github \ @Moonveil on Cracked.io")
        else:
            os.system("clear")

        print(Fore.YELLOW + ascii_text)

        self.get_positions()

        while True:
            try:
                shortcut_users = int(input(f"\n       {Fore.WHITE}[{Fore.YELLOW}Console{Fore.WHITE}] How many people are in this shortcut? "))
                break
            except ValueError:
                print(f"\n       {Fore.WHITE}[{Fore.YELLOW}Console{Fore.WHITE}] An error occurred with that input. Please try again. :) ")

        self.print_console("Low-End-PC", "1")
        self.print_console("Mid-PC", "2")
        self.print_console("High-End-PC", "3")
        options = int(input(f"\n       {Fore.WHITE}[{Fore.YELLOW}Console{Fore.WHITE}] Option: "))

        if options == 1:
            self.delay = 2  # Low-End-PC
        elif options == 2:
            self.delay = 1  # Mid-PC
        elif options == 3:
            self.delay = 0.5  # High-End-PC (no delay)

        self.print_console("Go to your chats, and then press the 'V' key when you're ready.")
        self.wait_for_key_press("v")

        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

        print(Fore.YELLOW + ascii_text)
        self.print_console("Sending snaps now...")
        self.started_time = time.time()

        self.print_console("If you want to stop the operation, press and hold the 'F4' key for approximately 3 seconds.")
        self.wait_for_key_press("f4")

        while True:
            if keyboard.is_pressed("F4"):
                break
            self.send_snap(shortcut_users)
            time.sleep(self.delay)

        self.print_console(f"Finished sending {self.sent_snaps} snaps.")

obj = SnapchatBot()
obj.main()
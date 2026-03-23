#The goal of this program is to "Organically" take a copy of text and "write" it out as a "human"

import time
import random
import os
from pyautogui import typewrite, press, FAILSAFE

#Constants
TEXT_DELAY = (0.01, 0.1) # Simulate human typing with random delay between 10ms and 100ms
DELETE_CHANCE = 0.1 # 10% chance to simulate a typing error
DELAY_BEFORE_START = 3 # 3 seconds before starting to type

def clear_console():
    # Clear the console for better readability
    os.system('cls' if os.name == 'nt' else 'clear')

def get_text()->str:
    text = input("Enter the text you want to be typed out: ")
    pause =input("Open where you want your text, then go back to this window and press enter to start: ")
    print(f"Starting in {DELAY_BEFORE_START} seconds...")
    time.sleep(DELAY_BEFORE_START)
    return text

def random_delete():
    #Humans are not perfect typists, so we can simulate that by randomly inserting wrong characters and then deleting them:  # 10% chance to delete a character
    typewrite(random.choice('abcdefghijklmnopqrstuvwxyz'))  # Type a random wrong character
    press('backspace')


def text_maker(text):
    print("Typing started. Move to any corner to stop.")
    for i in text:
        if random.random() < DELETE_CHANCE:  # 10% chance to simulate a typing error
            random_delete()
        typewrite(i)
        time.sleep(random.uniform(*TEXT_DELAY)) # Simulate human typing with random delay
    clear_console()
# Example usage

def config():
    global TEXT_DELAY, DELETE_CHANCE, DELAY_BEFORE_START
    try:
        TEXT_DELAY = tuple(map(float, input("Enter the typing delay range in seconds (min max): ").split()))
        DELETE_CHANCE = float(input("Enter the chance of a typing error (0-1): "))
        DELAY_BEFORE_START = float(input("Enter the delay before starting to type in seconds: "))
    except ValueError:
        print("Invalid input. Using default settings.")
    menu()

def menu():
    clear_console()
    print("1. Start typing")
    print("2. Configure settings")
    print("3. Exit")
    choice = input("Enter your choice: ")
    clear_console()
    if choice == "2":
        config()
    elif choice == "1":
        text = get_text()
        text_maker(text)
    elif choice == "3":
        exit()
    else:
        print("Invalid choice. Please try again.")
        menu()


if __name__ == "__main__":
    menu()




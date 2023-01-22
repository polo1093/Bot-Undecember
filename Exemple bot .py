import time
import keyboard as keyboard
import pyautogui
import numpy as np
import pydirectinput

print('1. Make Sure You Are Using 1280x720 Client Size')
print("2. Make Sure You Are in The Party Screen")
print("3. If The Queue is Dodged Cancel The Queue and Restart The Bot")
op = input('Enter Done to Continue : ')
time.sleep(np.random.uniform(0.1, 1))
while not keyboard.is_pressed('k'):
    start = None
    while start is None:
        start = pyautogui.locateOnScreen('assets/Capture.png', grayscale=True, confidence=0.8)
        if start is not None:
            start = pyautogui.center(start)
            pyautogui.leftClick(start)
        else:
            print('Looking For Start')
    time.sleep(np.random.uniform(0.1, 1))
    accept = None
    while accept is None:
        accept = pyautogui.locateOnScreen('assets/accept.png', grayscale=True, confidence=0.8)
        if accept is not None:
            accept = pyautogui.center(accept)
            pyautogui.leftClick(accept)
        else:
            print('Looking For Accept')
    time.sleep(np.random.uniform(0.1, 1))
    time.sleep(120)
    pydirectinput.press('y')
    cont = None
    while cont is None:
        cont = pyautogui.locateOnScreen('assets/continue.png', grayscale=False, confidence=0.8)
        if cont is not None:
            cont = pyautogui.center(cont)
        else:
            keyboard.press('ctrl')
            keyboard.press('r')
            keyboard.release('ctrl')
            keyboard.release('r')
            time.sleep(np.random.uniform(0.1, 1))
            keyboard.press('ctrl')
            keyboard.press('q')
            keyboard.release('ctrl')
            keyboard.release('q')
            time.sleep(np.random.uniform(0.1, 1))
            keyboard.press('ctrl')
            keyboard.press('w')
            keyboard.release('ctrl')
            keyboard.release('w')
            time.sleep(np.random.uniform(0.1, 1))
            keyboard.press('ctrl')
            keyboard.press('e')
            keyboard.release('ctrl')
            keyboard.release('e')
            time.sleep(np.random.uniform(0.1, 1))
            pyautogui.rightClick(1548, 918)
            pydirectinput.press('a')
            time.sleep(np.random.uniform(10, 20))
            time.sleep(np.random.uniform(0.1, 1))
            pydirectinput.press('q')
            time.sleep(np.random.uniform(0.1, 1))
            pydirectinput.press('w')
            time.sleep(np.random.uniform(0.1, 1))
            pydirectinput.press('e')
            time.sleep(np.random.uniform(0.1, 1))
            pydirectinput.press('r')
            time.sleep(np.random.uniform(0.1, 1))
            pydirectinput.press('f')
            time.sleep(np.random.uniform(0.1, 1))
            pydirectinput.press('d')
    time.sleep(np.random.uniform(0.1, 1))
    honor = None
    while honor is None:
        honor = pyautogui.locateOnScreen('assets/honor.png', grayscale=True, confidence=0.8)
        if honor is not None:
            honor = pyautogui.center(honor)
            time.sleep(np.random.uniform(7, 10))
            pyautogui.leftClick(honor)
            pyautogui.leftClick(492, 540)
            time.sleep(10)
            pyautogui.leftClick(827, 835)
        else:
            print('Looking For Honor')
    time.sleep(np.random.uniform(0.1, 1))
    play_again = None
    while play_again is None:
        play_again = pyautogui.locateOnScreen('assets/play_again.png', grayscale=False, confidence=0.8)
        if play_again is not None:
            play_again = pyautogui.center(play_again)
            pyautogui.leftClick(play_again)
        else:
            print('Looking For Play Again')
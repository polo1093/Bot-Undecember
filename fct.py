import numpy as np
import time
from time import sleep 
import pyautogui
import pydirectinput
import pandas as pd
import re
import math


def click_icone(path,boucle=10,wait=0.3,gris=True,confidence=0.95):
    while boucle > 0:
        time.sleep(np.random.uniform(wait, wait*3)) 
        find = pyautogui.locateOnScreen(path, grayscale=gris, confidence=confidence)
        if find is not None:
            find = pyautogui.center(find)
            pyautogui.leftClick(find,duration=0.3)
            return True
        else:
            print(f'Looking For {path}')
        boucle -=1
    return False

def launch():
    time.sleep(1)
    path_img='screen/launch/icone.png'
    find = pyautogui.locateOnScreen(path_img, grayscale=True, confidence=0.8)
    if find is not None:
        click_icone('screen/launch/icone.png')
        pyautogui.leftClick()
        time.sleep(np.random.uniform(13.1, 15))

        in_game = 0
        while in_game == 0:
            if click_icone('screen/launch/start_1.png',20,0.6,False,0.99) == False:
                return False
            time.sleep(np.random.uniform(5.1, 7))

            if click_icone('screen/launch/perso1.png',20,0.6) == False:
                return False
            time.sleep(np.random.uniform(0.3, 0.7))
            
            
            if click_icone('screen/launch/start_2.png',20,0.6) == False:
                return False
            time.sleep(np.random.uniform(2, 2.7)) 
            
            in_game=20
            find = None
            find_2= None
            while find is None and in_game != 0:
                path_img='screen/launch/in_game.png'
                find = pyautogui.locateOnScreen(path_img, grayscale=True, confidence=0.90)
                path_img='screen/launch/party.png'
                find_2 = pyautogui.locateOnScreen(path_img, grayscale=True, confidence=0.90)
                if find is not None:
                    find = pyautogui.center(find)
                    pyautogui.leftClick(find)
                    time.sleep(np.random.uniform(1.1, 2))
                    click_icone('screen/launch/c_party.png')
                    time.sleep(np.random.uniform(1.1, 2))
                    click_icone('screen/launch/ok.png')
                    time.sleep(np.random.uniform(1.1, 3))
                    click_icone('screen/launch/ok.png')
                elif find_2 is not None: 
                    find=find_2
                time.sleep(np.random.uniform(1.1, 2))
                in_game -=1
        return True
    else: return False
    
def go_waypoint():
    if take_waypoint(True)==False :
        path_img='screen/launch/waypoint.png'
        find = pyautogui.locateOnScreen(path_img, grayscale=True, confidence=0.95)
        path_img='screen/launch/shield.png'
        find_2 = pyautogui.locateOnScreen(path_img, grayscale=True, confidence=0.90)
        if find_2 is not None:
            if find is  None:
                pyautogui.leftClick(pyautogui.center(find_2))
                time.sleep(np.random.uniform(0.4, 0.9))
            path_img='screen/launch/waypoint.png'
            find = pyautogui.locateOnScreen(path_img, grayscale=True, confidence=0.95)
            if find is not None:
                find = pyautogui.center(find)
                pyautogui.leftClick(find)
                cpt=20
                while cpt>0 :
                    if take_waypoint(True):
                        break
                    time.sleep(1)
            else: 
                print("error")
        else: 
            print("error")

def keyboard(key):
    pydirectinput.keyDown(key)
    time.sleep(np.random.uniform(0.3, 0.5))
    pydirectinput.keyUp(key)
    time.sleep(np.random.uniform(0.3, 0.5))
    
    
def take_waypoint(test=False):
    path_img='screen/launch/take_waypoint.png'
    find = pyautogui.locateOnScreen(path_img, grayscale=True, confidence=0.80)
    if find is not None:
        if test==False:
            keyboard('f')
        return True
    else:
        return False
    
def go_farm_act():
    go_waypoint()  
    take_waypoint()
    if  pyautogui.locateOnScreen('screen/launch/Ep_2_vert.png', grayscale=False, confidence=0.9) is None:
        click_icone('screen/launch/Ep_2_gris.png')
    if  pyautogui.locateOnScreen('screen/launch/A_10_vert.png', grayscale=False, confidence=0.9) is None:
        click_icone('screen/launch/A_10_gris.png')
    click_icone('screen/launch/farm_act.png')
    click_icone('screen/launch/move.png')

def go_blacksmith(wave):
    go_waypoint()
    move_trajet(wave["go_blacksmith"])
    click_icone('screen/launch/disassemble.png')
    click_icone('screen/launch/arme.png')
    click_icone('screen/launch/normal.png',1,0.3,True,0.99)
    click_icone('screen/launch/magic.png',1,0.3,True,0.98)
    click_icone('screen/launch/rare.png',1,0.3,True,0.98)
    click_icone('screen/launch/clear.png')
    
    click_icone('screen/launch/link.png')
    click_icone('screen/launch/normal.png',1,0.3,True,0.99)
    click_icone('screen/launch/magic.png',1,0.3,True,0.98)
    click_icone('screen/launch/rare.png',1,0.3,True,0.98)
    click_icone('screen/launch/clear.png')
    
    click_icone('screen/launch/detruire.png',1,0.3,True)

    click_icone('screen/launch/croix.png')
    time.sleep(np.random.uniform(0.3, 0.5))

def go_storage(wave):
    go_waypoint()
    move_trajet(wave["go_storage"])
    click_icone('screen/launch/storage.png',1)
    click_icone('screen/launch/clear.png',1)
    click_icone('screen/launch/currency.png')
    click_icone('screen/launch/clear.png')
    click_icone('screen/launch/alchimie.png')
    click_icone('screen/launch/clear.png')
    click_icone('screen/launch/map.png')
    click_icone('screen/launch/clear.png')
    click_icone('screen/launch/charm.png')
    click_icone('screen/launch/clear.png')
    
    click_icone('screen/launch/croix.png')


def go_tower(wave):
    go_waypoint()
    move_trajet(wave["go_tower"])
    click_icone('screen/launch/dungeon.png')
    

    
def move_trajet(trajet) :
    for n in trajet:
        if pd.isna(n) :
            break
        n=re.findall(r'\d+',n)
        pyautogui.leftClick(int(n[0]),int(n[1]),duration=0.3)
        time.sleep(np.random.uniform(1.5, 1.8))
    
    
    
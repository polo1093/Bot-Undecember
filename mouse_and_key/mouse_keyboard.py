import pyautogui
import random
import time
import numpy as np

def click_move( x, y,time_max=3,stepMin=1,stepMax=7,Tremble=20,time_press=0.25):
    """x2 : coordonnée cible
    y2 : coordonnée cible
    time_max : en second a few random marge 20%
    stepMin : 0 if you want direct move
    Tremble : tremblement de la souris dont la cible 
    time_press : temps du clic"""
    mouse_move( x, y,time_max-0.3,stepMin,stepMax,Tremble)
    mouse_clicker(time_press)
    mouse_move( x, y,0.3,1,1,Tremble)
         
def mouse_clicker( time_press=0.25):
    pyautogui.mouseDown(button='left')
    time.sleep(np.random.uniform(time_press*0.8, time_press*2, 1)[0])
    pyautogui.mouseUp(button='left')
    
def Keyboard_Press( key,time_press=0.25,time_max=0):
    """param key: la touche à press liste : https://pyautogui.readthedocs.io/en/latest/keyboard.html
    param time_press: _description_, defaults to 0.25
    param time_max: _description_, defaults to 0
    """
    if time_max!=0:
        time_press= np.random.uniform(time_press*0.8, time_press*2, 1)[0]
        wait_=time_max-time_press
        wait_=np.random.uniform(wait_*0.8, wait_*1.2, 1)[0]
        time.sleep(wait_)
    pyautogui.press(key) 
    time.sleep(time_press)
    pyautogui.keyUp(key)  
       
def mouse_move( x2, y2,time_max=3,stepMin=1,stepMax=7,Tremble=20):
    """x2 : coordonnée cible
    y2 : coordonnée cible
    time_max : en second a few random marge 20%
    stepMin : 0 if you want direct move
    Tremble : tremblement de la souris dont la cible """
    x1 ,y1 = pyautogui.position()
    
    xa=[]
    ya=[]
    rd1 = int(np.round(np.random.uniform(stepMin, stepMax, 1)[0]))
    rd2 = int(np.round(np.random.uniform(stepMin, stepMax, 1)[0]))
    
    if stepMax>1:
        for i in range(rd1):
            xa.append(int(np.random.uniform(x1, x2, 1)[0]))
        if x1>x2:xa.sort(reverse=True)
        if x1<x2:xa.sort()
        
        for i in range(rd2):
            ya.append(int(np.random.uniform(y1, y2, 1)[0]))
        if y1>y2:ya.sort(reverse=True)
        if y1<y2:ya.sort()
    
    for k in range(-1, max(0, rd1 - rd2)):
        ya.append(y2)
    for k in range(-1, max(0, rd2 - rd1)):
        xa.append(x2)
    #print(f'origine : {x1} , {y1} \n {rd1} {rd2} {len(xa)}')  
    #print(xa,ya)
    
    #pause si un utilisateur est decteté
    if (x1 ,y1)!=pyautogui.position():
        print("move")
        time.sleep(2.0)
   
    time_wait=0
    for i in range(len(xa)):
        x = xa[i] + int(+random.random() * Tremble)
        y = ya[i] + int(+random.random() * Tremble)
        speed=np.random.uniform(0.01 , time_max*1.4/len(xa) , 1)[0]
        pyautogui.moveTo(x,y,speed)
        wait=np.random.uniform(0.001 , time_max/(len(xa)*3) , 1)[0]
        time.sleep(wait)
        time_wait+= wait+speed
    #print(f'time wait : {time_wait}')
       

    
    
    
 
def test():
    time.sleep(1.0)
 
    click_move(2000,1000,1)
    Keyboard_Press("o")


if __name__ == '__main__':
    test()

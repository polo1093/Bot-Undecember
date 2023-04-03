import numpy as np
import time
import pyautogui
import pandas as pd
import re
import datetime
import math 

region={"Wanderer": "Aphros",
        "Plague" :  "Ortemis",
        "Flash" :   "Caspol",
        "Pirate":   "Ganida",
        "Hammer":   "Eunos",
        "Brazier":  "Tipan",
        "Air":      "Stra",
        "Shepherd": "Laia",
        "Greed":    "Tri",
        "Lighting": "Hira",
        "Cycle":    "Nemera"}

def click_icone(path,boucle=10,wait=0.3,gris=True,confidence=0.95):
    while boucle > 0:
        time.sleep(np.random.uniform(wait, wait*3)) 
        find = pyautogui.locateOnScreen(path, grayscale=gris, confidence=confidence)
        if find is not None:
            find = pyautogui.center(find)
            pyautogui.leftClick(find,duration=0.3)
            return True
        boucle -=1
    print(f'Looking For {path[7:]}')
    return False

def clik_move_map(x,y):
    a=pyautogui.screenshot(region=(x-50,y-50, 150, 150))
    pyautogui.leftClick(x,y,duration=0.08)
    time.sleep(0.08)
    b=pyautogui.screenshot(region=(x-50,y-50, 150, 150))
    # Obtenir les données de pixels de chaque image
    a_data = a.getdata()
    b_data = b.getdata()

    # Compter le nombre de pixels identiques entre les deux images en %
    similarity = sum(1 for a, b in zip(a_data, b_data) if a == b)/ len(a_data)

    # Vérifier si le pourcentage de pixels identiques est supérieur ou égal à 95 %
    if similarity >= 0.95:
        return False
    return True
    
def find_blue(path):
    find = pyautogui.locateAllOnScreen(path,region=[1930,363,2445-1930,1070-363], confidence=0.99)
    for i in find:
        p= pyautogui.screenshot().getpixel((i[0]+i[2]-5,i[1]+i[3]-5))
        if p[2] > 34 and 80 > p[0]+p[1]:
            return i
    return False


def reset_region():
    click_icone('screen/launch/start_filtre.png',1)
    click_icone('screen/launch/start_filtre.png',1)
    pyautogui.leftClick(1150,1000)
    if click_icone('screen/launch/select_all.png',1):
        click_icone('screen/launch/select_all.png',1)
    
def find_region(m,number=10):
    #mise ne place du filtre
    reset_region()   
    click_icone(f'screen/map/{region[m]}.png',1)
    click_icone('screen/map/ok_filtre.png',1)
    click_icone('screen/map/ok_filtre.png',1)
    
    #test si on a la map
    x_ligne=410+101*(int(number/5))
    if not pyautogui.locateOnScreen('screen/map/case_vide.png',region=[1920,x_ligne-65,130,130]):
        return 1980,x_ligne 
    return False

def filtre_map(list_map):
    reset_region()  
    for name_map in list_map: 
        click_icone(f'screen/map/{region[name_map]}.png',1)
    click_icone('screen/map/ok_filtre.png',1)
    click_icone('screen/map/ok_filtre.png',1)      


def launch_tower(wave,num_perso=2):
    if not launch_game(num_perso):
        return False
    else:
        start_time = time.perf_counter()
        while not go_tower(wave):
            if time.perf_counter()-start_time > 21*60:
                close_game("no_go_tower")
                launch_game(num_perso)
            if not in_city():
                leave_map()
        return True


def launch_remote_desk():
    pyautogui.leftClick(181,1406)
    time.sleep(0.2)
    pyautogui.leftClick(1400,600)
    time.sleep(0.1)
    pyautogui.leftClick(1000,500)
    pyautogui.write("total")
    time.sleep(0.1)
    pyautogui.keyDown('shift')
    pyautogui.write("22")
    pyautogui.keyUp('shift')
    pyautogui.leftClick(1100,735)
    time.sleep(2)
    
    
    
    
    
def launch_game(num_perso):
    path_img='screen/launch/icone.png'
    find = pyautogui.locateOnScreen(path_img, grayscale=True, confidence=0.8)
    if find :
        click_icone('screen/launch/icone.png')
        pyautogui.leftClick()
        time.sleep(np.random.uniform(13.1, 15))
        
        if click_icone('screen/launch/start_1.png',20,0.6,False) == False:
            pyautogui.leftClick(1650,15)
            time.sleep(1)
            launch_remote_desk()
            time.sleep(1)
            if click_icone('screen/launch/start_1.png',5,0.6,False) == False:
                return False
        time.sleep(np.random.uniform(5.1, 7))

        if click_icone(f'screen/launch/perso{num_perso}.png',20,0.6) == False:
            pyautogui.leftClick(1650,15)
            time.sleep(1)
            launch_remote_desk()
            time.sleep(1)
            if click_icone(f'screen/launch/perso{num_perso}.png',5,0.6) == False:
                return False
        time.sleep(np.random.uniform(0.3, 0.7))
        
        if click_icone('screen/launch/start_2.png',20,0.6) == False:
            return False
        time.sleep(7) 

        if not in_city():
            leave_map()
            if not in_city():
                return False
                
        return party_area()
    return True


def party_area():
    if not click_icone('screen/launch/party.png',1, confidence=0.90):
        #create party area
        if not click_icone('screen/launch/in_game.png',1): # un peu redontant avec c_party
            return False
        pyautogui.leftClick()
        click_icone('screen/launch/c_party.png')
        click_icone('screen/launch/c_party.png',1)
        time.sleep(np.random.uniform(0.2, 0.8))
        
        #create name
        pyautogui.leftClick(950,300)
        pyautogui.leftClick(950,300)
        pyautogui.write("TarStaP")
        while click_icone('screen/launch/button.png',1):
            1
        click_icone('screen/launch/Create.png',1)
        click_icone('screen/launch/Create.png',1)
        time.sleep(np.random.uniform(1.1, 2))
        click_icone('screen/launch/ok.png',1)
        click_icone('screen/launch/ok.png',1)
        time.sleep(np.random.uniform(2, 3))
        click_icone('screen/launch/party.png',1, confidence=0.90)
    #test si on y est
    if click_icone('screen/launch/move_to_party_area.png',1):
        time.sleep(np.random.uniform(2, 3))
        click_icone('screen/launch/party.png',1, confidence=0.90)
    if pyautogui.locateOnScreen('screen/launch/Leave_to_party_area.png',grayscale=True,confidence=0.9) \
            or pyautogui.locateOnScreen('screen/launch/Leave_to_party_area_light.png',grayscale=True,confidence=0.9):
        click_icone('screen/launch/reset.png',1)
        return True
    click_icone('screen/launch/reset.png',1)
    return False
    
    


def raid(creneau1=[15.45,18.15],creneau2=0):
    now = datetime.datetime.now()
    if now.hour>= int(creneau1[0]) and now.hour<=creneau1[1]:
        if now.hour==int(creneau1[1]) and now.minute>=creneau1[1]%1*100:
            return False
        if now.hour>int(creneau1[0]):
            return True
        if now.hour==int(creneau1[0]) and now.minute>=creneau1[0]%1*100:
            return True
    if creneau2:      
        if now.hour>= int(creneau2[0]) and now.hour<=creneau2[1]:
            if now.hour==int(creneau2[1]) and now.minute>=creneau2[1]%1*100:
                return False
            if now.hour>int(creneau2[0]):
                return True
            if now.hour==int(creneau2[0]) and now.minute>=creneau2[0]%1*100:
                return True
    return False


def go_waypoint():
    click_icone('screen/launch/reset.png',1)
    if not in_city():
        return False
    if take_waypoint(True)==False :
        path_img='screen/launch/waypoint.png'
        find = pyautogui.locateOnScreen(path_img, grayscale=True, confidence=0.95)
        if find is  None:
            pyautogui.leftClick((50,823))
            time.sleep(np.random.uniform(0.4, 0.9))
            pyautogui.moveTo((212,820))
            for j in range(30):
                pyautogui.scroll(3000)
        find = pyautogui.locateOnScreen(path_img, grayscale=True, confidence=0.95)
        if find :
            find = pyautogui.center(find)
            pyautogui.leftClick(find)
            time.sleep(0.2)
            pyautogui.leftClick(find)
            start_time = time.perf_counter()
            while time.perf_counter()-start_time < 10*60 :
                if take_waypoint(True):
                    time.sleep(1)
                    break
                time.sleep(0.2)
        else: 
            print("error_waypoint")
            return False
    return True

def keyboard(key,press=0.5,end=0.5):
    pyautogui.keyDown(key)
    time.sleep(np.random.uniform(press*0.8, press*1.2))
    pyautogui.keyUp(key)
    time.sleep(np.random.uniform(end*0.8, end*1.2))
    
    
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

def go_blacksmith():
    go_waypoint()
    click_icone('screen/launch/icone_blacksmith.png')
    time.sleep(5)
    if click_icone('screen/launch/disassemble.png')==False:
        return False
    time.sleep(0.5)
    click_icone('screen/launch/arme.png')
    click_icone('screen/launch/clear.png')
    
    click_icone('screen/launch/link.png')
    click_icone('screen/launch/clear.png')
    
    click_icone('screen/launch/detruire.png',1,0.3,True)
    click_icone('screen/launch/ok.png',1)

    click_icone('screen/launch/croix.png',2)
    click_icone('screen/launch/croix.png',1)
    click_icone('screen/launch/croix.png',1)
    time.sleep(0.5)
    return True

def go_sell():
    go_waypoint()
    click_icone('screen/launch/icone_blacksmith.png')
    time.sleep(5)
    if click_icone('screen/launch/icone_sell.png')==False:
        return False
    time.sleep(0.5)
    if click_icone('screen/launch/arme.png'):
        click_icone('screen/launch/arme.png')
        click_icone('screen/launch/clear.png')
        
        click_icone('screen/launch/sell.png',1,0.3,True)
        click_icone('screen/launch/ok.png',1)

    click_icone('screen/launch/croix.png',2)
    click_icone('screen/launch/croix.png',1)
    time.sleep(0.5)
    return True   

def go_storage():
    time.sleep(0.5)
    if go_waypoint() :
        click_icone('screen/launch/icone_storage.png')
        time.sleep(3)
        click_icone('screen/launch/storage.png',1)
        click_icone('screen/launch/storage_clear.png',1)
        
        click_icone('screen/launch/croix.png')
        time.sleep(0.5)
        return True
    else: return False


def go_tower(wave):
    if pyautogui.locateOnScreen(f'screen/launch/in_tower.png',confidence=0.7) is None :
        if go_waypoint()==False:
            return False
        move_trajet(wave["go_tower"])
        if click_icone('screen/launch/dungeon.png',1)==False:
            pyautogui.leftClick((1126,734),duration=0.08)
            time.sleep(0.5)
            if click_icone('screen/launch/dungeon.png',1)==False:
                return False
    return True
    
def go_alchimie(wave):
    time.sleep(1)
    if go_waypoint():
        move_trajet(wave["go_alchimie"])
        click_icone('screen/alchimie/take_alchimie.png',3)
        return True
    return False


def go_map(wave):
    for i in range(10):
        go_waypoint()
        move_trajet(wave["go_map"])
        keyboard('f')
        time.sleep(0.5)
        if in_city()==False:
            return True
    return False

def move_trajet(trajet) :
    for n in trajet:
        if pd.isna(n) :
            break
        n=re.findall(r'\d+',n)
        pyautogui.leftClick(int(n[0]),int(n[1]),duration=0.15)
        time.sleep(np.random.uniform(1.9, 2.2))

### Mapping
def error_start_map(list_map):
    for j in list_map:
        if pyautogui.locateOnScreen(f'screen/map/{j}_1.png',confidence=0.85):
            return j+ '_1'
        elif pyautogui.locateOnScreen(f'screen/map/{j}_2.png',confidence=0.85):
            return j+ '_2'
    return False

def prepar_run(num_perso=2):
    click_icone('screen/map/skill_passif.png',2)
    if num_perso==1 and click_icone('screen/map/aura_1.png',1,gris=False):
        keyboard('z',0.3)
    if num_perso>=2:
        pass
    click_icone('screen/map/skill_actif.png',2)
    
    if num_perso>=2:
            keyboard('a',0.7)
            time.sleep(1)
            keyboard('r',0.7)
            time.sleep(1)



    

     
def kill_boss(trajet,retry,num_perso=2,re_kill_boss=False):
    time.sleep(np.random.uniform(1.7, 2.2))
    if click_icone('screen/launch/boss.png',2) ==True:
        time.sleep(np.random.uniform(0.7, 1.2))
        keyboard('f')
        time.sleep(1)
        for i in range(100):
            if in_map():break
            time.sleep(0.5)
        move_trajet(trajet)
        if  num_perso==1:
            keyboard('z')
            keyboard('e')
            
        for i in range(100):
            if pyautogui.locateOnScreen(f'screen/launch/ok_map.png',confidence=0.7):
                break
            if death():return True
            if num_perso>=2 and i%4==3:keyboard('a',0.7)
            time.sleep(0.3)
        time.sleep(3)
        keyboard('w')
        time.sleep(np.random.uniform(3.5, 4.8)) 
        if not click_icone('screen/launch/ok.png') and re_kill_boss==False:
            kill_boss(trajet,retry,num_perso=2,re_kill_boss=True)
        time.sleep(np.random.uniform(4.9, 5.8)) 
        return True
    if retry:
        # en recommence la map si on ne peut pas invoquer le boss
        return False
    leave_map()
    return True
    

def leave_map(retry=True):
    if pyautogui.locateOnScreen(f'screen/map/scroll_cooldown.png',region=[700,1354,722,1416],confidence=0.9):
        start_time = time.perf_counter()
        while pyautogui.locateOnScreen(f'screen/map/scroll_cooldown.png',region=[700,1354,722,1416],confidence=0.9) \
        and time.perf_counter()-start_time <60*9:
            time.sleep(1)
        for i in range(61):time.sleep(1)
    if pyautogui.locateOnScreen(f'screen/map/scroll.png',confidence=0.9) \
        or pyautogui.locateOnScreen(f'screen/map/exit.png',confidence=0.9) :
        keyboard('w')
        keyboard('f') 
        click_icone('screen/launch/ok.png',1)
        time.sleep(np.random.uniform(4.5, 5.8))  
        return True
    if retry==True:
        for i in range(61):time.sleep(1)
        return leave_map(False)
    return False

def escape():
    keyboard("esc")
    click_icone('screen/map/setting.png')
    time.sleep(0.5)
    click_icone('screen/map/account.png')
    time.sleep(0.5)
    start_time = time.perf_counter()
    while not click_icone('screen/map/escape.png'):
        time.sleep(2.5)
        if time.perf_counter()-start_time < 60*5:
            click_icone('screen/launch/croix.png') 
            break
    click_icone('screen/launch/ok.png')   
    

    
         
        
def in_city():
    if pyautogui.locateOnScreen(f'screen/launch/shield.png',grayscale=True,confidence=0.9) is not None:
        return True
    return False

def calcul_distance(x1, y1):
    x2 = 1280
    y2 = 721
    return int(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))

def time_run(x,y):
    """Pr 1101 unité parcourus il faut 2.14s, on va multi par racine de deux pr avoir de la marge"""
    return (calcul_distance(x,y)*2.14/1101) * math.sqrt(2)

def in_map():
    path=f'screen/launch/test_in_game.png'
    find=pyautogui.locateOnScreen(path, grayscale=False, confidence=0.95)
    if find is None or in_city():
        return False
    return True

def death():
    path=f'screen/launch/death.png'
    if pyautogui.locateOnScreen(path, grayscale=False, confidence=0.95):
        time.sleep(1)
        pyautogui.leftClick(1400,1300)
        time.sleep(5)
        return True
    return False
    

    
    
def se_vider(sell=False):
    if in_city():
        if sell:
            if go_sell()==False:
                if go_sell()==False:return False           
        else:
            if go_blacksmith()==False:
                if go_blacksmith()==False:return False
        go_storage()
        return True 
    return False


def craft_charm(rare_charm=False):
    time.sleep(1)
    click_icone('screen/alchimie/synthesis.png',1)
    click_icone('screen/alchimie/synthesis.png',1)
    if rare_charm: path='screen/alchimie/rare_charm.png'
    else: path='screen/alchimie/magic_charm.png'
    if not click_icone(path,1,0.3):
        click_icone('screen/alchimie/charm.png',1,0.3,True,0.99)
        click_icone(path,1,0.3)
    pyautogui.leftClick(2100,700)
    for i in range(0,50):
        pyautogui.scroll(-30000)
    for i in range (0,3):
        pyautogui.rightClick(1980,950)
        time.sleep(0.3)
    click_icone('screen/alchimie/craft.png')
    
def alchimie_charm(rare_charm=False):
    if click_icone('screen/alchimie/atelier.png',1,0,confidence=0.8) :
        click_icone('screen/alchimie/receive.png')
        time.sleep(0.5)
        pyautogui.leftClick()
        time.sleep(0.5)
        pyautogui.leftClick()
        craft_charm(rare_charm)
    elif click_icone('screen/alchimie/atelier_vide.png',1,0):
        craft_charm(rare_charm)
        

def alchimie(wave,num_perso=2,rare_charm=False):
    for i in range(3):
        if pyautogui.locateOnScreen(f'screen/launch/in_alchimie.png',grayscale=True,confidence=0.9) is None :
            go_alchimie(wave)
            time.sleep(0.5)
    
        if pyautogui.locateOnScreen(f'screen/launch/in_alchimie.png',grayscale=True,confidence=0.9) :
            if num_perso==1:nbr_atelier=4
            else:nbr_atelier=1
            for i in range(nbr_atelier):
                alchimie_charm(rare_charm)
            click_icone('screen/launch/croix.png')
            time.sleep(0.5)
            return True
    return False
    
        
def close_game(message=""):
    if not pyautogui.locateOnScreen(f'screen/launch/icone.png',grayscale=True,confidence=0.9) :
        pyautogui.leftClick(2500,150)
        time.sleep(1)
        print(f'Close game for {message}')
        message+=" %s_%s "%(time.localtime().tm_hour,time.localtime().tm_min)
        pyautogui.screenshot(region=(0,0, 2500, 1400)).save(f"screen/erreur/close{message}.png") 
        pyautogui.keyDown('alt')
        pyautogui.keyDown('F4')
        time.sleep(np.random.uniform(0.3, 0.5))
        pyautogui.keyUp('alt')
        pyautogui.keyUp('F4')
        return True
    return False

SCREEN_RESOLUTION_actualy= pyautogui.size()
SCREEN_RESOLUTION_native= (2560,1440)
def resolution_scale(width,height):
    """_summary_

    Args:
        width (int): _description_
        height (int): _description_
    """    
    width=width*SCREEN_RESOLUTION_actualy.width//SCREEN_RESOLUTION_native[0]
    height=height*SCREEN_RESOLUTION_actualy.height//SCREEN_RESOLUTION_native[1]
    return width,height
    
        
            
        
    
           
    
    
    
    
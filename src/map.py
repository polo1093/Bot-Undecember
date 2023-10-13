import time
import fct
import pyautogui
import numpy as np

region_T10={"Wanderer": "Aphros",
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
region_T11={"Alyssa": "Aphros",
        "Vesper" :  "Ortemis",
        "Casthor" : "Caspol",
        "Miraseti": "Ganida",
        "Boreal":   "Eunos",
        "Capri":    "Tipan",
        "Aquilla":  "Stra",
        "Shepherd": "Laia",
        "Acuben":   "Hira",
        "Hamal":    "Prele",
        "Spica":    "Tri",
        "Leo":      "Nemera"}

class Map():
    def __init__(self,list_map,can_run_T11=False):
        self.list_map_T10=list_map["T10"]
        self.list_map_T11=list_map["T11"]
        self.can_run_T11=can_run_T11
        self.timer_betwen_map=fct.timer.Timer(0)
        self.TIME_BETEWEN_MAP=60*5.1
        
        
    def launch_map(self):
        while self.timer_betwen_map.is_running():time.sleep(1)
        self.reset_region()  
        
        if self.can_run_T11:
            self.active_filtre_T11()
            np.random.shuffle(self.list_map_T11)
            name_map=self.list_map_T11[0]
            pyautogui.rightClick(self.find_region(region_T11[name_map],stock_map=5))  

        else :
            self.active_filtre_T10()
            np.random.shuffle(self.list_map_T10)
            name_map=self.list_map_T10[0]
            pyautogui.rightClick(self.find_region(region_T10[name_map],stock_map=5))  
            
        
        time.sleep(1)
        fct.click_icone('screen/launch/activate.png',3,0.3,False,0.8)
        time.sleep(1)
        if fct.click_icone('screen/launch/croix.png',1):
            if self.can_run_T11: 
                self.list_map_T11.remove(name_map)
                if len( self.list_map_T11) <3: 
                    self.can_run_T11=False
            time.sleep(1)
            return False
        self.timer_betwen_map=fct.timer.Timer(self.TIME_BETEWEN_MAP)
        return name_map
    

    def find_region(self,name_region,stock_map=10):
        #mise ne place du filtre
        fct.click_icone(f'screen/map/{name_region}.png',1)
        fct.click_icone('screen/map/ok_filtre.png',1)
        fct.click_icone('screen/map/ok_filtre.png',1)
        
        x_ligne=410+101*(int(stock_map/5))
        time.sleep(0.1)
        return 1980,x_ligne 
        
    def reset_region(self):
        fct.click_icone('screen/launch/start_filtre.png',1,confidence=0.8)
        fct.click_icone('screen/launch/start_filtre.png',1,confidence=0.8)
        pyautogui.leftClick(1150,1000)
        fct.click_icone('screen/launch/select_all.png',1,confidence=0.8)
        fct.click_icone('screen/launch/select_all.png',1,confidence=0.8)
            
            
    def active_filtre_T11(self):
        if pyautogui.locateOnScreen('screen/map/is_T10.png',confidence=0.95):
            pyautogui.leftClick(1830,1000)
            fct.click_icone('screen/launch/select_all.png',1)
            fct.click_icone('screen/launch/select_all.png',1)
        if not pyautogui.locateOnScreen('screen/map/is_T11.png',confidence=0.95):
            pyautogui.leftClick(1544,837)
            time.sleep(0.3)
        if pyautogui.locateOnScreen('screen/map/is_T11.png'):
            return True
        return False
            
    def active_filtre_T10(self):
        if pyautogui.locateOnScreen('screen/map/is_T11.png',confidence=0.95):
            pyautogui.leftClick(1830,1000)
            fct.click_icone('screen/launch/select_all.png',1)
            fct.click_icone('screen/launch/select_all.png',1)
        if not pyautogui.locateOnScreen('screen/map/is_T10.png',confidence=0.95):
            pyautogui.leftClick(1830,760)
            time.sleep(0.3)
        if pyautogui.locateOnScreen('screen/map/is_T10.png',confidence=0.95):
            return True
        return False
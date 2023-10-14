import time
import fct
import pyautogui


class Alchimie():
    def __init__(self,wave,num_perso=2,T9_up=False,blue_charm=False,rare_charm=False):
        self.alchemy_wave=wave["go_alchimie"]
        self.num_perso=num_perso
        self.timer_T9=fct.timer.Timer(1 if T9_up else 60*40*40)
        self.blue_charm=blue_charm
        self.rare_charm=rare_charm
        self.NBR_ATELIER=3
    
    
    def run(self):
        for i in range(3):
            if pyautogui.locateOnScreen(f'screen/alchimie/in_alchimie.png',grayscale=True,confidence=0.9) :
                break
            self.go_alchimie()
            time.sleep(0.5)
           
        if pyautogui.locateOnScreen(f'screen/alchimie/in_alchimie.png',grayscale=True,confidence=0.9) :
            self.filtre_map=True#a modifier dans le futur
            for i in range(self.NBR_ATELIER):
                if self.is_one_clear_atelier():
                    if self.timer_T9.is_expire():
                        if not self.alchimie_T9up():
                            self.timer_T9.relaunch(60*40)
                    elif self.blue_charm or self.rare_charm:
                        if not self.craft_charm():
                            pass#self.blue_charm,self.rare_charm=False,False
            fct.click_icone('screen/launch/croix.png')
            time.sleep(0.5)
    
    def go_alchimie(self):
        time.sleep(1)
        if fct.go_waypoint():
            fct.move_trajet(self.alchemy_wave)
            fct.click_icone('screen/alchimie/take_alchimie.png',3)
            return True
        return False
    
    def is_one_clear_atelier(self):
        if fct.click_icone('screen/alchimie/atelier.png',1,0,confidence=0.8) :
            fct.click_icone('screen/alchimie/receive.png')
            time.sleep(0.5)
            pyautogui.leftClick()
            time.sleep(0.5)
            pyautogui.leftClick()
            return True
        elif fct.click_icone('screen/alchimie/atelier_vide.png',1,0):
            return True
        return False
    
    def craft_charm(self):
        time.sleep(1)
        fct.click_icone('screen/alchimie/synthesis.png',1)
        fct.click_icone('screen/alchimie/synthesis.png',1)
        if self.rare_charm: path='screen/alchimie/rare_charm.png'
        else: path='screen/alchimie/magic_charm.png'
        if not fct.click_icone(path,1,0.3):
            fct.click_icone('screen/alchimie/charm.png',1,0.3,True,0.99)
            fct.click_icone(path,1,0.3)
        pyautogui.leftClick(2100,700)
        for i in range(0,150):
            pyautogui.scroll(-3000,_pause=False)
            time.sleep(0.005)
        time.sleep(0.3)   
        for i in range (0,3):
            pyautogui.rightClick(1980,950)
            time.sleep(0.3)
        if fct.click_icone('screen/alchimie/craft.png'):
            return True
        return False
        
    # def alchimie_T9up(self):
    #     time.sleep(1)
    #     fct.click_icone('screen/alchimie/synthesis.png',1)
    #     fct.click_icone('screen/alchimie/synthesis.png',1)
    #     if not pyautogui.locateOnScreen('screen/alchimie/NormalChaos.png',grayscale=True,confidence=0.9):
    #         fct.click_icone('screen/alchimie/Chaos Card.png',1)
    #     pyautogui.moveTo(350,650)
    #     for i in range(0,20):
    #         pyautogui.scroll(-3000,_pause=False)
    #     time.sleep(0.3)
    #     if fct.click_icone('screen/alchimie/T9_map.png',2):
    #         fct.click_icone('screen/alchimie/T9_map.png',2)
    #         if self.filtre_map:
    #             fct.click_icone('screen/alchimie/filtre_map.png',1,0.7)
    #             fct.click_icone('screen/alchimie/select_all.png',1,0.7)
    #             fct.click_icone('screen/alchimie/ok_map_filtre.png',1,0.7)
    #             self.filtre_map=False
    #             pyautogui.rightClick(2000,620)
    #         for i in range (0,4):
    #             pyautogui.rightClick(2000,620)
    #             time.sleep(0.3)
    #         if fct.click_icone('screen/alchimie/craft.png'):
    #             return True
    #         if pyautogui.locateOnScreen('screen/alchimie/map_empty.png',grayscale=True,confidence=0.9):
    #             return False
    #     return True
    
    def alchimie_T9up(self):
        time.sleep(1)
        fct.click_icone('screen/alchimie/synthesis.png',1)
        fct.click_icone('screen/alchimie/synthesis.png',1)
        if not pyautogui.locateOnScreen('screen/alchimie/NormalChaos.png',grayscale=True,confidence=0.9):
            fct.click_icone('screen/alchimie/Chaos Card.png',1)
        time.sleep(0.3) 
        fct.click_icone('screen/alchimie/NormalChaos.png',1,confidence=0.9)
        fct.click_icone('screen/alchimie/NormalChaos.png',1,confidence=0.9)
        if self.filtre_map:
            fct.click_icone('screen/alchimie/filtre_map.png',1,0.7)
            fct.click_icone('screen/alchimie/select_all.png',1,0.7)
            fct.click_icone('screen/alchimie/ok_map_filtre.png',1,0.7)
            self.filtre_map=False
            pyautogui.rightClick(2000,620)
            time.sleep(0.3)  
        pyautogui.moveTo(350,650)
        for i in range(0,20):
            pyautogui.scroll(-3000,_pause=False)
        time.sleep(0.3)
        if fct.click_icone('screen/alchimie/T9_map.png',2):
            fct.click_icone('screen/alchimie/T9_map.png',2)
            # if self.filtre_map:
            #     fct.click_icone('screen/alchimie/filtre_map.png',1,0.7)
            #     fct.click_icone('screen/alchimie/select_all.png',1,0.7)
            #     fct.click_icone('screen/alchimie/ok_map_filtre.png',1,0.7)
            #     self.filtre_map=False
            #     pyautogui.rightClick(2000,620)
            for i in range (0,4):
                pyautogui.rightClick(2000,620)
                time.sleep(0.3)
            if fct.click_icone('screen/alchimie/craft.png'):
                return True
            if pyautogui.locateOnScreen('screen/alchimie/map_empty.png',grayscale=True,confidence=0.9):
                return False
        return True
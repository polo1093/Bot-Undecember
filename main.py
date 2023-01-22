import datetime
import logging.handlers
import sys
import threading

import warnings
from sys import platform
import virtualbox

import mouse_and_key.mouse_keyboard as mouse

from PIL import Image, ImageGrab
import pyautogui
import win32api
import random
import time
import numpy as np
# ==== MAIN PROGRAM =====

class VirtualBoxController():
    def __init__(self):
        self.vbox = virtualbox.VirtualBox()
        self.vm = self.vbox.find_machine(self.vbox.machines[1].name)
        self.session = self.vm.create_session()
        self.horizontal = 0
        self.vertical = 0
        self.xOrigin = 0
        self.yOrigin = 0
        self.update_position()
        

    def update_position(self):
        h, w, _, xOrigin, yOrigin, _ = self.session.console.display.get_screen_resolution(0)
        self.horizontal = h
        self.vertical = w
        self.xOrigin = xOrigin
        self.yOrigin = yOrigin
        
        
    def start_vm(self):
        try:
            
            self.session = self.vm.create_session()
        except Exception as e:
            self.logger.warning(str(e))
        

    def get_vbox_list(self):
        vm_list = [vm.name for vm in self.vbox.machines]
        return vm_list

    def get_screenshot_vbox(self):
        h, w, _, _, _, _ = self.session.console.display.get_screen_resolution(0)
        png = self.session.console.display.take_screen_shot_to_array(0, h, w, virtualbox.library.BitmapFormat.png)
        open('screenshot_vbox.png', 'wb').write(png)  # pylint: disable=consider-using-with

        time.sleep(0.1)
        return Image.open('screenshot_vbox.png')

    def mouse_move_vbox(self, x, y, dz=0, dw=0):
        self.session.console.mouse.put_mouse_event_absolute(x, y, dz, dw, 0)

    def mouse_click_vbox(self, x, y, dz=0, dw=0):
        self.session.console.mouse.put_mouse_event_absolute(x, y, dz, dw, 0b1)
        time.sleep(np.random.uniform(0.4, 0.6, 1)[0])
        self.session.console.mouse.put_mouse_event_absolute(x, y, dz, dw, 0)

    def get_mouse_position_vbox(self):
        # todo: not working
        x = self.session.console.mouse_pointer_shape.hot_x()
        y = self.session.console.mouse_pointer_shape.hot_y()
        return x, y

       

    
    
    
 
def test():
  #vm = VirtualBoxController()
  1
  time.sleep(1.0)
  vm = VirtualBoxController()
  vm.get_screenshot_vbox()
  
  #click_move(2000,1000,1)
  #Keyboard_Press("o")


if __name__ == '__main__':
    test()

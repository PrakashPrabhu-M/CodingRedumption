# https://note.nkmk.me/en/python-pillow-gif/
# https://www.geeksforgeeks.org/how-to-take-screenshots-using-python/
# https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/


# Python program to take
# screenshots
  
import numpy as np
import cv2
import pyautogui
import keyboard
from PIL import Image as im
   
pyautogui.time.sleep(3)
pyautogui.confirm('ok?')
images=[]

# take screenshot using pyautogui
while keyboard.is_pressed('q')==False:
    image = pyautogui.screenshot()
    
    # since the pyautogui takes as a 
    # PIL(pillow) and in RGB we need to 
    # convert it to numpy array and BGR 
    # so we can write it to the disk
    image = cv2.cvtColor(np.array(image),
                        cv2.COLOR_RGB2BGR)
    
    # writing it to the disk using opencv
    image=im.fromarray(image)
    images.append(image)
images[0].save('image.gif',save_all=True, append_images=images[1:], optimize=False, duration=100, loop=0)
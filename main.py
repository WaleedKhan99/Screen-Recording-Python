import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time 

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dim = (width,height)
f  = cv2.VideoWriter_fourcc(*"XVID") # XVID is a formate in which contain all video formats like mp4 etc.
output = cv2.VideoWriter("Python Record.mp4", f, 30.0,dim)
now_start_time = time.time()
dur = 60 # 60 seconds duration of video recording
end_time = now_start_time + dur
while True:
    image = pyautogui.screenshot()
    frame_1 = np.array(image)
    frame = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
    output.write(frame)
    c_time = time.time()  
    if c_time > end_time:
        break
output.release()
print("--- END ---")
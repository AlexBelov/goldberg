#!/usr/bin/env python3
import subprocess
import time

delay_slides = 1
delay_clicking = 0.3

for i in range(1,20):
  subprocess.Popen(["xdotool", "mousemove", "--sync", str(225), str(40)])
  time.sleep(delay_clicking)
  subprocess.Popen(["xdotool", "click", "1"])
  time.sleep(delay_slides)
  subprocess.Popen(["xdotool", "mousemove", "--sync", str(192), str(40)])
  time.sleep(delay_clicking)
  subprocess.Popen(["xdotool", "click", "1"])

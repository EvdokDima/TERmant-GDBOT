import numpy as np
import pyscreenshot
import cv2
from skimage.metrics import structural_similarity as compare_ssim

# Gets one frame
def get_screen():
    # 900x700 (size of GD without the things
    # behind the cube being recorded and the top being cut off)
    screen =  np.array(pyscreenshot.grab(bbox=(150, 40, 620, 450)))
    # Simplify image
    gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    gray_screen = cv2.Canny(gray_screen, threshold1 = 200, threshold2=300)
    return gray_screen

# Compares two following images and returns a boolean fo alive. If the image is the "Restart?"
# screen, structural similarity index will be 0.99+ which means the cube is dead. Else, it's alive.
def isalive(screen1, screen2):
    score, diff = compare_ssim(screen1, screen2, full=True)
    if score > 0.99:
        return False
    else:
        return True
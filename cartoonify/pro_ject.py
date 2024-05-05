# opencv is used for image processing , object detcetion, face recognition and 
# many more

# tkinter is used to make an interactive GUI



import cv2
import easygui # To open the file box
import numpy as np
import imageio # to read image from particular path
import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk,Image
import cartoonify

# filebox returns us the path of chossen file
def upload():
    image_path=easygui.fileopenbox()
    cartoonify(image_path)
upload()
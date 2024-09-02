# openCv2 is used for image processing , object detcetion, face recognition and 
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

# filebox returns us the path of chossen file
def cartoonify(image_path):
    originalmage=cv2.imread(image_path) # storing the image as numbers
    originalmage=cv2.cvtColor(originalmage,cv2.COLOR_BGR2RGB) 

    if originalmage is None:
        print("couldn't find any image, choose appropriate file")
        sys.exit()

    Resized1=cv2.resize(originalmage,(960,540))

    # grayscaling the image

    grayscaleimage=cv2.cvtColor(originalmage,cv2.COLOR_BGR2GRAY)
    Resized2=cv2.resize(grayscaleimage,(960,540))
    
    # smoothening the image
    
    smoothgrayscale=cv2.medianBlur(grayscaleimage,5)
    Resized3=cv2.resize(smoothgrayscale,(960,540))
    
    getEdge = cv2.adaptiveThreshold(smoothgrayscale, 255, 
    cv2.ADAPTIVE_THRESH_MEAN_C, 
    cv2.THRESH_BINARY, 9, 9)
    ReSized4 = cv2.resize(getEdge, (960, 540))
    
    # bilateral filter to remove noise
    
    colorimage=cv2.bilateralFilter(originalmage,9,300,300)
    Resized5=cv2.resize(colorimage,(960,540))
    
    cartoonimage=cv2.bitwise_and(colorimage,colorimage,mask=getEdge)
    global Resized6
    Resized6=cv2.resize(cartoonimage,(960,540))
    plt.imshow(Resized6,cmap='gray')
    t='Image cartoonified! Click on save your image to save'
    tk.messagebox.showinfo(title="Done",message=t)


def upload():
    global image_path
    image_path=easygui.fileopenbox()
    cartoonify(image_path) 
     
    
def save(Resized6,image_path): 
    new_name='cartoon_image'
    path1=os.path.dirname(image_path)
    extension=os.path.splitext(image_path)[1]
    path=os.path.join(path1,new_name+extension)
    cv2.imwrite(path,cv2.cvtColor(Resized6,cv2.COLOR_RGB2BGRA))
    t='Image saved by name' + new_name + ' at ' + path
    tk.messagebox.showinfo(title=None,message=t)




nw=Tk()
nw.geometry('500x500')
nw.title('cartoonify your image')
nw.configure(background='skyblue')

l1=Label(nw,text='',font='bold')
l1.grid(row=0,column=0)

upi=Button(nw,text='select your image',command=upload,height=3,width=20)
upi.configure(background='indigo',foreground='white')
upi.grid(row=1,column=2)

si=Button(nw,text='save your image',command=lambda:save(Resized6,image_path),height=3,width=20) 
si.configure(background='indigo',foreground='white')
l2=Label(nw,text='',font='bold')
l2.grid(row=2,column=0)
l3=Label(nw,text='',font='bold')
l3.grid(row=3,column=0)
si.grid(row=4,column=2)

nw.mainloop()





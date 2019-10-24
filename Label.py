from PIL import Image, ImageTk
from tkinter import Tk
from tkinter.ttk import Frame, Label
import sys
import io
import base64

try:
    from urllib2 import urlopen;
except ImportError:
    # Python3
    import tkinter as tk
    from urllib.request import urlopen

image_url = "https://bbk12e1-cdn.myschoolcdn.com/1142/photo/orig_photo753482_8435714.png?w=1920"

try:
            image_byt = urlopen(image_url).read()
            image_b64 = base64.encodestring(image_byt)
            photo = tk.PhotoImage(data=image_b64)

            cv = tk.Canvas(bg='white')
            cv.pack(side='top', fill='both', expand='yes')
# put the image on the canvas with
# create_image(xpos, ypos, image, anchor)
            cv.create_image(10, 10, image=photo, anchor='nw')


except IOError:
        print("Unable to load image")
        sys.exit(1)


   
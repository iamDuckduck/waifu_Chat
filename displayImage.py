import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import threading
from PIL import ImageFile, Image

ImageFile.LOAD_TRUNCATED_IMAGES = True
class App(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)

        # load initial image from url
        response = requests.get('https://i.pinimg.com/474x/ff/0d/f4/ff0df44c4cd43c7cd964e36b4354e56b.jpg')
        img_data = response.content
        img = Image.open(BytesIO(img_data))

        # convert the image to a Tkinter-compatible object
        self.img_tk = ImageTk.PhotoImage(img)

        # display the image
        self.label = tk.Label(self.root, image=self.img_tk)
        self.label.pack()

        self.root.mainloop()

    def update_label_image(self, image_url):
        # load image from url
        response = requests.get(image_url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))

        # convert the image to a Tkinter-compatible object
        self.img_tk = ImageTk.PhotoImage(img)

        self.label.config(image=self.img_tk)


def switch_image(image):
    app.update_label_image(image)


app = App()

##input('Enter to switch image')

##image = "https://replicate.delivery/pbxt/NAPfBla4Iei7XkdclpHb2PzBhhDJmK2MnD8h3IBLS0VEolfgA/out-0.png"
##app.update_label_image(image)

##input('Enter to switch image')

##switch_image()



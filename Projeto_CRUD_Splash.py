from tkinter import *
from PIL import Image, ImageTk

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()
    def tela(self):
        self.root.title('Cadastro de Moradores')
        self.root.configure(background= '#ffa900')
        self.root.geometry('750x580')
        self.root.resizable(True, True) #Responsividade da tela (Altura x Largura)
        self.root.minsize(width= 300, height= 200)

        icon_image = Image.open('logo_splash.png')  # Substitua pelo caminho do arquivo .png
        icon_photo = ImageTk.PhotoImage(icon_image)
        self.root.iconphoto(True, icon_photo)

Application()


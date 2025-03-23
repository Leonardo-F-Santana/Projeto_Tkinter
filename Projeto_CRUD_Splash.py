from tkinter import *
from PIL import Image, ImageTk

root = Tk() #janela principal

class Application():
    def __init__(self):
        self.root = root #vinculo da classe com objeto
        self.tela() #metodo que configura a tela
        self.frames_de_tela()
        root.mainloop() #outro metodo que mantem a tela ativa independente de interação

    def tela(self): #essa função configura aparencia e comportamento da tela 
        self.root.title('Cadastro de Moradores')
        self.root.configure(background= '#ffa900')
        self.root.geometry('750x580')
        self.root.resizable(True, True) #Responsividade da tela (Altura x Largura)
        self.root.minsize(width= 300, height= 200)

        icon_image = Image.open('logo_splash.png')  # Substitua pelo caminho do arquivo .png
        icon_photo = ImageTk.PhotoImage(icon_image)
        self.root.iconphoto(True, icon_photo)

    def frames_de_tela(self): #parametros da moldura de cima
        self.frame_1 = Frame(self.root, bd= 4, bg="#FFF", highlightbackground="#C0C0C0", highlightthickness=3) # borda, bg do frame, highlightbg cor do fundo e ...thickness largura da borda
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46) #relx = margem lado (entre 0 e 1 = 100%), rely = margem cima (entre 0 e 1), relwidt = largura do frame, relheight = altura do frame

        self.frame_2 = Frame(self.root, bd= 4, bg="#FFF", highlightbackground="#C0C0C0", highlightthickness=3) # borda, bg do frame, highlightbg cor do fundo e ...thickness largura da borda
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    

Application()


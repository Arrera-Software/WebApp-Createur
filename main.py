from tkinter import*
from PIL import Image, ImageTk


class CAWebAppCreator :
    def __init__(self) -> None:
        #Var 
        self.__nameApp = "WebApp Createur"#Definir le nom de l'app
        self.__versionApp = ""#Definir le nom de la version
        self.__imagePath = "image/icon.png"#Indiquer l'emplacement de l'icon
        #Fenetre
        self.__screen = Tk()
        self.__screen.title("Arrera: "+self.__nameApp)
        self.__screen.iconphoto(False,PhotoImage(file=self.__imagePath))
        self.__screen.maxsize(500,500)
        self.__screen.minsize(500,500)
        self.__screen.configure(bg="white")
        #menu
        menu = Menu(self.__screen,tearoff=0)
        menu.add_command(label="A Propos",command=self.__Apropop)
        self.__screen.configure(menu=menu)
    
    def boot(self):
        self.__screen.mainloop()
    
    
    def __Apropop(self):
        #Variable
        copyrightApp = "Copyright Arrera Software by Baptiste P 2023-2024"
        tailleIMG = (100,100)
        #Creation de la fenetre
        about = Toplevel()
        about.iconphoto(False,PhotoImage(file=self.__imagePath))
        about.title("A propos :"+self.__nameApp)
        about.maxsize(400,300)
        about.minsize(400,300)
        about.configure(bg="white")
        #Traitement Image
        imageOrigine = Image.open(self.__imagePath)    
        imageRedim = imageOrigine.resize(tailleIMG)
        icon = ImageTk.PhotoImage(imageRedim)
        #Label
        labelIcon = Label(about,image=icon,bg="white")
        labelName = Label(about,text="\n"+self.__nameApp+"\n",font=("arial","12"),bg="white")
        labelVersion = Label(about,text=self.__versionApp+"\n",font=("arial","11"),bg="white")
        labelCopyright = Label(about,text=copyrightApp,font=("arial","9"),bg="white")
        #affichage
        labelIcon.pack()
        labelName.pack()
        labelVersion.pack()
        labelCopyright.pack()
        about.mainloop()

CAWebAppCreator().boot()
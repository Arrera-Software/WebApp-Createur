from tkinter import*
from PIL import Image, ImageTk


class CAWebAppCreator :
    def __init__(self) -> None:
        #Var 
        self.__nameApp = "WebApp Createur"#Definir le nom de l'app
        self.__versionApp = ""#Definir le nom de la version
        self.__imagePath = "image/icon.png"#Indiquer l'emplacement de l'icon
        self.__background = "white"
        self.__fontground = "black"
        #Fenetre
        self.__screen = Tk()
        self.__screen.title("Arrera: "+self.__nameApp)
        self.__screen.iconphoto(False,PhotoImage(file=self.__imagePath))
        self.__screen.maxsize(500,500)
        self.__screen.minsize(500,500)
        self.__screen.configure(bg=self.__background)
        #menu
        menu = Menu(self.__screen,tearoff=0)
        menu.add_command(label="A Propos",command=self.__Apropop)
        self.__screen.configure(menu=menu)
        #frame
        self.__mainFrame = Frame(self.__screen,bg=self.__background,width=500,height=500)
        frameEntryName = Frame(self.__mainFrame)
        frameEntryLien = Frame(self.__mainFrame)
        #widget
        labelTitre = Label(self.__screen,text="WebApp Createur",font=("arial","15"),bg=self.__background,fg=self.__fontground)
        btnCreate = Button(self.__mainFrame,text="Cree",bg=self.__background,font=("arial","15"),width=40)
        btnSeletIcon = Button(self.__mainFrame,text="Selectionner icone",bg=self.__background,font=("arial","15"),width=40)
        labelIndName = Label(frameEntryName,text="Nom :",font=("arial","15"),bg=self.__background,fg=self.__fontground)
        labelIndLien = Label(frameEntryLien,text="Lien :",font=("arial","15"),bg=self.__background,fg=self.__fontground)
        entryLien = Entry(frameEntryLien,font=("arial","15"),bd=1)
        entryName = Entry(frameEntryName,font=("arial","15"),bd=1)
        #Creation de l'affichage des frames name et lien 
        labelIndLien.pack(side="left")
        labelIndName.pack(side="left") 
        entryLien.pack(side="right")  
        entryName.pack(side="right")
        #placement
        labelTitre.place(x=((self.__mainFrame.winfo_reqwidth()-labelTitre.winfo_reqwidth())//2),y=0)
        frameEntryName.place(x=100,y=100)
        frameEntryLien.place(x=100,y=175)
        btnSeletIcon.place(x=((self.__mainFrame.winfo_reqwidth()-btnSeletIcon.winfo_reqwidth())//2),y=250)
        btnCreate.place(x=((self.__mainFrame.winfo_reqwidth()-btnCreate.winfo_reqwidth())//2),y=300)
        self.__mainFrame.place(x=0,y=0)

    
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
        about.configure(bg=self.__background)
        #Traitement Image
        imageOrigine = Image.open(self.__imagePath)    
        imageRedim = imageOrigine.resize(tailleIMG)
        icon = ImageTk.PhotoImage(imageRedim)
        #Label
        labelIcon = Label(about,image=icon,bg=self.__background)
        labelName = Label(about,text="\n"+self.__nameApp+"\n",font=("arial","12"),bg=self.__background)
        labelVersion = Label(about,text=self.__versionApp+"\n",font=("arial","11"),bg=self.__background)
        labelCopyright = Label(about,text=copyrightApp,font=("arial","9"),bg=self.__background)
        #affichage
        labelIcon.pack()
        labelName.pack()
        labelVersion.pack()
        labelCopyright.pack()
        about.mainloop()

CAWebAppCreator().boot()
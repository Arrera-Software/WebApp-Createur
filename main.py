from tkinter import*
from tkinter.messagebox import*
import requests
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
        self.__screen.title("Arrera : "+self.__nameApp)
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
        self.__selectIcon = Frame(self.__screen,bg=self.__background,width=500,height=500)
        self.__iconLienInternet = Frame(self.__screen,bg=self.__background,width=500,height=500)
        #widget
        #Fenetre principal
        labelTitre = Label(self.__mainFrame,text="WebApp Createur",font=("arial","15"),bg=self.__background,fg=self.__fontground)
        #Main Frame
        btnCreate = Button(self.__mainFrame,text="Cree",bg=self.__background,font=("arial","15"),width=40)
        btnSeletIcon = Button(self.__mainFrame,text="Selectionner une icone",bg=self.__background,font=("arial","15"),width=40,command=self.__viewSelectIcon)
        labelIndName = Label(frameEntryName,text="Nom :",font=("arial","15"),bg=self.__background,fg=self.__fontground)
        labelIndLien = Label(frameEntryLien,text="Lien :",font=("arial","15"),bg=self.__background,fg=self.__fontground)
        entryLien = Entry(frameEntryLien,font=("arial","15"),highlightthickness=1,highlightbackground="black")
        entryName = Entry(frameEntryName,font=("arial","15"),highlightthickness=1,highlightbackground="black")
        #select Icon Frame
        labelTitreSelectIcon = Label(self.__selectIcon,text="Selectionner une icone",font=("arial","15"),bg=self.__background,fg=self.__fontground)
        btnWithFile = Button(self.__selectIcon,text="Fichier",font=("arial","15"),bg=self.__background,fg=self.__fontground,width=40)
        btnWithInternet = Button(self.__selectIcon,text="Internet",font=("arial","15"),bg=self.__background,fg=self.__fontground,width=40,command=self.__lienIconAddView)
        btnExitSelect = Button(self.__selectIcon,text="Annuler",font=("arial","15"),bg=self.__background,fg=self.__fontground,width=40,command=self.__backMain)
        # icon lien Internet
        labelTitreSelectIconInternet = Label(self.__iconLienInternet,text="Metter le lien de l'icone",font=("arial","15"),bg=self.__background,fg=self.__fontground)
        self.__entryLienIcon = Entry(self.__iconLienInternet,font=("arial","15"),highlightthickness=1,highlightbackground="black",width=40)
        btnLienIconInternet = Button(self.__iconLienInternet,font=("arial","15"),text="Valider l'icone",bg=self.__background,fg=self.__fontground,width=40,command=self.__addIconInternet)
        #Creation de l'affichage des frames name et lien 
        labelIndLien.pack(side="left")
        labelIndName.pack(side="left") 
        entryLien.pack(side="right")  
        entryName.pack(side="right")
        #placement
        #Fenetre principal
        labelTitre.place(x=((self.__mainFrame.winfo_reqwidth()-labelTitre.winfo_reqwidth())//2),y=0)
        #Main Frame
        frameEntryName.place(x=100,y=100)
        frameEntryLien.place(x=100,y=175)
        btnSeletIcon.place(x=((self.__mainFrame.winfo_reqwidth()-btnSeletIcon.winfo_reqwidth())//2),y=250)
        btnCreate.place(x=((self.__mainFrame.winfo_reqwidth()-btnCreate.winfo_reqwidth())//2),y=300)
        #select Icon Frame
        labelTitreSelectIcon.place(x=((self.__selectIcon.winfo_reqwidth()-labelTitreSelectIcon.winfo_reqwidth())//2),y=0)
        btnWithFile.place(x=((self.__selectIcon.winfo_reqwidth()-btnWithFile.winfo_reqwidth())//2),y=65)
        btnWithInternet.place(x=((self.__selectIcon.winfo_reqwidth()-btnWithInternet.winfo_reqwidth())//2),y=165)
        btnExitSelect.place(x=((self.__selectIcon.winfo_reqwidth()-btnExitSelect.winfo_reqwidth())//2),
                            y=(self.__selectIcon.winfo_reqheight()-btnExitSelect.winfo_reqheight()))
        #icon lien Internet
        labelTitreSelectIconInternet.place(x=((self.__iconLienInternet.winfo_reqwidth()-labelTitreSelectIconInternet.winfo_reqwidth())//2),y=0)
        self.__entryLienIcon.place(x=((self.__iconLienInternet.winfo_reqwidth()-self.__entryLienIcon.winfo_reqwidth())//2),
                            y=((self.__iconLienInternet.winfo_reqheight()-self.__entryLienIcon.winfo_reqheight())//2))
        btnLienIconInternet.place(x=((self.__iconLienInternet.winfo_reqwidth()-btnLienIconInternet.winfo_reqwidth())//2),
                                  y=(self.__iconLienInternet.winfo_reqheight()-btnLienIconInternet.winfo_reqheight()))
        #Affichage du cadre
        self.__mainFrame.place(x=0,y=0)

    def __backMain(self):
        self.__selectIcon.place_forget()
        self.__iconLienInternet.place_forget()
        self.__mainFrame.place(x=0,y=0)

    def boot(self):
        self.__screen.mainloop()
    
    def __viewSelectIcon(self):
        self.__mainFrame.place_forget()
        self.__selectIcon.place(x=0,y=0)
    
    def __lienIconAddView(self):
        self.__selectIcon.place_forget()
        self.__iconLienInternet.place(x=0,y=0)
        
    def __addIconInternet(self):
        self.__backMain()
        response = requests.get(self.__entryLienIcon.get())
        if response.status_code == 200:
            with open("image.ico", "wb") as f:
                f.write(response.content)
            showinfo("Information","Votre image a été telecharger")
        else:
            showerror("Erreur","Votre image ne peux pas ce telecharger")

        
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
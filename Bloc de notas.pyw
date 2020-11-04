from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.scrolledtext import ScrolledText

root = Tk()
root.title('Bloc de notas')
root.iconbitmap("icono.ico")

def acercaDe():
    messagebox.showinfo('Acerca de','Bloc de notas. Version 0.1')

def salir():
    value = messagebox.askquestion('Salir?','Esta seguro de que desea salir?')
    if value == 'yes':
        root.destroy()


def abrirArchivo():
    fichero = filedialog.askopenfilename(title='Abrir documento',filetypes=(('Documentos de texto','*.txt'),('Todos los archivos','*.*')))
    fichero = open(fichero,'r')
    doc = fichero.read()
    bloctexto.insert(END,doc)
    fichero.close()

def guardarArchivo():
    fichero = filedialog.asksaveasfilename(title='Guardar documento',defaultextension='.txt',filetypes=(('Documentos de texto','*.txt'),('Todos los archivos','*.*')))
    fichero = open(fichero,'w')
    fichero.write(bloctexto.get(1.0,END))


menubar = Menu(root)
root.config(menu=menubar,width=400,height=300)  

archivomenu = Menu(menubar,tearoff=0)
archivomenu.add_command(label='Abrir archivo',command=lambda:abrirArchivo())
archivomenu.add_command(label='Guardar archivo',command=lambda:guardarArchivo())
archivomenu.add_separator()
archivomenu.add_command(label='Salir',command=lambda:salir())

ayudamenu = Menu(menubar,tearoff=0)
ayudamenu.add_command(label='Acerca de',command=lambda:acercaDe())

menubar.add_cascade(label = 'Archivo',menu=archivomenu)
menubar.add_cascade(label = 'Ayuda',menu=ayudamenu)


bloctexto = ScrolledText(root)
bloctexto.pack(expand=True,fill=BOTH)



root.mainloop()

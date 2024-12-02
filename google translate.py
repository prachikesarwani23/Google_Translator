from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text=text1,src=src1,dest=dest1)
    return trans1.text

def data():
    s=comb_sor.get()
    d=comb_dest.get()
    masg=Sor_txt.get(1.0,END)
    textget=change(text=masg,src=s,dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)


root=Tk()
root.title("PRACHI'S GOOGLE TRANSLATOR")
#def wm_geometry(self, newGeometry='500*800'):
    #return self.tk.call('wm', 'geometry', self._w, newGeometry)

#geometry = wm_geometry

root.config(bg='Black')
lab_txt=Label(root,text="Translator",font=("Time New Roman",40,"bold"),bg="Black",fg="Light Blue")
lab_txt.place(x=550,y=30,height=100,width=300)

frame=Frame(root).pack(side=BOTTOM)

lab_txt=Label(root,text="Source Text",font=("Time New Roman",20,"bold"),fg="Light Blue",bg="Black")
lab_txt.place(x=129,y=130,height=20,width=300)

Sor_txt=Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
Sor_txt.place(x=60,y=168,height=250,width=480)

list_text=list(LANGUAGES.values())

comb_sor=ttk.Combobox(frame,value=list_text,font=("Time New Roman",15,"bold"))
comb_sor.place(x=190,y=450,height=60,width=150)
comb_sor.set("English")

button_change=Button(frame,text="Translate",relief=RAISED,command=data,font=("Time New Roman",15,"bold"))
button_change.place(x=620,y=300,height=60,width=150)

comb_dest=ttk.Combobox(frame,value=list_text,font=("Time New Roman",15,"bold"))
comb_dest.place(x=1000,y=450,height=60,width=150)
comb_dest.set("English")

lab_txt=Label(root,text="Destination Text",font=("Time New Roman",20,"bold"),fg="Light Blue",bg="Black")
lab_txt.place(x=950,y=130,height=20,width=300)

dest_txt=Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=850,y=168,height=250,width=480)

root.mainloop()
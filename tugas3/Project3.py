#Nama: Muhammad Alif Taufiqurahman
#Nim: 210511127
#Kelas: R3(C) Teknik Informatika


from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()
root.title('Aplikasi Suara Hewan')
root.config(background='red')

mixer.init()

Label(root, text="Pemutar Suara Hewan mp3", bg='lightyellow', 
      font="Normal 40").grid(row=0, column=0, columnspan=3, pady=10)

def cari():
    file = filedialog.askopenfilename(filetypes=[('mp3', '*.mp3')])
    if file == "":
        return
    mixer.music.load(file)
    t.config(state=NORMAL)
    t.delete(1.0, END)
    t.insert(END, file)
    t.config(state=DISABLED)
b = Button(root, text='Cari', font='Normal 25',command=cari, 
           relief=RIDGE, bd=10, activebackground='yellow')

b.grid(row=1, column=1 , ipadx=30, ipady=5)

t = Text(root, font='Normal 15', bg='lightyellow', wrap=WORD, height=3, width=50)
t.grid(row=2, columnspan=3, pady=15)
t.config(state=DISABLED)

def pause():
    mixer.music.pause()
b1 = Button(root, text='Pause', font="Normal 25", command=pause, relief=RIDGE, bd=10,
            activebackground='red')
b1.grid(row=3, column=0, padx=15, ipadx=15)

def play():
    mixer.music.play(-1)
b2 = Button(root, text='Play', font="Normal 25", command=play, relief=RIDGE, bd=10,
            activebackground='green')
b2.grid(row=3, column=1,padx=10)

def unpause():
    mixer.music.unpause()
b3 = Button(root, text='Unpause', font="Normal 25", command=unpause, relief=RIDGE, bd=10, 
            activebackground='blue')
b3.grid(row=3, column=2, padx=15)

def stop():
    mixer.music.stop()
b4 = Button(root, text='Stop', font="Normal 25", command=stop, relief=RIDGE, bd=10,
            activebackground='red')
b4.grid(row=4, column=1, padx=10, pady=20)

root.mainloop()
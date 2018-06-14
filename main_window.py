from tkinter import *
import tkinter
from Pesel_Faker import Pesel

def create_pesel():
    pesel_entry.configure(text=f'{Pesel.pesel_final}')

# tworzę główne okno
root = tkinter.Tk()
root.columnconfigure(3)

# labelki
pesel_label = tkinter.Label(master=root, text='PESEL')
pesel_label.grid(row=0, column=0)

nip_label = tkinter.Label(master=root, text='NIP')
nip_label.grid(row=1, column=0)

regon_label = tkinter.Label(master=root, text='REGON')
regon_label.grid(row=2, column=0)

#
pesel_entry = tkinter.Label(master=root)
pesel_entry.grid(row=0, column=1, columnspan=2)

nip_entry = tkinter.Entry(master=root)
nip_entry.grid(row=1, column=1, columnspan=2)

regon_entry = tkinter.Entry(master=root)
regon_entry.grid(row=2, column=1, columnspan=2)

# buttony
pesel_button = tkinter.Button(master=root, text='Generuj!', command=lambda: create_pesel())
pesel_button.grid(row=0, column=3, columnspan=2)

nip_button = tkinter.Button(master=root, text='Generuj!')
nip_button.grid(row=1, column=3, columnspan=2)

regon_button = tkinter.Button(master=root, text='Generuj!')
regon_button.grid(row=2, column=3, columnspan=2)

root.title('ULTRA SUPER GENERATOR')
root.mainloop()
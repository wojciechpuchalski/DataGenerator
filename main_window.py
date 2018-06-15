from tkinter import *
import tkinter
from Pesel_Faker import pesel
from NIP_Faker import nip


def create_pesel():
    pesel_entry.configure(text=f'{pesel()}')

def create_nip():
    nip_entry.configure(text=f'{nip()}')

def copy_text_to_clipboard(new):
    root.clipboard_clear()  # clear clipboard contents
    root.clipboard_append(new)  # append new value to clipbaord

# tworzę główne okno
root = tkinter.Tk()
root.columnconfigure(3)
root.title('ULTRA SUPER GENERATOR')

# labelki
pesel_label = tkinter.Label(master=root, text='PESEL:')
pesel_label.grid(row=0, column=0, sticky=E)

nip_label = tkinter.Label(master=root, text='NIP:')
nip_label.grid(row=1, column=0, sticky=E)

regon_label = tkinter.Label(master=root, text='REGON:')
regon_label.grid(row=2, column=0, sticky=E)

#
pesel_entry = tkinter.Label(master=root)
pesel_entry.grid(row=0, column=1, padx=20, pady=10)
pesel_entry.configure(bg='yellow', width=13, height=1, relief=SUNKEN)
pesel_entry.bind("<Button-1>", copy_text_to_clipboard(new=pesel_entry))

nip_entry = tkinter.Label(master=root)
nip_entry.grid(row=1, column=1, padx=20, pady=10)
nip_entry.configure(bg='yellow', width=13, height=1, relief=SUNKEN)

regon_entry = tkinter.Label(master=root)
regon_entry.grid(row=2, column=1, padx=20, pady=10)
regon_entry.configure(bg='yellow', width=13, height=1, relief=SUNKEN)

# buttony
pesel_button = tkinter.Button(master=root, text='Generuj!', command=lambda: create_pesel())
pesel_button.grid(row=0, column=3, columnspan=2)

nip_button = tkinter.Button(master=root, text='Generuj!', command=lambda: create_nip())
nip_button.grid(row=1, column=3, columnspan=2)

regon_button = tkinter.Button(master=root, text='Generuj!')
regon_button.grid(row=2, column=3, columnspan=2)


root.mainloop()
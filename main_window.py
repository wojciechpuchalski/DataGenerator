from tkinter import *
import tkinter
from Pesel_Faker import pesel
from NIP_Faker import nip
from REGON_Faker import regon


def create_pesel():
    pesel_entry.configure(text=f'{pesel()}')

def create_nip():
    nip_entry.configure(text=f'{nip()}')

def create_regon():
    regon_entry.configure(text=f'{regon()}')

def copy_to_clipboard(new):
    root.clipboard_clear()  # clear clipboard contents
    root.clipboard_get()

# tworzę główne okno
root = tkinter.Tk()
root.columnconfigure(5)
root.title('ULTRA SUPER GENERATOR')

# labelki
pesel_label = tkinter.Label(master=root, text='PESEL:')
pesel_label.grid(row=0, column=0, sticky=E)

nip_label = tkinter.Label(master=root, text='NIP:')
nip_label.grid(row=1, column=0, sticky=E)

regon_label = tkinter.Label(master=root, text='REGON:')
regon_label.grid(row=2, column=0, sticky=E)

# style labelek
pesel_entry = tkinter.Label(master=root)
pesel_entry.grid(row=0, column=1, padx=20, pady=10)
pesel_entry.configure(bg='yellow', width=13, height=1, relief=SUNKEN)

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

regon_button = tkinter.Button(master=root, text='Generuj!', command=lambda: create_regon())
regon_button.grid(row=2, column=3, columnspan=2)


# kopiuj do schowka
pesel_copy = tkinter.Button(master=root, text='Kopiuj do schowka', command=lambda: copy_to_clipboard(new=pesel_entry))
pesel_copy.grid(row=0, column=5, columnspan=2)

nip_copy = tkinter.Button(master=root, text='Kopiuj do schowka', command=lambda: copy_to_clipboard(new=nip_entry))
nip_copy.grid(row=1, column=5, columnspan=2)

regon_copy = tkinter.Button(master=root, text='Kopiuj do schowka', command=lambda: copy_to_clipboard(new=regon_entry))
regon_copy.grid(row=2, column=5, columnspan=2)



root.mainloop()
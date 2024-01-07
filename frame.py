import tkinter as tk
from tkinter import ttk

import tkinter as tk
from tkinter import ttk

def on_combobox_change(event):
    frame.pack_forget()  # Nasconde il frame temporaneamente
    # Aggiungi qui il codice da eseguire quando l'elemento del Combobox viene selezionato
    root.update()  # Aggiorna la finestra principale per rimuovere l'effetto di evidenziazione
    frame.pack()  # Mostra nuovamente il frame

root = tk.Tk()

frame = ttk.Frame(root)
frame.pack(pady=10)

# Crea un Combobox all'interno del frame
combobox = ttk.Combobox(frame, values=["Elemento 1", "Elemento 2", "Elemento 3"])
combobox.pack()

# Aggiungi un bind per gestire l'evento di cambio selezione nel Combobox
combobox.bind("<<ComboboxSelected>>", on_combobox_change)

root.mainloop()
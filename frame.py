import tkinter as tk

def mostra_prove():
    print("Mostra Prove")

def clear_list_box():
    print("Cancella Listbox")

root = tk.Tk()
root.title("Esempio con Frames Separati")

# Frame per la colonna 0
frame_colonna_0 = tk.Frame(root)
frame_colonna_0.pack(side="left", padx=10)

# Listbox nella colonna 0
list_box = tk.Listbox(frame_colonna_0, selectmode=tk.MULTIPLE, width=20, height=5)
list_box.grid(row=0, column=0, pady=10)

# Frame per la colonna 1
frame_colonna_1 = tk.Frame(root)
frame_colonna_1.pack(side="left", padx=10)

# Button "Mostra Prove" nella colonna 1
mostra_prove_button = tk.Button(frame_colonna_1, text="Mostra Prove", width=15, height=2, command=mostra_prove)
mostra_prove_button.grid(row=0, column=0, pady=10)

# Frame per la colonna 2
frame_colonna_2 = tk.Frame(root)
frame_colonna_2.pack(side="left", padx=10)

# Button "Cancella" nella colonna 2
clear_listbox = tk.Button(frame_colonna_2, text="Cancella", width=15, height=2, command=clear_list_box)
clear_listbox.grid(row=0, column=0, pady=10)

root.mainloop()
import os
import tkinter as tk
from tkinter import ttk, filedialog
import sys

import os
import tkinter as tk
from tkinter import ttk, filedialog

class PrimaFinestra:
    def __init__(self, root):
        self.root = root
        self.root.title("Easy Math")

        # Imposta le dimensioni della finestra principale
        self.root.geometry("465x800")  # Modifica le dimensioni secondo necessità

        # 1. Option Button per Teoria ed Esercizi
        self.opzione_var = tk.StringVar()
        self.opzione_var.set("Teoria")
        self.opzione_var.trace_add("write", self.aggiorna_primo_menu)  # Aggiungi callback all'opzione_var

        opzione1 = tk.Radiobutton(root, text="Teoria", variable=self.opzione_var, value="Teoria")
        opzione2 = tk.Radiobutton(root, text="Esercizi", variable=self.opzione_var, value="Esercizi")
        opzione1.grid(row=0, column=0, padx=(50, 10), pady=10, sticky="e")
        opzione2.grid(row=0, column=1, padx=(10, 50), pady=10, sticky="w")

                # Aggiungi una label per il tipo di scuola
        label_tipo_scuola = tk.Label(root, text="Livello Scuola")
        label_tipo_scuola.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # 2. Menù a tendina per Tipo Scuola
        self.tipo_scuola_var = tk.StringVar()
        self.tipo_scuola_menu = ttk.Combobox(root, textvariable=self.tipo_scuola_var, state="readonly",width=70)
        self.tipo_scuola_menu.grid(row=2, column=0, pady=5, padx=10, columnspan=2, sticky="ew")

        label_tipo_argomenti = tk.Label(root, text="Argomenti")
        label_tipo_argomenti.grid(row=3, column=0, padx=10, pady=5, sticky="w")


        # 3. Menù a tendina per Argomenti
        self.argomenti_var = tk.StringVar()
        self.argomenti_menu = ttk.Combobox(root, textvariable=self.argomenti_var, state="readonly",width=70)
        
        self.argomenti_menu.grid(row=5, column=0, pady=5, padx=10)  # Modifica le dimensioni secondo necessità
        self.argomenti_menu.grid(row=5, column=0, pady=5, padx=10, columnspan=2, sticky="ew")
        
        # 4. Listbox per selezionare i file
        self.file_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=70, height=30)  # Modifica le dimensioni secondo necessità
        self.file_listbox.grid(row=7, column=0, pady=5, padx=10)  # Modifica le dimensioni secondo necessità
        self.file_listbox.grid(row=7, column=0, pady=5, padx=10, columnspan=3, sticky="ew")
        # 5. Tasto Apri
        apri_tasto = tk.Button(root, text="Apri", width=30, height=5, command=self.apri_file_selezionato)
        apri_tasto.grid(row=12, column=0, padx=10,pady=5, columnspan=2, sticky="ew")

        # 6. Menu in cima
        barra_menu = tk.Menu(root)
        root.config(menu=barra_menu)

        # Menu File
        menu_file = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="File", menu=menu_file)
        menu_file.add_command(label="Esci", command=root.destroy)

        # Menu Strumenti
        menu_strumenti = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Strumenti", menu=menu_strumenti)
        menu_strumenti.add_command(label="Generatore Verifiche", command=self.apri_seconda_finestra)

        nomi_cartelle = [nome for nome in os.listdir(path_teoria) if os.path.isdir(os.path.join(path_teoria, nome))]
        self.tipo_scuola_menu["values"] = nomi_cartelle

        # Collega la funzione di aggiornamento del secondo menù all'evento di cambio del primo menù
        #self.tipo_scuola_menu.bind("<<ComboboxSelected>>", self.aggiorna_argomenti_menu)

        self.tipo_scuola_var.trace_add("write", self.aggiorna_argomenti_menu)
        self.opzione_var.trace_add("write", self.aggiorna_argomenti_menu)

        self.argomenti_var.trace_add("write", self.aggiorna_lista_file)
        self.opzione_var.trace_add("write", self.aggiorna_lista_file)

    def aggiorna_primo_menu(self, *args):
        # Callback chiamata quando cambia il valore di opzione_var
        # Aggiorna il primo menù a tendina in base alla scelta dell'opzione
        global path_teoria
        opzione_selezionata = self.opzione_var.get()
        path=parent_directory+'\\'+opzione_selezionata
        nomi_cartelle = [nome for nome in os.listdir(path) if os.path.isdir(os.path.join(path, nome))]
        self.tipo_scuola_menu["values"] = nomi_cartelle
        self.argomenti_menu.set("")  # Imposta il menù a tendina degli 

    def apri_file_selezionato(self):
        # Ottieni l'indice del file selezionato nella Listbox
        indice_selezionato = self.file_listbox.curselection()
        tipo_scuola_selezionato = self.tipo_scuola_menu.get()
        opzione_selezionata = self.opzione_var.get()
        tipo_arg = self.argomenti_menu.get()

        if indice_selezionato:
            # Ottieni il nome del file selezionato
            nome_file = self.file_listbox.get(indice_selezionato[0])
            path_file=parent_directory+'\\'+opzione_selezionata+'\\'+tipo_scuola_selezionato+'\\'+tipo_arg+'\\'+nome_file
            os.startfile(path_file)

    def apri_seconda_finestra(self):
        # Implementa la logica per aprire la seconda finestra
        pass

    def aggiorna_argomenti_menu(self, *args):
        # Callback chiamata quando cambia la selezione nel menù a tendina Tipo Scuola
        self.argomenti_menu.set("")  # Imposta il menù a tendina degli 
        tipo_scuola_selezionato = self.tipo_scuola_menu.get()
        opzione_selezionata = self.opzione_var.get()
        if tipo_scuola_selezionato:
        # Aggiorna il menù a tendina degli argomenti in base ai valori selezionati
        # Ad esempio, puoi combinare i valori di tipo_scuola_selezionato e opzione_selezionata per ottenere i percorsi corretti
            path_arg=parent_directory+'\\'+opzione_selezionata+'\\'+tipo_scuola_selezionato
            nomi_cartelle = [nome for nome in os.listdir(path_arg) if os.path.isdir(os.path.join(path_arg, nome))]
            self.argomenti_menu ["values"] = nomi_cartelle
        else:
        # Se Tipo Scuola non è selezionato, mostra una lista vuota
            self.argomenti_menu["values"] = []

    def aggiorna_lista_file(self, *args):
        # Ottieni il percorso della cartella selezionata nel menù a tendina Tipo Scuola
        tipo_scuola_selezionato = self.tipo_scuola_menu.get()
        opzione_selezionata = self.opzione_var.get()
        tipo_arg = self.argomenti_menu.get()
        cartella_selezioanta=parent_directory+'\\'+opzione_selezionata+'\\'+tipo_scuola_selezionato+'\\'+tipo_arg

        if tipo_arg:
        # Leggi la lista dei file nella cartella
            try:
                lista_file = os.listdir(cartella_selezioanta)
            except FileNotFoundError:
                lista_file = []
        else:
             lista_file = []
            # Aggiorna la Listbox con i nomi dei file
        self.file_listbox.delete(0, tk.END)  # Cancella i vecchi elementi
        for file in lista_file:
            self.file_listbox.insert(tk.END, file)



if __name__ == "__main__":
    global current_dir 
    global parent_directory
    global path_teoria
    current_dir = sys.argv[0]
    parent_directory = os.path.dirname(current_dir)
    path_teoria=parent_directory+"\\Teoria"
    root = tk.Tk()
    finestra = PrimaFinestra(root)
    root.mainloop()
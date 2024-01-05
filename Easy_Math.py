import os
import time  
import timeit
from datetime import date
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk, filedialog
import sys
import subprocess
import io
import json
import tkinter as tk
from PIL import Image
import json
import tkinter as tk
from tkinter import messagebox
import random
from tkinter import ttk, filedialog
from tkinter import scrolledtext
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
from io import BytesIO
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import re
from sympy import symbols, Eq, solve, preview
import pdfplumber

class PrimaFinestra:
    def __init__(self, root):
        self.root = root
        self.root.title("Easy Math")

        # Imposta le dimensioni della finestra principale
        self.root.geometry("518x865")  # Modifica le dimensioni secondo necessità

        row_init=0
        column_init=0


        # 1. Option Button per Teoria ed Esercizi
        self.opzione_var = tk.StringVar()
        self.opzione_var.set("Teoria")


        opzione1 = tk.Radiobutton(root, text="Teoria", variable=self.opzione_var, value="Teoria")
        opzione2 = tk.Radiobutton(root, text="Esercizi", variable=self.opzione_var, value="Esercizi")
        opzione1.grid(row=row_init, column=column_init, padx=(50, 10), pady=10, sticky="e")
        opzione2.grid(row=row_init, column=column_init+1, padx=(10, 50), pady=10, sticky="w")

        # Aggiungi una label per il tipo di scuola
        label_tipo_scuola = tk.Label(root, text="Livello Scuola:")
        label_tipo_scuola.grid(row=row_init+1, column=column_init, padx=10, pady=5, sticky="w")

        # 2. Menù a tendina per Tipo Scuola
        self.tipo_scuola_var = tk.StringVar()
        self.tipo_scuola_menu = ttk.Combobox(root, textvariable=self.tipo_scuola_var, state="readonly",width=70)
        self.tipo_scuola_menu.grid(row=row_init+2, column=column_init, pady=5, padx=10, columnspan=2, sticky="ew")


        # Aggiungi una label per il tipo di materia
        label_tipo_materia = tk.Label(root, text="Materia:")
        label_tipo_materia.grid(row=row_init+3, column=column_init, padx=10, pady=5, sticky="w")
        # 3. Menù a tendina per Matera
        self.materia_var = tk.StringVar()
        self.materia_menu = ttk.Combobox(root, textvariable=self.materia_var, state="readonly",width=70)
        
        self.materia_menu.grid(row=row_init+4, column=column_init, pady=5, padx=10)  # Modifica le dimensioni secondo necessità
        self.materia_menu.grid(row=row_init+4, column=column_init, pady=5, padx=10, columnspan=2, sticky="ew")


      
        label_tipo_argomenti = tk.Label(root, text="Argomenti:")
        label_tipo_argomenti.grid(row=row_init+6, column=column_init, padx=10, pady=5, sticky="w")
        # 3. Menù a tendina per Argomenti
        self.argomenti = []
        self.filtered_argomenti = []
        self.argomenti_var = tk.StringVar()
        self.argomenti_menu = ttk.Combobox(root, textvariable=self.argomenti_var, state="readonly",width=70)
        
        self.search_entry = tk.Entry(root, width=70,foreground="gray", font=("Arial", 10, "italic"))
        self.search_entry.insert(0, "Cerca...")
        self.search_entry.grid(row=row_init+7, column=column_init, pady=5, padx=10, columnspan=2, sticky="ew")


        self.argomenti_menu.grid(row=row_init+8, column=column_init, pady=5, padx=10)  # Modifica le dimensioni secondo necessità
        self.argomenti_menu.grid(row=row_init+8, column=column_init, pady=5, padx=10, columnspan=2, sticky="ew")



        # 4. Listbox per selezionare i file
        self.file_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=70, height=30)  # Modifica le dimensioni secondo necessità
        self.file_listbox.grid(row=row_init+10, column=column_init, pady=5, padx=10)  # Modifica le dimensioni secondo necessità
        self.file_listbox.grid(row=row_init+10, column=column_init, pady=5, padx=10, columnspan=3, sticky="ew")
        # 5. Tasto Apri
        apri_tasto = tk.Button(root, text="Apri", width=30, height=5, command=self.apri_file_selezionato)
        apri_tasto.grid(row=row_init+15, column=column_init, padx=10,pady=5, columnspan=2, sticky="ew")

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
        menu_strumenti.add_command(label="Estrai Esercizi da PDF", command=self.estrai_esercizi_da_pdf)

        nomi_cartelle = [nome for nome in os.listdir(path_teoria) if os.path.isdir(os.path.join(path_teoria, nome))]
        self.tipo_scuola_menu["values"] = nomi_cartelle

        # Collega la funzione di aggiornamento del secondo menù all'evento di cambio del primo menù
        #self.tipo_scuola_menu.bind("<<ComboboxSelected>>", self.aggiorna_argomenti_menu)

        self.opzione_var.trace_add("write", self.aggiorna_primo_menu) 


        self.tipo_scuola_var.trace_add("write", self.aggiorna_materia_menu)
        self.opzione_var.trace_add("write", self.aggiorna_materia_menu)

        self.tipo_scuola_var.trace_add("write", self.aggiorna_argomenti_menu)
        self.materia_var.trace_add("write", self.aggiorna_argomenti_menu)
        self.opzione_var.trace_add("write", self.aggiorna_argomenti_menu)

        self.argomenti_var.trace_add("write", self.aggiorna_lista_file)
        self.opzione_var.trace_add("write", self.aggiorna_lista_file)

        self.update_combobox()
        self.search_entry.bind("<FocusIn>", self.clear_placeholder)
        self.search_entry.bind("<FocusOut>", self.restore_placeholder)
        self.search_entry.bind("<KeyRelease>", self.filter_items)

    def update_combobox(self):
        tipo_scuola_selezionato = self.tipo_scuola_menu.get()
        materia_selezionata= self.materia_menu.get()
        opzione_selezionata = self.opzione_var.get()
        if materia_selezionata:
        # Aggiorna il menù a tendina degli argomenti in base ai valori selezionati
        # Ad esempio, puoi combinare i valori di tipo_scuola_selezionato e opzione_selezionata per ottenere i percorsi corretti
            path_arg=parent_directory+'\\'+opzione_selezionata+'\\'+tipo_scuola_selezionato +'\\'+materia_selezionata

            self.argomenti= [nome for nome in os.listdir(path_arg) if os.path.isdir(os.path.join(path_arg, nome))]
            self.argomenti_menu["values"] = self.filtered_argomenti

    def filter_items(self, event):
        search_text = self.search_entry.get().lower()
        self.filtered_argomenti = [argomento for argomento in self.argomenti if search_text in argomento.lower()]
        self.update_combobox()

    def clear_placeholder(self, event):
        if self.search_entry.get() == "Cerca...":
            self.search_entry.delete(0, tk.END)
            self.search_entry.config(foreground="black", font=("Arial", 10, "normal"))

    def restore_placeholder(self, event):
        if not self.search_entry.get():
            self.search_entry.insert(0, "Cerca...")
            self.search_entry.config(foreground="gray", font=("Arial", 10, "italic"))    
  
    def aggiorna_primo_menu(self, *args):
        # Callback chiamata quando cambia il valore di opzione_var
        # Aggiorna il primo menù a tendina in base alla scelta dell'opzione
        global path_teoria
        opzione_selezionata = self.opzione_var.get()
        path=parent_directory+'\\'+opzione_selezionata
        nomi_cartelle = [nome for nome in os.listdir(path) if os.path.isdir(os.path.join(path, nome))]
        self.tipo_scuola_menu["values"] = nomi_cartelle
        self.argomenti_menu.set("")  # Imposta il menù a tendina degli 
        self.materia_menu.set("")  # Imposta il menù a tendina degli 

    def aggiorna_materia_menu(self, *args):
        # Callback chiamata quando cambia la selezione nel menù a tendina Tipo Scuola
        self.argomenti_menu.set("")
        self.materia_menu.set("")  # Imposta il menù a tendina degli   # Imposta il menù a tendina degli 
        tipo_scuola_selezionato = self.tipo_scuola_menu.get()  
        opzione_selezionata = self.opzione_var.get()
        if tipo_scuola_selezionato:
        # Aggiorna il menù a tendina degli argomenti in base ai valori selezionati
        # Ad esempio, puoi combinare i valori di tipo_scuola_selezionato e opzione_selezionata per ottenere i percorsi corretti
            path_materia=parent_directory+'\\'+opzione_selezionata+'\\'+tipo_scuola_selezionato 
            nomi_cartelle = [nome for nome in os.listdir(path_materia) if os.path.isdir(os.path.join(path_materia, nome))]
            self.materia_menu ["values"] = nomi_cartelle
        else:
        # Se Tipo Scuola non è selezionato, mostra una lista vuota
            self.argomenti_menu["values"] = []

    def aggiorna_argomenti_menu(self, *args):
        # Callback chiamata quando cambia la selezione nel menù a tendina Tipo Scuola
        self.argomenti_menu.set("")  # Imposta il menù a tendina degli 
        tipo_scuola_selezionato = self.tipo_scuola_menu.get()
        materia_selezionata= self.materia_menu.get()
        opzione_selezionata = self.opzione_var.get()
        if materia_selezionata:
        # Aggiorna il menù a tendina degli argomenti in base ai valori selezionati
        # Ad esempio, puoi combinare i valori di tipo_scuola_selezionato e opzione_selezionata per ottenere i percorsi corretti
            path_arg=parent_directory+'\\'+opzione_selezionata+'\\'+tipo_scuola_selezionato +'\\'+materia_selezionata
            try:
                self.argomenti= [nome for nome in os.listdir(path_arg) if os.path.isdir(os.path.join(path_arg, nome))]
                self.filtered_argomenti = self.argomenti
                self.argomenti_menu ["values"] = self.filtered_argomenti

            except FileNotFoundError:
                print(f"")
        
        else:
        # Se Tipo Scuola non è selezionato, mostra una lista vuota
            self.argomenti_menu["values"] = []

    def aggiorna_lista_file(self, *args):
        # Ottieni il percorso della cartella selezionata nel menù a tendina Tipo Scuola
        tipo_scuola_selezionato = self.tipo_scuola_menu.get()
        opzione_selezionata = self.opzione_var.get()
        tipo_arg = self.argomenti_menu.get()
        materia_selezionata= self.materia_menu.get()
        cartella_selezioanta=parent_directory+'\\'+opzione_selezionata+'\\'+tipo_scuola_selezionato+'\\'+materia_selezionata+'\\'+tipo_arg

        if tipo_arg:
        # Leggi la lista dei file nella cartella
            try:
                lista_file = os.listdir(cartella_selezioanta)
            except FileNotFoundError:
                print("nessun file trovato")
                lista_file = []
        else:
             lista_file = []
            # Aggiorna la Listbox con i nomi dei file
        self.file_listbox.delete(0, tk.END)  # Cancella i vecchi elementi
        for file in lista_file:
            self.file_listbox.insert(tk.END, file)
    
    def apri_file_selezionato(self):
        # Ottieni l'indice del file selezionato nella Listbox
         indice_selezionato = self.file_listbox.curselection()
         tipo_scuola_selezionato = self.tipo_scuola_menu.get()
         opzione_selezionata = self.opzione_var.get()
         materia_selezionata= self.materia_menu.get()
         tipo_arg = self.argomenti_menu.get()
                 

         if indice_selezionato:
             # Ottieni il nome del file selezionato
             nome_file = self.file_listbox.get(indice_selezionato[0])
             path_file=parent_directory+'\\'+opzione_selezionata+'\\'+tipo_scuola_selezionato+'\\'+materia_selezionata+'\\'+tipo_arg+'\\'+nome_file
             os.startfile(path_file)

    def estrai_esercizi_da_pdf(self):
        indice_selezionato = self.file_listbox.curselection()
        tipo_scuola_selezionato = self.tipo_scuola_menu.get()
        opzione_selezionata = self.opzione_var.get()
        tipo_arg = self.argomenti_menu.get()
        materia_selezionata= self.materia_menu.get()
        output_file=parent_directory+'\\Output Esercizi\\'
        if indice_selezionato:
             # Ottieni il nome del file selezionato
             nome_file = self.file_listbox.get(indice_selezionato[0])
             path_file=parent_directory+'\\'+opzione_selezionata+'\\'+tipo_scuola_selezionato+'\\'+materia_selezionata+'\\'+tipo_arg+'\\'+nome_file
             #os.startfile(path_file)

        with pdfplumber.open(path_file) as pdf:
           with open(output_file+nome_file+'.txt', "w", encoding="utf-8") as text_file:
            for page in pdf.pages:
                testo_pagina = page.extract_text()
                text_file.write(testo_pagina)
                text_file.write("\n")  # Aggiungi un separatore tra le pagine
            
        
        os.startfile(output_file)

    def apri_seconda_finestra(self):
         generatore_verifiche = GeneratoreVerifiche((self.root))
         generatore_verifiche.run()

class GeneratoreVerifiche:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Generatore Verifiche")
        self.root.geometry("770x800")
        self.opzione_media = tk.StringVar(value="Medie")
        opzione_media_button = ttk.Radiobutton(self.root, text="Medie", variable=self.opzione_media, value="Medie", command=self.aggiorna_tipo_materia_menu)
        opzione_superiore_button = ttk.Radiobutton(self.root, text="Superiori", variable=self.opzione_media, value="Superiori", command=self.aggiorna_tipo_materia_menu)
        self.opzione_media.trace_add("write", self.svuota_combobox) 
      

        # Strutture per gli esercizi
        self.strutture = []
        for _ in range(5):
            struttura = self.crea_struttura()
            self.strutture.append(struttura)

        # Pulsanti
        seleziona_button = ttk.Button(self.root, text="Mostra Esercizi", command=self.mostra_esercizi)
        genera_test_button = ttk.Button(self.root, text="Genera Test", command=self.genera_test_casuale)
        btn_clear = ttk.Button(self.root, text="Clear", command=self.clear_list_box)

        # Posizionamento degli elementi
        opzione_media_button.grid(row=0, column=0, columnspan=2, padx=(50, 10), pady=10,sticky="w")
        opzione_superiore_button.grid(row=0, column=2, columnspan=2,padx=(10, 50), pady=10, sticky="w")

        for i, struttura in enumerate(self.strutture):
            struttura.grid(row=i+1, column=0, columnspan=4,padx=7, pady=5)

        #self.text_box = scrolledtext.ScrolledText(self.root, width=65, height=10)
        self.list_box = tk.Listbox(self.root, selectmode=tk.MULTIPLE, width=120, height=30)
        self.list_box.grid(row=len(self.strutture)+1, column=1, columnspan=2,padx=7, pady=7,rowspan=5)

        seleziona_button.grid(row=len(self.strutture)+10, column=0, columnspan=2, pady=10)
        genera_test_button.grid(row=len(self.strutture)+10, column=2, columnspan=2, pady=10)
        btn_clear.grid(row=len(self.strutture)+12, column=2, columnspan=2, pady=10)


         # Dichiarazione della variabile globale
        self.soluzione_checkbox_var = tk.IntVar()
        # Aggiungi un check box e un testo con l'etichetta "Soluzione"
        self.soluzione_checkbox = ttk.Checkbutton(self.root, text="Soluzione", variable=self.soluzione_checkbox_var)
        self.soluzione_checkbox.grid(row=len(self.strutture)+10, column=0,columnspan=2, padx=25,pady=10, sticky="w")



         # 6. Menu in cima
        barra_menu = tk.Menu(self.root)
        self.root.config(menu=barra_menu)

        # Menu File
        menu_file = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="File", menu=menu_file)
        menu_file.add_command(label="Esci", command=self.root.destroy)

        # Menu Strumenti
        menu_strumenti = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Strumenti", menu=menu_strumenti)
        menu_strumenti.add_command(label="Estrai Argomenti da JSON", command=self.estrai_argomenti_json)
        menu_strumenti.add_command(label="Check Duplicati JSON", command=self.find_duplicates)

    
    def estrai_argomenti_json(self):
        tipo_scelto =   self.opzione_media.get()
        primo_combobox = self.strutture[0].comboboxes[0]
        materia_es = primo_combobox.get()
        percorso_json = parent_directory+'\\Verifiche Input\\'+tipo_scelto+'\\'+materia_es
        json_file = [f for f in os.listdir(percorso_json) if f.endswith('.json')][0]
        json_path = os.path.join(percorso_json, json_file)
        output_file=parent_directory+'\\Output Esercizi\\'

        # Leggi il JSON
        if os.path.exists(json_path):
            with open(json_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

                    # Estrai gli argomenti unici
            argomenti_unici = list(set(esercizio["argomento"] for esercizio in data["esercizi"]))
            with open(output_file+tipo_scelto+'_'+materia_es+'_Argomenti_JSON.txt', "w", encoding="utf-8") as file:
                    for argomento in argomenti_unici:
                        file.write(f"{argomento}\n")

        
        os.startfile(output_file)
         
    def crea_struttura(self):
       
        struttura = ttk.Frame(self.root)
        

        # Rimuovi il quadrato nero dentro dai check button
        check_button = ttk.Checkbutton(struttura, command=self.abilita_disabilita_combobox)
        tipo_materia_var = tk.StringVar()
        tipo_materia_label = tk.Label(struttura, text="Tipo Materia", background="lightgray")
        tipo_materia_menu = ttk.Combobox(struttura, textvariable=tipo_materia_var, values=["Aritmetica", "Geometria"], state="disabled", background="lightgray")
        argomenti_label = tk.Label(struttura, text="Argomenti", background="lightgray")
        argomenti_menu = ttk.Combobox(struttura, state="disabled", background="lightgray",width=30)
        numeri_label = tk.Label(struttura, text="Numero Esercizi", background="lightgray")
        numeri_menu = ttk.Combobox(struttura, values=list(range(1, 11)) + ["Tutti"], state="disabled", background="lightgray")

        check_button.grid(row=0, column=0, sticky="w")
        tipo_materia_label.grid(row=0, column=1, sticky="w")
        tipo_materia_menu.grid(row=0, column=2, sticky="w")
        argomenti_label.grid(row=0, column=3, sticky="w")
        argomenti_menu.grid(row=0, column=4, sticky="w")
        numeri_label.grid(row=0, column=5, sticky="w")
        numeri_menu.grid(row=0, column=6, sticky="w")

        # Aggiungi le combobox alla lista delle combobox della struttura
        struttura.comboboxes = [tipo_materia_menu, argomenti_menu, numeri_menu]

        struttura.tipo_materia_var = tipo_materia_var

        self.bind_combobox_selected(tipo_materia_menu, self.aggiorna_tipo_argomento, argomenti_menu)

        return struttura

    def bind_combobox_selected(self, widget, callback, *args):
         widget.bind("<<ComboboxSelected>>", lambda event, arg_combobox=args[0]: callback(event, arg_combobox, *args[1:]))

    def abilita_disabilita_combobox(self):
        # Ottieni il check button che ha generato l'evento
        check_button = self.root.focus_get()
        
        # Ottieni la struttura a cui appartiene il check button
        struttura = check_button.master

        # Ottieni lo stato del check button
        stato_check = tk.BooleanVar(value=check_button.instate(['selected']))

        # Abilita/disabilita tutte le combobox della struttura in base allo stato del check button
        for combo in struttura.comboboxes:
            combo["state"] = "readonly" if stato_check.get() else "disabled"

    def aggiorna_tipo_materia_menu(self):
    # Ottieni il valore dell'opzione button (Medie o Superiore)
        tipo_scelto =   self.opzione_media.get()

        # Imposta il percorso in base alla scelta
        path_arg=parent_directory+'\\Verifiche Input\\'+tipo_scelto


        # Ottieni la lista dei nomi delle cartelle nel percorso
        nomi_cartelle = [d for d in os.listdir(path_arg) if os.path.isdir(os.path.join(path_arg, d))]
        for struttura in self.strutture:
            prima_combobox = struttura.comboboxes[0]
            prima_combobox["values"] = nomi_cartelle
    
    def aggiorna_tipo_argomento(self, event, arg_combobox, *args):
        idx = arg_combobox.master.grid_info()["row"]
   
        #tipo_materia = args[0].get()
        tipo_scelto =   self.opzione_media.get()
        materia_es = event.widget.get()
        percorso_json = parent_directory+'\\Verifiche Input\\'+tipo_scelto+'\\'+materia_es
        json_file = [f for f in os.listdir(percorso_json) if f.endswith('.json')][0]
        json_path = os.path.join(percorso_json, json_file)

        # Leggi il JSON
        if os.path.exists(json_path):
            with open(json_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

                    # Estrai gli argomenti unici
            argomenti_unici = list(set(esercizio["argomento"] for esercizio in data["esercizi"]))
            # Aggiorna la combobox degli argomenti nella stessa struttura
            struttura = self.strutture[idx-1]
            argomenti_menu = struttura.comboboxes[1]
            argomenti_menu["values"] = argomenti_unici
            argomenti_menu.set("")  # Azzera la selezione precedente
        else:
            # Il JSON non esiste, gestisci l'errore o fai qualcos'altro
            pass

    def svuota_combobox(self, *args):
    # Svuota tutti i Combobox in tutte le strutture
        
        for struttura in self.strutture:
    # Accedi alla prima combobox di ogni struttura
            prima_combobox = struttura.comboboxes[0]
            prima_combobox.set("")

        for struttura in self.strutture:
            for combobox in struttura.comboboxes:
                combobox.set("")

    def mostra_esercizi(self):
        #finestra_selezione = tk.Toplevel(self.root)
        #finestra_selezione.title("Seleziona Esercizi")
        esercizi = []
        dati_inseriti = self.leggi_dati()
        for riga in dati_inseriti:
            tipo_scuola, tipo_materia, tipo_argomento, num_esercizi = riga

            # Costruisci il percorso del JSON
            percorso_json = parent_directory+'\\Verifiche Input\\'+tipo_scuola+'\\'+tipo_materia
            json_file = [f for f in os.listdir(percorso_json) if f.endswith('.json')][0]
            json_path = os.path.join(percorso_json, json_file)
          

            # Leggi gli esercizi dal JSON
            esercizi_disponibili = self.leggi_esercizi_da_json(json_path,tipo_argomento)

            # Scegli 'num_esercizi' esercizi in modo casuale
            if num_esercizi=='Tutti':
                esercizi_selezionati=esercizi_disponibili
            else:
                esercizi_selezionati = random.sample(esercizi_disponibili, int(num_esercizi))

            # Aggiungi gli esercizi alla lista generale
            esercizi.extend(esercizi_selezionati)


            #self.text_box.delete(1.0, tk.END)
        self.esercizi_generati = esercizi
           # Aggiunta degli esercizi alla text box
        a=1
        for esercizio in esercizi: 
            if self.soluzione_checkbox_var.get() == 1: 
                espressione_pattern_es = self.converti_latex_to_pattern(esercizio['esercizio'])
                espressione_pattern_sol = self.converti_latex_to_pattern(esercizio['soluzione'])
                self.list_box.insert(tk.END, f"Argomento: {esercizio['argomento']} | Esercizio {a}:  {espressione_pattern_es} | Soluzione:  {espressione_pattern_sol} \n")
                a+=1        
            else:
                espressione_pattern = self.converti_latex_to_pattern(esercizio['esercizio'])
            
                self.list_box.insert(tk.END, f"Argomento: {esercizio['argomento']}   |   Esercizio {a} :  {espressione_pattern}  \n")
                a+=1
    
    def genera_test_casuale(self):
        # Ottieni gli indici degli elementi selezionati
        selezionati = self.list_box.curselection()

        if selezionati:
            es_selezionato = self.esercizi_generati[selezionati[0]]
            current_datetime = datetime.now().strftime("%Y%m%d")
            tipo_mat = es_selezionato["tipo_materia"]
            path_output=parent_directory+'\\Verifiche Output\\'
            latex_filename_path = f"{path_output}Verifica_{tipo_mat}_{current_datetime}.tex"
            #self.crea_file_pdf_canvas(path_output, tipo_mat, current_datetime,self.esercizi_generati,selezionati)
            self.crea_file_latex(latex_filename_path,selezionati,self.esercizi_generati)
            output_file_name=self.compile_latex(latex_filename_path)
            os.startfile(output_file_name)   
        else:     
            es_selezionato = self.esercizi_generati[0]
            current_datetime = datetime.now().strftime("%Y%m%d")
            tipo_mat = es_selezionato["tipo_materia"]
            path_output=parent_directory+'\\Verifiche Output\\'
            latex_filename_path = f"{path_output}Verifica_{tipo_mat}_{current_datetime}.tex"
            #self.crea_file_pdf_canvas(path_output, tipo_mat, current_datetime,self.esercizi_generati)
            self.crea_file_latex(latex_filename_path,selezionati,self.esercizi_generati)
            output_file_name=self.compile_latex(latex_filename_path)
            os.startfile(output_file_name)   

    def converti_latex_to_pattern(self,espressione_latex):

        text=espressione_latex
         # Sostituisci il simbolo di integrale
        text = re.sub(r'\\int', '\u222b', text)

        text = re.sub(r'\\begin{cases}', '{', text)
        text = re.sub(r'\\end{cases}', '', text)

        # Sostituisci il pattern per la frazione
        text = re.sub(r'\\frac{(.*?)}{(.*?)}', r'\1/\2', text)

        # Sostituisci altri pattern specifici
        text = re.sub(r'\\sin', 'sin', text)

        text = re.sub(r'\\cos', 'cos', text)

        text = re.sub(r'\\tan', 'tan', text)

        text = re.sub(r'\\log', 'log', text)

        text = re.sub(r'\\lim_{{([^}}]+)}}', r'lim{\1}', text)

        text = re.sub(r'\\infty', 'inf', text)
        
        
        
        # Decodifica gli esponenti
        text = re.sub(r'\^(\d+)', lambda match: ''.join(['⁰¹²³⁴⁵⁶⁷⁸⁹'[int(digit)] for digit in match.group(1)]), text)
                # Decodifica gli esponenti
         
        # Sostituzioni dei simboli matematici
        text = text.replace('=', ' = ')
        text = text.replace('(', ' ( ')
        text = text.replace(')', ' ) ')
        text = text.replace('+', ' + ')
        text = text.replace('-', ' - ')

        # Sostituzione della radice quadrata con il simbolo Unicode
        text = re.sub(r'\\sqrt{([^}]+)}', lambda match: '√(' + match.group(1) + ')', text)

        text = re.sub(r'e\^{?(\w+)}?', lambda match: 'e^(' + match.group(1) + ')', text)
        text = re.sub(r'e\^\((\w+)\)', lambda match: 'e^(' + match.group(1) + ')', text)


        # Sostituzione delle parole nella forma \\text{parola} con solo "parola"
        text = re.sub(r'\\text{([^}]+)}', lambda match: match.group(1), text)

        # Sostituzione di "\\quad x \\neq" con "x ≠"
        text = text.replace('\\quad x \\neq', 'x ≠')

        # Sostituzione di "\\quad x \\neq \\pm x" con "x ≠ ± "
        text = re.sub(r'\\pm', '±', text)

        text = re.sub(r'\\geq', '>=', text)

        text = re.sub(r'\\leq', '<=', text)



        
        return text


######################crea pdf formato canvas non simboli matematici################################

    def crea_file_pdf_canvas(self, path_output, tipo_mat, current_datetime,vettore,selezionati):
        y_start = 750
        pdf_filename_path = f"{path_output}Verifica_{tipo_mat}_{current_datetime}.pdf"
        c = canvas.Canvas(pdf_filename_path)
        if selezionati:
            for indice in selezionati:
                esercizio = self.esercizi_generati[indice]
                argomento = esercizio['argomento']
                testo_esercizio = esercizio['esercizio']
                soluzione = esercizio['soluzione']
                self.scrivi_esercizio_pdf(c, indice, argomento, testo_esercizio, soluzione,y_start)
                y_start -= 150

            c.save()
        else:
            for indice, esercizio in enumerate(vettore):
                esercizio = self.esercizi_generati[indice]
                argomento = esercizio['argomento']
                testo_esercizio = esercizio['esercizio']
                soluzione = esercizio['soluzione']
                y_start=self.scrivi_esercizio_pdf(c, indice, argomento, testo_esercizio, soluzione,y_start)
                y_start -= 150

            c.save()

    def scrivi_esercizio_pdf(self,c, numero, argomento, testo_esercizio, soluzione,y_start):

        dist_es_sol=70
        
        # Verifica se c'è spazio sufficiente per scrivere l'esercizio sulla pagina corrente
        if y_start < 100:
            # Cambia pagina se non c'è spazio sufficiente
            c.showPage()
            y_start = 750  # Ripristina la coordinata Y per la nuova pagina

               # Calcola la lunghezza del testo dell'esercizio
        lunghezza_testo_esercizio = c.stringWidth(testo_esercizio, "Helvetica", 10)
        lunghezza_soluzione = c.stringWidth(f"[Soluzione: {soluzione}]", "Helvetica-Oblique", 10)
        lung_tot=lunghezza_testo_esercizio+lunghezza_soluzione

    
         # Verifica se il testo dell'esercizio può entrare nella pagina corrente
        if y_start - 30 - dist_es_sol < 100 or lung_tot > (c._pagesize[0] - 200):
            # Cambia pagina se il testo non può entrare
            c.showPage()
            y_start = 750  # Ripristina la coordinata Y per la nuova pagina


        # Scrivi il numero dell'esercizio e l'argomento
        c.setFont("Helvetica", 12)
        c.drawString(100, y_start, f"Esercizio {numero+1} ({argomento}):")

 
        # Scrivi il testo dell'esercizio
        c.setFont("Helvetica", 10)
        c.drawString(100, y_start - 30, f"{testo_esercizio}")

    
        # Scrivi la soluzione
        c.setFont("Helvetica-Oblique", 10)
        c.drawString(100, y_start - dist_es_sol, f"[Soluzione: {soluzione}]")
        return y_start

####################################################################################################

######################crea pdf formato latex con simboli matematici################################
    def crea_file_latex(self, latex_filename_path,selezionati,vettore):
        with open(latex_filename_path, 'w') as file_latex:
            if file_latex.tell() == 0:
            # Se il file è vuoto, aggiungi l'intestazione del documento LaTeX
                file_latex.write(r'\documentclass{article}'+ '\n')
                file_latex.write(r'\usepackage{amsmath}' + '\n')
                file_latex.write(r'\usepackage[italian]{babel}'+ '\n')
                file_latex.write(r'\usepackage[letterpaper,top=1.5cm,bottom=2cm,left=1.5cm,right=3cm,marginparwidth=1.75cm]{geometry}'+ '\n')
                file_latex.write(r'\usepackage{siunitx}'+ '\n')
                file_latex.write(r'\usepackage{amsmath}'+ '\n')
                file_latex.write(r'\usepackage{tabto}'+ '\n')
                file_latex.write(r'\usepackage{xcolor}'+ '\n')
                file_latex.write(r'\usepackage{enumitem}'+ '\n')
                file_latex.write(r'\usepackage[colorlinks=true, allcolors=blue]{hyperref}'+ '\n')
                file_latex.write(r'\title{\raggedright Verifica di Matematica  ' + str(today)+'/'+str(month)+'/'+str(year)+'}'+ '\n')
                file_latex.write(r'\date{}'+ '\n')
                file_latex.write(r'\begin{document}' + '\n\n')
                file_latex.write(r'\maketitle' + '\n\n')

            if selezionati:
                a=1
                for indice in selezionati:
                    esercizio = self.esercizi_generati[indice]
                    argomento = esercizio['argomento']
                    argomento=argomento.replace("1°","\\ang{1}")
                    argomento=argomento.replace("2°","\\ang{2}")
                    testo_esercizio = esercizio['esercizio']
                    soluzione = esercizio['soluzione']
                    file_latex.write('\\textbf{Esercizio '+str(a)+' ('+argomento+')}:'+'\\\\'+ '\n')
                    file_latex.write('\\par $'+testo_esercizio+'$ \\\\\\\\'+'\n\n')
                    file_latex.write('\\textit{[ Soluzione: $'+soluzione+ '$ ]}'+'\\\\\\\\'+'\n\n')
                    a+=1
            else:        
                for indice, esercizio in enumerate(vettore):
                    argomento = esercizio['argomento']
                    argomento=argomento.replace("1°","\\ang{1}")
                    testo_esercizio = esercizio['esercizio']
                    soluzione = esercizio['soluzione']
                    file_latex.write('\\textbf{Esercizio '+str(indice+1)+' ('+argomento+')}:'+'\\\\'+ '\n')
                    file_latex.write('\\par $'+testo_esercizio+'$ \\\\\\\\'+'\n\n')
                    file_latex.write('\\textit{[ Soluzione: $'+soluzione+ '$ ]}'+'\\\\\\\\'+'\n\n')

            file_latex.write(r'\end{document}' + '\n')    

    def compile_latex(self,file_path):
        # Imposta il percorso del compilatore LaTeX
        latex_compiler = "pdflatex"
        output_folder=os.path.dirname(file_path)
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        #subprocess.run([latex_compiler, file_path])
        # Esegui il compilatore LaTeX sul file specificato
        subprocess.run([latex_compiler, "-output-directory=" + output_folder, file_path])
        #subprocess.run([latex_compiler, "-output-directory=" + output_folder, file_path])
            # Elimina i file ausiliari
        output_file_name=output_folder+'\\'+base_name+'.pdf'
        auxiliary_file_extensions = ['.aux', '.log', '.out','.toc','.idx']   

        for extension in auxiliary_file_extensions:
            auxiliary_file = os.path.join(output_folder, f"{base_name}{extension}")
            if os.path.exists(auxiliary_file):
                os.remove(auxiliary_file)
                print(f"File eliminato: {auxiliary_file}")
        return output_file_name

####################################################################################################   
    def leggi_dati(self):
        dati_inseriti = []
        for struttura in self.strutture:
            dati_riga = self.leggi_valori_struttura(struttura)
            if dati_riga is not None:
                dati_inseriti.append(dati_riga)
            
        return dati_inseriti

    def leggi_valori_struttura(self, struttura):
        # Leggi i valori dalla struttura
        opzione_selezionata = self.opzione_media.get()
        tipo_materia_var, argomenti_var, numeri_var = struttura.comboboxes
        state=str(tipo_materia_var["state"])
        
        # Verifica se la combobox è abilitata
        if state.lower() != "disabled":
            tipo_materia = tipo_materia_var.get()
            argomento = argomenti_var.get()
            num_esercizi = numeri_var.get()
            if tipo_materia != "" and argomento != "" and num_esercizi != "":
                return opzione_selezionata,tipo_materia,argomento,num_esercizi
            else:
                return None

    def leggi_esercizi_da_json(self,json_path, tipo_argomento):
        esercizi = []

        if os.path.exists(json_path):
            with open(json_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                esercizi_disponibili = data.get("esercizi", [])

                if tipo_argomento:
                    esercizi = [esercizio for esercizio in esercizi_disponibili if esercizio.get("argomento") == tipo_argomento]
                else:
                    esercizi = esercizi_disponibili

        return esercizi

    def run(self):
        self.root.mainloop()

    def clear_list_box(self):
        # Cancella il contenuto della list box
        self.list_box.delete(0, tk.END)

    def find_duplicates(self):
        tipo_scelto =   self.opzione_media.get()
        primo_combobox = self.strutture[0].comboboxes[0]
        materia_es = primo_combobox.get()
        percorso_json = parent_directory+'\\Verifiche Input\\'+tipo_scelto+'\\'+materia_es
        json_file = [f for f in os.listdir(percorso_json) if f.endswith('.json')][0]
        json_path = os.path.join(percorso_json, json_file)
    
        esercizi_set = set()
        duplicati = []
        if os.path.exists(json_path):
            with open(json_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
      
  
        for esercizio in data["esercizi"]:
            esercizio_str = json.dumps(esercizio, sort_keys=True)
            if esercizio_str in esercizi_set:
                duplicati.append(esercizio)
            else:
                esercizi_set.add(esercizio_str)

                    # Carica il tuo file JSON
   
        if duplicati:
            print("Gli elementi duplicati sono:")
            for duplicato in duplicati:
                print(json.dumps(duplicato, indent=2))
            conferma = messagebox.askyesno("Conferma Rimozione", "Sono presenti elementi duplicati. Vuoi rimuoverli?")
            if conferma:
                self.remove_duplicates(data, json_path,duplicati)
                messagebox.showinfo("Rimozione Completata", "Elementi duplicati rimossi con successo.")
            else:
                messagebox.showinfo("Nessun Duplicato", "Nessun elemento duplicato trovato")
        else:
            print("Nessun elemento duplicato trovato.")

        return duplicati

    def remove_duplicates(self,json_data,json_path, duplicati):
        for duplicato in duplicati:
            json_data["esercizi"].remove(duplicato)
        
        with open(json_path, "w") as file:
                json.dump(json_data, file, indent=2)


if __name__ == "__main__":
    global current_dir 
    global parent_directory
    global path_teoria
    global today
    global month
    global year

    today = date.today().day
    month=date.today().month
    year=date.today().year
    current_dir = sys.argv[0]
    parent_directory = os.path.dirname(current_dir)
    path_teoria=parent_directory+"\\Teoria"
    root = tk.Tk()
    finestra = PrimaFinestra(root)
    root.mainloop()
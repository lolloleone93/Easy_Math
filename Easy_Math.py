import os
import tkinter as tk
from tkinter import ttk, filedialog
import sys
import json
import os
import tkinter as tk
from tkinter import ttk, filedialog

class PrimaFinestra:
    def __init__(self, root):
        self.root = root
        self.root.title("Easy Math")

        # Imposta le dimensioni della finestra principale
        self.root.geometry("465x850")  # Modifica le dimensioni secondo necessità

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
        # 3. Menù a tendina per Argomenti
        self.materia_var = tk.StringVar()
        self.materia_menu = ttk.Combobox(root, textvariable=self.materia_var, state="readonly",width=70)
        
        self.materia_menu.grid(row=row_init+4, column=column_init, pady=5, padx=10)  # Modifica le dimensioni secondo necessità
        self.materia_menu.grid(row=row_init+4, column=column_init, pady=5, padx=10, columnspan=2, sticky="ew")


        # Aggiungi una label per il tipo di scuola
        label_tipo_argomenti = tk.Label(root, text="Argomenti:")
        label_tipo_argomenti.grid(row=row_init+6, column=column_init, padx=10, pady=5, sticky="w")
        # 3. Menù a tendina per Argomenti
        self.argomenti_var = tk.StringVar()
        self.argomenti_menu = ttk.Combobox(root, textvariable=self.argomenti_var, state="readonly",width=70)
        
        self.argomenti_menu.grid(row=row_init+7, column=column_init, pady=5, padx=10)  # Modifica le dimensioni secondo necessità
        self.argomenti_menu.grid(row=row_init+7, column=column_init, pady=5, padx=10, columnspan=2, sticky="ew")

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
        self.argomenti_menu.set("")  # Imposta il menù a tendina degli 
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
         generatore_verifiche = GeneratoreVerifiche((self.root))
         generatore_verifiche.run()

class GeneratoreVerifiche:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Generatore Verifiche")
        self.root.geometry("700x500")
        
  
     
  
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
        seleziona_button = ttk.Button(self.root, text="Seleziona Esercizi", command=self.seleziona_esercizi)
        genera_test_button = ttk.Button(self.root, text="Genera Test Casuale", command=self.genera_test_casuale)

        # Posizionamento degli elementi
        opzione_media_button.grid(row=0, column=0, columnspan=2, padx=(50, 10), pady=10,sticky="w")
        opzione_superiore_button.grid(row=0, column=2, columnspan=2,padx=(10, 50), pady=10, sticky="w")

        for i, struttura in enumerate(self.strutture):
            struttura.grid(row=i+1, column=0, columnspan=4, pady=5)

        seleziona_button.grid(row=len(self.strutture)+1, column=0, columnspan=2, pady=10)
        genera_test_button.grid(row=len(self.strutture)+1, column=2, columnspan=2, pady=10)
        
       

    def crea_struttura(self):
       
        struttura = ttk.Frame(self.root)
        

        # Rimuovi il quadrato nero dentro dai check button
        check_button = ttk.Checkbutton(struttura, command=self.abilita_disabilita_combobox)
        tipo_materia_var = tk.StringVar()
        tipo_materia_label = tk.Label(struttura, text="Tipo Materia", background="lightgray")
        tipo_materia_menu = ttk.Combobox(struttura, textvariable=tipo_materia_var, values=["Aritmetica", "Geometria"], state="disabled", background="lightgray")
        argomenti_label = tk.Label(struttura, text="Argomenti", background="lightgray")
        argomenti_menu = ttk.Combobox(struttura, state="disabled", background="lightgray")
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
            for combobox in struttura.comboboxes:
                combobox["values"] = nomi_cartelle

    
    def aggiorna_tipo_argomento(self, event, arg_combobox, *args):
        # Qui dovresti già avere la logica per aggiornare il tipo di materia (Media o Superiore)

        # Determina il percorso del JSON in base al tipo di materia scelto
            # Ottieni l'indice della riga associata al combobox della seconda colonna
        
        idx = arg_combobox.master.grid_info()["row"]
    # Ottieni il tipo di materia selezionato nel combobox della prima colonna
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
            argomenti_unici = list(set(esercizio["argomenti"] for esercizio in data["esercizi"]))
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
            for combobox in struttura.comboboxes:
                combobox.set("")

    def carica_argomenti_da_json(self):
        # Sostituisci con il percorso effettivo del tuo JSON
        

        tipo_scelto =   self.opzione_media.get()
        materia_es = self.ti
        percorso_json = parent_directory+'\\Verifiche Input\\'+tipo_scelto+'\\'+materia_es

        if os.path.exists(percorso_json):
            with open(percorso_json, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data.get("argomenti", [])
        else:
            return []


        # Implementa la logica per selezionare gli esercizi
        pass

    def genera_test_casuale(self):
        # Implementa la logica per generare il test casuale
        pass


    def seleziona_esercizi(self):
        finestra_selezione = tk.Toplevel(self.root)
        finestra_selezione.title("Seleziona Esercizi")

        esercizi_selezionati = []
        for struttura in self.strutture:
            tipo_materia, argomento, num_esercizi = self.leggi_tutti_valori(struttura)

            # Simula la lettura degli esercizi dal tuo JSON
            esercizi = self.carica_esercizi_da_json(tipo_materia, argomento,num_esercizi)

            # Crea i Checkbutton per ogni esercizio
            for esercizio in esercizi:
                check_var = tk.BooleanVar()
                check_button = ttk.Checkbutton(finestra_selezione, text=esercizio, variable=check_var)
                check_button.grid(sticky="w")

                # Aggiungi una funzione di callback per raccogliere gli esercizi selezionati
                check_button.bind("<Button-1>", lambda event, var=check_var, es=esercizio: self.raccogli_esercizio(var, es))

        # Aggiungi un pulsante per confermare la selezione
        conferma_button = ttk.Button(finestra_selezione, text="Conferma Selezione", command=finestra_selezione.destroy)
        conferma_button.grid()

    def carica_esercizi_da_json(self, tipo_materia, argomento,num_esercizi):
        # Implementa la logica per leggere gli esercizi dal JSON in base al tipo di materia e argomento
        # Restituisce una lista di esercizi
        return ["Esercizio 1", "Esercizio 2", "Esercizio 3"]  # Sostituisci con la tua logica

    def raccogli_esercizio(self, var, esercizio):
        if var.get():
            print(f"Esercizio selezionato: {esercizio}")
        else:
            print(f"Esercizio deselezionato: {esercizio}")

    def leggi_valori_struttura(self, struttura):
        tipo_materia_var, argomenti_var, numeri_var = struttura.comboboxes  # Supponendo che le comboboxes siano create correttamente nella tua struttura
        tipo_materia = tipo_materia_var.get()
        argomento = argomenti_var.get()
        num_esercizi = numeri_var.get()
        return tipo_materia, argomento, num_esercizi
    def leggi_tutti_valori(self):
        valori_totali = []
        for struttura in self.strutture:
            valori_riga = self.leggi_valori_struttura(struttura)
            valori_totali.append(valori_riga)
        return valori_totali

    def run(self):
        self.root.mainloop()



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
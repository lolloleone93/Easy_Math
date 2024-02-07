#!/bin/bash

echo Credenziali commit:
echo Nome Utente: lolloleone93
echo Email: leone.lorenzo@hotmail.it
echo ----------------------------
echo ----------------------------
git config user.name "lolloleone93"
git config user.email "leone.lorenzo@hotmail.it"

read -p "Inserisci il messaggio del commit: " commit_message

# Aggiungi tutti i file modificati al commit
git add .

# Esegui il commit con il messaggio specificato
git commit -m "$commit_message"

# Esegui il push
git push origin main

echo "Commit eseguito con successo."


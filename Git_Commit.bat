@echo off

REM Imposta le nuove credenziali
git config user.name "lolloleone93"
git config user.email "leone.lorenzo@hotmail.it"

echo Inserisci il messaggio di commit:
set /p commit_message=

git add .
git commit -m "%commit_message%"

echo Commit effettuato con successo!

git push origin main

echo Push sul repositary effettuato con successo!

REM Ripristina le credenziali originali
git config --unset user.name
git config --unset user.email

echo Credenziali ripristinate.

REM Salva le credenziali originali
set "original_username="
for /f "delims=" %%G in ('git config user.name') do set "original_username=%%G"

set "original_email="
for /f "delims=" %%G in ('git config user.email') do set "original_email=%%G"

REM Visualizza le credenziali originali
echo Credenziali originali:
echo Nome Utente: %original_username%
echo Email: %original_email%
echo ----------------------------


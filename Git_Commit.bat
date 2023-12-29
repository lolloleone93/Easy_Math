@echo off

REM Imposta le nuove credenziali
echo ----------------------------
echo ----------------------------
echo Credenziali commit:
echo Nome Utente: lolloleone93
echo Email: leone.lorenzo@hotmail.it
echo ----------------------------
echo ----------------------------
git config user.name "lolloleone93"
git config user.email "leone.lorenzo@hotmail.it"



echo Inserisci il messaggio di commit:
set /p commit_message=

git add .
git commit -m "%commit_message%"

echo ----------------------------
echo ----------------------------
echo Commit effettuato con successo!
echo ----------------------------
echo ----------------------------

git push origin main
echo ----------------------------
echo ----------------------------
echo Push sul repositary effettuato con successo!
echo ----------------------------
echo ----------------------------

REM Ripristina le credenziali originali
git config --unset user.name
git config --unset user.email

echo ----------------------------
echo ----------------------------

echo Credenziali ripristinate.
echo ----------------------------
echo ----------------------------

REM Salva le credenziali originali
set "original_username="
for /f "delims=" %%G in ('git config user.name') do set "original_username=%%G"

set "original_email="
for /f "delims=" %%G in ('git config user.email') do set "original_email=%%G"

REM Visualizza le credenziali originali
echo ----------------------------
echo Credenziali originali:
echo Nome Utente: %original_username%
echo Email: %original_email%
echo ----------------------------


REM Pause per mantenere aperta la console
pause


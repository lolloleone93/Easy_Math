@echo off
setlocal enabledelayedexpansion

REM Imposta il percorso del file di testo contenente gli elenchi di nomi
REM set "file_txt=nomi.txt"
set "file_txt=gem_sup.txt"

REM Verifica se il file di testo esiste
if not exist "%file_txt%" (
    echo Il file di testo "%file_txt%" non esiste.
    exit /b
)

REM Leggi ogni riga dal file di testo e crea una cartella con il nome
for /f "tokens=*" %%a in (%file_txt%) do (
    set "nome_cartella=%%a"
    set "nome_cartella=!nome_cartella: =_!"  REM Sostituisci gli spazi con underscores
    mkdir "!nome_cartella!"
    echo Cartella creata: "!nome_cartella!"
)

echo Operazione completata.
pause
endlocal
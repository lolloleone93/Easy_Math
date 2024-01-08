@echo off

:: Lista delle librerie da installare
set librerie=tkinter pandas os sys re datetime shutil reportlab matplotlib time timeit subprocess io json PIL random sympy pdfplumber tqdm

:: Percorso dell'interprete Python
set python_interpreter=python

:: Itera attraverso la lista delle librerie e installale con pip
for %%i in (%librerie%) do (
    %python_interpreter% -m pip install %%i
)

:: Messaggio di completamento
echo Librerie installate con successo.
pause


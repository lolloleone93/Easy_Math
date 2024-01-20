#!/bin/bash

LIBRARY_LIST=(
    "tkinter"
    "pandas"
    "os"
    "sys"
    "re"
    "datetime"
    "shutil"
    "reportlab"
    "matplotlib"
    "time"
    "timeit"
    "subprocess"
    "io"
    "json"
    "PIL"
    "random"
    "sympy"
    "pdfplumber"
    "tqdm"
)

for library in "${LIBRARY_LIST[@]}"; do
    echo "Installazione di $library..."
    pip3 install "$library"
    echo "----------------------------------------"
done

echo "Installazione completata!"


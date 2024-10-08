# Deutsch

## CSV Zeilenumbruch Bereiniger

Dieses Tool ist ein Python-Programm, das eine ausgewählte CSV-Datei
liest und alle Zeilenumbrüche innerhalb von Anführungszeichen entfernt.
Es erstellt eine temporäre Datei mit den bereinigten Daten, die dann vom
Benutzer gespeichert werden kann.

### Installation

1.  Stellen Sie sicher, dass Python auf Ihrem System installiert ist.
    Dieses Tool wurde mit Python 3.8 entwickelt, sollte aber auch mit
    neueren Versionen kompatibel sein.
2.  Laden Sie die Python-Datei herunter oder klonen Sie dieses
    Repository.
3.  Installieren Sie die benötigten Python-Bibliotheken mit folgendem
    Befehl:

``` \"language-bash\"
pip install chardet
```

### Verwendung

Starten Sie das Programm und klicken Sie auf "CSV-Datei auswählen", um
eine CSV-Datei auszuwählen. Das Programm erkennt automatisch die
Codierung der Datei und beginnt mit der Bereinigung der Zeilenumbrüche.
Der Fortschritt wird in einem Fortschrittsbalken angezeigt. Sobald die
Bereinigung abgeschlossen ist, können Sie auf "Datei abspeichern"
klicken, um die bereinigte Datei zu speichern. Der Dateinname wird 
beim Speicerhn wieder verwendet und ein '_BEREINIGT' wird vor der 
Dateiendung eingefügt.

### Anforderungen an die Eingabedatei

Die Eingabe muss eine CSV-Datei sein, bei der Textfelder durch
Anführungszeichen qualifiziert sind. Das bedeutet, dass alle Textfelder,
die Kommas oder Zeilenumbrüche enthalten, in Anführungszeichen
eingeschlossen sein müssen ("Lorem Ipsum"). Als Trennzeichen wurde mit
Semikolons (;) und Kommas (,) getestet.

------------------------------------------------------------------------

# English

## CSV Line Break Cleaner

This tool is a Python program that reads a selected CSV file and removes
all line breaks within quotes. It creates a temporary file with the
cleaned data, which can then be saved by the user.

### Installation

1.  Make sure Python is installed on your system. This tool was
    developed with Python 3.8 but should also be compatible with newer
    versions.
2.  Download the Python file or clone this repository.
3.  Install the required Python libraries using the following command:

``` \"language-bash\"
pip install chardet
```

### Usage

Start the program and click on "Select CSV file" to select a CSV file.
The program automatically detects the encoding of the file and starts
cleaning the line breaks. The progress is displayed in a progress bar.
Once the cleaning is complete, you can click on "Save File" to save the
cleaned file. The file name is used again when saving and a '_BEREINIGT' 
is inserted before the file extension.

### Input File Requirements

The input must be a CSV file where text fields are qualified by quotes.
This means that any text fields containing commas or line breaks must be
enclosed in quotes ("Lorem Ipsum"). Semicolons (;) and commas (,) were 
tested as separators.

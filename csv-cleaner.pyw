import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import time
import threading
import os
import tempfile
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        return result['encoding']

def clean_csv(input_file, output_file, encoding, progress_var):
    line_count = sum(1 for _ in open(input_file, 'r', encoding=encoding))
    processed_lines = 0

    with open(input_file, 'r', newline='', encoding=encoding) as infile, open(output_file, 'w', newline='', encoding=encoding) as outfile:
        in_quotes = False
        for line in infile:
            processed_lines += 1
            progress = int((processed_lines / line_count) * 100)
            progress_var.set(progress)
            time.sleep(0.01)  # Simuliere etwas längere Verarbeitungszeit
            root.update_idletasks()

            # Entferne Zeilenumbrüche innerhalb von Anführungszeichen
            cleaned_line = ""
            for char in line:
                if char == '"':
                    in_quotes = not in_quotes  # Umschalten des Status für Anführungszeichen
                if char == '\n' and in_quotes:
                    cleaned_line += " "
                else:
                    cleaned_line += char
            outfile.write(cleaned_line)

def start_conversion(input_file, encoding, progress_var, progress_bar, save_button):
    start_time = time.time()
    
    # Dateiname für die temporäre, versteckte Datei
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    temp_file_path = temp_file.name
    temp_file.close()
    
    # Datei wird zeilenweise verarbeitet
    clean_csv(input_file, temp_file_path, encoding, progress_var)
    
    elapsed_time = time.time() - start_time
    if elapsed_time < 2:
        time.sleep(2 - elapsed_time)

    progress_var.set(100)  # Fortschrittsbalken auf 100% setzen
    root.update_idletasks()
    
    # Speichern-Button sichtbar machen und mit dem temporären Dateipfad und Original-Dateinamen verbinden
    save_button.config(command=lambda: save_cleaned_file(button_select, progress_bar, save_button, temp_file_path, input_file))
    save_button.pack(pady=10)

def select_file(button_select, progress_var, progress_bar, save_button):
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        encoding = detect_encoding(file_path)
        button_select.config(state=tk.DISABLED)  # Deaktiviere den "CSV-Datei auswählen"-Button
        progress_bar.pack(pady=10)  # Zeige den Fortschrittsbalken an
        save_button.pack_forget()  # Verstecke den Speichern-Button
        
        # Starte die Verarbeitung in einem separaten Thread
        threading.Thread(target=start_conversion, args=(file_path, encoding, progress_var, progress_bar, save_button)).start()

def save_cleaned_file(button_select, progress_bar, save_button, temp_file_path, original_file_path):
    # Extrahiere den Dateinamen und die Erweiterung
    original_dir, original_name = os.path.split(original_file_path)
    name, ext = os.path.splitext(original_name)
    
    # Erstelle den neuen Dateinamen mit der Kennzeichnung "_BEREINIGT"
    suggested_name = f"{name}_BEREINIGT{ext}"
    output_file = filedialog.asksaveasfilename(initialdir=original_dir, initialfile=suggested_name, defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    
    if output_file:
        try:
            # Lösche die vorhandene Datei, falls sie existiert, um sie zu überschreiben
            if os.path.exists(output_file):
                os.remove(output_file)
            # Benenne die temporäre Datei im Temp-Ordner um
            os.rename(temp_file_path, output_file)
            messagebox.showinfo("Erfolg", f"Datei wurde gespeichert als {os.path.basename(output_file)}")
        except Exception as e:
            messagebox.showerror("Fehler", f"Beim Speichern der Datei ist ein Fehler aufgetreten: {str(e)}")
        finally:
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)  # Lösche die temporäre Datei

    # Setze das Fenster in den Ausgangszustand zurück
    progress_bar.pack_forget()
    save_button.pack_forget()
    button_select.config(state=tk.NORMAL)

# GUI einrichten
root = tk.Tk()
root.title("CSV Zeilenumbruch Bereiniger")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Wählen Sie eine CSV-Datei aus, um Zeilenumbrüche zu bereinigen:")
label.pack(pady=10)

button_select = tk.Button(frame, text="CSV-Datei auswählen", command=lambda: select_file(button_select, progress_var, progress_bar, button_save))
button_select.pack(pady=10)

progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(frame, orient="horizontal", length=300, mode="determinate", variable=progress_var, maximum=100)

button_save = tk.Button(frame, text="Datei abspeichern")

root.mainloop()

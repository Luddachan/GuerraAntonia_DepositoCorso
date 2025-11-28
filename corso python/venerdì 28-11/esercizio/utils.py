import numpy as np
import os
import csv

# leggo e carico i csv
def read(path):
    if not os.path.exists(path):
        print("File non trovato.")
        return None

    data = np.genfromtxt(path, delimiter=",", skip_header=1)
    if data.size == 0:
        print(f"Il file '{path}' è vuoto o non contiene dati numerici.")
        return None

    print(f"File '{path}' caricato correttamente!")
    return data


# salvo il file su csv
def salva_csv(data_dict, path):
    mode = "a" if os.path.exists(path) else "w"
    with open(path, mode, newline="") as f:
        writer = csv.writer(f)
        for k, v in data_dict.items():
            writer.writerow([k])
            if isinstance(v, np.ndarray):
                if v.ndim == 1:
                    writer.writerow(v.tolist())
                else:
                    for row in v:
                        writer.writerow(row.tolist())
            else:
                writer.writerow([v])
        writer.writerow([])
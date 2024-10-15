import tkinter as tk
from tkinter import messagebox

# Definiera globala produktpriser
Tea = 30
Kaffe = 30
Smörgås = 50

# Skapa en klass för produkter
class Produkt:
    def __init__(self, namn, pris):
        self.namn = namn
        self.pris = pris

# Klass för beställning
class Beställning:
    def __init__(self):
        self.produkter = []  # En lista som sparar beställningar

    def lägg_till_beställning(self, produkt):
        self.produkter.append(produkt)  # Lägg till varor i beställningen

    def räkna_priset(self):
        return sum(produkt.pris for produkt in self.produkter)

# Spara kvitto i en fil
def spara_kvitto(beställning):
    try:
        with open('Kvitto.txt', 'w', encoding='utf-8') as fil:
            fil.write("Kvitto:\n")
            for produkt in beställning.produkter:
                fil.write(f"{produkt.namn}: {produkt.pris} KR\n")
            fil.write(f"Total: {beställning.räkna_priset()} KR\n")
        messagebox.showinfo("Sparat", "Ditt kvitto har sparats.")
    except Exception as e:
        messagebox.showerror("Fel", f"Kunde inte spara kvitto: {str(e)}")

# Tkinter GUI
def skapa_fönster():
    program = tk.Tk()
    program.title("Kvitto App")

    # Skapa en beställning
    min_beställning = Beställning()

    # Skapa produktlista
    produkter = [
        Produkt("Kaffe", 30),
        Produkt("Tea", 30),
        Produkt("Smörgås", 50)
    ]

    # Etikett för beställningar
    tk.Label(program, text="Välj din beställning:", font=("Helvetica", 14)).pack()

    # Knapp för att lägga till produkter
    for produkt in produkter:
        tk.Button(
            program, 
            text=f"{produkt.namn} - {produkt.pris} KR", 
            command=lambda p=produkt: lägg_till_beställning(p, min_beställning),
            bg="lightblue", fg="black", font=("Helvetica", 12), width=20
        ).pack(pady=5)

    # Knapp för att spara kvitto
    tk.Button(
        program, 
        text="Spara kvitto", 
        command=lambda: spara_kvitto(min_beställning), 
        bg="salmon", fg="black", font=("Helvetica", 12), width=20
    ).pack(pady=20)

    program.geometry("300x400")
    program.mainloop()

# Lägg till produkt till beställningen
def lägg_till_beställning(produkt, beställning):
    beställning.lägg_till_beställning(produkt)

# Starta Tkinter GUI
if __name__ == "__main__":
    skapa_fönster()



         
    

    

import tkinter as tk
from tkinter import ttk, messagebox
from logic.strings_logic import get_prefixes, get_suffixes, get_substrings
from logic.languages_logic import get_kleene_closure, get_positive_closure

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Practica 1: Teoria de la Computacion - ESCOM")
        self.root.geometry("800x700")
        self.root.configure(bg="#0f172a")

        # --- ESTILOS ---
        style = ttk.Style()
        style.theme_use('default')
        
        style.configure("TNotebook", background="#0f172a", borderwidth=0)
        style.configure("TNotebook.Tab", 
                        background="#1e293b", 
                        foreground="white", 
                        padding=[20, 10], 
                        font=('Segoe UI', 10, 'bold'))
        style.map("TNotebook.Tab", background=[("selected", "#38bdf8")], foreground=[("selected", "black")])

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both", padx=20, pady=20)

        # --- PESTAÑA 1 ---
        self.tab1 = tk.Frame(self.notebook, bg="#1e293b", padx=20, pady=20)
        self.notebook.add(self.tab1, text="  Ejercicio 1: Cadenas  ")
        self.setup_tab1()

        # --- PESTAÑA 2 ---
        self.tab2 = tk.Frame(self.notebook, bg="#1e293b", padx=20, pady=20)
        self.notebook.add(self.tab2, text="  Ejercicio 2: Cerraduras  ")
        self.setup_tab2()

    def setup_tab1(self):
        tk.Label(self.tab1, text="Subcadenas, Prefijos y Sufijos", font=("Segoe UI", 16, "bold"), 
                 bg="#1e293b", fg="#38bdf8").pack(pady=(0, 20))
        
        tk.Label(self.tab1, text="Ingresa la cadena de entrada:", bg="#1e293b", fg="white", font=("Segoe UI", 10)).pack(anchor="w")
        self.entry_string = tk.Entry(self.tab1, font=("Consolas", 12), bg="#0f172a", fg="#00ff88", 
                                     insertbackground="white", borderwidth=0, highlightthickness=1, highlightbackground="#38bdf8")
        self.entry_string.pack(fill="x", pady=10)

        btn = tk.Button(self.tab1, text="CALCULAR Y EXPORTAR", command=self.solve_ej1, 
                        bg="#38bdf8", fg="black", font=("Segoe UI", 10, "bold"), 
                        activebackground="#0ea5e9", cursor="hand2", bd=0, padx=20, pady=10)
        btn.pack(pady=15)

        self.text_res1 = tk.Text(self.tab1, height=15, font=("Consolas", 11), bg="#0f172a", 
                                 fg="#cbd5e1", padx=15, pady=15, bd=0)
        self.text_res1.pack(expand=True, fill="both")

    def setup_tab2(self):
        tk.Label(self.tab2, text="Alfabetos y Cerraduras", font=("Segoe UI", 16, "bold"), 
                 bg="#1e293b", fg="#fbbf24").pack(pady=(0, 20))

        tk.Label(self.tab2, text="Alfabeto (separado por comas, ej: a,b):", bg="#1e293b", fg="white").pack(anchor="w")
        self.entry_alpha = tk.Entry(self.tab2, font=("Consolas", 12), bg="#0f172a", fg="#fbbf24", 
                                    insertbackground="white", borderwidth=0, highlightthickness=1, highlightbackground="#fbbf24")
        self.entry_alpha.pack(fill="x", pady=10)

        tk.Label(self.tab2, text="Longitud maxima:", bg="#1e293b", fg="white").pack(anchor="w")
        self.entry_limit = tk.Entry(self.tab2, font=("Consolas", 12), bg="#0f172a", fg="#fbbf24", width=10)
        self.entry_limit.insert(0, "3")
        self.entry_limit.pack(anchor="w", pady=10)

        btn = tk.Button(self.tab2, text="GENERAR LENGUAJES", command=self.solve_ej2, 
                        bg="#fbbf24", fg="black", font=("Segoe UI", 10, "bold"), 
                        activebackground="#f59e0b", cursor="hand2", bd=0, padx=20, pady=10)
        btn.pack(pady=15)

        self.text_res2 = tk.Text(self.tab2, height=15, font=("Consolas", 11), bg="#0f172a", 
                                 fg="#cbd5e1", padx=15, pady=15, bd=0)
        self.text_res2.pack(expand=True, fill="both")

    def solve_ej1(self):
        s = self.entry_string.get()
        if not s:
            messagebox.showwarning("Error de entrada", "Debes ingresar una cadena de texto.")
            return
        
        pref = get_prefixes(s)
        suff = get_suffixes(s)
        subs = get_substrings(s)

        res_txt = f"RESULTADOS PARA LA CADENA: '{s}'\n" + "-"*45 + \
                  f"\n\nPREFIJOS:\n{pref}\n\nSUFIJOS:\n{suff}\n\nSUBCADENAS:\n{subs}"
        
        self.text_res1.delete("1.0", tk.END)
        self.text_res1.insert(tk.END, res_txt)

        try:
            with open("ejercicio1_cadenas.txt", "w", encoding="utf-8") as f:
                f.write(res_txt)
            messagebox.showinfo("Operacion Exitosa", "Los calculos se realizaron correctamente y se guardaron en 'ejercicio1_cadenas.txt'")
        except Exception as e:
            messagebox.showerror("Error de Archivo", f"No se pudo guardar el archivo: {e}")

    def solve_ej2(self):
        alpha_raw = self.entry_alpha.get()
        limit_raw = self.entry_limit.get()
        
        if not alpha_raw or not limit_raw:
            messagebox.showwarning("Error de entrada", "Por favor completa el alfabeto y la longitud maxima.")
            return

        try:
            alphabet = [x.strip() for x in alpha_raw.split(",")]
            limit = int(limit_raw)

            kleene = get_kleene_closure(alphabet, limit)
            positive = get_positive_closure(alphabet, limit)

            res_txt = f"ALFABETO SIGMA: {{{', '.join(alphabet)}}}\n" + "-"*45 + \
                      f"\n\nCERRADURA DE KLEENE (SIGMA*):\n{kleene}\n\nCERRADURA POSITIVA (SIGMA+):\n{positive}"
            
            self.text_res2.delete("1.0", tk.END)
            self.text_res2.insert(tk.END, res_txt)

            with open("ejercicio2_cerraduras.txt", "w", encoding="utf-8") as f:
                f.write(res_txt)
            messagebox.showinfo("Operacion Exitosa", "Las cerraduras se generaron correctamente y se guardaron en 'ejercicio2_cerraduras.txt'")
        except ValueError:
            messagebox.showerror("Error de Formato", "La longitud maxima debe ser un numero entero.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrio un error inesperado: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

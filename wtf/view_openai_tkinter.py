
import tkinter as tk
from tkinter import ttk

# Funções de callback para os botões
def handle_flag_click(language):
    print(f"Selected language: {language}")

def handle_main_button_click(main_id):
    print(f"Main button {main_id} clicked")

def handle_sub_button_click(main_id, sub_id):
    print(f"Sub button {main_id}-{sub_id} clicked")

def handle_control_button_click(action):
    print(f"Control button {action} clicked")

# Configuração da janela principal
root = tk.Tk()
root.title("Translation App")
root.geometry("400x700")

# Seção superior
top_frame = tk.Frame(root, bg="#f1f1f1", pady=10)
top_frame.pack(fill="x")

tk.Label(top_frame, text="Choose Language:", bg="#f1f1f1").pack(side="left", padx=10)

for lang, emoji in [("en", "🇺🇸"), ("pt", "🇧🇷"), ("es", "🇪🇸")]:
    tk.Button(
        top_frame, text=emoji, width=3, command=lambda lang=lang: handle_flag_click(lang)
    ).pack(side="left", padx=5)

# Seção do meio
middle_frame = tk.Frame(root, bg="#eaeaea")
middle_frame.pack(fill="both", expand=True)

canvas = tk.Canvas(middle_frame, bg="#eaeaea")
scrollbar = ttk.Scrollbar(middle_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.configure(yscrollcommand=scrollbar.set)

content_frame = tk.Frame(canvas, bg="#eaeaea")
canvas.create_window((0, 0), window=content_frame, anchor="nw")

def populate_middle_section():
    for main_id in range(1, 3):
        main_button = tk.Button(
            content_frame,
            text=f"Main {main_id}",
            width=6,
            height=3,
            bg="#8ecae6",
            command=lambda main_id=main_id: handle_main_button_click(main_id),
        )
        main_button.pack(pady=10)

        sub_frame = tk.Frame(content_frame, bg="#eaeaea")
        sub_frame.pack()

        for sub_id in range(1, 4):
            tk.Button(
                sub_frame,
                text=f"S{sub_id}",
                width=4,
                height=2,
                bg="#ffb703",
                command=lambda main_id=main_id, sub_id=sub_id: handle_sub_button_click(main_id, sub_id),
            ).pack(side="left", padx=5)

populate_middle_section()
content_frame.update_idletasks()
canvas.configure(scrollregion=canvas.bbox("all"))

# Seção inferior
bottom_frame = tk.Frame(root, bg="#f1f1f1", pady=10)
bottom_frame.pack(fill="x")

for action, label in [("home", "🏠"), ("book", "📖"), ("repeat", "🔁")]:
    tk.Button(
        bottom_frame,
        text=label,
        width=8,
        height=2,
        bg="#fff",
        relief="groove",
        command=lambda action=action: handle_control_button_click(action),
    ).pack(side="left", padx=10)

# Executa a aplicação
root.mainloop()

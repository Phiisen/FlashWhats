import tkinter as tk
from tkinter import ttk, messagebox
import threading
import re
import pywhatkit
import pyautogui
import time

# Flag para parar envio
parar_envio = False

def extrair_contatos(texto):
    contatos = []
    linhas = texto.strip().split('\n')
    for linha in linhas:
        match = re.match(r"(.*)\((\d{2})\)(\d{8,9})", linha.strip())
        if match:
            nome = match.group(1).strip()
            ddd = match.group(2)
            numero = match.group(3)
            numero_formatado = f"55{ddd}{numero}"
            contatos.append((nome, numero_formatado))
    return contatos

def enviar_mensagens(contatos, mensagem_base):
    global parar_envio

    # Assumimos que WhatsApp Web já está aberto na primeira aba
    for nome, numero in contatos:
        if parar_envio:
            break
        mensagem = mensagem_base.replace("{nome}", nome)

        print(f"Enviando para {numero}: {mensagem}")

        # Usa pywhatkit para abrir o chat na mesma aba
        pywhatkit.sendwhatmsg_instantly(f"+{numero}", mensagem, wait_time=15, tab_close=False, close_time=2)

        time.sleep(2)  # Dar tempo da aba carregar mensagem

        # Fecha a aba atual, que é a do contato
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(1)

    messagebox.showinfo("Concluído", "Mensagens enviadas!")

def iniciar_envio():
    global parar_envio
    parar_envio = False
    texto_contatos = texto_lista.get("1.0", tk.END)
    mensagem = campo_mensagem.get("1.0", tk.END).strip()

    if not texto_contatos.strip() or not mensagem:
        messagebox.showwarning("Aviso", "Insira a lista de contatos e a mensagem.")
        return

    contatos = extrair_contatos(texto_contatos)
    if not contatos:
        messagebox.showerror("Erro", "Nenhum contato válido encontrado.")
        return

    threading.Thread(target=enviar_mensagens, args=(contatos, mensagem), daemon=True).start()

def parar():
    global parar_envio
    parar_envio = True

# -------------------- INTERFACE --------------------
root = tk.Tk()
root.title("FlashWhats - WhatsApp Automático")
root.iconbitmap("icone.ico")
root.geometry("500x600")
root.configure(bg="#1e1e1e")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", foreground="white", background="#333", padding=6, relief="flat")
style.map("TButton", background=[('active', '#444')])

# Título
titulo = tk.Label(root, text="FlashWhats", font=("Segoe UI", 18, "bold"), bg="#1e1e1e", fg="#00ff88")
titulo.pack(pady=10)

# Área de contatos
frame_top = tk.Frame(root, bg="#1e1e1e")
frame_top.pack(padx=20, pady=10, fill="both", expand=True)

tk.Label(frame_top, text="Contatos (Formato: Nome(DDD)Número):", bg="#1e1e1e", fg="white").pack(anchor="w")
texto_lista = tk.Text(frame_top, height=10, bg="#2e2e2e", fg="white", insertbackground="white")
texto_lista.pack(fill="x", pady=5)

# Área de mensagem
tk.Label(frame_top, text="Mensagem (use {nome} para personalizar):", bg="#1e1e1e", fg="white").pack(anchor="w")
campo_mensagem = tk.Text(frame_top, height=10, bg="#2e2e2e", fg="white", insertbackground="white")
campo_mensagem.pack(fill="x", pady=5)

# Botões
frame_botoes = tk.Frame(root, bg="#1e1e1e")
frame_botoes.pack(pady=10)

btn_enviar = ttk.Button(frame_botoes, text="Enviar Mensagens", command=iniciar_envio)
btn_enviar.grid(row=0, column=0, padx=10)

btn_parar = ttk.Button(frame_botoes, text="Parar Envio", command=parar)
btn_parar.grid(row=0, column=1, padx=10)

# Rodapé
tk.Label(root, text="Criado por Philipsen Berndt ⚡", bg="#1e1e1e", fg="#888888", font=("Segoe UI", 8)).pack(pady=5)

root.mainloop()

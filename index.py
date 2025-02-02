import customtkinter

# Definições de aparência
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Criando a janela
janela = customtkinter.CTk()
janela.geometry("500x300")

# Função do clique no botão
def clique():
    print("Fazer Login")

# Adicionando um texto (label)
texto = customtkinter.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

# Adicionando o campo de e-mail
email = customtkinter.CTkEntry(janela, placeholder_text="Seu e-mail")
email.pack(padx=10, pady=10)

# Adicionando o campo de senha
senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")
senha.pack(padx=10, pady=10)

# Checkbox para lembrar login
checkbox = customtkinter.CTkCheckBox(janela, text="Lembrar login")
checkbox.pack(padx=10, pady=10)

# Adicionando o botão
botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)

# Iniciando o loop da janela
janela.mainloop()



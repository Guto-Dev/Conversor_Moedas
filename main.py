import customtkinter

# Configuração da JANELA
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x500")
janela.title("Conversor de MOEDAS")

# Dados de câmbio fixo
taxas = {
    "Real": {"Dólar": 0.1765, "Euro": 0.1581, "Iene": 25.71},
    "Dólar": {"Real": 5.67, "Euro": 0.8957, "Iene": 145.74},
    "Euro": {"Real": 6.33, "Dólar": 1.1166, "Iene": 162.71},
    "Iene": {"Real": 0.0389, "Dólar": 0.0069, "Euro": 0.0062},
}


# Título
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("Arial", 20))
titulo.place(relx=0.5, y=20, anchor="center")

# Texto moeda origem
texto_moedas = customtkinter.CTkLabel(janela, text="Selecione a moeda")
texto_moedas.place(relx=0.5, y=70, anchor="center")

# Seleção de moedas entrada
moedas = ["Real", "Dólar", "Euro", "Iene"]

moeda_selecionada = customtkinter.CTkOptionMenu(janela, values=moedas,width=300, height=30)
moeda_selecionada.pack(pady=80)
moeda_selecionada.set("Real")

# Entrada do valor
moeda_entrada = customtkinter.CTkEntry(janela, placeholder_text="Digite o valor")
moeda_entrada.place(relx=0.5, y= 160, anchor="center")

# Texto moeda destino
moeda_saida = customtkinter.CTkLabel(janela, text="Selecione a moeda para transformação")
moeda_saida.place(relx=0.5, y=220, anchor="center")

# Resultado
resultado_label = customtkinter.CTkLabel(janela, text="", font=("Arial", 16))
resultado_label.place(relx=0.5, y=310, anchor="center")

# Seleção de moedas entrada
moedas_saida = ["Real", "Dólar", "Euro", "Iene"]

moedas_transfor = customtkinter.CTkOptionMenu(janela, values=moedas_saida, width=300, height=30)
moedas_transfor.place(relx=0.5, y=250, anchor="center")
moedas_transfor.set("Dólar")

def converter():
    try:
        valor = float(moeda_entrada.get())
        origem = moeda_selecionada.get()
        destino = moedas_transfor.get()

        if origem == destino:
            resultado = valor
        else:
            taxa = taxas[origem][destino]
            resultado = valor * taxa

        resultado_label.configure(text=f"{valor:.2f} {origem} = {resultado:.2f} {destino}")
    except:
        resultado_label.configure(text="Erro: digite um valor válido.")

# Botão de converter
botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter)
botao_converter.place(relx=0.5, y=360, anchor="center")

# Fazer a janela rodar
janela.mainloop()
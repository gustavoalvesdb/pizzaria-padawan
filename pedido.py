# pizzaria
pizzaria = "Pizzas Padawan"

#variáveis básicas
nome = input(f"Olá! Seja muito bem-vindo(a) à {pizzaria}! Para iniciar o pedido, poderia nos informar o seu nome? ")

# sabores válidos
sabores_validos = {
    "calabresa": 35.90,
    "marguerita": 32.50,
    "peperoni": 36.00,
    "frango": 34.90
}
tamanhos_validos = ["broto", "médio", "grande"]

# exibição dos sabores
print("Sabores disponíveis:")
for sabor in sabores_validos:
    print(f"{sabor} — R$ {sabores_validos[sabor]:.2f}")

# validação dos sabores
while True:
  sabor = input(f"Olá {nome}, agora nos diga qual o sabor da pizza que deseja: ").lower()
  if sabor in sabores_validos:
    print(f"Opaa, {nome}, o sabor de {sabor} foi escolhido com sucesso!")
    break
  else:
    print(f"Opa, o sabor {sabor} não está disponível ainda em nosso cardápio, os disponíveis são: ")
    for item in sabores_validos:
      print(item)

# validação dos tamanhos
while True:
  tamanho = input("Por fim, nos informe o tamaho da pizza que deseja, temos broto, média e grande: ").lower()
  if tamanho in tamanhos_validos:
    print(f"Opaa, {nome}, o tamanho {tamanho} foi escolhido com sucesso!")
    break
  else:
    print(f"Opa, o tamanho {tamanho} não está disponível ainda em nosso cardápio, os disponíveis são: ")
    for item in tamanhos_validos:
      print(item)

# multiplicador do preço por tamanho
fatores_tamanho = {
    "broto": 1,
    "médio": 1.5,
    "grande": 2
}

# definição do valor total
preco_base = sabores_validos[sabor]
multiplicador = fatores_tamanho[tamanho]
preco_final = preco_base * multiplicador


# exibição do recibo
print("\n🧾 Pedido confirmado!")
print(f"Cliente: {nome}")
print(f"Pizza: {tamanho.capitalize()} de {sabor.capitalize()}")
print(f"Preço total: R$ {preco_final:.2f}")
print("Previsão de entrega: 30 minutos 🍕")

# criação do arquivo
with open("pedido.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("----\n")
    arquivo.write(f"Cliente: {nome}\n")
    arquivo.write(f"Pizza: {tamanho.capitalize()} de {sabor.capitalize()}\n")
    arquivo.write(f"Preço: R$ {preco_final:.2f}\n")
    arquivo.write("Entrega em 30 min\n")

import random

# Nome do arquivo com as palavras
# caminho relativo
arquivo = 'exercicio/lista4/br-sem-acentos.txt'

# Lê todas as linhas do arquivo
with open(arquivo, 'r', encoding='utf-8') as file:
    palavras = file.readlines()

# Filtra palavras com pelo menos 3 letras e remove espaços em branco
palavras_validas = [palavra.strip() for palavra in palavras if len(palavra.strip()) >= 7]

# Escolhe uma palavra aleatoriamente
palavra_secreta = random.choice(palavras_validas)

# print(f"A palavra escolhida para o jogo da forca é: {palavra_secreta}")
print(f"palavra secreta tem {len(palavra_secreta)} letras")

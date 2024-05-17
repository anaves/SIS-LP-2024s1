email = "    adalovelace@programadora.com.br   "
email = email.strip() # remove espacos iniciais e finais
partes = email.split("@")
print(partes)
print(len(partes))
login = partes[0]
print(login)
buscar = email.find("ad",4,10)
print(buscar)
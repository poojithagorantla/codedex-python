pesos = int(input("What do you have left in pesos :"))
soles = int(input("What do you have left in soles :"))
reais = int(input("What do you have left in reais :"))

pesosusd = pesos * 0.059
solesusd = soles * 0.26
reaisusd = reais * 0.20

Total = pesosusd + solesusd + reaisusd
print (Total)
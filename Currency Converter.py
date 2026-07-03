# Taking input from user
pesos = float(input("What do you have left in pesos? "))
soles = float(input("What do you have left in soles? "))
reais = float(input("What do you have left in reais? "))

# Formula for Conversion
pesos_To_Dollars = pesos/3684.31
soles_To_Dollars = soles/3.36
reais_To_Dollars = reais/5.20

# Calculating  Total
total = pesos_To_Dollars + soles_To_Dollars + reais_To_Dollars 
print ("You have ", total, "$")
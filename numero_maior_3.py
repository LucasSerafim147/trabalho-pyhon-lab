numero1 = int(input("Adicione um numero inteiro: "))
numero2 = int(input("Adicione outro numero inteiro: "))
numero3 = int(input("Adicione mais um numero inteiro"))

if numero1>numero2 and numero1>numero3:
    print(f"{numero1} é maior")
elif numero2>numero1 and numero2>numero3:
    print(f"{numero2} é maior")
else:
    print(f"{numero3} é maior")

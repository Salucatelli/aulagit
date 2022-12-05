print("Bem Vindo a Calculadora da equação de Torricelli\n\t\t\tV²=V0²+2*a*Δs")

V0 = int(input("\nDigite o valor da velocidade inicial 'V0' em m/s: "))
a = int(input("\nDigite o valor da aceleração 'a' em m/s²: "))
s = int(input("\nDigite o valor da variação do espço 'Δs' em m: "))

V = (V0**2 + (2*a*s))**0.5

print("O valor da Velocidade final V será de:",round(V,2))
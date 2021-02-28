import math

def calcularHipotenusa(cateto1, cateto2):
  soma = (cateto1 * cateto1) + (cateto2 * cateto2)
  return math.sqrt(soma)

c1 = float(input("Digite o valor do primeiro cateto: "))
c2 = float(input("Digite o valor do segundo cateto: "))

vlr = calcularHipotenusa(c1,c2)
print(f"O valor da hipotenusa é {vlr:.2f}")
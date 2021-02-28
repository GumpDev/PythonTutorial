nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

soma = nota1 + nota2 + nota3
media = soma / 3
print(f"Sua média foi {media:.2f}")

if media >= 6:
  print("Você passou!")
else:
  print("Você não passou!")

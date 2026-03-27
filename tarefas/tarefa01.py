def calculadora_salario ():
 salario = float(input("digite seu salario:"))
 cargo = input("digite seu cargo: ")
 novo_salario = 0
 cargo_valido = True
 if cargo == "junior":
    curso = input("vc esta fazendo algum curso ?: ")
    if curso == "sim":
     novo_salario = salario * 1.1 + 100
    else:
        novo_salario = salario * 1.1 
 elif cargo  == "pleno":
    diploma = input("vc possui um diploma:")
    if diploma == "sim":
        novo_salario = salario * 1.3 + 200
    else:
     novo_salario = salario * 1.3
 elif cargo == "senior":
    tempo = float(input("quanto tempo vc esta na emplesa:"))
    novo_salario = salario * 1.5 + tempo * 100
 else:
    print("cargo não encontrado")
    cargo_valido =  False

 if cargo_valido:
    return f"o seu salario é R$ {novo_salario:.2f}" 
 else:
    return "cargo não encontrado "

while True:
 resultado = calculadora_salario()
 print(resultado)
 programa = input("digite sim ou nao para sair do programa: ")
 if programa == "sim":
      print("saindo do programa...")
      break
 elif programa == "nao":
      print("continuando o programa...")
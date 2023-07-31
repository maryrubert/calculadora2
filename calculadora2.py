def calculadora (n1, n2, op):
  calculo = 0
  if(op==1):
    calculo = n1+n2
  elif(op==2):
    calculo = n1-n2
  elif(op==3):
    calculo = n1*n2
  elif(op==4):
    calculo = n1/n2
  return calculo


while(True):
    op = int(input("Escolha a operação: "))
    if(op==0): break
    else: 
      print("Essa operação não existe")

    
    n1 = int(input("Digite o primeiro número  "))
    n2 = int(input("Digite o segundo número  "))

    resultado = calculadora(n1, n2, op)
    print("Resultado:   ", resultado)


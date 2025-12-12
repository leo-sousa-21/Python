a=int(input("Indique um número:"))
b=int(input("Indique outro número"))
print("Operações: 1=+, 2=-, 3=*, 4=/, 5=//, 6=%, 7=**")
op=int(input("Escolha a operação:"))
if op==1:
    op_adicao=a+b
    print ( "Adição- > ",a,"+" , b, "=" ,op_adicao)
if op==2:
    op_subtracao=a-b
    print("Subtração->",a,"-",b,"=" , op_subtracao)
if op==3:
    op_multiplicacao=a*b
    print("Multiplicação->" ,a,"X" ,b,"=" , op_multiplicacao)
if op==4:
    op_divisao=a/b
    print( "Dívisão-> ",a," / ",b,"=",op_divisao)
if op==5:
    op_divisao_int=a//b
    print( "Dívisão inteira->",a,"//",b,"=",op_divisao_int)
if op==6:
    op_modulo_div=a%b
    print("Módulo-> ",a,"%", b, "=" , op_modulo_div)
if op==7:
    op_exponenciacao=a** b
    print("Exponenciação->",a,"**" ,b,"=" , op_exponenciacao)
escolha=input("Escolhe A(Adição) ou M(Multiplicação): ")
m1=a1=float(input("Digite o primeiro número: "))
m2=a2=float(input("Digite o segundo número: "))
def adicao(a1,a2):
    adicao= a1+a2
    return adicao
def multiplicacao(m1,m2):
    multiplicacao= m1*m2
    return multiplicacao
match: escolha
if escolha == "M":
    print("A multiplicação de",m1," com",m2,"é igual",multiplicacao(m1,m2))
elif escolha == "A":
    print("A soma de ",a1," com ",a2,"é igual a ",adicao(a1,a2))
else:
    print("A OPERAÇÃO É INVÁLIDA!")


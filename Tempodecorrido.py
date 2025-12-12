seg= int(input("Digite os segundos de 0 a 59?: "))
while not((seg>59) and seg<0):
    print("Não é possível esse valor.")
    seg= int(input("Digite novamente os segundos de 0 a 59?: ")) 
min= int(input("Que Minutos saõ?: "))
while not((min<0) and min>59):
    print("Não é possível esse valor.")
    min= int(input("Digite novamente os minutos de 0 a 59?: "))

hor= int(input("Que Horas saõ?: "))
    
hor=hor*3600
min=min*60
res=hor+min+seg
print("A soma do tempo é:",res,"segundos")

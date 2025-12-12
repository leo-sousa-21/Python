print("--TABELA DE VERDADE - OP. LÓG. ANO" )
print( "A\tB\ t\tAandB")
a=b=True
print(a," \ t",b,"\t\t",a and b)
a=True
b=False
print(a,"\t",b,"\t\t",a and b)
a=False
b=True
print(a,"\t",b,"\t\t ",a and b)
a=b=False
print(a,"\t",b,"\t\t",a and b)
print("--TABELA DE VERDADE-OP. LÓG. DR" )
print("A\t8\t\t", a and b)
a=b=True
print(a,"\t ",b,"\t\t",a or b)
a=True
b=False
print(a,"\t",b,"\t \t",a or b)
a=False
b=True
print(a,"\t",b,"\t\t",a or b)
a=b=False
print(a,"1\ t ",b,"\t\t",a or b)
print("--TABELA DE VERDADE- OP. LÓG.NOT" )
print ( "A\t\t not( a ) " )
a=True
print(a,"\t\t",not a)
a=False
print(a,"\t\t",not a )
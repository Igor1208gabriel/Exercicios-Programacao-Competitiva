dias = int(input())

anos = dias // 365

meses = (dias%365)//30

dias = (dias%365)%30

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")
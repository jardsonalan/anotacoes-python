import datetime

ano = int(input("Qual o ano que deseja analisar? Coloque 0 se quiser analisar o ano atual: "))

if ano == 0:
    ano = datetime.date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano de {ano} é BISSEXTO")

else:
    print(f"O ano de {ano} NÃO é BISSEXTO")
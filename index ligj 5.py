salary = [340, 210, 450, 600, 230, 500, 550, 300]
shuma = 0
for paga in salary:
    shuma = shuma + paga

    

pagaMin = min(salary)
pagaMax = max(salary)
print(f"Paga minimale eshte {pagaMin} ")
print(f"Paga maximale eshte {pagaMax} ")

pagaMin = salary[0]
for pagaAktuale in salary:
    if(pagaAktuale < pagaMin):
        pagaMin = pagaAktuale
    print(f"Paga minimale eshte {pagaMin}")
    
    pagaMax = salary[0]
    for pagaAktuale in salary:
        if(pagaAktuale > pagaMax)
        pagaMax = pagaAktuale
        print(f"Paga maximale eshte {pagaMax}")
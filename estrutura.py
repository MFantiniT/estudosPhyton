# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
def Salario():
    ganhaHora = int(input("quanto você ganha por hora "))
    horasDia = int(input("quantas horas por dia você trabalha?? "))
    trabFind = (input("trabalha final de semana?? (S/N) "))
    if(trabFind == "S"):
        # 26 porque segundos as normas trabalhistas para quem trabalha a semana completa, tem q ter uma folga fixa/semana e um dom/mês. dom(-1) fixa(-4)
        horasMes = horasDia*26
        salarioBruto = horasMes*ganhaHora
    else:
        # considerando um "mês perfeito" de 31 dias, 4 finais de semana dois dias cada (31-8)
        horasMes = horasDia*23
        salarioBruto = horasMes*ganhaHora

    # calculos que definem as porcetagens de cada desconto em folha:

    IR = salarioBruto*0.11
    INSS = salarioBruto*0.08
    sindicato = salarioBruto*0.05

    # feito dessa forma porque já tinha digitado o calculo pras porcentagens antes de pensar em como seria feito o calculo do salário liquido hehe

    print("salario base: ", salarioBruto)
    print("IR: ", IR)
    print("INSS: ", INSS)
    print("Sindicato: ", sindicato)
    print("Salário líquido: ", salarioBruto-INSS-IR-sindicato)
    return salarioBruto


folhaDePagamento = Salario()

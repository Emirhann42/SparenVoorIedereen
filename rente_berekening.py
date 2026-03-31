import datetime

date = datetime.datetime.now()
saldo = 100

rente_voor_spaarder = 0.018
def rentepercentage_berekenen(saldo):
   if saldo <= 0:
       raise ValueError("Saldo is telaag")
   elif saldo <= 10000:
       return rente_voor_spaarder - 0.0025
   elif saldo <= 25000:
       return rente_voor_spaarder
   elif saldo <= 50000:
       return rente_voor_spaarder - 0.0015
   elif saldo <= 100000:
       return rente_voor_spaarder - 0.005
   elif saldo >= 1000000:
       return 0

def schrikkel_jaar():
    jaar = date.year
    return (jaar % 4 == 0 and jaar % 100 != 0) or (jaar % 400 == 0)

def rente_berekenen(saldo):
    jaar = date.year
    rentepercentage = rentepercentage_berekenen(saldo)
    if schrikkel_jaar():
        rente = (rentepercentage / 366) * saldo
    else:
        rente = (rentepercentage / 365) * saldo
    return rente

def welke_kwartaal():
    maand = date.month
    if  maand < 3 and schrikkel_jaar():
        return 1
    elif maand < 3:
        return 1.5
    elif maand < 6:
        return 2
    elif maand < 9:
        return 3
    elif maand < 12:
        return 4

def bereken_kwartaal(saldo):
    kwartaal = welke_kwartaal()
    match kwartaal:
        case 1:
            return rente_berekenen(saldo)  * 91
        case 1.5:
            return rente_berekenen(saldo) * 90
        case 2:
            return rente_berekenen(saldo) * 91
        case 3:
            return  rente_berekenen(saldo) * 92
        case 4:
            return rente_berekenen(saldo) * 92







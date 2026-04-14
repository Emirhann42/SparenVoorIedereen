import datetime

date = datetime.datetime.now()

rente_voor_spaarder = 0.018
def rentepercentage_berekenen(saldo):
   if saldo <= 0:
       print("error")
   elif saldo <= 10000:
       return rente_voor_spaarder - 0.0025
   elif saldo <= 25000:
       return rente_voor_spaarder
   elif saldo <= 50000:
       return rente_voor_spaarder - 0.0015
   elif saldo <= 100000:
       return rente_voor_spaarder - 0.005
   elif saldo <= 1000000:
       return 0

def rente_berekenen(saldo):
    jaar = date.year
    rentepercentage = rentepercentage_berekenen(saldo)
    if jaar % 4 == 0:
        rente = (rentepercentage / 366) * saldo
    else:
        rente = (rentepercentage / 365) * saldo
    return rente









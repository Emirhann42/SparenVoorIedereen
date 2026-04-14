import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS klanten("
            "klant_id INTEGER PRIMARY KEY,"
            "naam TEXT,"
            "adres TEXT,"
            "email TEXT,"
            "telefoonnummer TEXT,"
            "wachtwoord TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS spaarrekening("
            "rekening_id INTEGER PRIMARY KEY,"
            "klant_id INTEGER,"
            "saldo DECIMAL,"
            "openings_datum DATE,"
            "status TEXT,"
            "FOREIGN KEY (klant_id) REFERENCES klanten(klant_id))")
cur.execute("CREATE TABLE IF NOT EXISTS transacties("
            "transactie_id INTEGER PRIMARY KEY,"
            "rekening_id INTEGER,"
            "type TEXT,"
            "bedrag DECIMAL,"
            "datum DATE,"
            "omschrijving TEXT,"
            "FOREIGN KEY (rekening_id) REFERENCES spaarrekening(rekening_id))")
cur.execute("CREATE TABLE IF NOT EXISTS rentetarief("
            "tarief_id INTEGER PRIMARY KEY,"
            "saldoklasse_min DECIMAL,"
            "saldoklasse_max DECIMAl,"
            "rentepercentage DECIMAL,"
            "ingangsdatum DATE)")
cur.execute("CREATE TABLE IF NOT EXISTS renteregistratie("
            "registratie_id INTEGER PRIMARY KEY,"
            "rekening_id INTEGER,"
            "tarief_id INTEGER,"
            "bedrag DECIMAL,"
            "berekeningsdatum DATE,"
            "uitkeringsdatum DATE,"
            "FOREIGN KEY (tarief_id) REFERENCES rentetarief(tarief_id),"
            "FOREIGN KEY (rekening_id) REFERENCES spaarrekening(rekening_id))")
con.commit()
con.close()
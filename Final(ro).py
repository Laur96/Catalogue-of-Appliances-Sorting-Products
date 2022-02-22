class Catalog:
    
    Clasa = "Electrocasnice Mari"
    clasa = "Electrocasnice Mici"
    lista = []

    def __init__(self, pret, consum, producator, cod_produs):
        self.p = pret
        self.c = consum
        self.pr = producator
        self.cp = cod_produs
        self.lista.append(self)


    def __str__(self):
        sir1 = 'Pretul: {} de lei || '.format(self.p)
        sir2 = 'Consumul: {} de W || '.format(self.c)
        sir3 = 'Producator: {}  || '.format(self.pr)
        sir4 = 'Codul Produsului este: {} \n'.format(self.cp)
        return sir1 + sir2 + sir3 + sir4


    def __repr__(self):
        return self.__str__()


    @classmethod
    def sorteaza_dupa_pret(cls):
        print("\nSe sorteaza dupa pret: ")
        for count, obj in enumerate(sorted(cls.lista, key = lambda elem: elem.p, reverse = True)):
            print("Pozitia {0}. {1} de lei".format(count + 1, obj.p))


    @classmethod
    def sorteaza_dupa_consum(cls):
        print("\nSe sorteaza dupa consum: ")
        for count, obj in enumerate(sorted(cls.lista, key = lambda elem: elem.c, reverse = True)):
            print("Locul {1}. {0} de W".format(obj.c, count + 1))


    @classmethod
    def afisare_producator(Cls):
        print("\nAfisare producatori: ")
        for count, obj in enumerate(sorted(Cls.lista, key = lambda elem: elem.pr)):
            print(f"{count + 1}. {obj.pr}")




class ElectrocasniceMari(Catalog):

    def __init__(self, pret, consum, producator, cod_produs, adancime, latime, inaltime):
        Catalog.__init__(self, pret, consum, producator, cod_produs)
        self.a = adancime
        self.l = latime
        self.inn = inaltime


    def __str__(self):
        rs1 = 'Adancimea: {}m || '.format(self.a)
        rs2 = 'Latimea: {}m || '.format(self.l)
        rs3 = 'Inaltimea: {}m || '.format(self.inn)
        return rs1 + rs2 + rs3


    def __repr__(self):
        return self.__str__()


class ElectrocasniceMici(Catalog):

    def __init__(self, pret, consum, producator, cod_produs, lungime_cablu, baterie):
        Catalog.__init__(self, pret, consum, producator, cod_produs)
        self.lc = lungime_cablu
        self.b = baterie


    def __str__(self):
        sri1 = 'Lungimea cablului: {}m || '.format(self.lc)
        sri2 = 'Baterie: {}V || '.format(self.b)
        return sri1 + sri2


    def __repr__(self):
        return self.__str__()


class Frigider(ElectrocasniceMari, Catalog):

    subclasa = "Frigider"
    def __init__(self, pret, consum, producator, cod_produs, adancime, latime, inaltime, capacitate_congelator, capacitate_frigider):
        ElectrocasniceMari.__init__(self, pret, consum, producator, cod_produs, adancime, latime, inaltime)
        Catalog.__init__(self, pret, consum, producator, cod_produs)
        self.cc = capacitate_congelator
        self.cf = capacitate_frigider


    def __str__(self):
        s1ir = 'Capacitatea congelatorului: {} || '.format(self.cc)
        s2ir = 'Capacitatea frigiderului: {} '.format(self.cf)
        return Catalog.__str__(self) + ElectrocasniceMari.__str__(self) + s1ir + s2ir


    def __repr__(self):
        return self.__str__()


class Aragaz(ElectrocasniceMari, Catalog):

    subclasa = "Aragaz"
    def __init__(self, pret, consum, producator, cod_produs, adancime, latime, inaltime, nr_arzatoare):
        ElectrocasniceMari.__init__(self, pret, consum, producator, cod_produs, adancime, latime, inaltime)
        Catalog.__init__(self, pret, consum, producator, cod_produs)
        self.na = nr_arzatoare


    def __str__(self):
        skl = 'Nr.arzatoare: {} '.format(self.na)
        return Catalog.__str__(self) + ElectrocasniceMari.__str__(self) + skl


    def __repr__(self):
        return self.__str__()


class Mixer(ElectrocasniceMici, Catalog):

    subclasa = "Mixer"
    def __init__(self, pret, consum, producator, cod_produs, lungime_cablu, baterie, rotatii_pe_minut):
        ElectrocasniceMici.__init__(self, pret, consum, producator, cod_produs, lungime_cablu, baterie)
        Catalog.__init__(self, pret, consum, producator, cod_produs)
        self.rpm = rotatii_pe_minut


    def __str__(self):
        spp1 = f"Rotatii pe minut: {self.rpm} "
        return Catalog.__str__(self) + ElectrocasniceMici.__str__(self) + spp1


    def __repr__(self):
        return self.__str__()


class FierCalcat(ElectrocasniceMici, Catalog):

    subclasa = "Fier Calcat"
    def __init__(self, pret, consum, producator, cod_produs, lungime_cablu, baterie, rezervor):
        ElectrocasniceMici.__init__(self, pret, consum, producator, cod_produs, lungime_cablu, baterie)
        Catalog.__init__(self, pret, consum, producator, cod_produs)
        self.r = rezervor


    def __str__(self):
        smm = f"Rezervor: {self.r} litri "
        return Catalog.__str__(self) + ElectrocasniceMici.__str__(self) + smm


    def __repr__(self):
        return self.__str__()


a1 = Frigider(386.72, 500, "Arctic", "dftg45erg35", 0.45, 0.50, 1.80, 40, 30)
b = Aragaz(172.50, 200, "Zass", "dfge53twreht", 0.30, 0.35, 0.50, 5)
c = Mixer(79.65, 100, "Bosch", "cbgeevtr", 1.50, 40, 500)
d = FierCalcat(100, 150, "Tefal", "fgvg35etv4gr", 0.45, 45, 0.12)

print(a1.p, a1.c, a1.pr, a1.cp, a1.a, a1.l, a1.inn, a1.cc, a1.cf)
print(b.p, b.c, b.pr, b.cp, b.a, b.l, b.inn, b.na)
print(c.p, c.c, c.pr, c.cp, c.lc, c.b, c.rpm)
print(d.p, d.c, d.pr, d.cp, d.lc, d.b, d.r)
print("\n")
print(a1.subclasa + "(" + a1.Clasa + ") ->", a1, "\n")
print(b.subclasa + "(" + b.Clasa + ") ->", b, "\n")
print(c.subclasa + "(" + c.clasa + ") ->", c, "\n")
print(d.subclasa + "(" + d.clasa + ") ->", d, "\n")

d.sorteaza_dupa_pret()
d.sorteaza_dupa_consum()
d.afisare_producator()

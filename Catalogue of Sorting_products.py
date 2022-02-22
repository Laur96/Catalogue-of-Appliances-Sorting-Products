""" Catalogue of Appliances — Sorting Products """

class Catalogue:

    PClass = "Large Appliances"
    CClass = "Small Appliances"
    the_list = []

    def __init__(self, price, consumption, producer, product_code):
        self.p = price
        self.c = consumption
        self.pr = producer
        self.pc = product_code
        self.the_list.append(self)


    def __str__(self):
        sir1 = 'The Price: ${} || '.format(self.p)
        sir2 = 'The Consumption is: {}W || '.format(self.c)
        sir3 = 'Manufacturer: {}  || '.format(self.pr)
        sir4 = 'The Product Code is: {} \n'.format(self.pc)
        return sir1 + sir2 + sir3 + sir4


    def __repr__(self):
        return self.__str__()


    @classmethod
    def sort_by_price(cls):
        print("\nSort by Price: ")
        for count, obj in enumerate(sorted(cls.the_list, key = lambda elem: elem.p, reverse = True)):
            print("Position {0}. ${1}".format(count + 1, obj.p))


    @classmethod
    def sort_by_consumption(cls):
        print("\nSort by Consumption: ")
        for count, obj in enumerate(sorted(cls.the_list, key = lambda elem: elem.c, reverse = True)):
            print("#Nb.{1}. {0}W".format(obj.c, count + 1))


    @classmethod
    def show_manufacturer(Cls):
        print("\nShow the producers: ")
        for count, obj in enumerate(sorted(Cls.the_list, key = lambda elem: elem.pr)):
            print(f"{count + 1}. {obj.pr}")



class Large_Appliances(Catalogue):

    def __init__(self, price, consumption, producer, product_code, depth, width, height):
        Catalogue.__init__(self, price, consumption, producer, product_code)
        self.d = depth
        self.w = width
        self.h = height


    def __str__(self):
        rs1 = 'Depth is: {}m || '.format(self.d)
        rs2 = 'Width is: {}m || '.format(self.w)
        rs3 = 'Height is: {}m || '.format(self.h)
        return rs1 + rs2 + rs3


    def __repr__(self):
        return self.__str__()


class Small_Appliances(Catalogue):

    def __init__(self, price, consumption, producer, product_code, cable_length, battery_type):
        Catalogue.__init__(self, price, consumption, producer, product_code)
        self.cl = cable_length
        self.b = battery_type


    def __str__(self):
        sri1 = "Cable's Length: {}m || ".format(self.cl)
        sri2 = 'Battery: {}V || '.format(self.b)
        return sri1 + sri2


    def __repr__(self):
        return self.__str__()


class Fridge(Large_Appliances, Catalogue):

    subclass = "Fridge"
    def __init__(self, price, consumption, producer, product_code, depth, width, height, freezer_capacity, fridge_capacity):
        Large_Appliances.__init__(self, price, consumption, producer, product_code, depth, width, height)
        Catalogue.__init__(self, price, consumption, producer, product_code)
        self.Fc = freezer_capacity
        self.fc = fridge_capacity


    def __str__(self):
        s1ir = 'Total Volume of the freezer is: {} cube meters || '.format(self.Fc)
        s2ir = 'Total Volume of the fridge is: {} cube meters '.format(self.fc)
        return Catalogue.__str__(self) + Large_Appliances.__str__(self) + s1ir + s2ir


    def __repr__(self):
        return self.__str__()


class GasCooker(Large_Appliances, Catalogue):

    subclass = "GasCooker"
    def __init__(self, price, consumption, producer, product_code, depth, width, height, gas_cooker_burners):
        Large_Appliances.__init__(self, price, consumption, producer, product_code, depth, width, height)
        Catalogue.__init__(self, price, consumption, producer, product_code)
        self.gcb = gas_cooker_burners


    def __str__(self):
        skl = 'The number of gas cooker burners is: {} '.format(self.gcb)
        return Catalogue.__str__(self) + Large_Appliances.__str__(self) + skl


    def __repr__(self):
        return self.__str__()


class Mixer(Small_Appliances, Catalogue):

    subclass = "Mixer"
    def __init__(self, price, consumption, producer, product_code, cable_length, battery_type, rotations_per_minute):
        Small_Appliances.__init__(self, price, consumption, producer, product_code, cable_length, battery_type)
        Catalogue.__init__(self, price, consumption, producer, product_code)
        self.rpm = rotations_per_minute


    def __str__(self):
        spp1 = f"Rotations Per Minute: {self.rpm} "
        return Catalogue.__str__(self) + Small_Appliances.__str__(self) + spp1


    def __repr__(self):
        return self.__str__()


class SteamIron(Small_Appliances, Catalogue):

    subclass = "SteamIron"
    def __init__(self, price, consumption, producer, product_code, cable_length, battery_type, rezervoir):
        Small_Appliances.__init__(self, price, consumption, producer, product_code, cable_length, battery_type)
        Catalogue.__init__(self, price, consumption, producer, product_code)
        self.r = rezervoir


    def __str__(self):
        smm = f"Rezervoir capacity is: {self.r} liters "
        return Catalogue.__str__(self) + Small_Appliances.__str__(self) + smm


    def __repr__(self):
        return self.__str__()


a1 = Fridge(386.72, 500, "Arctic", "dftg45erg35", 0.45, 0.50, 1.80, 40, 30)
b = GasCooker(172.50, 200, "Zass", "dfge53twreht", 0.30, 0.35, 0.50, 5)
c = Mixer(79.65, 100, "Bosch", "cbgeevtr", 1.50, 40, 100)
d1 = SteamIron(100, 150, "Tefal", "fgvg35etv4gr", 0.45, 45, 0.12)

print(a1.p, a1.c, a1.pr, a1.pc, a1.d, a1.w, a1.h, a1.Fc, a1.fc)
print(b.p, b.c, b.pr, b.pc, b.d, b.w, b.h, b.gcb)
print(c.p, c.c, c.pr, c.pc, c.cl, c.b, c.rpm)
print(d1.p, d1.c, d1.pr, d1.pc, d1.cl, d1.b, d1.r)
print("\n")
print(a1.subclass + "(" + a1.PClass + ") ->", a1, "\n")
print(b.subclass + "(" + b.PClass + ") ->", b, "\n")
print(c.subclass + "(" + c.CClass + ") ->", c, "\n")
print(d1.subclass + "(" + d1.CClass + ") ->", d1, "\n")

d1.sort_by_price()
d1.sort_by_consumption()
d1.show_manufacturer()

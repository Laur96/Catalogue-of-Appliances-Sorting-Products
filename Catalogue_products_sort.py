#Catalogue of Appliances — Sorting Products

class Catalogue:
      the_list=[]
      Parent_Class=None
      Child_Class=None
      def __init__(self, Price, Consumption, Producer, ProductCode):
            self.Price = Price
            self.Consumption = Consumption
            self.Producer = Producer
            self.ProductCode = ProductCode
            self.the_list.append(self)

      def __str__(self):
            sir = '\nThe Price: ${}  \n'.format(self.Price)
            sir += 'The Consumption is: {} de W \n'.format(self.Consumption)
            sir += 'Manufacturer: {}  \n'.format(self.Producer)
            sir += 'The Code of Product is: {} \n'.format(self.ProductCode)
            return sir

      def __repr__(self):
            return self.__str__()

      def add_object(self, ObjectName):
            self.the_list.append(ObjectName)

      @classmethod
      def sort_by_price(cls):
            print("\nSort by Price: ")
            count = 0
            for obj in sorted(cls.the_list, key = lambda elem:elem.Price, reverse=True):
                  count += 1
                  print(f"Position {count}. ${obj.Price}")

      @classmethod
      def sort_by_consumption(cls):
            print("\nSort by Consumption: ")
            count=0
            for obj in sorted(cls.the_list, key = lambda elem:elem.Consumption, reverse=True):
                  count += 1
                  print(f"The Place {count}. {obj.Consum} Watts")

      @classmethod
      def show_manufacturer(cls):
            print("\nShow the producers: ")
            count=0
            for obj in sorted(cls.the_list, key = lambda elem:elem.Producer, reverse=True):
                  count += 1
                  print(f"{count}. {obj.Producer}")

      @classmethod
      def display_object(cls):
            search_object = input("\nDisplay The Object: ")
            count = 0
            for obj in sorted(cls.the_list, key = lambda elem:elem.Producer, reverse=True):
                  if obj.Producer == search_object:
                        obj.Producer = search_object
                        count += 1
                        print(f'Case: {count} => the object {count} / {object.Producer}')
                  else:
                        return Catalogue.show_manufacturer()

class Large_Appliances(Catalogue):
      def __init__(self, Depth, Width, Height, Price, Consumption, Producer, ProductCode):
            super(Large_Appliances).__init__(Price, Consumption, Producer, ProductCode)
            self.Depth = Depth
            self.Width = Width
            self.Height = Height
            if Catalogue.Parent_Class is None:
                  self.Parent_Class = " "
            self.Parent_Class += "\nLarge_Appliances"

      def __str__(self):
            sdc = "Depth is: {} cm \n".format(self.Depth)
            sdc += "Width is: {} cm \n".format(self.Width)
            sdc += "Height is: {} cm \n".format(self.Height)
            return super().__str__ + sdc

      def __repr__(self):
            return self.__str__()

class Small_Appliances(Catalogue):
      def __init__(self, CableLength, BatteryType, Price, Consumption, Producer, ProductCode):
            super(Small_Appliances).__init__(Price, Consumption, Producer, ProductCode)
            self.CableLength = CableLength
            self.BatteryType = BatteryType
            if Catalogue.Parent_Class is None:
                  self.Parent_Class = " "
            self.Parent_Class += "\nSmall_Appliances"

      def __str__(self):
            cds = "Cable's Length : {} cm \n".format(self.CableLength)
            cds = "Battery Type : {} \n".format(self.BatteryType)
            return super().__str__() + cds

      def __repr__(self):
            return self.__str__()

class Fridge(Large_Appliances):
      def __init__(self, FreezerCapacity, FridgeCapacity, Price, Consumption, Producer, ProductCode):
            super(Fridge).__init__(Price, Consumption, Producer, ProductCode, Depth, Width, Height)
            self.FreezerCapacity = FreezerCapacity
            self.FridgeCapacity = FridgeCapacity
            if Catalog.Child_Class is None:
                  self.Child_Class = " "
            self.Child_Class += "\nFridge"

      def __str__(self):
            strd = "Total Volue of the freezer is: {} cube meters \n".format(self.FreezerCapacity)
            strd = "Total Volue of the fridge is: {} cube meters \n".format(self.FridgeCapacity)
            return super().__str__() + strd

      def __repr__(self):
            return self.__str__()

class Gas_Cooker(Large_Appliances):
      def __init__(self, GasCookerBurners, Price, Consumption, Producer, ProductCode):
            super(Gas_Cooker).__init__(Price, Consumption, Producer, ProductCode, Depth, Width, Height)
            self.GasCookerBurners = GasCookerBurners
            if Catalogue.Child_Class is None:
                  self.Child_Class = " "
            self.Child_Class += "\nGas Cooker"

      def __str__(self):
            ddrt = "The number of gas cooker burners is : {} \n".format(self.GasCookerBurners)
            return super().__str__() + ddrt

      def __repr__(self):
            return self.__str__()

class Mixer(Small_Appliances):
      def __init__(self, RotationsPerMinute, Price, Consumption, Producer, ProductCode):
            super(Mixer).__init__(Price, Consumption, Producer, ProductCode, LungimeCablu, Baterie)
            self.RotationsPerMinute = RotationsPerMinute
            if Catalogue.Child_Class is None:
                  self.Child_Class = " "
            self.Child_Class += "\nMixer"

      def __str__(self):
            kjli = "Rotations Per Minute: {} \n".format(self.RotationsPerMinute)
            return super().__str__() + kjli

      def __repr__(self):
            return self.__str__()

class SteamIron(Small_Appliances):
      def __init__(self, RotationsPerMinute, Price, Consumption, Producer, ProductCode):
            super(SteamIron).__init__(Price, Consumption, Producer, ProductCode, CableLength, BatteryType)
            self.RotationsPerMinute = RotationsPerMinute
            if Catalogue.Child_Class is None:
                  self.Child_Class = " "
            self.Child_Class += "\nSteamIron"

      def __str__(self):
            ffgr = "Reservoir capacity is : {} liters \n".format(self.Reservoir)
            return super().__str__() + ffgr

      def __repr__(self):
            return self.__str__()

object1 = Catalogue(98, 40, "Orion", "dsfr4rfsd")
object2 = Catalogue(56.79, 9.9, "Arctic", "qwsd23r")
object3 = Catalogue(357.49, 54, "Lg", "rgn4ju65y")
object4 = Catalogue(
int(input("Tell us the price: ")),
int(input("Now the consumption: ")),
str(input("Who is the manufacturer?: ")),
str(input("And finally the product code:"))
)

print(object1)
print(object2)
print(object3)
print(object4)

object1.add_object(object1)
object2.add_object(object2)
object3.add_object(object3)
object3.add_object(object4)

print(Catalogue.the_list)

Catalogue.sort_by_price()
Catalogue.sort_by_consumption()
Catalogue.show_manufacturer()
Catalogue.display_object()

class Automobile:

    def __init__(self, make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    def add_vehicle(self):
        #auto = Automobile()
        vehicle_file = open('vehicle.txt', 'a')
        make = input("Enter make: ")
        model = input("Enter model: ")
        color = input("Enter color: ")
        year = input("Enter year: ")
        mileage = input("Enter mileage: ")

        vehicles = Automobile(make, model, color, year, mileage)
        vehicle_list = [vehicles.make, vehicles.model, vehicles.color, vehicles.year, vehicles.mileage]

        for i in vehicle_list:
            vehicle_file.write("%s\t" % item)
            vehicle_file.write("\n")
            vehicle_file.close()
        print("Your record has been succesfully added to the inventory")

    def delete_vehicle(self):
        del_rec = input("Enter record to delete: ")

        with open("vehicle.txt","r+") as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                if del_rec not in line:
                    f.write(line)
            f.truncate()
        print("Succesfully deleted record from inventory")

    def set_make(self, make):
        self.make = make

    def get_make(self):
        return self.make

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_mileage(self, mileage):
        self.mileage = mileage

    def get_mileage(self):
        return self.mileage

def main():
    menu = {}
    menu['1']="Add Vehicle." 
    menu['2']="Delete Vehicle."
    menu['3']="Find Vehicle"
    menu['4']="Exit"

user=True
while user:
    print ("""
    1.Add a Vehicle
    2.Delete a Vehicle
    3.View Inventory
    4.Exit/Quit
    """)
    ans=input("What would you like to do? ") 
    if ans=="1": 
      Automobile.add_vehicle
    elif ans=="2":
      Automobile.delete_vehicle(self)
    elif ans=="3":
      print(Automobile.vehicles) 
    elif ans=="4":
      print("\n Goodbye")
      break
    elif ans !="":
      print("\n Invaild Entry")

if __name__ == "__main__":
    main()
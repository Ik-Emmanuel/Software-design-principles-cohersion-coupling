"""
Analysing code cohesion and coupling and improving on it  
"""
import string
import random

class VehicleRegistry:
    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"


class Application:
    def register_vehicle(self, brand: string):
        """ A method with very low cohesion doing alot of things which is considered too much
        also  it is highly coupled cause it directly dependent on the Vehicle Registry class.  so a change in vehicle registry will require a chance in this class as well. 
        """
        # create a registry instance
        registry = VehicleRegistry()

        # generate a vehicle id of length 12
        vehicle_id = registry.generate_vehicle_id(12)

        # now generate a license plate for the vehicle
        # using the first two characters of the vehicle id
        license_plate = registry.generate_vehicle_license(vehicle_id)

        
        """
        Computing the catalogue price we can
        spot high coupling between brand name and its catalogue price which is inefficient 
        """
        catalogue_price = 0
        if brand == "Tesla Model 3":
            catalogue_price = 60000
        elif brand == "Volkswagen ID3":
            catalogue_price = 35000
        elif brand == "BMW 5":
            catalogue_price = 45000


        """
         compute the tax percentage (default 5% of the catalogue price, except for electric cars where it is 2%) we can
        spot high coupling between tax payable  and car brand which is also inefficient 
        """
        tax_percentage = 0.05
        #hard coding the brand check makes it hard to scale and add more brands
        if brand == "Tesla Model 3" or brand == "Volkswagen ID3":
            tax_percentage = 0.02

        # compute the payable tax
        payable_tax = tax_percentage * catalogue_price

        # print out the vehicle registration information
        print("Registration complete. Vehicle information:")
        print(f"Brand: {brand}")
        print(f"Id: {vehicle_id}")
        print(f"License plate: {license_plate}")
        print(f"Payable tax: {payable_tax}")

app = Application()
app.register_vehicle("BMW 5")
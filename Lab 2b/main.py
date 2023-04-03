class Property:
    def __init__(self, square_feet, num_bedrooms, num_bathrooms):
        self.square_feet = square_feet
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms

    def display(self):
        print("PROPERTY DETAILS")
        print(f"Square Feet: {self.square_feet}, Bedrooms: {self.num_bedrooms}, Bathrooms: {self.num_bathrooms}")

class House(Property):
    def __init__(self, square_feet, num_bedrooms, num_bathrooms, num_stories, garage, fenced_yard):
        super().__init__(square_feet, num_bedrooms, num_bathrooms)
        self.num_stories = num_stories
        self.garage = garage
        self.fenced_yard = fenced_yard

    def display(self):
        super().display()
        print("HOUSE DETAILS")
        print(f"Stories: {self.num_stories}, Garage: {self.garage}, Fenced Yard: {self.fenced_yard}")

    @staticmethod
    def prompt_init():
        return dict(square_feet=input("Enter the square feet: "),
                    num_bedrooms=input("Enter the number of bedrooms: "),
                    num_bathrooms=input("Enter the number of bathrooms: "),
                    num_stories=input("Enter the number of stories: "),
                    garage=input("Does it have a garage? (yes/no) "),
                    fenced_yard=input("Does it have a fenced yard? (yes/no) "))

class Apartment(Property):
    def __init__(self, square_feet, num_bedrooms, num_bathrooms, balcony, laundry):
        super().__init__(square_feet, num_bedrooms, num_bathrooms)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print(f"Balcony: {self.balcony}, Laundry: {self.laundry}")

    @staticmethod
    def prompt_init():
        return dict(square_feet=input("Enter the square feet: "),
                    num_bedrooms=input("Enter the number of bedrooms: "),
                    num_bathrooms=input("Enter the number of bathrooms: "),
                    balcony=input("Does it have a balcony? (yes/no) "),
                    laundry=input("Does it have laundry? (yes/no) "))

class Purchase:
    def __init__(self, price, taxes):
        self.price = price
        self.taxes = taxes

    def display(self):
        print("PURCHASE DETAILS")
        print(f"Price: {self.price}, Taxes: {self.taxes}")

    @staticmethod
    def prompt_init():
        return dict(price=input("Enter the price: "),
                    taxes=input("Enter the taxes: "))

class Rental:
    def __init__(self, rent, utilities, furnished):
        self.rent = rent
        self.utilities = utilities
        self.furnished = furnished

    def display(self):
        print("RENTAL DETAILS")
        print(f"Rent: {self.rent}, Utilities: {self.utilities}, Furnished: {self.furnished}")

    @staticmethod
    def prompt_init():
        return dict(rent=input("What is the monthly rent? "),
                    utilities=input("What are the estimated monthly utilities? "),
                    furnished=input("Is the property furnished? (yes/no) "))


class HousePurchase(House, Purchase):
    def __init__(self, square_feet, num_bedrooms, num_bathrooms, num_stories, garage, fenced_yard, price, taxes):
        House.__init__(self, square_feet, num_bedrooms, num_bathrooms, num_stories, garage, fenced_yard)
        Purchase.__init__(self, price, taxes)

    def display(self):
        House.display(self)
        Purchase.display(self)

    @staticmethod
    def prompt_init():
        prop_dict = House.prompt_init()
        prop_dict.update(Purchase.prompt_init())
        return prop_dict

class HouseRental(House, Rental):
    def __init__(self, square_feet, num_bedrooms, num_bathrooms, num_stories, garage, fenced_yard, rent, utilities, furnished):
        House.__init__(self, square_feet, num_bedrooms, num_bathrooms, num_stories, garage, fenced_yard)
        Rental.__init__(self, rent, utilities, furnished)

    def display(self):
        House.display(self)
        Rental.display(self)

    @staticmethod
    def prompt_init():
        prop_dict = House.prompt_init()
        prop_dict.update(Rental.prompt_init())
        return prop_dict

class ApartmentPurchase(Apartment, Purchase):
    def __init__(self, square_feet, num_bedrooms, num_bathrooms, balcony, laundry, price, taxes):
        Apartment.__init__(self, square_feet, num_bedrooms, num_bathrooms, balcony, laundry)
        Purchase.__init__(self, price, taxes)

    def display(self):
        Apartment.display(self)
        Purchase.display(self)

    @staticmethod
    def prompt_init():
        prop_dict = Apartment.prompt_init()
        prop_dict.update(Purchase.prompt_init())
        return prop_dict

class ApartmentRental(Apartment, Rental):
    def __init__(self, square_feet, num_bedrooms, num_bathrooms, balcony, laundry, rent, utilities, furnished):
        Apartment.__init__(self, square_feet, num_bedrooms, num_bathrooms, balcony, laundry)
        Rental.__init__(self, rent, utilities, furnished)

    def display(self):
        Apartment.display(self)
        Rental.display(self)

    @staticmethod
    def prompt_init():
        prop_dict = Apartment.prompt_init()
        prop_dict.update(Rental.prompt_init())
        return prop_dict

class Agent:
    def __init__(self):
        self.properties = []

    def display_properties(self):
        for p in self.properties:
            print("=====================================")
            p.display()
            print("=====================================")

    def add_property(self):
        prop_type = input("Enter property type (house or apartment): ")
        payment_method = input("Enter payment method (rent or purchase): ")
        if prop_type == "house":
            if payment_method == "rent":
                prop_dict = HouseRental.prompt_init()
                self.properties.append(HouseRental(**prop_dict))
            elif payment_method == "purchase":
                prop_dict = HousePurchase.prompt_init()
                self.properties.append(HousePurchase(**prop_dict))
            else:
                print("Invalid payment method.")
        elif prop_type == "apartment":
            if payment_method == "rent":
                prop_dict = ApartmentRental.prompt_init()
                self.properties.append(ApartmentRental(**prop_dict))
            elif payment_method == "purchase":
                prop_dict = ApartmentPurchase.prompt_init()
                self.properties.append(ApartmentPurchase(**prop_dict))
            else:
                print("Invalid payment method.")
        else:
            print("Invalid property type.")


def main():
    agent = Agent()
    while True:
        print("\n=== Real Estate Agent Menu ===")
        print("1. Add property")
        print("2. Display properties")
        print("3. Quit")
        choice = input("Enter choice: ")
        if choice == "1":
            agent.add_property()
        elif choice == "2":
            agent.display_properties()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
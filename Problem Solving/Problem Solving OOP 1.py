#Problem 1
class HackathonTeam:
    def __init__(self,team_name, *args):
        self.team_name = team_name
        self.participant = args
    def information(self):
        print(f"Team Name: {self.team_name}")
        print("Participants:")
        for i in self.participant:
            print(i)
        print()

# Write your codes for subtasks here.
team_1 = HackathonTeam("Atlantean", "Aquaman")
team_1.information()


print("=================")


team_2 = HackathonTeam("Avengers", "Ironman", "Thor", "Hulk")
team_2.information()


print("=================")


team_3 = HackathonTeam("X-Men", "Storm", "Mystique")
team_3.information()


#Problem 2
class Foodie:
    def __init__(self, name):
        self.name = name
        self.orders = []
        self.tips = 0
        self.total = 0

    def order(self, *args):
        for i in args:
            item = i.split('-')
            x = item[0]  # keeping the food name
            self.orders.append(item[0])
            quantity = int(item[1])  # keeping the quantity
            price_per_unit = 0
            for j in menu:
                if j in x:
                    price_per_unit = menu[j]
                    break
            print(f"Ordered - {x}, quantity - {quantity}, price (per Unit) - {price_per_unit}. ")
            print(f"Total price - {quantity * price_per_unit}")  # just showing per order price
            self.total += quantity * price_per_unit  # adding prices to total cost

    def pay_tips(self, tip=0):
        if tip == 0:
            print(f"No tips to the waiter.")
        else:
            self.tips += tip
            self.total+= self.tips
            print(f"Gives {self.tips}/- tips to the waiter.")

    def show_orders(self):
        print(f"{self.name} has  {len(self.orders)} item(s) in the cart.")
        print(f"Items : {self.orders}")
        return f"Total spent: {self.total}."


menu = {'Chicken Lollipop': 15, 'Beef Nugget': 20, 'Americano': 180, 'Red Velvet': 150, 'Prawn Tempura': 80,
        'Saute Veg': 200}
f1 = Foodie('Frodo')
print(f1.show_orders())
print('1----------------------')
f1.order('Chicken Lollipop-3', 'Beef Nugget-6', 'Americano-1')
print('2----------------------')
print(f1.show_orders())
print('3----------------------')
f1.order('Red Velvet-1')
print('4----------------------')
f1.pay_tips(20)
print('5----------------------')
print(f1.show_orders())
f2 = Foodie('Bilbo')
print('6----------------------')
f2.order('Prawn Tempura-6', 'Saute Veg-1')
print('7----------------------')
f2.pay_tips()
print('8----------------------')
print(f2.show_orders())

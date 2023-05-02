class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"{self.first_name} {self.last_name} {self.email} {self.age}")

    def enroll(self):
        if self.is_rewards_member != False:
            print("FAIL")
            return False
        else:
            self.gold_card_points += 200
            self.is_rewards_member = True
            print("SUCCESS")
            return True



    def spend_points(self, amount):
        if self.gold_card_points - amount >= 0:
            self.gold_card_points = self.gold_card_points - amount
            print(self.gold_card_points)
            return True
        else:
            print("Insufficient Points.")


    
        
obi = User("Obi", "Kobi", "AniSlayer@gmail.com","38")
ani = User("Ani", "Lavasinker", "NotChosenWan@yahoo.com", "22")
yoda = User("Yoda", "Smalls", "LilGreenMartian@gmail.com", "864")


obi.display_info()

# obi.gold_card_points += 200
# obi.is_rewards_member=False
print(obi.enroll())
print(obi.gold_card_points)
print(obi.spend_points(50))

print(ani.enroll())
print(ani.spend_points(80))

print(yoda.spend_points(40))

people = [obi,ani,yoda]

for person in people:
    print(person.display_info())
class User:
    def __init__(self, seats):
        self.seats = seats
        self.number = 0

    def carPrint(self, user):
        self.number += 1
        user.number = 3



user_1 = User(5)
user2 = User(4)

user_1.carPrint(user2)

print(f"new user being created...{user2.number}")
print(f"new user being created...{user_1.number}")


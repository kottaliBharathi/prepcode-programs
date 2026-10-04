amount=float(input("order amount:"))
premium=input("premium member?")
if amount>=1000 or premium=="yes":
    print("free delivery")
else:
    print("delivery charge applies")
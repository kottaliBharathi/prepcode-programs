price=1000
quanitity=2
member= True
coupon= True
total=price*quanitity
if member:
    total-=total*10/100
if coupon:
    total-=total*5/100
print("final amount:",total)
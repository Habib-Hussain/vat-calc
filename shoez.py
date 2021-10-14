from threading import Event
print("CToS loading")
for index in range(3):
    Event().wait(0.4)
    print(".")

country=input("what country shall you seek to calculate VAT from ")

if country == 'france':
    cashmoney=int(input("shoe price (e.g 46.69) "))
    price= cashmoney*1.20
    exvat= cashmoney*0.20
    price=str(price)
    exvat=str(exvat)
    print("Price with vat is £"+price+", amount of vat added is £"+exvat+)
else country == 'portugal':
    cashmoney=int(input("shoe price (e.g 46.69) "))
    price= cashmoney*1.23
    exvat= cashmoney*0.23
    price=str(price)
    exvat=str(exvat)
    print("Price with vat is £"+price+", amount of vat added is £"+exvat+)
elif country == 'germany':
    cashmoney=int(input("shoe price (e.g 46.69) "))
    price= cashmoney*1.19
    exvat= cashmoney*0.19
    price=str(price)
    exvat=str(exvat)
    print("Price with vat is £"+price+", amount of vat added is £"+exvat+)
elif country == 'spain':
    cashmoney=int(input("shoe price (e.g 46.69) "))
    price= cashmoney*1.21
    exvat= cashmoney*0.21
    price=str(price)
    exvat=str(exvat)
    print("Price with vat is £"+price+", amount of vat added is £"+exvat+)
elif country == 'italy':
    print("italy working")



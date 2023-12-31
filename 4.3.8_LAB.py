# 1 American mile = 1609.344 metres
# 1 American gallon = 3.785411784 litres

def liters_100km_to_miles_gallon(liters):
    gallon = liters / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallon

def miles_gallon_to_liters_100km(miles):
    km100 = miles * 1609.344 / 1000 / 100
    liters = 3.785411784
    return liters / km100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

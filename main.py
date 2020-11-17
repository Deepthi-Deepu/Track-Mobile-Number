import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
number = int(input())
num = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(num,"en"))
print(geocoder.description_for_number(num,"en"))
print("###################")


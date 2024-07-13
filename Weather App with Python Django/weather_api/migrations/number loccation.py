import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+919701864077")
phone_number2 = phonenumbers.parse("+919652044832")
phone_number3 = phonenumbers.parse("+917702703521")
phone_number4 = phonenumbers.parse("+917995840311")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1"en")
print(geocoder.description_for_number(phone_number2,"en"
print(geocoder.description_for_number(phone_number3,"en"
print(geocoder.description_for_number(phone_number4,"en"                                    

#lets track your phone numbers
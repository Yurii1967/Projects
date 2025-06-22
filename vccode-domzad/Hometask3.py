#програма приводить номер телефону до вигляду +380681208899


phone_numbers =[ "068tel1208558", "38(068)1208558", "+36(095)2223311", '0681208558']
import re
def normalized_phone_number (number):

    start_number = re.sub ("[^0-9]", "", number)
    normalized_number = "+" + start_number if len(start_number) == 12 else "+38" + start_number

    return normalized_number

for number in phone_numbers:
    
    print (normalized_phone_number(number))
    
    






    


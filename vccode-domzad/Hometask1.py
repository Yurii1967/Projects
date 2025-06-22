from datetime import datetime
# Вводимо з терміналу бажану дату
# Запобігаємо введення замість цифр у році літер
# Розраховуємо різницю між поточною та введеною датою

try: 
    my_year = int(input("Year 4 arabic digits: "))


    print (my_year)
except ValueError:
        print("that was no digits, try again") 
        my_year = int(input("Second attempt: year 4 arabic digits: "))

my_mohth = int (input("month from 1 to 12 "))
my_day = int (input ("day from 1 to 31 "))
my_date = datetime(my_year, my_mohth, my_day).date()
print (my_date)


def get_days_from_today (my_date):
     
 current_day = datetime.now().date()
 print (current_day)
 days_from_today = my_date - current_day
 return days_from_today
 
 
gap_days = get_days_from_today(my_date).days
print(f"Till Your date { gap_days} days")

# Привитання з днем народження

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.06.21"}, {"name": "Ivan Rebro", "birthday": "1967.06.22"}
]
def get_upcoming_birthday (user):

   from datetime import datetime, timedelta



   current_date = datetime.today().date()
#    print (current_date)
   
# шукаємо дні народження найближчим тижнем

   congr_interval = timedelta(days = 6)
# якщо день народження припадає на неділю - переносимо вітання на насиупний день
# якщо на суботу - на два дні вперед

   sun_shift = timedelta(days=1)
   std_shift = timedelta(days=2)
   congr_date = 0
   congr_finish = current_date + congr_interval
#    print (congr_finish)


   user_birthday = datetime.strptime( user ["birthday"], "%Y.%m.%d").date()
#    print(user_birthday ) 
   upcoming_birtday = datetime ( current_date.year, user_birthday.month, user_birthday.day).date()
#    print(upcoming_birtday)
   if  current_date <= upcoming_birtday <= congr_finish :
       if upcoming_birtday.weekday() == 6 :
           congr_date = upcoming_birtday + sun_shift
       elif upcoming_birtday.weekday() == 5 :
           congr_date = upcoming_birtday + std_shift
       else:
           congr_date = upcoming_birtday
           
   else :
       pass
   if congr_date == 0:
      user ["congratulation date"] = 'not yet'
   else:
      user["congratulation date"] = congr_date.strftime("%Y.%m.%d")
   return user
for user in users :
  get_upcoming_birthday(user)


print(users)
                 
       
    
   
   
       




    
import re
import pyperclip


#TOdo: Get text from clipboard
counter = 0
text = str(pyperclip.paste()) 
mathces = []
rejected = []
checks = True
days = ""
month = ""
year = ""

#todo: set date format to search for and numbers to look for  dd/mm/yyyy
dateRegex = re.compile(r'''\d{1,2}\/\d{1,2}\/\d{2,4}''')#This just looks for the patern
#you will have to check it to make sure it is right 

#todo:comfirm that the date is valid
dayscheck = int(days)
mothcheck = int(month)
yearcheck = int(year)
leapyear = yearcheck % 4

def ValidDate(days,month,year):
  days = dayscheck
  month = mothcheck
  year = yearcheck
  if days <= 31 and month <=12 and year <= 2999:
    return True
  else:
    return False


def ValidMonthdayCheck(month,date):
    month = mothcheck
    date = dayscheck

    if  month == 6 or month == 9 or month == 10:
         if date <= 30:
              return True
    if  month != 6 or month != 9 or month != 10:
         if date <= 31:
              return True
              
         
def Leapcheck (leap,days,month):
    days = dayscheck
    month = mothcheck
    leap = leapyear
    if month == 4:
         
        if leap == 0:
             if days <= 29:
                  return True
             elif days > 29:
                  return False
        else:
         if leap != 0:
              if days <=28:
                   return True
              else:
                   return False
    

for dates in dateRegex.findall(text):
    for i in dates:
        #counter to track where you are in string it is +1 indexed 
        counter+=1
        if counter <= 2 and counter != 3:
            days += i
        if counter == 4 or counter == 5:
            month += i
        elif counter > 6:
            year += i
    if counter > 10:
        ValidDate(dayscheck,mothcheck,yearcheck)
        ValidMonthdayCheck(mothcheck,dayscheck)
        Leapcheck(leapyear,dayscheck,mothcheck)

    
         

if ValidDate == True:
    if ValidMonthdayCheck == True:
         if Leapcheck == True:
              counter = 0
              mathces.append(dates)
              dayscheck = ""
              mothcheck = ""
              yearcheck = ""
else:
    ValidDate = False
    ValidMonthdayCheck = False
    Leapcheck = False
    rejected.append(dates)
    counter = 0
    dayscheck = ''
    mothcheck = ''
    yearcheck = ''
#left off here last night might need tweaked tomorrow while testing 


'''

    while checks == True:
        if dayscheck <= 31 and mothcheck <= 12 and yearcheck <= 2999:
             checks = True
        if mothcheck == 4 or mothcheck == 6 or mothcheck == 9 or mothcheck == 10 and dayscheck >= 30:
                        checks = True
        elif mothcheck == 4 or mothcheck == 6 or mothcheck == 9 or mothcheck == 10 and dayscheck <= 31:
                        rejected.append(dates)
                        counter = 0
                        checks = False
                        days = ""
                        month = ""
                        year = ""


        else:
                mathces.append(dates)
                checks = False
                counter = 0
                days = ""
                month = ""
                year = ""


  '''      

#todo:Display the matches in a good fashion and copy to clipboard 
for i in mathces:
    print(f'{i}')
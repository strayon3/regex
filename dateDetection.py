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
    if counter > 9:
        checks = True

#todo:comfirm that the date is valid
    dayscheck = int(days)
    mothcheck = int(month)
    yearcheck = int(year)
    leapyear = yearcheck % 4

    while checks == True:
        if dayscheck <= 31 and mothcheck <= 12 and yearcheck <= 2999:
             checks = True
        if dayscheck > 31 or mothcheck > 12 or yearcheck > 2999:
              rejected.append(dates)
              counter = 0
              days= ''
              month = ''
              year = ''                                 #logic for dates that dont meet the rage 
              checks = False
              break
        if  mothcheck == 6 or mothcheck == 9 or mothcheck == 10 and dayscheck <= 30: #months with 30 days check 
                        checks = True
        elif  mothcheck == 6 or mothcheck == 9 or mothcheck == 10 and dayscheck <= 31: #if over 30 rejcts it not valid 
                        rejected.append(dates)
                        counter = 0
                        checks = False
                        days = ""
                        month = ""
                        year = ""
                        break

        if leapyear == 0 and mothcheck == 2: #checks leap year 
              if dayscheck <= 29:
                mathces.append(dates)
                checks = False
                counter = 0
                days = ""
                month = ""
                year = ""
                break
        elif leapyear != 0 and mothcheck == 2:
              if dayscheck <= 28:
                    mathces.append(dates)
                    checks = False
                    counter = 0
                    days = ''
                    month = ''
                    year = ''
                    break
        elif mothcheck == 2 and dayscheck > 29:
              rejected.append(dates)
              checks = False
              counter = 0
              days = ''
              month = ''
              year = ''
              break
        else:
              mathces.append(dates)
              counter = 0
              days = ''
              month = ''
              year = ''
              checks = False

        

#todo:Display the matches in a good fashion and copy to clipboard 
for i in mathces:
    print(f'* {i}')
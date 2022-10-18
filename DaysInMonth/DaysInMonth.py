def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return "True"
      else:
        return "False"
    else:
      return "True"
  else:
    return "False"

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(year) == "False":
    if month == 1:
      return(month_days[0])
    elif month == 2:
      return(month_days[1]) 
    elif month == 3:
      return(month_days[2])  
    elif month == 4:
      return(month_days[3])  
    elif month == 5:
      return(month_days[4])  
    elif month == 6:
      return(month_days[5])  
    elif month == 7:
      return(month_days[6])  
    elif month == 8:
      return(month_days[7])  
    elif month == 9:
      return(month_days[8]) 
    elif month == 10:
      return(month_days[9]) 
    elif month == 11:
      return(month_days[10]) 
    elif month == 12:
      return(month_days[11])      
  else:
    if month == 1:
      return(month_days[0])
    elif month == 2:
      return("29") 
    elif month == 3:
      return(month_days[2])  
    elif month == 4:
      return(month_days[3])  
    elif month == 5:
      return(month_days[4])  
    elif month == 6:
      return(month_days[5])  
    elif month == 7:
      return(month_days[6])  
    elif month == 8:
      return(month_days[7])  
    elif month == 9:
      return(month_days[8]) 
    elif month == 10:
      return(month_days[9]) 
    elif month == 11:
      return(month_days[10]) 
    elif month == 12:
      return(month_days[11])  
      
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
# Programmer: 
# Description: 

def convert_grade (grade):
    if grade < 0 or grade > 100:
            return("Invalid percent!")
    elif grade >=80:
            return "A"
    elif grade >=70:
            return "B"
    elif grade >=60:
            return "C"
    elif grade >=50:
            return "D"
    elif 0 <= grade <= 50:
            return "F"
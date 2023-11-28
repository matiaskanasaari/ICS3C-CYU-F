# Programmer: 
# Description: 

def convert_grade (
if grade < 0 or grade > 100:
            return("Invalid percent!")
elif grade >=80:
            return(f"{grade}% is a Level A.")
elif grade >=70:
            return(f"{grade}% is a Level B.")
elif grade >=60:
            return(f"{grade}% is a Level C.")
elif grade >=50:
            return(f"{grade}% is a Level D.")
elif 0 <= grade <= 50:
            return(f"{grade}% is an F. ")
from datetime import date #importing date 

pupilName = input("ENTER FULL NAME: ") #asks for pupil name

validForms = ["1C","1F","1H","1M","1O","1S","2C","2F","2H","2M","2O","2S","3C","3F","3H","3M","3O","3S"]

validInterest = ["python","scratch"]                                                                    # setting up valid inputs

validSkill = ["pioneer", "explorer", "scout", "expert"]

form = ""
while form not in validForms:
  form = input("ENTER FORM: ").upper() # adding the value to form in the uppercase format only if the value is valid else it asks again

interest = ""
while interest not in validInterest:
  interest = input("PYTHON OR SCRATCH: ").lower()#  adding the value to intrest in the case format only if the value is valid else it asks again

skill = ""
while skill not in validSkill:
  skill = input("ENTER SKILL LEVEL: PIONEER , EXPLORER , SCOUT , EXPERT: ").lower() #  adding the value to skill in the lowercase format only if the value is valid else it asks again

today = date.today() 
attendanceDate = today.strftime("%d/%m/%Y") # gets todays date in dd/mm/yy

pupilNames = open("Register.txt","a") # opens register.txt in append mode
info = f"{pupilName} in {form} likes {interest} and they are a {skill}. Date: {attendanceDate}\n" '# adds all relevant info to register.txt
pupilNames.write(info)
pupilNames.close() #closes register.txt

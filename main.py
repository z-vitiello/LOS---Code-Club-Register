from datetime import date

pupilname = input("ENTER FULL NAME: ")

validforms = ["1C","1F","1H","1M","1O","1S","2C","2F","2H",
"2M","2O","2S","3C","3F","3H","3M","3O","3S"]

validinterest = ["python","scratch"]

validskill = ["pioneer", "explorer", "scout", "expert"]

form = ""
while form not in validforms:
  form = input("ENTER FORM: ").upper()

interest = ""
while interest not in validinterest:
  interest = input("PYTHON OR SCRATCH: ").lower()

skill = ""
while skill not in validskill:
  skill = input("ENTER SKILL LEVEL: PIONEER , EXPLORER , SCOUT , EXPERT: ").lower()
today = date.today()
attendancedate = today.strftime("%d/%m/%Y")

pupilnames = open("Register.txt","a")
info = f"{pupilname} in {form} likes {interest} and they are a {skill}. Date:{attendancedate}\n"
pupilnames.write(info)
pupilnames.close()
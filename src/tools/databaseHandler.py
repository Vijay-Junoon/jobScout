import psycopg2
import re

conn = psycopg2.connect("dbname=JobScout user=postgres password=Lucifer545@")
cursor = conn.cursor()
print("Connection established!")


class Validator:

  def __init__(self):
    pass

  def validateName(self,name):
    if name is None:
      return False,"Name cannot be empty!"
    
    for i in name:
      if not i.isalpha():
        return False,"Name can only have alphabets"
      
    name = name.capitalize()
    return True,name

  def validateEmail(self,email):

    if email is None:
      return False, "Email cannot be empty"

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if re.match(pattern, email):
        return True, email

    return False, "Invalid email format"

  def validatePwd(self,password):
    if password is None:
      return False, "Password cannot be empty!"
    
    l,u,d,s = len(password),0,0,0
    for i in password:
      if i.isupper():u+=1
      elif i.isdigit():d+=1
      elif i != " " and not i.isalpha():s+=1

    if l < 7 or u == 0 or d == 0 or s == 0:
      return False, 'Password should have one of each: 1)Length greater than 7 2)Atleast one upper case letter 3)Atleast one digit 4)Atleast one special character'
    return True,password 

  def validateRole(self,jobRole):
    if jobRole is None:
      return False, "Job Role cannot be empty"

    return True, jobRole

  def validateExperience(self,exp):
    if exp is None:
      return False,"Experience cannot be empty"
  
    if type(exp) == str:
      return False,"Experience can only have numeric values"

    return True,exp

  def validateLocation(self,location):
    if location is None:
      return False,"Location cannot be empty"
    
    for i in location:
      if not i.isalpha():
        return False, "Location can only have alphabets"
      
    return True,location

  def validateSalary(self,salary):
    if salary is None:
      return False,"Salary cannot be empty"

    if type(salary) != float:
      return False,"Salary can only contain numerical values"
    
    return True,salary

def create_table():

  query = "CREATE TABLE IF NOT EXISTS USER_DETAILS(userId SERIAL PRIMARY KEY , name varchar(50), email varchar(30) UNIQUE, pwd varchar(20), jobRole varchar(25),experience INTEGER, location varchar(30),salary numeric(12,2))"
  cursor.execute(query)
  conn.commit()

def put(name,email,pwd,jobRole,experience,location,salary):
  
  validator = Validator()
  status = False

  status,name = validator.validateName(name)
  if not status:
    return name
  status,msg = validator.validateEmail(email)
  if not status:
    return msg
  status,msg = validator.validatePwd(pwd)
  if not status:
    return msg
  status,msg = validator.validateRole(jobRole)
  if not status:
    return msg
  status,msg = validator.validateExperience(experience)
  if not status:
    return msg
  status,msg = validator.validateLocation(location)
  if not status:
    return msg
  status,msg = validator.validateSalary(salary)
  if not status:
      return msg

  query = "SELECT * from USER_DETAILS WHERE email = %s"
  cursor.execute(query,(email,))
  data = cursor.fetchall()
  if data != []:
    return "User with the same email exists."
  query = "INSERT INTO USER_DETAILS(name,email,pwd,jobRole,experience,location,salary)VALUES(%s,%s,%s,%s,%s,%s,%s)"
  cursor.execute(query,(name,email,pwd,jobRole,experience,location,salary))
  conn.commit()
  return "Done"

def fetch():
  pass

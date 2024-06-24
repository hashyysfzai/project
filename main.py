name = str(input('Name: '))
print('Name: ' + name)

age = int(input('Age: '))
print('Age: ', age)


gender = str(input('Gender: '))
print('Gender: ' , gender)

if gender != "male" and gender != "female":
  print('invalid response')
 # gender = str(input('Gender: '))
def bronchitis() :
  sore = str(input("do you have a sore throat? (yes/no)"))
  fever = str(input('do you have a fever?(yes/no)'))
  painWhenCough = str(input('do you have chest pain when coughing?(yes/no)'))
  if sore = 'yes' and fever = 'yes' and painWhenCough = 'yes':
    print('you have bronchitis... this often gets better within 3 weeks')
  

def cough_type() :
  coughType = input('is your cough: A: chesty B: mucus or C: dry')
  if coughType != "A" and coughType != "B" and coughType != "C":
    print('invalid')

print(f'Hi {name}, we will now ask you some questions')

cough = str(input('Do you have a cough? (yes/no)'))
if cough == "yes":
  cough_type()
else:
  pass
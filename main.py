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
  if sore == 'yes' and fever == 'yes' and painWhenCough == 'yes':
    print('you have bronchitis... this often gets better within 3 weeks.')
  else:
      pass
  treatB = str(input('would you like to know what to do next? (yes/no)'))
  if treatB == 'yes':
    print('-Take plenty of rest')
    print('-Drink lots of fluids')
    print('-Take painkillers')
    print('-Wash hands regularly')
    print('-Cover your mouth and nose with a tissue when you cough or sneeze')
  else:
    pass

def cough_type() :
  coughType = input('is your cough: A: chesty B: mucus or C: dry')
  if coughType != "A" and coughType != "B" and coughType != "C":
    print('invalid')
  if coughType == "B":
    bronchitis()
  else:
    pass

print(f'Hi {name}, we will now ask you some questions')

cough = str(input('Do you have a cough? (yes/no)'))
if cough == "yes":
  cough_type()
else:
  pass

pain = str()
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

pain = str(input('Do you have any pain?(yes/no)'))
if pain == 'yes':
  where = input('where do you feel this pain?(head/back/stomach')
  if where == 'head':
      print('you have a headache.')
      treatPH = str(input('would you like to know what to do next? (yes/no)'))
      if treatPH == 'yes':
        print('-Drink fluids')
        print('-Have plenty of rest')
        print('-Take painkillers')
  elif where == 'back':
    print('You have back pain due to your posture')
    treatPB = str(input('would you like to know what to do next? (yes/no)'))
    if treatPB == 'yes':
      print('-Improve your posture when carrying out daily activities')
  elif where == 'stomach':
    stomachType = input('Is it an A: acidic pain or B: aching pain ')
    if stomachType == "A":
      print("You have indigestion")
      treatSI = input("Whould you like to know what to do next?(yes/no)")
      if treatSI == 'yes':
        print('-cut down on tea, coffee, cola or alcohol')
        print('-raise your head and shoulders up when in bed – this can stop stomach acid coming up while you sleep')
        print("-lose weight if you're overweight")
    if  stomachType == 'B':
        print('you have a stomach ache')
        treatSA = input('Would you like to know what to do next?(yes/no)')
        if treatSA == 'yes':
          print('See a GP if:')
          print('-a stomach ache gets much worse quickly')
          print("-you're losing weight without trying to")
          print('-you have diarrhoea that does not go away after a few days')
          print('-peeing is suddenly painful')
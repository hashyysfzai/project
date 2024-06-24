name = str(input('Name: '))
print('Name: ' + name)

age = int(input('Age: '))
print('Age: ', age)


gender = str(input('Gender: '))
print('Gender: ' , gender)

#if gender != "male" and gender != "female":
 # gender = str(input('Gender: '))

print(f'Hi {name}, we will now ask you some questions')

cough = bool(input('Do you have a cough?'))
if cough:
  coughType = str('Is it a mucus, dry or chesty cough?')

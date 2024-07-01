#introduction
print(
    'Hi, this is a survey which asseses your physical and mental state of wellbeing. You will be given advice based on your physical and mental state of wellbeing.'
)
print(
    'ONE RULE: Please answer these questions truthfully and sincerely  for your own wellbeing'
)

#credentials
print('Enter your credentials below:')
name = str(input('Name:'))
age = int(input('Age:'))
gender = str(input('Gender:'))

if gender != 'male' and gender != 'female':
  print('Invalid response')
  gender = str(input('Gender:'))
#make it redo the question
else:
  pass

#questions
energy = int(
    input('On a scale from 1-10 how energetic are you feeling right now?'))
fitness = int(input('On a scale from 1-10 how fit are you right now?'))
depressed = int(
    input('On a scale from 1-10 how depressed are you feeling right now?'))
sleep = int(input('On a scale from 1-10 how is your sleep right now?'))
water = int(input('How many glasses of water do you drink a day?'))
diet = input('What is a rough percentage of your diet that is junk food')
feel = int(input('On a scale from 1-10 how would YOU rate your lifestyle'))

print('hmm interesting...')

print('What is YOUR biggest concern?')
print('A: Sleep Quality')
print('B: Feeling Energised')
print('C: Getting Stronger')
print('D: Losing Weight')
concern = str(input('Enter:'))

#if concern == .... AND diet = ..... print......

#if statements to be done
#errors

if gender != 'male' and gender != 'female':
  print('Invalid response')
  gender = str(input('Gender:'))
#make it redo the question
else:
  pass

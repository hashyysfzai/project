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
diet = int(input('What is a rough percentage of your diet that is junk food'))
feel = int(input('On a scale from 1-10 how would YOU rate your lifestyle'))

print('hmm interesting...')

print('What is YOUR biggest concern?')
print('A: Sleep Quality')
print('B: Feeling Energised')
print('C: Getting Stronger')
print('D: Losing Weight')
concern = str(input('Enter:'))

if concern == 'A' and depressed > 3:
    print('The reason for yur depression may be due to your lack of sleep')
    print('-DO NOT: eat 3 hours before bed; drink 2 hours before bed; use devices 1 hour before bed')
    print('if these do not work then feel free to contact us')

if concern == 'A' and sleep > 7:
    print('There doesnt seem to be an issue with your sleep, however if you would still like help the contact us')

if concern == 'A' and energy > 7:
    print('If you drink too much caffiene then cut down on it')

if concern == 'B' and concern == 'D' and diet > 30:
    print('Cut down on junk food as this will cause energy crashes during the day and unhealthy weight gain')
    
if concern == 'B' and concern == 'D' and diet < 30:
    print('It seems that your diet is alright, however if you would still like help the contact us')

if concern == 'C' and fitness < 5:
    print('It is good that you have a good diet, however it seems that you may need to improve your fitness as well')

if concern == 'C' and fitness > 5:
    print('It seems that you are doing well in terms of fitness, however if you would still like help the contact us')

if concern == 'B' and energy < 5:
    print('It seems that you are lacking in energy, try getting some more exercise')
if concern == 'B' and energy > 5:
    print('It seems that you have good energy levels, however if you would still like help the contact us')

if concern == 'D' and diet > 30:
    print('You should cut down on junk food as this will cause unhealthy weight gain')
if concern == 'D' and diet < 30:
    print('It seems that you are doing well in terms of diet, however if you would still like help the contact us')
    
#if concern == .... AND diet = ..... print......

#if statements to be done
#errors

if concern == 'A' and diet > 30:
    print('You should cut down on junk food as this can affect sleep quality and lead to unhealthy weight gain.')
if concern == 'A' and diet < 30:
    print('It seems that you are doing well in terms of diet, however if you would still like help the contact us')

if concern == 'B' and diet > 30:
    print('You should cut down on junk food as this can cause energy crashes during the day and unhealthy weight gain.')
if concern == 'B' and diet < 30:
    print('It seems that you are doing well in terms of diet, however if you would still like help the contact us')

if concern == 'C' and diet > 30:
    print('You should cut down on junk food as it can hinder your progress in gaining muscle and strength.')
if concern == 'C' and diet < 30:
    print('It seems that you are doing well in terms of diet, however if you would still like help the contact us')

if concern == 'D' and diet > 30:
    print('You should cut down on junk food as this will cause unhealthy weight gain.')
if concern == 'D' and diet < 30:
    print('It seems that you are doing well in terms of diet, however if you would still like help the contact us')
if concern == 'A' and water < 8:
    print('You should drink more water as this can affect sleep quality.')
if concern == 'A' and water > 8:
    print('It seems that you are doing well in terms of water intake, however if you would still like help the contact us')

if concern == 'B' and water < 8:
    print('You should drink more water as this can cause energy crashes during the day.')
if concern == 'B' and water > 8:
    print('It seems that you are doing well in terms of water intake, however if you would still like help the contact us')

if concern == 'C' and water < 8:
    print('You should drink more water as it can hinder your progress in gaining muscle and strength.')
if concern == 'C' and water > 8:
    print('It seems that you are doing well in terms of water intake, however if you would still like help the contact us')

if concern == 'D' and water < 8:
    print('You should drink more water as this can cause unhealthy weight gain.')
if concern == 'D' and water > 8:
    print('It seems that you are doing well in terms of water intake, however if you would still like help the contact us')

if concern == 'A' and fitness < 5:
    print('You should improve your fitness as this can affect sleep quality.')
if concern == 'A' and fitness > 5:
    print('It seems that you are doing well in terms of fitness, however if you would still like help the contact us')

if concern == 'B' and fitness < 5:
    print('You should improve your fitness as this can cause energy crashes during the day.')
if concern == 'B' and fitness > 5:
    print('It seems that you are doing well in terms of fitness, however if you would still like help the contact us')

if concern == 'C' and fitness < 5:
    print('You should improve your fitness as this can hinder your progress in gaining muscle and strength.')
if concern == 'C' and fitness > 5:
    print('It seems that you are doing well in terms of fitness, however if you would still like help the contact us')

if concern == 'D' and fitness < 5:
    print('You should improve your fitness as this can cause unhealthy weight gain.')
if concern == 'D' and fitness > 5:
    print('It seems that you are doing well in terms of fitness, however if you would still like help the contact us')
    
if concern == 'A' and feel < 5:
    print('You should focus on improving your lifestyle as this can affect sleep quality.')
if concern == 'A' and feel > 5:
    print('It seems that you are doing well in terms of lifestyle, however if you would still like help the contact us')

if concern == 'B' and feel < 5:
    print('You should focus on improving your lifestyle as this can cause energy crashes during the day.')
if concern == 'B' and feel > 5:
    print('It seems that you are doing well in terms of lifestyle, however if you would still like help the contact us')

if concern == 'C' and feel < 5:
    print('You should focus on improving your lifestyle as this can hinder your progress in gaining muscle and strength.')
if concern == 'C' and feel > 5:
    print('It seems that you are doing well in terms of lifestyle, however if you would still like help the contact us')

if concern == 'D' and feel < 5:
    print('You should focus on improving your lifestyle as this can cause unhealthy weight gain.')
    
if concern == 'D' and feel > 5:
    print('It seems that you are doing well in terms of lifestyle, however if you would still like help the contact us')

print('Do you have any other concerns?')
print('A: Yes')
print('B: No')
other_concerns = str(input('Enter:'))

if other_concerns == 'A':
    print('What is your concern?')
    print('A: Stress')
    print('B: Anxiety')
    print('C: Motivation')
    print('D: Sleep')
    print('E: Energy')
    print('F: Fitness')
    print('G: Weight')
    print('H: Diet')
    print('I: Water')
    print('J: Lifestyle')
    print('K: Other')
    other_concern = str(input('Enter:'))
    if other_concern == 'A':
        print('Take some deep breaths and focus on your breathing for 5 minutes')
    if other_concern == 'B':
        print('Engage in physical activity to reduce your stress levels and anxiety')
    if other_concern == 'C':
        print('Set achievable goals and celebrate your small victories')
    if other_concern == 'D':
        print('Try using a sleep tracker to monitor your sleep patterns')
    if other_concern == 'E':
        print('Eat a balanced diet and get regular exercise')
    if other_concern == 'F':
        print('Start with small steps and gradually increase the intensity of your workouts')
    if other_concern == 'G':
        print('Focus on healthy eating habits and regular exercise')
    if other_concern == 'H':
        print('Make sure to include plenty of fruits, vegetables, and whole grains in your diet')
    if other_concern == 'I':
        print('Drink plenty of water throughout the day')
    if other_concern == 'J':
        print('Make sure to prioritize your physical and mental health')
    if other_concern == 'K':
        print('Please contact us for more information')
if other_concerns == 'B':
    print('That is great to hear')

if concern == 'C' and diet > 30:
    print('You should cut down on junk food as this can affect your fitness goals.')
if concern == 'C' and diet < 30:
    print('It seems that you are doing well in terms of diet, however if you would still like help the contact us')

if concern == 'D' and water < 8:
    print('You should drink at least 8 glasses of water a day to help with weight loss.')
if concern == 'D' and water > 8:
    print('It seems that you are doing well in terms of water intake, however if you would still like help the contact us')

print('Thank you for taking the time to complete this survey')
print('We hope you found it helpful')
print('Please remember to take care of your physical and mental health')
print('If you have any further questions, please contact us')

feedback = input("Please provide any feedback you may have:")
if feedback:
    print("Thank you for your feedback!")
    print("We will use it to improve our survey.")
else:
    print("No feedback provided.")

#if concern == .... AND diet = ..... print......

#if statements to be done
#errors


if gender != 'male' and gender != 'female':
  print('Invalid response')
  gender = str(input('Gender:'))
#make it redo the question
else:
  pass

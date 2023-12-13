while True:
    try:
        h_cm = int(input('Enter height (in cm): '))
        wt = int(input('Enter weight (in Kg): '))
        if wt > 1000 and h_cm > 300:
            print("Error: The height amd weight seems unusually large. Please check your input.")
        elif wt > 1000:
            print("Error: The weight seems unusually large. Please check your input.")
        elif h_cm > 300:
        	print("Error: The height seems unusually large. Please check your input")
        elif wt > 0 and h_cm > 0:
         	break
        else:
            print('Error: Weight and height cannot be negative. Please check your input.')
    except ValueError:
        print('Error: Please enter valid integers for weight and height.')
        
h_m = h_cm / 100
bmi = round(wt /h_m**2,1)
sug_min = round(18.5*h_m**2,1)
sug_max= round(25*h_m**2,1)
print('Your current BMI is', bmi)

if bmi < 18.5:
    print("You are Underweight.")
elif 18.5 <= bmi < 25:
    print("You are Normal.")
elif 25 <= bmi < 30:
    print("You are Overweight.")
else:
    print("You are Obese.")
print('Analysis:')
print('Your Height: ',h_cm,'cm')
print('Suggested Weight is:',sug_min,'~',sug_max,'kg')
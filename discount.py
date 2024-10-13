# Store discount program
# We have 3 categories of discount
# Senior citizens 12% discount; aged above 70 years
# Students 10% discount
# Kids under 7 years 12% discount

age = int(input('How old are you? '))
is_student = input("Are you a student? 'yes' or 'no' ")

if age > 70 or age < 7:
    print('12% discount')
elif is_student in ('Yes','yes','Y','y'):
    print('10% discount')
else:
    print('Discount not available')
print('Proceed to payment')
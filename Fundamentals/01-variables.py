# Variables

firstname = 'Sebastian' #Valid variable name.
last_name = 'Fuentes'   #Valid variable name with snake case, best practice.
MyTest = 'Testing'      #Valid variable name, but this is a bad practice.

print(firstname)
print(last_name)

int_age = 16
age_to_str = str(int_age)
bool_variable = True    # Or False

#Variable Concat with print 
print(firstname, last_name, ",I'm", int_age, 'Years.')
print(type(age_to_str), age_to_str)
print(float(int_age))

#Some system methods
print(len(firstname))

#Inline variables
name, surname, alias, age = 'Sebastian', 'Fuentes', 'SEB DEV', 27

# Don't abuse this syntax
print("I'm", name, surname, "I'm", age, "years", 'and my alias is:', alias)

#Using input to prompt the user for values via console
# full_name = input('What is your name?: ')
# input_age = input ('How old are you?: ')

# print(full_name, input_age)
# print(full_name+input_age)

address: str = 'My Address'
print(address, type(address))

address = 11

print(address, type(address))
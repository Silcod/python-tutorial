#Functions are containers for few lines of codes that perform a specific task
#So while building complex programs we should break up our code into smaller reusable chunks which we call functions
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
greet_user(first_name="Ibrahim", last_name="Sanusi")
greet_user("Mubarak", "Sanusi ")
print("Finish")

#Parameters: Passing information to your functions using parameters
#positional Argumennts: calc_cost(50,29)
#Keyword Arguments: the combination of having a parameter name followed by its value is called a keyword argument
#Keyword Arguments: calc_cost(total=50, shipping=29)
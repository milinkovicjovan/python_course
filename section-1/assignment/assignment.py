# 1 Task

# my_name = 'Jovan'
# my_age = 20
my_name = input('Enter your name: ')
my_age = input('Enter your age: ')

# 2 Task


def print_my_data():
    print(my_name + ' - ' + my_age)


print_my_data()

# 3 Task


def print_concatenated_data(el1, el2):
    print(el1 + ' - ' + el2)


print_concatenated_data(my_name, my_age)

# 4 Task


def calculate_decades(age):
    decades_lived = age // 10
    return decades_lived


decades = calculate_decades(int(my_age))
print(decades)

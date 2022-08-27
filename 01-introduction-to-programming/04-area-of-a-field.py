'''Create a program that reads the length and width of a farmer's field from the user in
feet. Display the area of the field in acres.'''

farm_width = float(input("Enter the width of the farm field in feet (ft.): "))
farm_lenght = float(
    input("Enter the lenght of the farm field in feet (ft.): "))

area_feet = farm_lenght * farm_width

area_acre = area_feet/43560

print("There are {} acres in a farmland {}ft long and {}ft wide".format(
    area_acre, farm_lenght, farm_width))

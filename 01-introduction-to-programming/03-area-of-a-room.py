"""
Write a program that asks the user to enter the width and length of a room. Once the values have been read, your program should compute and display the area of the room. The length and the width will be entered as floating point numbers. Include units in your prompt and output message; either feet or meters, depending on which unit you are more comfortable working with.
"""
width_of_room = float(input("Enter the width of the room in meters (m): "))
length_of_room = float(input("Enter the length of the room in meters (m): "))


area_of_room = length_of_room * width_of_room

print("The area of a room of length {}m and width {}m is {}m".format(
    length_of_room, width_of_room, area_of_room))

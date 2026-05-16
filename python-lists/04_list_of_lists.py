# Course: Introduction to Python
# Chapter 2: Python Lists
# Exercise: List of Lists

# -------------------------------------------------------
# Notes
# -------------------------------------------------------
# As an SOC we will be dealing with a lot of data, we need to group this data
# Instead of a list with a mix of strings and floats, that represents names and numbers you create a list of lists
# "hallway" string, hall is a variable that is set to a float 11.25
'''
Instructions
Finish the list of lists so that it also contains the bedroom and bathroom data. Make sure you enter these in order!
Print out house; does this way of structuring your data make more sense?
'''
# -------------------------------------------------------
# Solution
# -------------------------------------------------------
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
        ["bedroom", bed],
        ["bathroom", bath]]

# Print out house
print(house)

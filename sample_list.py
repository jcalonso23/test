#!/usr/bin/python3

sample_list = [1, 2, 3, 4, 5, 6]
new_sample_list = []
x = 0

# get the sum of elements
for i in sample_list:
	x = i + x

# create new sample list
for j in sample_list:
	y = j * x
	new_sample_list.append(y)

print(sample_list)
print(new_sample_list)

#!/usr/bin/python3

people = {
	"Juan" : "11/23",
	"Aldo" : "09/18",
	"Martha" : "07/29",
	"Carlos" : "10/06"
}

age = {
	"Juan" : 32,
	"Aldo" : 24,
	"Martha" : 52,
	"Carlos" : 55
}

print(people)

#people.update({"Juan" : 32})
#people.update({"Aldo" : 24})
#people.update({"Martha" : 52})
#people.update({"Carlos" : 55})

people.update(age)
print(people)

people.update({"Alida" : 45})
print(people)

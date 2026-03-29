import copy
# userDictionary = {
#     "name":"chaitanya",
#     "age": 25,
#     70: "abc",
#     "newObj":{
#         "name":"xyz"
#     }
# }
# print(userDictionary)
# print(len(userDictionary))
# userDictionary['married'] = False
# print(userDictionary)

# userDictionary.pop(70)
# print(userDictionary)

# if(userDictionary.get('value')== None):
#     userDictionary['value'] = 20

# print(userDictionary)

# for key, value in userDictionary.items():
#     print(key, value)

# #dictCopy = userDictionary.copy()
# dictCopy = copy.deepcopy(userDictionary)
# print(dictCopy)
# dictCopy['value']= 90
# print(dictCopy, userDictionary)
# dictCopy["newObj"]['name'] = 'chai'
# print(userDictionary, dictCopy)

#assignment
my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

for key, value in my_vehicle.items():
    print(key, value)

vehicle2 = copy.deepcopy(my_vehicle)
vehicle2["number_of_tiers"] = 4
vehicle2.pop("mileage")
print(vehicle2)

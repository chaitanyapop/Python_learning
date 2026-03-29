def funcAssignment(firstName, lastName, age):
    userObj = {
        "firstName":firstName,
        "lastName":lastName,
        "age":age
    }
    return userObj

value = funcAssignment("chaitanya","parandkar",26)
print(value)
print(type(value))
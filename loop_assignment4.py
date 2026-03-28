my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

i = 1
while i <= 3:
    print(my_list)
    i = i+1

for itr in my_list:
    if(itr == "Monday"):
        continue
    else:
        print(itr)
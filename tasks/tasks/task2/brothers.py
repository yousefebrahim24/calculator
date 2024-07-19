first_person = input("please enter your name :")
second_person = input("please enter your name :")
first_parent_index = first_person.index(" ")
second_parent_index= second_person.index(" ")
first_parent = first_person[first_parent_index :]
second_parent = second_person[second_parent_index :]
if first_parent == second_parent :
    print("you may be brothers :")
else :
    print("you can't be brothers :")
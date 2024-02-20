def madlibs(person, color, animal, adjective, name, place, adjective_2, verb):
    # my madlibs

    print("\n\n")
    print(f"{person} had a {color} {animal}")
    print(f"{person} had a {color} {animal}")
    print(f"It was very {adjective}")
    print(f"The {animal}'s name was {name}")
    print()
    print(f"{person} & {animal} love hanging out at {place}")
    print(f"They have a {adjective_2} when they are together")
    print(f"After their {adjective_2} time, they {verb} to slumber")



person = input("Please enter the name of a person:  ")
place = input("Please enter a place: ")
animal = input("Please enter the kind of aniaml:  ")
color = input("Please enter a color:  ")
adjective  = input("Please enter an adjective: ")
name = input("Please enter a pets name: ")
adjective_2 = input("Please enter another adjective:   ")
verb = input("Please enter a verb:  ")


madlibs(person, color, animal, adjective, name, place, adjective_2, verb)

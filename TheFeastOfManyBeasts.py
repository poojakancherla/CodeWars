notAllowed = ["-", " "]

def constraints(beast, dish):
    for i in notAllowed:
        if beast[0] == i or beast[len(beast) - 1] == i or dish[0] == i or dish[len(dish) - 1] == i:
            return False
        else:
            return True
def matching(beast, dish):
    if beast[0] == dish[0] and beast[len(beast) - 1] == dish[len(dish) - 1]:
        return True
    else:
        return False

def feast(beast, dish):
    if len(beast) >= 2 and len(dish) >= 2:
        if constraints(beast, dish) and matching(beast, dish):
            return True
        else:
            return False
    else:
        return False



print(feast("brown bear", "bear claw"))

def can_find(biograms: list, strings: list):
    for biogram in biograms:
        for string in strings:
            if biogram in string:
                break
        else:
            return False

    return True


print(can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"]))
print(can_find(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]))
print(can_find(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]))
print((can_find(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks", "cooks"])))

def fuzzy_union(set1, set2):
    result = {}
    for element, membership in set1.items():
        result[element] = max(float(membership), set2.get(element, 0))
    for element, membership in set2.items():
        if element not in result:
            result[element] = float(membership)
    return result

def fuzzy_intersection(set1, set2):
    result = {}
    for element, membership in set1.items():
        if element in set2:
            result[element] = min(float(membership), set2[element])
    return result

def fuzzy_complement(set1):
    result = {}
    for element, membership in set1.items():
        result[element] = 1.0 - float(membership)
    return result

def fuzzy_difference(set1, set2):
    result = {}
    for element, membership in set1.items():
        if element in set2:
            result[element] = max(0, float(membership) - set2[element])
        else:
            result[element] = float(membership)
    return result

def fuzzy_scaling(set1, scalar):
    result = {}
    for element, membership in set1.items():
        result[element] = float(membership) * scalar
    return result

def fuzzy_power(set1, power):
    result = {}
    for element, membership in set1.items():
        result[element] = float(membership) ** power
    return result

setA = {'a': 0.3, 'b': 0.5, 'c': 0.7}
setB = {'b': 0.6, 'c': 0.2, 'd': 0.3}
power = 2.0
scalar = 0.5
# setA = {'a': 0.2, 'b': 0.4, 'c': 0.6}
# setB = {'b': 0.5, 'c': 0.3, 'd': 0.7}
# power = 0.5
# scalar = 1.5

# Union of sets A and B
union_result = fuzzy_union(setA, setB)
print("Union:", union_result)

# Intersection of sets A and B
intersection_result = fuzzy_intersection(setA, setB)
print("Intersection:", intersection_result)

# Complement of A and B
complement_result_A = fuzzy_complement(setA)
complement_result_B = fuzzy_complement(setB)
print("Complement of A:", complement_result_A)
print("Complement of B:", complement_result_B)

# Difference of A and B
difference_result_A = fuzzy_difference(setA, setB)
difference_result_B = fuzzy_difference(setB, setA)
print("Difference of A and B:", difference_result_A)
print("Difference of B and A:", difference_result_B)

# Scaling of A and B
scaled_result_A = fuzzy_scaling(setA, scalar)
scaled_result_B = fuzzy_scaling(setB, scalar)
print(f"Scaled A by {scalar}:", scaled_result_A)
print(f"Scaled B by {scalar}:", scaled_result_B)

# Power operation on A and B
power_result_A = fuzzy_power(setA, power)
power_result_B = fuzzy_power(setB, power)
print(f"Set A raised to the power {power}:", power_result_A)
print(f"Set B raised to the power {power}:", power_result_B)

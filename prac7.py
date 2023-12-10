rules = [
    ({"temperature": "high", "humidity": "low"}, "Turn on the air conditioner"),
    ({"temperature": "low", "humidity": "high"}, "Turn on the humidifier"),
    ({"temperature": "high", "humidity": "high"}, "Turn on the fan"),
    ({"temperature": "low", "humidity": "low"}, "Do nothing"),
]

def apply_rules(state, rules):
    for condition, action in rules:
        if all(state[key] == value for key, value in condition.items()):
            return action
    return "No applicable action"

# # Test Case 1
# test_state_1 = {"temperature": "high", "humidity": "low"}
# action_1 = apply_rules(test_state_1, rules)
# print("Test 1 - Current state:", test_state_1)
# print("Action to take:", action_1)

# # Test Case 2
# test_state_2 = {"temperature": "low", "humidity": "high"}
# action_2 = apply_rules(test_state_2, rules)
# print("Test 2 - Current state:", test_state_2)
# print("Action to take:", action_2)


# # Test Case 3
# test_state_3 = {"temperature": "high", "humidity": "high"}
# action_3 = apply_rules(test_state_3, rules)
# print("Test 3 - Current state:", test_state_3)
# print("Action to take:", action_3)


# # Test Case 4
# test_state_4 = {"temperature": "low", "humidity": "low"}
# action_4 = apply_rules(test_state_4, rules)
# print("Test 4 - Current state:", test_state_4)
# print("Action to take:", action_4)


# # Test Case 5
test_state_5 = {"temperature": "medium", "humidity": "medium"}
action_5 = apply_rules(test_state_5, rules)
print("Test 5 - Current state:", test_state_5)
print("Action to take:", action_5)

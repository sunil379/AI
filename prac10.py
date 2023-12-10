import numpy as np

# Define the step function
def step(x):
    return 1 if x >= 0 else 0

# Perceptron for the AND gate
def AND_gate(x1, x2):
    weights = np.array([1, 1])
    bias = -1.5
    result = np.sum(weights * np.array([x1, x2])) + bias
    return step(result)

# Perceptron for the OR gate
def OR_gate(x1, x2):
    weights = np.array([1, 1])
    bias = -0.5
    result = np.sum(weights * np.array([x1, x2])) + bias
    return step(result)

# Perceptron for the NOT gate
def NOT_gate(x):
    weight = -1
    bias = 0.5
    result = weight * x + bias
    return step(result)

# Test the logic gates
print("AND Gate:")
print(AND_gate(0, 0))  # Should output 0
print(AND_gate(0, 1))  # Should output 0
print(AND_gate(1, 0))  # Should output 0
print(AND_gate(1, 1))  # Should output 1

print("OR Gate:")
print(OR_gate(0, 0))  # Should output 0
print(OR_gate(0, 1))  # Should output 1
print(OR_gate(1, 0))  # Should output 1
print(OR_gate(1, 1))  # Should output 1

print("NOT Gate:")
print(NOT_gate(0))  # Should output 1
print(NOT_gate(1))  # Should output 0

bayesian_network = {
    'A': {
        'prob': 0.3,
    },
    'B': {
        'prob': 0.6,  
    },
    'C': {
        'prob_given_A': {
            'True': 0.9, 
            'False': 0.2, 
        },
    },
    'D': {
        'prob_given_B': {
            'True': 0.8, 
            'False': 0.1,  
        },
    },
}


def calculate_conditional_probability(network, event):
    if 'prob' in network:
        return network['prob']
    elif 'prob_given_A' in network:
        return network['prob_given_A'][event['A']]
    elif 'prob_given_B' in network:
        return network['prob_given_B'][event['B']]

evidence = {'A': 'True', 'B': 'True', 'C': 'True', 'D': 'False'}
query_variable = 'A'

result = calculate_conditional_probability(bayesian_network[query_variable], evidence)
print(f"P({query_variable} = True | A = True, B = True, C = True, D = False) = {result:.2f}")

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


def infer_bayesian_network(bayesian_network, evidence, query_variable):
    numerator = calculate_conditional_probability(bayesian_network[query_variable], evidence)
    denominator = 0  
    
    for outcome in ['True', 'False']:
        if 'A' in bayesian_network[query_variable]:
            evidence['A'] = outcome
        if 'B' in bayesian_network[query_variable]:
            evidence['B'] = outcome
        denominator += calculate_conditional_probability(bayesian_network[query_variable], evidence)

   
    if denominator == 0:
        result = 0  
    else:
        result = numerator / denominator
    return result

evidence = {'A': 'True', 'B': 'True'} 
query_variable = 'C'
result = infer_bayesian_network(bayesian_network, evidence, query_variable)

print(f"P({query_variable} = True | A = True, B = True) = {result:.2f}")

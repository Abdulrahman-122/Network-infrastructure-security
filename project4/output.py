import json

def save_result(data, filename='result.json'):
    """Save the scan results to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# print(show_result({"mohamed":"I love him","Mahmoud":"I hate him","Nour":"fuck","Eman":"Nice","Abeer":"Beautiful"}))

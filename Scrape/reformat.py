import json

def reformat_json(input_file, output_file):
    # Read the input JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    # Write the data back in the desired format
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)

# Example usage
reformat_json('only_connect_data.json', 'output.json')

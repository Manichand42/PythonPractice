import json

def update_json_file(json_file, target_key, new_value):
    # Read JSON file
    with open(json_file, 'r') as file:
        json_data = json.load(file)
        print(json_data)

    # Update JSON value
    if target_key in json_data:
        json_data[target_key] = new_value
        print(f"Updated JSON value: {target_key} -> {new_value}")
    else:
        print(f"Key '{target_key}' not found in JSON file.")

    # Write updated JSON back to the file
    with open(json_file, 'w') as file:
        json.dump(json_data, file, indent=4)

# Example usage
json_file = 'C:\InputFiles\FscmTopModelAM.InventoryAM.InvTxnReasonPVO.json'
target_key = 'LastUpdateDate'
new_value = 'true'

update_json_file(json_file, target_key, new_value)

import pandas as pd
import json

def flatten_json(data, prefix=''):
    flattened_data = {}
    for key, value in data.items():
        if isinstance(value, dict):
            flattened_sub_data = flatten_json(value, prefix + key + '_')
            flattened_data.update(flattened_sub_data)
        else:
            flattened_data[prefix + key] = value
    return flattened_data

# Read JSON file into a pandas DataFrame
with open('C:\InputFiles\FscmTopModelAM.ContractProjectLinkAM.BillPlanPVO_10072023_011219.json') as file:
    json_data = json.load(file)

# Flatten the JSON data
flattened_data = flatten_json(json_data)

# Convert the flattened data to a DataFrame
data_frame = pd.DataFrame([flattened_data])

# Specify the file path where you want to save the Excel file
file_path = 'C:\outputFiles\data.xlsx'

# Export DataFrame to Excel
data_frame.to_excel(file_path, index=False)

print("JSON data exported to Excel successfully.")

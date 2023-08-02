import pandas as pd

def find_duplicate_records(file_path, sheet_name, columns_to_check):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # Find duplicate rows based on the specified columns
    duplicates = df[df.duplicated(subset=columns_to_check, keep=False)]

    return duplicates

if __name__ == "__main__":
    # Replace 'file_path' with the path to your Excel file
    file_path = "C:\InputFiles\elemententrypvo.xlsx"
    print('---------',file_path)
    # Replace 'sheet_name' with the name of the sheet you want to process
    sheet_name = "elemententrypvo"
    # Replace 'columns_to_check' with a list of column names to check for duplicates
    columns_to_check = ["ElementEntryId"]

    duplicate_records = find_duplicate_records(file_path, sheet_name, columns_to_check)

    if not duplicate_records.empty:
        print("Duplicate Records:")
        print(duplicate_records)
    else:
        print("No duplicate records found.")

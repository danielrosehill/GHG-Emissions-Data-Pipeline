import os
import csv
from datetime import datetime

# Define paths relative to the script's location
script_dir = os.path.dirname(os.path.abspath(__file__))  # scripts folder
repo_root = os.path.abspath(os.path.join(script_dir, '..'))  # repository root
csv_file_path = os.path.join(repo_root, 'company_data.csv')  # company_data.csv at root
output_dir = os.path.join(repo_root, 'csv-structure')  # CSV-structure folder

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Generate timestamp for the output file name
timestamp = datetime.now().strftime('%d%m%y')
output_file_path = os.path.join(output_dir, f'{timestamp}.csv')

# Copy the header row from company_data.csv to the new file
try:
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as input_file:
        reader = csv.reader(input_file)
        header = next(reader)  # Read the header row

    with open(output_file_path, mode='w', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(header)  # Write the header row to the new file

    print(f"Header row copied successfully to {output_file_path}")

except FileNotFoundError:
    print(f"Error: The file {csv_file_path} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
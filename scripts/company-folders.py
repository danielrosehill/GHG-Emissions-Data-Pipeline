import os
import csv
import json
import re

# Define paths relative to the scripts folder
scripts_folder = os.getcwd()
root_folder = os.path.abspath(os.path.join(scripts_folder, '..'))
data_sources_folder = os.path.join(root_folder, 'data_sources')
company_data_file = os.path.join(root_folder, 'company_data.csv')
memory_folder = os.path.join(root_folder, 'memory')
memory_file = os.path.join(memory_folder, 'processed_companies.json')

# Create necessary folders if they don't exist
if not os.path.exists(data_sources_folder):
    os.makedirs(data_sources_folder)
if not os.path.exists(memory_folder):
    os.makedirs(memory_folder)

# Load memory of processed companies
if os.path.exists(memory_file):
    with open(memory_file, 'r') as f:
        processed_companies = set(json.load(f))
else:
    processed_companies = set()

# Function to normalize folder names
def normalize_folder_name(name):
    # Convert to lowercase
    name = name.lower()
    # Replace spaces with hyphens
    name = name.replace(' ', '-')
    # Remove special characters (keep only alphanumeric and hyphens)
    name = re.sub(r'[^a-z0-9\-]', '', name)
    return name

# Read the CSV file
if os.path.exists(company_data_file):
    with open(company_data_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            company_name = row['company_name']
            normalized_name = normalize_folder_name(company_name)

            # Skip if company is already processed
            if normalized_name in processed_companies:
                continue

            company_folder = os.path.join(data_sources_folder, normalized_name)

            # Create company folder if it doesn't exist
            if not os.path.exists(company_folder):
                os.makedirs(company_folder)

            # Create record.md file if it doesn't exist
            record_file = os.path.join(company_folder, 'record.md')
            if not os.path.exists(record_file):
                with open(record_file, 'w') as f:
                    f.write(f"# Record for {company_name}\n")

            # Create screenshots folder if it doesn't exist
            screenshots_folder = os.path.join(company_folder, 'screenshots')
            if not os.path.exists(screenshots_folder):
                os.makedirs(screenshots_folder)

            # Mark company as processed
            processed_companies.add(normalized_name)

# Save updated memory
with open(memory_file, 'w') as f:
    json.dump(list(processed_companies), f)
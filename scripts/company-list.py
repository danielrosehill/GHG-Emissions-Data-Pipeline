import os
import pandas as pd

# Define paths
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
data_file = os.path.join(repo_root, "company_data.csv")
output_file = os.path.join(repo_root, "companies.md")
memory_folder = os.path.join(repo_root, "memory")
memory_file = os.path.join(memory_folder, "processed_companies.txt")

# Ensure memory folder exists
if not os.path.exists(memory_folder):
    os.makedirs(memory_folder)

# Load processed companies from memory
if os.path.exists(memory_file):
    with open(memory_file, 'r') as f:
        processed_companies = set(f.read().splitlines())
else:
    processed_companies = set()

# Read the data file
try:
    data = pd.read_csv(data_file)
except Exception as e:
    print(f"Error reading the CSV file: {e}")
    exit(1)

# Open the markdown file in append mode
with open(output_file, 'a') as md_file:
    for _, row in data.iterrows():
        try:
            company_name = row['company_name']

            # Skip if the company has already been processed
            if company_name in processed_companies:
                continue

            # Write header for the company
            md_file.write(f"# {company_name}\n\n")

            # Add LLM derived badge if applicable
            if row['llm_derived'] == 1:  # Ensure column name matches exactly
                md_file.write("![LLM Derived](https://img.shields.io/badge/LLM%20Derived-%E2%9C%94-green?style=flat-square)\n\n")

            # Add human verified badge based on value
            if row['human_verified'] == 0:  # Not Human Verified
                md_file.write("![Not Human Verified](https://img.shields.io/badge/Human%20Verified-%E2%9C%98-red?style=flat-square)\n\n")
            elif row['human_verified'] == 1:  # Human Verified
                md_file.write("![Human Verified](https://img.shields.io/badge/Human%20Verified-%E2%9C%94-green?style=flat-square)\n\n")

            # Mark this company as processed
            processed_companies.add(company_name)

        except KeyError as e:
            print(f"Missing expected column in data: {e}")
        except Exception as e:
            print(f"Error processing row: {e}")

# Update memory file with newly processed companies
with open(memory_file, 'w') as f:
    f.write("\n".join(processed_companies))
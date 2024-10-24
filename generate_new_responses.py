import pandas as pd
import random

# Load the existing dataset from the Excel file
input_file = 'DATASET01.xlsx'  # Ensure this file exists in the same directory
df = pd.read_excel(input_file)

# Function to generate new patterns
def generate_new_responses(existing_responses):
    new_responses = []
    for response in existing_responses:
        # Example transformation: adding variations
        new_responses.append(response)  # Original response
        new_responses.append(f"Absolutely! {response}")  # Affirmative response
        new_responses.append(f"Yes, {response}")  # Another affirmative response
        new_responses.append(f"That's correct: {response}")  # Another variation
    return new_responses

# Generate new responses for each tag
new_data = []
for index, row in df.iterrows():
    tag = row['tag']
    existing_responses = row['responses'].split(',')  # Assuming responses are comma-separated
    all_new_responses = generate_new_responses(existing_responses)
    
    # Create new entries with the same tag but new responses
    for new_response in all_new_responses:
        new_data.append({'tag': tag, 'patterns': row['patterns'], 'responses': new_response})

# Convert new data to DataFrame
new_df = pd.DataFrame(new_data)

# Append new data to existing DataFrame
updated_df = pd.concat([df, new_df], ignore_index=True)

# Save the updated DataFrame to a new Excel file
output_file = 'UPDATED_DATASET01.xlsx'  # Change this to your desired output file name
updated_df.to_excel(output_file, index=False)

print(f"Updated dataset saved as '{output_file}' with {len(new_df)} new rows.")

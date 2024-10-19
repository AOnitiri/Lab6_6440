import pandas as pd
import numpy as np


# Read the NDJSON file
df = pd.read_json('data/test-patients.ndjson', lines=True)

df['maritalStatus_display'] = df['maritalStatus'].apply(lambda x: x['coding'][0]['display'] if isinstance(x, dict) and 'coding' in x and isinstance(x['coding'], list) and len(x['coding']) > 0 else None)

# Print the DataFrame with the new 'maritalStatus_display' column
print(df[['id','maritalStatus_display']])

marital_dummies = pd.get_dummies(df['maritalStatus_display'], prefix='married')

# Ensure all expected columns are present, even if some categories don't appear in the data
expected_columns = ['married_Divorced', 'married_Married', 'married_Widowed', 'married_Never Married']

# Add missing columns if necessary
for col in expected_columns:
    if col not in marital_dummies.columns:
        marital_dummies[col] = 0

# Convert the boolean values to integers (True -> 1, False -> 0)
marital_dummies = marital_dummies.astype(int)

# Concatenate the original 'id' column with the one-hot encoded columns
result_df = pd.concat([df['id'], marital_dummies[expected_columns]], axis=1)

# Display the final DataFrame
print(result_df)

# df['married_status'] = np.where(df['maritalStatus'].apply(lambda x: x['text'] if isinstance(x, dict) and 'text' in x else None) == 'Married', 'Yes', 'No')

# selected_columns = ['id', 'married_Divorced', 'birthDate']  # Replace these with your desired columns

# # Create a new DataFrame with only the selected columns
# df_selected = df[selected_columns]

# # Print the resulting table
# print(df_selected)


# id,married_Divorced,married_Married,married_Widowed,married_Never Married
# 1a,1,0,0,0
# 2a,0,1,0,0
# 3a,0,0,1,0
# 4a,0,0,0,1
# 5a,0,0,0,1

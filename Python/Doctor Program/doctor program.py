import csv

# Read dr_best.csv
dr_best_file = r'C:\Users\inali\Downloads\dr_best.csv'

with open(dr_best_file, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    dr_best = [row for row in reader]

# Read dr_cushing.csv
dr_cushing_file = r'C:\Users\inali\Downloads\dr_cushing.csv'

with open(dr_cushing_file, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    dr_cushing = [row for row in reader]

# Combine the two lists
all_data = dr_best + dr_cushing

# Sort by birth year (column index 3)
all_data.sort(key=lambda x: int(x[3]))

# Save to a new file
nameFileOut = r'C:\Users\inali\Downloads\merged_customers.csv'

with open(nameFileOut, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(all_data)

print("Combined file created successfully:", nameFileOut)

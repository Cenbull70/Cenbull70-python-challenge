import os
import csv

#Create Variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0


# Path to collect data from the Resources folder
poll = os.path.join("Resources", "election_data.csv")

#Open csv file in read mode
with open (poll, "r") as poll_data:
	csvreader = csv.reader(poll_data, delimiter = ",")
	header = next(csvreader)

#loop thought csv file
	for row in csvreader:
		ballet = row[0]
		county = row[1]
		name = row[2]

		total_votes += 1
		
		if name not in candidates:
			candidates[name] = 0 

		candidates[name] +=1

# Print results to the console
print("Election Results")
print("------------------------")
print()
print(f'Total Votes: {total_votes}')
print()
print("------------------------")
print()

# Prepare data for exporting
results = [
    ["Election Results"],
    ["-------------------------"],
    [f"Total Votes: {total_votes}"],
    ["-------------------------"],
    ]

# Calculate candidates % of votes
for name, votes in candidates.items():
    percentage = (votes / total_votes) * 100 if total_votes > 0 else 0
    print(f"{name}: ({round(percentage, 2)}%) ({votes})")
    results.append([f"{name}: {round(percentage, 2)}% ({votes})"])

# Print statements to make results look good
print()
print("------------------------")
print()

# Determine the winner
for name, votes in candidates.items():
    if votes > winner_votes:
        winner = name
        winner_votes = votes

# Print results to the console
print(f'Winner: {winner}')
print()
print("------------------------")

# Prepare data for exporting
results.append(["-------------------------"])
results.append([f"Winner: {winner}"])
results.append(["-------------------------"])

# Path for the output CSV file
output_path = os.path.join("analysis", "poll_results")

# Export results to CSV
with open(output_path, "w", newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(results)






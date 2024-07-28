#Import modules
import os
import csv

#Create Variables
total_months = 0
net_total = 0
average_change = 0
changes = []
greatest_increase = float('-inf')
greatest_increase_date = ""
greatest_decrease = float('inf')
greatest_decrease_date = ""


# Path to collect data from the Resources folder
budget = os.path.join("Resources", "budget_data.csv")

#Open csv file in read mode
with open (budget, "r") as budget_data:
	csvreader = csv.reader(budget_data, delimiter = ",")
	header = next(csvreader)

	previous_value = None

#loop thought csv file
	for row in csvreader:
		#Calculate number of months in csv
		total_months += 1
		#set where income values are in the csv
		current_value = int(row[1])
		#Calculate the total profites
		net_total += current_value
		#set row that contains the dates
		date = row[0]

		#Calculate the change from the previous value
		if previous_value is not None:
			change = current_value - previous_value
			changes.append(change)

			#Calculate the date with the greates increase
			if change > greatest_increase:
				greatest_increase = change
				greatest_increase_date = date

			#Calculate the date with the greates decrease
			if change < greatest_decrease:
				greatest_decrease = change
				greatest_decrease_date = date

		#Update value for the next iteration
		previous_value = current_value

#Calculate the average of the changes
average_change = sum(changes) / len(changes) if changes else 0

#set output location for text file
output_path = os.path.join("analysis", "budget_analysis")

#open text file in write mode and write results to it
with open(output_path, "w",) as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow([f"Richard Wallace Analysis"])
	csvwriter.writerow([f'Total Months:, {total_months}'])
	csvwriter.writerow([f'Total: ${net_total}'])
	csvwriter.writerow([f'Average Change: ${round(average_change, 2)}'])
	csvwriter.writerow([f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})'])
	csvwriter.writerow([f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})'])

#print results in terminal
print(f'Total Months: {total_months}')
print(f'Total: ${net_total}')
print(f'Average Change: ${round(average_change, 2)}')
print(f'Greatest Increase in Profits {greatest_increase_date} (${greatest_increase})')
print(f'Greatest Decrease in Profites: {greatest_decrease_date} (${greatest_decrease})')

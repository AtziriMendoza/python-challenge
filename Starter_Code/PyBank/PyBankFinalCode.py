# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = r"C:\Users\luzch\Data Science Boot Camp\NU-VIRT-DATA-PT-10-2024-U-LOLC\python-challenge\Starter_Code\PyBank\Resources\budget_data.csv"  # Input file path
file_to_output = r"C:\Users\luzch\Data Science Boot Camp\NU-VIRT-DATA-PT-10-2024-U-LOLC\python-challenge\Starter_Code\PyBank\analysis\.gitkeep"  # Output file path

# Define variables to track the financial data- this will track total number of months and net total amount of "Profit/Losses"
total_months = 0 #setting the value to zero will ensure that the 
total_net = 0
previous_PL = None #None is a Python constant that indicates the absence of a value or a null value. It will be used to indicate that the variable has no value assigned to it yet.
greatest_inc = ("", 0) #will track the month and the amount of the greatest inc
greatest_dec = ("", 0) #will track the month and the amount of the greatest dec
# Add more variables to track other necessary financial data
net_changes = [] #this is going to be the variable that I am going to track the net changes in a list
# Open and read the csv
with open(file_to_load, 'r') as financial_data: 
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)
    # Extract first row to avoid appending to net_change_list
    

    # Track the total and net change- tracks changes in profit and losses
    
    # Process each row of data
    for row in reader:
        date = row [0]
        profit_loss = int(row[1]) #converting profit and loss to an integer

        # Track the total months
        total_months += 1 #shorthand for incrementing the variables by one
            
        # Track the net change
        total_net = total_net + profit_loss
             #there are python shorthand called syntactic sugar- += is syntactic sugar

# adding the net_change to to the list net_changes
        if previous_PL is not None:  
            net_change = profit_loss - previous_PL
            net_changes.append(net_change)
# Calculate the greatest increase in profits (month and amount)
            if net_change > greatest_inc[1]:
                greatest_inc = (date, net_change)
# Calculate the greatest decrease in losses (month and amount)
            if net_change < greatest_dec[1]:
                greatest_dec = (date, net_change)
        previous_PL = profit_loss #this loops it back to the next row of data
# Calculate the average net change across the months
average_net_change = sum(net_changes)/ len(net_changes) if net_changes else 0
# Generate the output summary


# Print the output
output= (f"Financial Analysis \n"
"----------------------------\n"
f"Total Months: {str(total_months)} \n"
f"Total: ${total_net} \n"
f"Average Change: ${average_net_change:.2f} \n"
f"Greatest Increase In Profits: {greatest_inc[0]} ({greatest_inc[1]}) \n"
f"Greatest Decrease In Profits: {greatest_dec[0]} ({greatest_dec [1]}) \n")
print(output)
# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

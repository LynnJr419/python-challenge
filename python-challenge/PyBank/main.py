import csv
import os


#paths for input and output files
csvpath = r'PyBank\Resources\budget_data.csv'
output_csvpath = r'PyBank\Resources\budget_data_analysis.csv'

def analyze_budget_data(csvpath, output_csvpath):
    dates = []
    profits_losses = []
    
    with open(csvpath, mode='r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        
        for row in csvreader:
            dates.append(row[0])
            profits_losses.append(int(row[1]))

# perform calculations
    total_months = len(dates)
    net_total = sum(profits_losses)
    changes = [profits_losses[i] - profits_losses[i - 1] for i in range(1, len(profits_losses))]
    average_change = sum(changes) / len(changes)
    greatest_increase = max(changes)
    greatest_increase_date = dates[changes.index(greatest_increase) + 1]
    greatest_decrease = min(changes)
    greatest_decrease_date = dates[changes.index(greatest_decrease) + 1]

    with open(output_csvpath, mode='w', newline='') as file:
        csvwriter = csv.writer(file)
        
        # Write headers to the output CSV
        csvwriter.writerow(["Metric", "Value"])
        csvwriter.writerow(["Total Months", total_months])
        csvwriter.writerow(["Net Total", f"${net_total}"])
        csvwriter.writerow(["Average Change", f"${average_change:.2f}"])
        csvwriter.writerow(["Greatest Increase in Profits", f"{greatest_increase_date} (${greatest_increase})"])
        csvwriter.writerow(["Greatest Decrease in Profits", f"{greatest_decrease_date} (${greatest_decrease})"])

#print results to the terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Net Total: ${net_total}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

analyze_budget_data(csvpath, output_csvpath)

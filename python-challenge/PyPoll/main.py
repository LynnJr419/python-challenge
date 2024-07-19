import csv

#paths for input and output files
csvpath = r'Pypoll\Resources\election_data.csv'
output_csvpath = r'Pypoll\Resources\election_data_analysis.csv'

def analyze_election_data(csvpath, output_csvpath):

    total_votes = 0
    candidates = {}
    
    with open(csvpath, mode='r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)

        for row in csvreader:
            total_votes += 1
            candidate = row[2]
            if candidate not in candidates:
                candidates[candidate] = 0
            candidates[candidate] += 1

  #determine the winner
    winner = None
    winner_votes = 0


#open and write to the outfile file
    with open(output_csvpath, mode='w', newline='') as file:
        csvwriter = csv.writer(file)
        
       
        csvwriter.writerow(["Candidate", "Percentage", "Votes"])
        
        for candidate, votes in candidates.items():
            percentage = (votes / total_votes) * 100
            csvwriter.writerow([candidate, f"{percentage:.3f}%", votes])
            
          
            if votes > winner_votes:
                winner = candidate
                winner_votes = votes
        
        csvwriter.writerow([])
        csvwriter.writerow(["Winner", winner])
    
     #print to the console   
    print("Election Results")
    print("-----------------")
    print(f"Total Votes: {total_votes}")
    print("-----------------")
    
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})")
        
    print("-----------------")
    print(f"Winner: {winner}")
    print("-----------------")

analyze_election_data(csvpath, output_csvpath)

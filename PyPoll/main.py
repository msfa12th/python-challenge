#  Python-Challenge
#  PyPoll
#  main.py
#
#  author: Mary Brown
#  date created: 8/24/2019
#
#  a Python script for analyzing voting data from a small town
#  source file: (PyPoll/Resources/election_data.csv.csv)
#       The dataset is composed of three columns: 
#               `Voter ID`, `County`, and `Candidate`. 

# utilize tools for csv
import os
import csv
import sys

# initialize variables
candidateNames = []
candidateTally = []
candidatePercentVote = []
ballots = []
numCandidates = 0
totalVotes = 0
voteTally = 0
winningTally = 0


#read in raw data
election_csv = os.path.join("Resources","election_data.csv")

# open the file
with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader, None)  # skip the headers

    for row in csvreader:
        totalVotes = totalVotes +1
        ballots.append(row[2])
        if row[2] not in candidateNames:
            candidateNames.append(row[2])
            numCandidates = numCandidates +1
    

# done with file do calculations
for i in range(numCandidates):
    voteTally = 0
    for j in range(totalVotes):
        if ballots[j] == candidateNames[i]:
            voteTally = voteTally+ 1

    if voteTally > winningTally:
        winningTally = voteTally

    candidateTally.append(voteTally)
    candidatePercentVote.append(float(voteTally/totalVotes))

# compile results 
electionResults = zip(candidateNames, candidateTally, candidatePercentVote) 
    
# 1st print results
print("   ")
print("Election Results")
print("---------------------------------------------")
print(f'Total Votes: {totalVotes}')
print("---------------------------------------------")

for candidate, votes, pctVotes in electionResults:
    print('{}: {:.2%}  ({})'.format(candidate,pctVotes,votes))
    if votes == winningTally:
        winningCandidate = candidate

print("---------------------------------------------")
print(f'Winner: {winningCandidate}')
print("---------------------------------------------")
print("   ")

# 2nd print results to file
filename  = open("output.txt",'w')
sys.stdout = filename

print("   ")
print("Election Results")
print("---------------------------------------------")
print(f'Total Votes: {totalVotes}')
print("---------------------------------------------")

for candidate, votes, pctVotes in electionResults:
    print('{}: {:.2%}  ({})'.format(candidate,pctVotes,votes))
    if votes == winningTally:
        winningCandidate = candidate

print("---------------------------------------------")
print(f'Winner: {winningCandidate}')
print("---------------------------------------------")
print("   ")


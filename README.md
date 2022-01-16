# Election_Analysis
## Overview of Election Audit
This project is to assist Colorado Board of Elections in tabulated election audits in U.S. Congressional precincts in Colorado. There are three counties Araphahoe, Denver, and Jefferson and three candidates Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane in Colorado. Specifically, we will deliver the total votes cast, total votes for each candidate, the percentage of votes each candidate won, the winner, each county's vote turnover, and the county with the largest turnover. We used Python to create a template which automate the process of analysis and applicable to other similar election audits including senatorial and local elections.

## Election Audit Results
The analysis of election shows that:
- Total votes: 369,711

- County votes:
  - Jefferson: 10.5% (38855)
  - Denver: 82.8% (306055)
  - Arapahoe: 6.7% (24801)
- **County with the largest turnover: Denver**

- Candidate votes:
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)
- **Winner: Diana DeGette 73.8% (272,892)**

## Election Audit Summary
This script is also usable for auditing other elections. The script can read and count votes for each candidate and determine the winner, as well as calculate the turnover for each county and select the one with the larget turnover. When using this python script for different election audits, just modify the index of candidate name according to the original poll file. If you would like to count and analyze vote results based on other factors, just change the index number of county into that of the factor you would like to analyze. 
1. For instance, in the upcoming election in November 2022, 34 candidates will be elected as new Class 3 senators. If we are using this script to audit election, we can count total votes and each candidate' votes by using the same piece of script: a for loop to audit total votes, a if statement to create a candidate lists, and another for loop to count each candidate's votes. What we will only modify here is the index of candidate name.

![Modify the index of candidate name](https://github.com/ZiwenLyu/Election_Analysis/blob/main/screenshots/candidate%20Screenshot.png)

As for the county part script, we can replace it with the partisan to see whether Democrates or Republicans take more seats. Most parts of the script will remain the same, all we need to modify is the index number of county to that of partisan. You can also re-name county-related variables without changing the algorithm if that will easier and more readable.

![Modify the index of county](https://github.com/ZiwenLyu/Election_Analysis/blob/main/screenshots/county%20Screenshot.png)
![Modify the variables' names without changing the algorithm](https://github.com/ZiwenLyu/Election_Analysis/blob/main/screenshots/original%20county%20if%20Screenshot.png)
![Modify the variables' names without changing the algorithm](https://github.com/ZiwenLyu/Election_Analysis/blob/main/screenshots/party%20if%20Screenshot.png)

2. Another example will be the local election. A city in Virginia is selecting its mayor, we can still use the script to count total votes and candidates' votes by using the same algorithm and only modify the index number of candidate name. For the mayor election, maybe we would like to know which area, or zipcode has the largest turnover, so we may also change the original index of county into the index of zipcode here.

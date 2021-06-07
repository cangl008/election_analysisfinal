{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "eda63148",
   "metadata": {},
   "outputs": [],
   "source": [
    "# -*- coding: UTF-8 -*-\n",
    "\"\"\"PyPoll Homework Challenge Solution.\"\"\"\n",
    "\n",
    "# Add our dependencies.\n",
    "import csv\n",
    "import os\n",
    "\n",
    "# Add a variable to load a file from a path.\n",
    "file_to_load = os.path.join(\".\", \"resources\", \"election_results.csv\")\n",
    "# Add a variable to save the file to a path.\n",
    "file_to_save = os.path.join(\"analysis\", \"election_analysis.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "976a7488",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'.\\\\resources\\\\election_results.csv'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "file_to_load"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "bc7db1ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Initialize a total vote counter.\n",
    "total_votes = 0\n",
    "\n",
    "# Candidate Options and candidate votes.\n",
    "candidate_options = []\n",
    "candidate_votes = {}\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "98e9f2b1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1: Create a county list and county votes dictionary.\n",
    "\n",
    "county_names=[] # holding our county\n",
    "county_votes={} # \"key\":\"value\" ie. \"County\":200 # votes\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "af09fe4e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Track the winning candidate, vote count and percentage\n",
    "winning_candidate = \"\"\n",
    "winning_count = 0\n",
    "winning_percentage = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "330a9120",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2: Track the largest county and county voter turnout.\n",
    "largest_county_with_votes=\"\"\n",
    "largest_county_votes=0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "30a63c1a",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(file_to_load) as election_data:\n",
    "    reader = csv.reader(election_data)\n",
    "\n",
    "    # Read the header\n",
    "    header = next(reader)\n",
    "\n",
    "    # For each row in the CSV file.\n",
    "    for row in reader:\n",
    "\n",
    "        # Add to the total vote count\n",
    "        total_votes = total_votes + 1\n",
    "\n",
    "        # Get the candidate name from each row.\n",
    "        candidate_name = row[2]\n",
    "\n",
    "        # 3: Extract the county name from each row.\n",
    "        county_name=row[1] # gols county\n",
    "\n",
    "        # If the candidate does not match any existing candidate add it to\n",
    "        # the candidate list\n",
    "        if candidate_name not in candidate_options:\n",
    "\n",
    "            # Add the candidate name to the candidate list.\n",
    "            candidate_options.append(candidate_name)\n",
    "\n",
    "            # And begin tracking that candidate's voter count.\n",
    "            candidate_votes[candidate_name] = 0\n",
    "\n",
    "        # Add a vote to that candidate's count \n",
    "        candidate_votes[candidate_name] += 1    # var = var + 1\n",
    "\n",
    "        # 4a: Write an if statement that checks that the\n",
    "        # county does not match any existing county in the county list.\n",
    "        if county_name not in county_names:\n",
    "            \n",
    "\n",
    "            # 4b: Add the existing county to the list of counties.\n",
    "            county_names.append(county_name)\n",
    "\n",
    "            # 4c: Begin tracking the county's vote count.\n",
    "            county_votes[county_name]=0\n",
    "\n",
    "        # 5: Add a vote to that county's vote count.\n",
    "        county_votes[county_name]=county_votes[county_name] + 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "810b0615",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3e192ec8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Jefferson': 38855, 'Denver': 306055, 'Arapahoe': 24801}"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "county_votes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "976b4a0e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Charles Casper Stockham': 85213,\n",
       " 'Diana DeGette': 272892,\n",
       " 'Raymon Anthony Doane': 11606}"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "candidate_votes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "da33331b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "9a776b82",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Election Results\n",
      "-------------------------\n",
      "Total Votes: 369,711\n",
      "-------------------------\n",
      "\n",
      "County Votes:\n",
      "Jefferson 38855 has pctg 10.51%\n",
      "Denver 306055 has pctg 82.78%\n",
      "Arapahoe 24801 has pctg 6.71%\n",
      "Largest Turnout Arapahoe 24801 has pctg 6.71%\n",
      "Charles Casper Stockham: 23.0% (85,213)\n",
      "\n",
      "Diana DeGette: 73.8% (272,892)\n",
      "\n",
      "Raymon Anthony Doane: 3.1% (11,606)\n",
      "\n",
      "-------------------------\n",
      "Winner: Diana DeGette\n",
      "Winning Vote Count: 272,892\n",
      "Winning Percentage: 73.8%\n",
      "-------------------------\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Save the results to our text file.\n",
    "with open(file_to_save, \"w\") as txt_file:\n",
    "\n",
    "    # Print the final vote count (to terminal)\n",
    "    election_results = (\n",
    "        f\"\\nElection Results\\n\"\n",
    "        f\"-------------------------\\n\"\n",
    "        f\"Total Votes: {total_votes:,}\\n\"\n",
    "        f\"-------------------------\\n\\n\"\n",
    "        f\"County Votes:\\n\")\n",
    "    print(election_results, end=\"\")\n",
    "\n",
    "    txt_file.write(election_results)\n",
    "\n",
    "    # 6a: Write a for loop to get the county from the county dictionary.\n",
    "    \n",
    "    for county in county_votes:\n",
    "        \n",
    "\n",
    "        # 6b: Retrieve the county vote count.\n",
    "        county_vote=county_votes[county]\n",
    "        # 6c: Calculate the percentage of votes for the county.\n",
    "        county_vote_percent=(county_vote/total_votes) * 100\n",
    "\n",
    "         # 6d: Print the county results to the terminal.\n",
    "        county_results = f\"{county} {county_vote} has pctg {county_vote_percent:.2f}%\"\n",
    "        print(county_results)\n",
    "         # 6e: Save the county votes to a text file.\n",
    "        txt_file.write(county_results)\n",
    "         # 6f: Write an if statement to determine the winning county and get its vote count.\n",
    "        if (county_vote > largest_county_votes):\n",
    "            largest_county_votes=county_vote\n",
    "            largest_county_with_votes = county\n",
    "\n",
    "    # 7: Print the county with the largest turnout to the terminal.\n",
    "    largest_turnout_results = f\"Largest Turnout {county} {county_vote} has pctg {county_vote_percent:.2f}%\"\n",
    "    print(largest_turnout_results)\n",
    "\n",
    "    # 8: Save the county with the largest turnout to a text file.\n",
    "    txt_file.write(largest_turnout_results)\n",
    "\n",
    "    # Save the final candidate vote count to the text file.\n",
    "    for candidate_name in candidate_votes:\n",
    "\n",
    "        # Retrieve vote count and percentage\n",
    "        votes = candidate_votes.get(candidate_name)\n",
    "        vote_percentage = float(votes) / float(total_votes) * 100\n",
    "        candidate_results = (\n",
    "            f\"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\\n\")\n",
    "\n",
    "        # Print each candidate's voter count and percentage to the\n",
    "        # terminal.\n",
    "        print(candidate_results)\n",
    "        #  Save the candidate results to our text file.\n",
    "        txt_file.write(candidate_results)\n",
    "\n",
    "        # Determine winning vote count, winning percentage, and candidate.\n",
    "        if (votes > winning_count) and (vote_percentage > winning_percentage):\n",
    "            winning_count = votes\n",
    "            winning_candidate = candidate_name\n",
    "            winning_percentage = vote_percentage\n",
    "\n",
    "    # Print the winning candidate (to terminal)\n",
    "    winning_candidate_summary = (\n",
    "        f\"-------------------------\\n\"\n",
    "        f\"Winner: {winning_candidate}\\n\"\n",
    "        f\"Winning Vote Count: {winning_count:,}\\n\"\n",
    "        f\"Winning Percentage: {winning_percentage:.1f}%\\n\"\n",
    "        f\"-------------------------\\n\")\n",
    "    print(winning_candidate_summary)\n",
    "\n",
    "    # Save the winning candidate's name to the text file\n",
    "    txt_file.write(winning_candidate_summary)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e7117fa5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3-PythonData",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

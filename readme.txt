This file contains instructions for running Nick Chen’s Twitter streaming application.

Step 1 - Create the Database
- Navigate to the folder ex2/serving_scripts and run the python file called setup_postgres_db_for_ex2.py
- This script deletes any existing database called ‘tcount’, creates a new blank database called ’tcount’, and creates a table called ‘tweetwordcount’ into which words and their counts will later be placed by the streaming application.

Step 2 - Run the Streaming Application
- Navigate to the folder ex2/ExerciseTweetwordcount
- run the command: sparse run
- After about one minute, you will begin to see parsed words logged to the screen. This indicates that the application is running. Let the application run for as long as you would like.
- As words are logged to the screen, they are also written to the DB.
- When you want to stop the stream, use ctrl + C to stop the stream.

Step 3 - Get Results
- The python script finalresults.py in the folder ex2/serving_scripts allows you to easily access the results of twitter stream.
- If you want to get the the number of times a specific word occurred in the stream, run this script followed by the word you are interested in. For example: python finalresults.py testword
- If you would like to see all words that occurred within a certain range of times, run this script followed by two integers. For example: python final results.py 5 10
- If you would simply like to see all of the words that occurred in the stream along with their counts, run this script with no additional arguments: python finalresults.py
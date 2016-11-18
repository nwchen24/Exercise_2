#Author: Nick Chen
#Purpose: To return the total number of occurrences of an argument given to the scrip

import psycopg2
import sys

#Defina a function test how many arguments were passed with the command to run this script
def num_args_func(arg_list):
    try:
        arg_list[2]
        return 2
    except IndexError:
        try:
            arg_list[1]
            return 1
        except IndexError:
            return 0

num_args = (num_args_func(sys.argv))


#Define connection
conn = psycopg2.connect(database = "tcount", user = "postgres", password = "pass", host = "localhost", port = "5432")

#open cursor
cur = conn.cursor()

###########
#If no arguments are passed with the run command then return a list of all the words in the stream along with their counts.
if num_args == 0:
    
    #Get a list of all the words in the stream along with their counts
    cur.execute("select * from tweetwordcount order by word")

    all_words = cur.fetchall()

    conn.commit()
    conn.close()

    print(all_words)


##########
#If there is only one argument passed with the python script, then get and return the number of instances of that word
if num_args == 1:
    
    word = sys.argv[1].upper()

    #Get the number of occurrences of the word
    cur.execute("select count from tweetwordcount where word = %s", (word,))
    word_count = cur.fetchall()

    conn.commit()
    conn.close()
    
    try:
        print("The number of occurrences of " + word + " is: " + str(word_count[0][0]))
    except IndexError:
        print(word + " did not occur in the stream.")

##########
#If two arguments are passed, return all words where their count of appearances in the stream is between the two arguments
if  num_args == 2:

    lower_lim = min(sys.argv[1], sys.argv[2])
    upper_lim = max(sys.argv[1], sys.argv[2])

    #Get all words whose number of occurrences falls between the two arguments passed to the function
    cur.execute("select * from tweetwordcount where count <= %s and count >= %s order by count", (upper_lim, lower_lim))
    
    hist_words = cur.fetchall()

    conn.commit()
    conn.close()

    print(hist_words)















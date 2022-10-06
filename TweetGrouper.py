import pandas as pd

def combineTweets():
    # Creating new CSV file
    tweets = open('OriginalCombinedTweets.csv', 'w')

    # Writing every line for each individual Tweets file into 1 file
    for num in range(1, 12):
        for line in open(r'Tweets/OhioTweets' + str(num) + '.csv'):
            tweets.write(line)
    
    # Closing file
    tweets.close()

def removeDuplicates(file):
    # Reading file into dataframe and removing additional index column
    dfTweets = pd.read_csv(file)
    dfTweets = dfTweets.drop(columns= 'Unnamed: 0')

    # Dropping duplicate rows
    dfTweets = dfTweets.drop_duplicates()

    # Exporting unique tweets csv
    dfTweets.to_csv('UniqueCombinedTweets.csv')

# Calling functions
combineTweets()
removeDuplicates('OriginalCombinedTweets.csv')
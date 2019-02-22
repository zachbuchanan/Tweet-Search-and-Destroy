#zach buchanan
#november 14, 2018
#just for fun


import tweepy

consumer_key = ""
consumer_secret = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

screenName = raw_input("Enter your twitter user name: ")

keyword = []
inputKey = raw_input("Type a keyword you would like to search for and hit enter. Type 'Done' to be finished adding keywords\n")
while(inputKey != "Done"):
    inputKey = raw_input()
    if(inputKey != "Done"): keyword.append(inputKey)

status = api.user_timeline(screen_name = screenName, count = 100, include_rts = True)

for tweet in status:
    for key in keyword:
        if tweet.text.find(key) != -1:
            try:
                api.destroy_status(tweet.id)
                print "Deleted: ", tweet.id
                break;
            except:
                print "Failed to delete: ", tweet.text

print "Finished"






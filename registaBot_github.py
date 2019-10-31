"""
Alperen Gormez
"""

import tweepy
import praw
import random
import urllib.request
import os
import time

# for reddit
client_id = ''
client_secret = ''
username = ''
password = ''
user_agent = ''


# for twitter
consumer_key = '' #(API key)
consumer_secret = '' #(API secret key)
access_token = '' #(Access token)
access_token_secret = '' #(Access token secret)


# authorize reddit and twitter apis
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent
                    )

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


# in this dictionary (essentially hash table), we store the time of a mention to our bot
# the purpose is not to reply to this mention again
# the probability of multiple mentions coming at the same time is low, so that is why I use time
# more sophisticated methods can be applied such as random string generation and appending it to the time etc.
mentions_hash_table = {}

# since our code will run on a server and it may crash, we have to store the past mentions
# so that we will not reply them again when our code runs again

filepath = '/home/hash_table.txt'
with open(filepath, 'r') as fp:
    for line in fp:
        print(line.strip())
        mentions_hash_table[str(line.strip())] = str(line.strip())
    
    line = fp.readline().strip()
    print(line)
    while line:    
        line = fp.readline().strip()
        print(line)
        mentions_hash_table[str(line)] = str(line)


while True: # probably there is a better way other than constantly checking mentions, but we can think about it later

    # it is useful to note that mention_list is like a stack. most recent mention is stored at index 0 afai tested
    mention_list = api.mentions_timeline() # get the mentions
    mention_list

    for mention in mention_list:
        time_of_mention = str(mention.created_at)
        if not (time_of_mention in mentions_hash_table): # if not previously replied

            if ":tj" in mention.text: # reply with a random post from /r/pics

                mentions_hash_table[time_of_mention] = time_of_mention # replied now
                
                filepath = '/home/hash_table.txt'
                with open(filepath, 'a') as fp:
                    fp.write('\n')
                    fp.write(time_of_mention)
                   
                
                
                limit = 20
                subreddit = reddit.subreddit("pics")
                hot_posts = subreddit.hot(limit=limit)
                r = random.randint(1, limit)
                meme_url = ""

                i = 1
                for post in hot_posts:
                    if i == r:
                        if not post.stickied:
                            meme_url = post.url
                        break
                    i += 1


                index_of_last_dot = (-1)*(meme_url[::-1].find('.') + 1) # to find the index of . in .jpg/png/jpeg
                img_name = "will_be_deleted_anyyway" + meme_url[index_of_last_dot:]
                try:
                    urllib.request.urlretrieve(meme_url, img_name) # download the image
                    status = '@' + mention.user.screen_name + ' Credit: /u/' + post.author.name + ". Title: " + post.title
                    api.update_with_media(img_name, status, in_reply_to_status_id=mention.id) # reply to mention

                    os.remove(img_name) # remove the image so that it does not allocate memory in the server
                except:
                    status = '@' + mention.user.screen_name + ' Things went wrong. Sorry.'
                    api.update_status(status, mention.id)


            elif ":denizli" in mention.text:
                mentions_hash_table[time_of_mention] = time_of_mention
                filepath = '/home/hash_table.txt'
                with open(filepath, 'a') as fp:
                    fp.write('\n')
                    fp.write(time_of_mention)
                status = '@' + mention.user.screen_name + ' A spectacular city, famous for its roosters. I love this place.'
                api.update_status(status, mention.id)

            elif ":ezel" in mention.text:
                mentions_hash_table[time_of_mention] = time_of_mention
                filepath = '/home/hash_table.txt'
                with open(filepath, 'a') as fp:
                    fp.write('\n')
                    fp.write(time_of_mention)
                status = '@' + mention.user.screen_name + ' Her ihanet sevgiyle başlar.'
                api.update_status(status, mention.id)

            elif ":ferrari" in mention.text:
                mentions_hash_table[time_of_mention] = time_of_mention
                filepath = '/home/hash_table.txt'
                with open(filepath, 'a') as fp:
                    fp.write('\n')
                    fp.write(time_of_mention)
                status = '@' + mention.user.screen_name + " Ferrari F1'in sefiridir. Biat edin."
                api.update_status(status, mention.id)

            elif ":random" in mention.text:
                mentions_hash_table[time_of_mention] = time_of_mention
                filepath = '/home/hash_table.txt'
                with open(filepath, 'a') as fp:
                    fp.write('\n')
                    fp.write(time_of_mention)
                status = '@' + mention.user.screen_name + ' ne yapacaktım buraya unuttum'
                api.update_status(status, mention.id)

            elif ":nopirlo" in mention.text:
                mentions_hash_table[time_of_mention] = time_of_mention
                filepath = '/home/hash_table.txt'
                with open(filepath, 'a') as fp:
                    fp.write('\n')
                    fp.write(time_of_mention)
                status = '@' + mention.user.screen_name + ' No Party'
                api.update_status(status, mention.id)

            elif ":playchess" in mention.text:
                # implement later
                mentions_hash_table[time_of_mention] = time_of_mention
                filepath = '/home/hash_table.txt'
                with open(filepath, 'a') as fp:
                    fp.write('\n')
                    fp.write(time_of_mention)
                status = '@' + mention.user.screen_name + ' Not implemented yet.'
                api.update_status(status, mention.id)

            elif ":secret" in mention.text:
                mentions_hash_table[time_of_mention] = time_of_mention
                filepath = '/home/hash_table.txt'
                with open(filepath, 'a') as fp:
                    fp.write('\n')
                    fp.write(time_of_mention)
                send_only_to_these = ['', '', '','',
                                      '', '', '', ''
                                     ]
                mentioned_by = mention.user.screen_name
                if mentioned_by in send_only_to_these:
                    limit = 20
                    subreddit = reddit.subreddit("pics")
                    hot_posts = subreddit.hot(limit=limit)
                    r = random.randint(1, limit)
                    url = ""

                    i = 1
                    for post in hot_posts:
                        if i == r:
                            if not post.stickied:
                                url = post.url
                            break
                        i += 1

                    api.send_direct_message(mention.user.id, url)
                    status = '@' + mention.user.screen_name + ' Check your DM box.'
                    api.update_status(status, mention.id)
                else:
                    status = '@' + mention.user.screen_name + ' Apparently my creator did not give permission to you for this feature. Please contact him.'
                    api.update_status(status, mention.id)

            elif ":joke" in mention.text:
                mentions_hash_table[time_of_mention] = time_of_mention
                filepath = '/home/hash_table.txt'
                with open(filepath, 'a') as fp:
                    fp.write('\n')
                    fp.write(time_of_mention)
                
                limit = 20
                subreddit = reddit.subreddit("jokes")
                hot_posts = subreddit.hot(limit=limit)
                r = random.randint(1, limit)
                
                i = 1
                for post in hot_posts:
                    if i == r:
                        break
                    i += 1
                
                status = '@' + mention.user.screen_name + post.title + " - " + post.selftext + ". Credit: /u/" + post.author.name
                api.update_with_media(img_name, status, in_reply_to_status_id=mention.id) # reply to mention

            else:
                mentions_hash_table[time_of_mention] = time_of_mention
                filepath = '/home/hash_table.txt'
                with open(filepath, 'a') as fp:
                    fp.write('\n')
                    fp.write(time_of_mention)
                status = '@' + mention.user.screen_name + ' Command not found.'
                api.update_status(status, mention.id)
                
    time.sleep(15)



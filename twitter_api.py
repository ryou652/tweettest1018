# -*- coding: utf-8 -*-
import tweepy

def main():
    CONSUMER_KEY="0lLJV0iQqZDiG6u5bouVb5pHY"
    CONSUMER_SECRET="uIE6XmxYV4gLe9NBYoCoYoh9vDG47QCVCS1LiQoAAx6SlFksrh"
    ACCESS_TOKEN="1084025738251067393-KABf3vH0TOPCnW13LHx44q9EwXc1dE"
    ACCESS_SECERET="ktSZpBT9NWxu91SRUqSfJ6ONIifcNSGGA6iwrGNniuLxZ"

    auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_SECERET)
    api=tweepy.API(auth)

    q_list=["#はてなブログ","#ブログ書け"]
    count=20
    for q in q_list:
        print("Now:QUERY-->>{}".format(q))
        search_results=api.search(q=q,count=count)
        for status in search_results:
            tweet_id=status.id
            try:
                api.create_favorite(tweet_id)
            except:
                pass

if __name__ == '__main__':
    main()

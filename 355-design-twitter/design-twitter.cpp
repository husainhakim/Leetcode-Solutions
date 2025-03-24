class Twitter 
{
private:
    map<int, list<pair<int,int>>> tweet;
    map<int, set<int>> followers;
    int timestamp;

public:
    Twitter() : timestamp(0)
    {
        
    }
    
    void postTweet(int userId, int tweetId)
    {
        tweet[userId].push_front({timestamp++,tweetId});
    }
    
    vector<int> getNewsFeed(int userId)
    {
        // max heap can be used to get the recent 10 tweets.
        priority_queue<pair<int,int>> recent_tweets;
        for( const auto& val : tweet[userId])
        {
            recent_tweets.push(val);
        }

        // We have to get the tweets from followee also
        for( const auto& f : followers[userId])
        {
            for( const auto& ft : tweet[f])
            {
                recent_tweets.push(ft);
            }
        }

        // Now we need to find the recent 10 tweets.
        vector<int> tweets;
        int tweet_count = 0;
        while(!recent_tweets.empty() && tweet_count < 10)
        {
            tweets.push_back(recent_tweets.top().second);
            recent_tweets.pop();
            ++tweet_count;
        }
        return tweets;
    }
    
    void follow(int followerId, int followeeId)
    {
        followers[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId)
    {
        followers[followerId].erase(followeeId);
    }
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
 */
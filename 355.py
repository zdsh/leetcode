class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.rela={}
        self.twitters=[]
        self.twitter_id={}
    

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.twitters.append(tweetId)
        self.twitter_id[tweetId]=userId
        
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        ret=[]
        f=[userId]
        if userId in self.rela:
            f+=self.rela[userId]
        for t in self.twitters[::-1]:
            if len(ret)<10 and self.twitter_id[t] in f:
                ret.append(t)
        return ret
        
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.rela:
            self.rela[followerId]=[]
        self.rela[followerId].append(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.rela and followeeId in self.rela[followerId]:
            self.rela[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(set)
        self.tweetTimestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].add((self.tweetTimestamp, tweetId))
        self.tweetTimestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []

        users = self.followers[userId]
        users.add(userId)

        for user in users:
            for tweet in self.tweets[user]:
                heapq.heappush(tweets, tweet)
        
        result, i = [], 0
        while tweets and i < 10:
            result.append(heapq.heappop(tweets)[1])
            i += 1
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

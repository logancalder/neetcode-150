class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.tweetTimestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.tweetTimestamp, tweetId))
        self.tweetTimestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []

        self.followers[userId].add(userId)
        
        for follower in self.followers[userId]:
            if not self.tweets[follower]:
                continue

            index = len(self.tweets[follower]) - 1 
            tweet = self.tweets[follower][index]
            heapq.heappush(tweets, (tweet[0], tweet[1], index, follower))
        
        result = []

        while tweets and len(result) < 10:
            tweet = heapq.heappop(tweets)
            result.append(tweet[1])

            follower_id, index = tweet[3], tweet[2] - 1

            if index >= 0:
                tweet = self.tweets[follower_id][index]
                heapq.heappush(tweets, (tweet[0], tweet[1], index, follower_id))
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

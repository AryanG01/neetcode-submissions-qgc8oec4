class Twitter:

    def __init__(self):
        self.time = 0
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        self.followers[userId].add(userId)

        for followee in self.followers[userId]:
            for time, tweet in self.tweets[followee]:
                heapq.heappush(heap, (-time, tweet))
        
        res = []
        for i in range(min(10, len(heap))):
            res.append(heapq.heappop(heap)[1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

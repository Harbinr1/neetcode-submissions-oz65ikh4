class Twitter:

    def __init__(self):
        self.storage = defaultdict(list)
        self.following = defaultdict(set)
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.storage[userId].append([self.timestamp,tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        
        minHeap = []
        users = self.following.get(userId, set())
        users.add(userId)

        for uid in users:
            tweets = self.storage.get(uid, [])
            for timestamp, tweetId in tweets:
                heapq.heappush(minHeap, (timestamp, tweetId))
                if len(minHeap) > 10:
                    heapq.heappop(minHeap)

        # Extract only tweetIds in descending order of timestamp
        return [tweetId for (timestamp, tweetId) in sorted(minHeap, reverse=True)]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)


        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)

        

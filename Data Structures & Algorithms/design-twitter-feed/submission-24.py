class Twitter:

    def __init__(self):
        self.storage = defaultdict(list)
        self.following = defaultdict(set)
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.storage[userId].append([self.timestamp,tweetId])
        self.timestamp -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        res = []
        self.following[userId].add(userId)
        for followeeId in self.following[userId]:
            if followeeId in self.storage:
                index = len(self.storage[followeeId]) - 1
                count,tweetId =  self.storage[followeeId][index]
                minHeap.append([count,tweetId,followeeId,index -1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count,tweetId,followeeId,index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count,tweetId  = self.storage[followeeId][index]
                heapq.heappush(minHeap,[count,tweetId,followeeId,index - 1])
        return res





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

        

class Twitter:

    def __init__(self):
        self.u=defaultdict(list)
        self.f=defaultdict(set)
        self.c=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.u[userId].append([self.c,tweetId])
        self.c-=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        mh=[]
        res=[]
        self.f[userId].add(userId)

        for followeeId in self.f[userId]:
            if followeeId in self.u:
                idx=len(self.u[followeeId])-1
                cnt, tweetId = self.u[followeeId][idx]
                heapq.heappush(mh,[cnt,tweetId,followeeId,idx-1])

        while mh and len(res)<10:
            cnt,tweetId,followeeId,idx=heapq.heappop(mh)
            res.append(tweetId)
            if idx>=0:
                cnt,tweetId=self.u[followeeId][idx]
                heapq.heappush(mh,[cnt,tweetId,followeeId,idx-1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.f[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.f[followerId]:
            self.f[followerId].remove(followeeId)
        

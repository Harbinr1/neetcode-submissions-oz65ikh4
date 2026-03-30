class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = []
        for task,freq in count.items():
            heapq.heappush(maxHeap,(-freq,task))

        time = 0
        q = deque()
        while maxHeap or q:
            time += 1
            if maxHeap:
                neg_freq,task = heapq.heappop(maxHeap)

                remaining = -neg_freq - 1

                if remaining > 0:
                    q.append([remaining,task,time + n])
            
            while q and q[0][2] <= time:
                remaining,task,_ = q.popleft()
                heapq.heappush(maxHeap,(-remaining,task))
        return time 

        

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_to_freq = defaultdict(int)
        for task in tasks:
            task_to_freq[task] += 1

        max_heap = [-f for f in task_to_freq.values()]
        heapq.heapify(max_heap)

        q = deque() # holds (count/remaining # of tasks , time it can be processed again)

        time = 0
        while max_heap or q:
            time += 1
            if max_heap:
                freq = 1 + heapq.heappop(max_heap)
                if freq != 0:
                    q.append((freq,time+n))

            if q and q[0][1] == time:
                freq, time = q.popleft()
                heapq.heappush(max_heap, freq)

        return time
        
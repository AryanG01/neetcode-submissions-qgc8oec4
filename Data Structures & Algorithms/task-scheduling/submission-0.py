class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        f_max = max(freq.values())
        num_max = sum(1 for task in freq if freq[task] == f_max)
        
        intervals = (f_max - 1) * (n + 1) + num_max
        return max(len(tasks), intervals)
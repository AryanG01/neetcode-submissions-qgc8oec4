class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
        for(int stone: stones) {
            pq.add(stone);
        }
        while(pq.size() > 1) {
            int first = pq.poll();
            int second = pq.poll();

            int diff = Math.abs(first - second);
            if(diff != 0) {
                pq.add(diff);
            }
        }

        return pq.isEmpty() ? 0 : pq.poll();
    }
}

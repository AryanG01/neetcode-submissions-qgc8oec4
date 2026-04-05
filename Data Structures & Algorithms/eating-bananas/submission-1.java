class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int start = 1;
        int end = Integer.MAX_VALUE;
        int rate = 0;

        // for(int i=0; i<piles.length; i++) {
        //     end += piles[i];
        // }

        while(start <= end) {
            int mid = end + (start - end) / 2;

            if(timeTaken(piles, mid) <= h) {
                rate = mid;
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }

        return rate;
    }

    public int timeTaken(int[] piles, int rate) {
        int total = 0;

        for (int i=0; i<piles.length; i++) {
            total += piles[i] / rate;
            total += piles[i] % rate == 0 ? 0 : 1;    
        }

        return total;
    }
}

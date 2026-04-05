class Solution {
    public class Coords {
        int x;
        int y;
        int distanceSquared;  // Store squared distance to avoid sqrt computation

        public Coords(int x, int y) {
            this.x = x;
            this.y = y;
            this.distanceSquared = x * x + y * y;
        }
    }

    public class CoordsComparator implements Comparator<Coords> {
        public int compare(Coords p1, Coords p2) {
            return Integer.compare(p1.distanceSquared, p2.distanceSquared);
        }
    }

    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<Coords> pq = new PriorityQueue<>(new CoordsComparator());
        int[][] res = new int[k][2];
        for(int[] point : points) {
            pq.add(new Coords(point[0], point[1]));
        } 

        for(int i = 0; i < k; i++) {
            Coords c = pq.poll();
            res[i] = new int[] {c.x, c.y};
        }

        return res;
    }
}

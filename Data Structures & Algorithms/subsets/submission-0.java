class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> arr = new ArrayList<>();
        arr.add(new ArrayList<Integer>());

        for (int i=0; i<nums.length; i++) {
            List<List<Integer>> dup = new ArrayList<>();

            for(List<Integer> subset : arr) {
                List<Integer> newSubset = new ArrayList<>(subset);
                newSubset.add(nums[i]);
                dup.add(newSubset);
            }
            arr.addAll(dup);
        }

        return arr;
    }
}

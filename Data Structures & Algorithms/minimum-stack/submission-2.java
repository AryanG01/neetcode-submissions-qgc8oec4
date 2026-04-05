class MinStack {

    List<int[]> stack;
    int min = Integer.MAX_VALUE;
    int len = 0;

    public MinStack() {
        this.stack = new ArrayList<>();
    }
    
    public void push(int val) {
        if(val < this.min) {
            this.min = val;
        }
        this.stack.add(new int[] {val, this.min});
        this.len += 1;
    }
    
    public void pop() {
        if(len > 0) {
            this.stack.remove(this.len - 1);
            this.len -= 1;
        }
        if (len > 1) {
            this.min = this.stack.get(this.len - 1)[1];
        } else if (len == 0) {
            this.min = Integer.MAX_VALUE;
        }
    }
    
    public int top() {
        if(len > 0) {
            return this.stack.get(this.len - 1)[0];
        }
        return 0;
    }
    
    public int getMin() {
        return this.stack.get(this.len - 1)[1];
    }
}
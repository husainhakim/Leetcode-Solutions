class MinStack {
    private: 
    stack<int> ogStack, minStack;
public:
    void push(int val) {
        ogStack.push(val);
        // if(minStack.empty())
        // {
        //     minStack.push(val);
        // }
        // else if (val<minStack.top())
        // {
        //     minStack.push(val);
        // }
        minStack.push(minStack.empty() ? val: (min(minStack.top(),val)));
    }
    
    void pop() {
        ogStack.pop();
        minStack.pop();
    }
    
    int top() {
        return ogStack.top();
    }
    
    int getMin() {
       return minStack.top(); 
    }
};


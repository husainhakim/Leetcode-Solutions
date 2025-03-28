class MinStack {
private:
    stack<int> dataStack, minStack; 

public:
    void push(int val) {
        dataStack.push(val);
        minStack.push(minStack.empty() ? val : min(minStack.top(), val));
    }
    
    void pop() {
        dataStack.pop();
        minStack.pop();
    }
    
    int top() {
        return dataStack.top();
    }
    
    int getMin() {
        return minStack.top();
    }
};
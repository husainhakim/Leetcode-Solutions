class MinStack {
private:
    stack<long long> st;
    long long minElement;

public:
    MinStack() {}

    void push(int value) {
        if (st.empty()) {
            st.push(value);
            minElement = value;
        } else {
            if (value < minElement) {
                st.push(2LL * value - minElement); // Encode min
                minElement = value;
            } else {
                st.push(value);
            }
        }
    }

    void pop() {
        if (st.top() < minElement) {
            minElement = 2 * minElement - st.top(); // Decode previous min
        }
        st.pop();
    }

    int top() {
        if (st.top() < minElement) return minElement; // Encoded value case
        return st.top();
    }

    int getMin() {
        return minElement;
    }
};
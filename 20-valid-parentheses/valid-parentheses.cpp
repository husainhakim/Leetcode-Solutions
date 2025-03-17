class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        unordered_map<char, char> pairs = {
            {')', '('},
            {'}', '{'},
            {']', '['}
        };

        for (char bracket : s) {
            if (bracket == '(' || bracket == '{' || bracket == '[') {
                st.push(bracket);
            } else {
                if (st.empty() || st.top() != pairs[bracket]) {
                    return false;
                }
                st.pop();
            }
        }

        return st.empty();
    }
};

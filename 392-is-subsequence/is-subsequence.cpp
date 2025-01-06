class Solution {
public:
    bool isSubsequence(string s, string t) {
        string filtered = ""; 

        for (char c : t) { 
            if (!s.empty() && c == s[0]) { 
                filtered += c; 
                s.erase(s.begin()); 
            }
        }

        return s.empty(); 
    }
};
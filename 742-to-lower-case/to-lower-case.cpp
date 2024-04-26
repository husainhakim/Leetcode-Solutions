class Solution {
public:
    string toLowerCase(string s) {
        string ans="";
        for(int i=0;i<s.size();i++)
        {
            if(s[i]<=90 && s[i]>=65)
            {
                ans+=s[i]+32;
            }
            else
            {
                ans+=s[i];
            }
        }
        return ans;
    }
};
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> mergedVector;
        
        for (int i = 0; i < intervals.size(); i++) {
         
            if (mergedVector.empty() || mergedVector.back()[1] < intervals[i][0]) {
                mergedVector.push_back(intervals[i]);
            } else {
                mergedVector.back()[1] = max(mergedVector.back()[1], intervals[i][1]);
            }
        }
        
        return mergedVector;
    }
};
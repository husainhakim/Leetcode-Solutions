class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        // Sort the intervals based on the start time
        sort(intervals.begin(), intervals.end());

        vector<vector<int>> merged;

        for (auto interval : intervals) {
            // If the merged list is empty or no overlap, add the current interval
            if (merged.empty() || merged.back()[1] < interval[0]) {
                merged.push_back(interval);
            } 
            // If overlap, merge the intervals by updating the end time
            else {
                merged.back()[1] = max(merged.back()[1], interval[1]);
            }
        }

        return merged;
    }
};
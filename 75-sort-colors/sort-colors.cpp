class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n - 1; i++) {  // Loop through each element
            for (int j = i + 1; j < n; j++) {  // Compare with the next elements
                if (nums[i] > nums[j]) {  // Swap if the current element is greater than the next element
                    int temp = nums[j];
                    nums[j] = nums[i];
                    nums[i] = temp;
                }
            }
        }
    }
};
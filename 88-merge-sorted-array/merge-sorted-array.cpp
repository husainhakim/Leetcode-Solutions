class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        if(n == 0)return;
        int len1 = nums1.size();
        int last= len1-1;
        while(n > 0 && m > 0){
            if(nums2[n-1] >= nums1[m-1]){
                nums1[last] = nums2[n-1];
                n--;
            }else{
                nums1[last] = nums1[m-1];
                m--;
            }
            last--;
        }
        while (n > 0) {
            nums1[last] = nums2[n-1];
            n--;
            last--;
        }
    }
};
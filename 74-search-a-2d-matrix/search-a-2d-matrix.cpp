class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) 
    {
       
        int start=0;
        for(int i=0;i<matrix.size();i++)
        {
           if(matrix[i] [ matrix[0].size()-1 ] >=target){start=i;break;}

        }

        int low=0,high=matrix[0].size()-1;

        while(low<=high)
        {
            int mid=(low+high)/2;
            if(matrix[start][mid]==target)return true;
            else if(matrix[start][mid]<target)low=mid+1;
            else high=mid-1;
        }
        
        return false;
    }
};
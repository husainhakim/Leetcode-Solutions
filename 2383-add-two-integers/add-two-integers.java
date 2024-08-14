class Solution {
    public int sum(int num1, int num2) {
        int c;
        while(num2!=0)
        {
            c=num1&num2;
            num1=num1^num2;
            num2=c<<1;
        }
        return num1;
    }
}
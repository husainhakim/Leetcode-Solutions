class Solution {
public:
    string defangIPaddr(string address) {
        string newadress="";
        for(int i=0;i<address.size();i++)
        {
            
            if (address[i]=='.')
            {
newadress+="[.]";
            }
             else
        {
            newadress+=address[i];
        }
        }
        return newadress;
    }
};


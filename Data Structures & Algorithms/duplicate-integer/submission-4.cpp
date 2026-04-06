class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> yup; // for good time complexity
        for(int num : nums){
            if(yup.count(num)){
                return true;
            }               
            yup.insert(num);
        }

        return false;
    }
};
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        vector<int> checked;

        while (!nums.empty()) {
            int x = nums.back();
            nums.pop_back();

            for (int i = 0; i < checked.size(); ++i) {
                if (checked[i] == x) {
                    return true;
                }
            }

            checked.push_back(x);
        }

        return false;
    }
};

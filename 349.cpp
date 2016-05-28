#include<iostream>
#include<algorithm>
using namespace std;

class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;
	set<int> s(nums2.begin(),nums2.end());
        nums2.assign(s.begin(),s.end()); 
        for(int num:nums1){  
            vector<int>::iterator position=std::find(nums2.begin(),nums2.end(),num);
            if(position!=nums2.end()){
                res.push_back(*position);
                nums2.erase(position);
            }   
        }
        return res;
    }
};

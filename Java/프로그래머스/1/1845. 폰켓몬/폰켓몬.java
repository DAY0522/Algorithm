// 최대한 많은 종류의 폰켓몬 가져가기!

import java.util.*;

class Solution {
    public int solution(int[] nums) {
        Set<Integer> set = new HashSet<>();
        int max = (nums.length)/2;
        
        for(Integer n:nums){
            set.add(n);
        }
        
        int answer = (set.size() >= max)? max: set.size();
        return answer;
    }
}
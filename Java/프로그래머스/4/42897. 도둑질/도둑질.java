import java.util.*;

class Solution {
    public int solution(int[] money) {
        int answer = 0;
        int N = money.length;
        
        if (N<4){
            return Math.max(money[0], Math.max(money[1], money[2]));
        }
        
        int[] dp1 = new int[N]; // 마지막 집을 선택하지 않음(0~N-2)
        int[] dp2 = new int[N]; // 마지막 집을 선택함(1~N-3) + N
        
        dp1[0] = money[0];
        dp1[1] = money[1];
        dp1[2] = money[0] + money[2];
        for (int i=3; i<=N-2; i++){
            dp1[i] = Math.max(dp1[i-2], dp1[i-3]) + money[i];
        }
        
        answer = Math.max(dp1[N-2], dp1[N-3]);
        answer = Math.max(answer, dp1[N-4]);
        
        dp2[1] = money[1];
        dp2[2] = money[2];
        dp2[3] = money[1] + money[3];
        for (int i=4; i<=N-3; i++){
            dp2[i] = Math.max(dp2[i-2], dp2[i-3]) + money[i];
        }
        
        answer = Math.max(answer, dp2[N-3]+money[N-1]);
        answer = Math.max(answer, dp2[N-4]+money[N-1]);
        if (N>4){
            answer = Math.max(answer, dp2[N-5]+money[N-1]);
        }
        
        return answer;
    }
}
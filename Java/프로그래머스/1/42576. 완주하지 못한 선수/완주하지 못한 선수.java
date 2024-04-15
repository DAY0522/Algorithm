import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        Map<String, Integer> map = new HashMap<>();
        for(String name:completion){
            if(map.get(name)==null) map.put(name, 1);
            else{
                int val = map.get(name);
                map.put(name, val+1);
            }
        }
        
        for(String name:participant){
            if(map.get(name)==null) return name;
            else{
                int val = map.get(name);
                if(val<=0) return name;
                map.put(name, val-1);
            }
        }
        
        for(String key: map.keySet()){
            int val = map.get(key);
            System.out.println(key + ": " + val);
        }
        
        return null;
    }
}
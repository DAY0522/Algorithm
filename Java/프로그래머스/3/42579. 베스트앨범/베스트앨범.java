import java.util.*;

class Solution {
    
    static class Music{
        String genre;
        int play;
        int idx;
        
        public Music(String genre, int play, int idx){
            this.genre = genre;
            this.play = play;
            this.idx = idx;
        }
    }
    
    public int[] solution(String[] genres, int[] plays) {
        
        ArrayList<Integer> answer = new ArrayList<>();
        HashMap<String, Integer> map = new HashMap<>();
        for(int i=0;i<genres.length;i++){
            map.put(genres[i], map.getOrDefault(genres[i], 0)+plays[i]);
        }
        
        ArrayList<String> arr = new ArrayList<>();
        for(String g:map.keySet()){
            arr.add(g);
        }
        arr.sort((g1, g2)->map.get(g2)-map.get(g1));
        
        ArrayList<Music> music = new ArrayList<>();
        for(String g:arr){
            ArrayList<Music> genre_music = new ArrayList<>(); // 장르가 동일한 music list
            for(int i=0; i<genres.length; i++){
                if (genres[i].equals(g)){ // 현재 장르와 동일한 경우
                    genre_music.add(new Music(g, plays[i], i));
                }
            }
            genre_music.sort((m1, m2)->m2.play-m1.play); // play 내림차순으로 정렬
            answer.add(genre_music.get(0).idx);
            if(genre_music.size()>1){
                answer.add(genre_music.get(1).idx);
            }
        }
        
        // System.out.println(answer);
        return answer.stream().mapToInt(i->i).toArray();
    }
}
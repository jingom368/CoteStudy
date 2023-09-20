import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = {(int) Arrays.stream(num_list).filter(s->s%2==0).count(),(int) Arrays.stream(num_list).filter(s->s%2!=0).count()};
        return answer;
    }
}


// answer = [[0 if i%2==0 else 1 for i in num_list].count(0),[0 if i%2==0 else 1 for i in num_list].count(1)]
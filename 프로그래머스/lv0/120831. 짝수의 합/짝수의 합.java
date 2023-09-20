import java.util.stream.IntStream;

class Solution {
    public int solution(int n) {
        return IntStream.rangeClosed(0,n)
                .filter(s->s%2==0)
                .sum();

    }
}
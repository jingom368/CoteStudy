import java.util.Arrays;

class Solution {
    public int solution(int[] sides) {
        Arrays.sort(sides);
        return sides[0] + sides[1] > sides[2] ? 1 : 2;
    }
}

// answer = [1 if sorted(sides)[0] + sorted(sides)[1] > sorted(sides)[2] else 2][0]
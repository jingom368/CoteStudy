class Solution {
    public int solution(int[] dot) {
        return dot[0]>0 && dot[1]>0 ? 1 : dot[0]<0 && dot[1]>0 ? 2 : dot[0]<0 && dot[1]<0 ? 3 : 4;
    }
}

// answer = [1 if dot[0]>0 and dot[1]>0 else 2 if dot[0]<0 and dot[1]>0 else 3 if dot[0]<0 and dot[1]<0 else 4][0]


// class Solution {
//     public int solution(int[] dot) {
//         return dot[0] > 0 && dot[1] > 0 ? 1 : dot[0] < 0 && dot[1] > 0 ? 2 : dot[0] > 0 && dot[1] < 0 ? 4 : 3;
//     }
// }
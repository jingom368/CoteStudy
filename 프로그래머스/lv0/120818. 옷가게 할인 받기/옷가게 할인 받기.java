class Solution {
    public int solution(int price) {
        int answer = 0;
        if (price >= 10 && price < 100000)
            answer = (int) (price);
        if (price >= 100000 && price < 300000)
            answer = (int) (price*(1-0.05));
        if (price >= 300000 && price < 500000)
            answer = (int) (price*(1-0.1));
        if (price >= 500000)
            answer = (int) (price*(1-0.2));
        return answer;
    }
}

    // discount = [0,0.05,0.1,0.2]
    // i=0
    // if price >=10 and price < 100000:
    //     i=0
    // elif price>=100000 and price<300000:
    //     i=1
    // elif price>=300000 and price<500000:
    //     i=2
    // else:
    //     i=3
    // answer = int(price*(1-discount[i]))
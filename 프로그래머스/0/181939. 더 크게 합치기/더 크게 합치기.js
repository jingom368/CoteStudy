function solution(a, b) {
    var answer = Math.max(a.toString()+b.toString(), b.toString()+a.toString())
    return answer;
}
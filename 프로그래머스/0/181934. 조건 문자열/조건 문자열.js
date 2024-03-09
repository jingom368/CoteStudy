function solution(ineq, eq, n, m) {
    if (ineq+eq === "<=") {
        answer = Number(n <= m)
    } else if (ineq+eq === ">=") {
        answer = Number(n >= m)
    } else if (ineq+eq === "<!") {
        answer = Number(n < m)
    } else {
        answer = Number(n > m)
    }
    return answer;
}
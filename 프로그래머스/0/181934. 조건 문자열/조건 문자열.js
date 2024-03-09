// function solution(ineq, eq, n, m) {
//     if (ineq+eq === "<=") {
//         answer = Number(n <= m)
//     } else if (ineq+eq === ">=") {
//         answer = Number(n >= m)
//     } else if (ineq+eq === "<!") {
//         answer = Number(n < m)
//     } else {
//         answer = Number(n > m)
//     }
//     return answer;
// }


const operations = {
  '>=': (n, m) => n >= m,
  '<=': (n, m) => n <= m,
  '>!': (n, m) => n > m,
  '<!': (n, m) => n < m,
};

function solution(ineq, eq, n, m) {
  const op = operations[ineq + eq];
  return Number(op(n, m));
}

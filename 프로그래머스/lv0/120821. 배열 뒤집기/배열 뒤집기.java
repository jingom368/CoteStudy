import java.util.*;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
        // int[] answer = new int[num_list.length];
        // for (int i=0; i<num_list.length; i++) {
        //     answer[i] = num_list[num_list.length-1-i];
        // }
        // return answer;
        
        List<Integer> list = Arrays.stream(num_list).boxed().collect(Collectors.toList());
        // boxed() 메소드는 IntStream 같이 원시 타입에 대한 스트림 지원을 클래스 타입(예: IntStream -> Stream<Integer>)으로 전환하여 전용으로 실행 가능한 (예를 들어 본문과 같이 int 자체로는 Collection에 못 담기 때문에 Integer 클래스로 변환하여 List<Integer> 로 담기 위해 등) 기능을 수행하기 위해 존재합니다.
        // Collectors란 "Stream을 일반적인 List, Set등으로 변경시키는 Stream 메서드"라고 입니다.

        Collections.reverse(list);
        // Collections.reverse : 배열을 반대로 해주는
        return list.stream().mapToInt(Integer::intValue).toArray();
        // mapToInt는 Stream<T>타입의 스트림을 기본형 스트림으로 변환할때 아래의 메서드들을 사용한다.
    }
}

// answer = list(reversed(num_list))
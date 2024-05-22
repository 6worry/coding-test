// 문제
// 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

// 입력
// 첫째 줄에 테스트 케이스의 개수 T가 주어진다.

// 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

// 출력
// 각 테스트 케이스마다 A+B를 출력한다.

// 예제 입력
// 5
// 1 1
// 2 3
// 3 4
// 9 8
// 5 2
// 예제 출력 
// 2
// 5
// 7
// 17
// 7

import java.util.Scanner;

class Main {
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        
        for(int i = 0; i < num; i++) {
            int A = sc.nextInt();
            int B = sc.nextInt();

            System.out.println(A + B);
        }

        sc.close();
    }
}

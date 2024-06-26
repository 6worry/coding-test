// 하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.


// [제약 사항]

// 자연수 N은 1부터 9999까지의 자연수이다. (1 ≤ N ≤ 9999)


// [입력]

// 입력으로 자연수 N이 주어진다.


// [출력]

// 각 자릿수의 합을 출력한다.

// 입력
// 6789

// 출력
// 30


import java.util.Scanner;
 
class Solution {
    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();
        int result = 0;
 
        String str = Integer.toString(T);
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            result += Character.getNumericValue(c);
        }
 
        System.out.println(result);

        sc.close();
    }
}
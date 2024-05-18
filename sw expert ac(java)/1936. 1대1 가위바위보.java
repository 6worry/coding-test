// A와 B가 가위바위보를 하였다.

// 가위는 1, 바위는 2, 보는 3으로 표현되며 A와 B가 무엇을 냈는지 입력으로 주어진다.

// A와 B중에 누가 이겼는지 판별해보자. 단, 비기는 경우는 없다.

 

// [입력]

// 입력으로 A와 B가 무엇을 냈는지 빈 칸을 사이로 주어진다.

 
 

// [출력]

// A가 이기면 A, B가 이기면 B를 출력한다.

// 입력
// 3 2

// 출력
// A

import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		int T2;
		T2=sc.nextInt();
        
		if(T == (T2 + 1)) {
            System.out.println("A");
        } else if(T == (T2 + 2)) {
            System.out.println("B");
        }
        
        if(T2 == (T + 1)) {
            System.out.println("B");
        } else if(T2 == (T + 2)) {
            System.out.println("A");
        }
	}
}
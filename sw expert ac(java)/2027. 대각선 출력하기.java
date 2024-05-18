// 주어진 텍스트를 그대로 출력하세요.
 

// 입력
// 출력
// #++++
// +#+++
// ++#++
// +++#+
// ++++#

import java.util.Scanner;
import java.io.FileInputStream;

class Solution {
	public static void main(String args[]) throws Exception {
        int size = 5;
        
        for(int i = 0; i < size; i++){
            for(int j = 0; j < size; j++){
                if(i == j) {
                    System.out.print("#");
                } else {
                    System.out.print("+");
                }
            }
            
            System.out.println();
        }
	}
}
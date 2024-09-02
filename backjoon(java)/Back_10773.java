import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(br.readLine());
        Stack<Integer> st = new Stack<>();

        for (int i = 0; i < k; i++) {
            int num = Integer.parseInt(br.readLine());

            if(num == 0) {
                if(!st.isEmpty()) {
                    st.pop();
                }
            } else {
                st.push(num);
            }
        }

        int sum = 0;

        for (int num : st) {
            sum += num;
        }

        System.out.println(sum);
    }
}
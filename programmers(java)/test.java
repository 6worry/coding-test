import java.util.Arrays;

class Solution {
    public long solution(int n, int[] works) {
        long answer = 0;

        for(int i = 0; i < n; i++) {
            Arrays.sort(works);

            if(works[works.length - 1] == 0) {
                break;
            }

            works[works.length - 1]--;
        }

        for(int work: works) {
            answer += Math.pow(work, 2);
        }

        return answer;
    }
}
class Solution {
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        int[] score = new int[8];

        for(int i = 0; i < survey.length; i++) {
            String s = survey[i];
            int choice = choices[i];

            int index = s.charAt(0) - 'A';
            int index2 = s.charAt(1) - 'A' + 4;

            if(choice > 4) {
                score[index2] += (choice - 4);
            } else if(choice < 4) {
                score[index] += (4 - choice);
            }
        }

        answer += (score[0] >= score[1]) ? "R" : "T";
        answer += (score[2] >= score[3]) ? "C" : "F";
        answer += (score[4] >= score[5]) ? "J" : "M";
        answer += (score[6] >= score[7]) ? "A" : "N";

        return answer;
    }
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution(new String[]{"AN", "CF", "MJ", "RT", "NA"}, new int[]{5, 3, 2, 7, 5})); // "TCMA"
        System.out.println(sol.solution(new String[]{"TR", "RT", "TR"}, new int[]{7, 1, 3})); // "RCJA"
    }
}
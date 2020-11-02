class Solution {
    public int solution(int N) {
        // write your code in Java SE 8
        String s = Integer.toBinaryString(N);
         
        if (s.indexOf("0") > 0) {
            int count = 0;
            int max = 0;
             
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '0') {
                    count++;    
                } else if (s.charAt(i) == '1') {
                    if (count > max) {
                        max = count;
                    }
                    count = 0;
                }
            }
            return max;
        }
        return 0;
    }
}
class Solution {
    public int[] solution(int[] A, int K) {
        // write your code in Java SE 8
        int len = A.length;
        int[] B = new int[len];
        
        for (int i=0; i<len; i++) {
            int index = i+K; 
            
            while (index >= len) {
                index -= len;
            } 
            
            B[index] = A[i];
            index = 0;
        }
        
        return B;
    }
}
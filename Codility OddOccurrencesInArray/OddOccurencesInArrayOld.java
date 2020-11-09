class Solution {
    public int solution(int[] A) {
        // Loop through the array
        for (int i=0; i < A.length; i++) {
            //Initialise count to 0
            int count = 0;
            
            //Do another loop and check how many occurences of number in loop
            for (int j = 0; j < A.length; j++) {
                if (A[i] == A[j]) {
                    count++;
                }
            }
            
            //If count is 1 or less return A[i]
            if (count <= 1) {
                return A[i];
            }
        }
        //Something went wrong
        return -1;
    }
}

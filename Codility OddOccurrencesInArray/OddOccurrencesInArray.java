class Solution {
    public int solution(int[] A) {
        //We sort Array in alphabetical order
        Arrays.sort(A);
        for (int i = 0; i < A.length; i++) {
            //If we are reaching end of loop and no odd occurences 
            //then it will be the last number with the odd occurence
            if (i == A.length-1) {
                return A[i];
            }
            
            //If this number and next number are same then skip next number
            //Else if they aren't then return current number as it does not have a pair
            if (A[i] == A[i+1]) {
                i += 1;
            } else if (A[i] != A[i+1]) {
                return A[i];
            }
        }       
        return 0;
    }
}
// Solutions to daily coding problem emails
import java.util.*;

public class DailyCodingProblem {

    public static void main(String[] args){
        int[] arr = {2, 3, 10, 5, 7};
        System.out.println(twoSum(arr, 17));
    }

    /**
     * 4-4-20 code problem
     * @param arr the array
     * @param targ the target number
     * @return true if two numbers in an array sum to a target
     */
    public static boolean twoSum(int[] arr, int targ){
        //O(n^2) solution, O(1) space
        /*
        for(int i = 0; i < arr.length; i++){
            for(int j = i; j < arr.length; j++){
                if(arr[i] + arr[j] == targ){
                    return true;
                }
            }
        }
        */

        // Handle edge cases
        if(arr.length <= 1){
            return false;
        }

        /*
        Hashmap solution - O(n) both because O(1) accesses
        
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < arr.length; i++){
            map.put(arr[i], targ - arr[i]);
            if(map.containsKey(targ - arr[i])){
                System.out.println("Hashmap found solution");
                return true;
            }
        }
         */

        //O(n) space, O(n) time
        //0 default array of length target
        int[] values = new int[targ];
        for(int i = 0; i < arr.length; i++){
            values[arr[i] - 1] = 1; // Put the value in the array for O(1) access
            int goal = targ - arr[i]; // Get "second half" of number
            if(values[goal - 1] != 0){ // If second half is in the array
                return true;
            }
        }
        return false;
    }
}

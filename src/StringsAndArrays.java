import java.util.*;

/**
 * Class for chapter 1 of CTCI - strings and arrays
 */
public class StringsAndArrays {

    /**
     * Main method
     * @param args command line arguments
     */
    public static void main(String[] args) {
        System.out.println(palindromePermutation("atco cta"));
        System.out.println(compress("aabcccccaaa"));
    }

    /**
     * 1.1 - String uniqueness
     * @param s the string
     * @return true if s has only unique characters
     */
    public static boolean isUnique(String s){
        // O(n) time, O(n) space
        HashMap<Character, Integer> map = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            if(map.containsKey(s.charAt(i))){
                return false;
            }
            else{
                map.put(s.charAt(i), 1);
            }
        }

        //O(n^2) solution, O(1) space
        /*
        for(int i = 0; i < s.length() - 1; i++){
            for(int j = i + 1; j < s.length(); j++){
                if(s.charAt(i) == s.charAt(j)){
                    return false;
                }
            }
        }
         */
        return true;
    }

    /**
     * 1.2 - check if a is a permutation of b
     * @param a first string
     * @param b second string
     * @return true if a and b are permutations
     */
    public static boolean isPermutation(String a, String b){
        // O(n + m) time and space
        if(a.length() != b.length()){
            return false; // Short cut
        }

        HashMap<Character, Integer> map = new HashMap<>();
        HashMap<Character, Integer> map2 = new HashMap<>();

        for(int i = 0; i < a.length(); i++){
            if(!map.containsKey(a.charAt(i))){
                map.put(a.charAt(i), 1);
            }
            else{
                map.put(a.charAt(i), map.get(a.charAt(i)) + 1);
            }
        }

        for(int i = 0; i < b.length(); i++){
            if(!map2.containsKey(b.charAt(i))){
                map2.put(b.charAt(i), 1);
            }
            else{
                map2.put(b.charAt(i), map2.get(b.charAt(i)) + 1);
            }
        }

        Set<Map.Entry<Character, Integer>> set1 = map.entrySet();
        Set<Map.Entry<Character, Integer>> set2 = map2.entrySet();
        return set1.equals(set2);
    }

    /**
     * 1.3 - turn string into URL
     * @param s the string
     * @return a URL version of the string
     */
    public static String urlIfy(String s){
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == ' '){
                String s1 = s.substring(0, i);
                String s2= s.substring(i+1, s.length());
                s = s1 + "%20" + s2;
            }
        }
        return s;
    }


    /**
     * 1.4 - Check if a string is a permutation of a palindrome
     * @param s the string
     * @return true if s is a permutation of a palindrome
     */
    public static boolean palindromePermutation(String s){
        // O(n) time and space
        // Replace spaces
        s = s.replace(" ", "");
        HashMap<Character, Integer> map = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            if(map.containsKey(s.charAt(i))){
                map.put(s.charAt(i), map.get(s.charAt(i)) + 1);
            }
            else {
                map.put(s.charAt(i), 1);
            }
        }

        // Palindrome can only have 1 or 0 odd characters
        int oddCount = 0;
        for(Map.Entry<Character, Integer> entry : map.entrySet()){
            if(entry.getValue() % 2 == 1){
                oddCount++;
            }
        }

        return oddCount <= 1 ? true : false;
    }

    /**
     * 1.5 - one away
     * Check if a string can be made by one edit
     * @param a original string
     * @param b target string
     * @return true if string can be reached by one edit
     */
    public static boolean oneAway(String a, String b){
        if(Math.abs(a.length() - b.length()) > 1){
            return false; // Different lengths
        }

        // Check for replacement
        int i = 0;
        while(i < a.length() && i < b.length() && a.charAt(i) == b.charAt(i)){
            i++;
        }
        String result = null;

        // replacement
        if(a.length() == b.length()){
            System.out.print("Replaced: ");
            result = a.replace(a.charAt(i), b.charAt(i));
        }

        // insertion
        else if(a.length() < b.length()){
            System.out.print("Inserted: ");
            result = a.substring(0, i) + String.valueOf(b.charAt(i)) + a.substring(i);
        }

        // deletion
        else if(a.length() > b.length()){
            System.out.print("Deleted: ");
            result = a.substring(0, i) + a.substring(i + 1);
        }

        System.out.println(result + " " + result.equals(b));

        if(result.equals(b)){
            return true;
        }
        return false;
    }

    /**
     * 1.6 - String compression
     * Return a string with counts of letters instead of actual letters
     * @param s the string to be compressed
     * @return the compressed string, or the original string if the length is equal
     */
    public static String compress(String s){
        // Error checks
        if(s == null){
            return null;
        }
        else if(s.length() <= 1){
            return s;
        }

        // O(n) time
        String ret = "";
        int temp = 1;
        char current = s.charAt(0);
        for(int i = 1; i < s.length(); i++){
            if(s.charAt(i) == current){
                temp++;
            }
            else{
                ret += String.valueOf(current) + temp;
                temp = 1;
            }
            // Update current character
            current = s.charAt(i);
        }
        // Add the extra at the very end
        ret += String.valueOf(current) + temp;
        return ret.length() >= s.length() ? s : ret;
    }

    /**
     * 1.7 - Rotate NxN matrix 90 degrees
     * @param mat the matrix
     * @return the rotated matrix
     */
    public int[][] rotateMatrix(int[][] mat){
        int[][] newMat = new int[mat.length][mat.length];

        for(int i = mat.length - 1; i >= 0; i--){
            int[] temp = mat[i];
            for(int j = 0; j < mat.length; j++){
                newMat[j][mat.length - i - 1] = temp[j];
            }
        }

        for(int i = 0; i < newMat.length; i++){
            System.out.println(Arrays.toString(newMat[i]));
        }

        return newMat;
    }

    /**
     * 1.8 - Zero matrix
     * Return a matrix where every 0 fills the row and column with 0's
     * @param mat the matrix
     * @return the zeroed matrix
     */
    public int[][] zeroMatrix(int[][] mat){
        int[][] newMat = mat.clone();

        ArrayList<Integer> columnsChanged = new ArrayList<>();

        for(int i = 0; i < mat.length; i++){
            for(int j = 0; j < mat.length; j++){
                if(mat[i][j] == 0){
                    newMat[i] = new int[mat.length]; // new array of zeroes
                    columnsChanged.add(i);
                }
            }
        }

        for(int i = 0; i < mat.length; i++){
            for(int j = 0; j < columnsChanged.size(); j++){
                newMat[i][columnsChanged.get(j)] = 0;
            }
        }

        for(int i = 0; i < newMat.length; i++){
            System.out.println(Arrays.toString(newMat[i]));
        }

        return newMat;
    }

    /**
     * 1.9 - Check for rotated substrings
     * @param a the original string
     * @param b the rotated string
     * @return true if a is a substring of b rotated
     */
    public boolean isRotatedSubstring(String a, String b){
        // Continue rotating A to get a substring in B
        int count = 0;
        while(count < a.length()){
            if(b.contains(a)){ // Lmao called contains but still counts
                return true;
            }
            char temp = a.charAt(0);
            a = a.substring(1, a.length());
            a += temp;
            count++;
        }
        return false;
    }
}

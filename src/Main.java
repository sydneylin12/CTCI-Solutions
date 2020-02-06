
import java.util.*;


public class Main {

    public static void main(String[] args) {
        System.out.println("Hello World!");
        Main m = new Main();
        //System.out.println(m.isUnique("abc"));
        //System.out.println(m.isUnique("aabc"));
        //m.isPermutation("racecar", "rreccaa");
        //m.urlIfy("Mr 3ohn Smith");
        m.oneAway("pale", "bale"); //True
        m.oneAway("pale", "ple"); //True
        m.oneAway("pale", "ale"); //True
        m.oneAway("a", "b"); //True
        m.oneAway("false", "true"); //False
        m.oneAway("pickle", "pickl"); //
    }

    // 1.1, does a string have all unique  O(n)
    public boolean isUnique(String s){
        HashMap<Character, Integer> map = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            // If the char is in the map
            if(map.containsKey(s.charAt(i))){
                // Can default to returning because it is not unique
                return false;
            }
            else{
                map.put(s.charAt(i), 1);
            }
        }
        return true;
    }

    // 1.2, check if 2 strings are permutations of each other O(n)
    public boolean isPermutation(String a, String b){
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
        System.out.println("Permutation result: " + set1.equals(set2));
        return set1.equals(set2);
    }

    // 1.3 URLify - does not use java default replace
    public String urlIfy(String s){
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == ' '){
                String s1 = s.substring(0, i);
                String s2= s.substring(i+1, s.length());
                //System.out.println(s1 + "%20" + s2);
                s = s1 + "%20" + s2;
            }
        }
        System.out.println("New URL: " + s);
        return s;
    }

    // 1.5 One away - is a string one edit away
    // Can insert, remove, and replace
    public boolean oneAway(String a, String b){
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


}

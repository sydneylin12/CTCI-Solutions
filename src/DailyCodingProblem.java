import java.util.*;

/**
 * Daily coding problem solutions
 */
public class DailyCodingProblem {

    /**
     * Main method for doing daily coding problems
     * @param args command line arguments
     */
    public static void main(String[] args){
        //int[] arr = {2, 3, 10, 5, 7};
        //System.out.println(twoSum(arr, 17));
        //int[] arr = {1, 2, 3, 4, 5};
        //allProduct(arr);
        //TreeNode<String> node = new TreeNode("Root", new TreeNode("Left", new TreeNode("Left.Left"), null), new TreeNode("Right"));
        //String ser = serialize(node);
        //System.out.println(ser);
        //TreeNode<String> des = deserialize(ser);
        //System.out.println(des.left.left.data);
        //System.out.println(missingPositive(new int[] {3, 4, -1, 1, 1, 1, 1}));
        //System.out.println(encoding("1313"));

        //TreeNode<Integer> root = new TreeNode<>(0, new TreeNode<>(1), new TreeNode<>(0,
                //new TreeNode<>(1, new TreeNode<>(1), new TreeNode<>(1)), new TreeNode<>(0)));
        //System.out.println(univalTree(root));
        System.out.println(nonAdjacentSum(new int[] {5, 1, 1, 5}));
    }

    /**
     * Problem 1 - two sum
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

    /**
     * Problem 2 - product of all array integers
     * @param arr an array of integers
     * @return a new array with each element as the product of all other elements except itself
     */
    public static int[] allProduct(int[] arr){
        // Solution that uses division
        // O(n) runtime, O(n) space complexity
        int[] ret = new int[arr.length];
        int prod = 1;
        for(int i = 0; i < arr.length; i++){
            prod *= arr[i];
        }
        for(int i = 0; i < arr.length; i++){
            ret[i] = prod/arr[i];
        }
        System.out.println("Division solution: " + Arrays.toString(ret));

        //O(n^2) time, O(1) space
        for(int i = 0; i < arr.length; i++){
            int temp = 1;
            for(int j = 0; j < arr.length; j++){
                if(j != i){
                    temp *= arr[j];
                }
            }
            ret[i] = temp;
        }
        System.out.println("No division solution: " + Arrays.toString(ret));
        return ret;
    }

    /**
     * Problem 3, part a
     * @param root the root node/passed in node
     * @return a string representation of the tree
     */
    public static String serialize(TreeNode root){
        // Runs in O(n)
        // Return if null, error handling
        if(root == null){
            return null;
        }

        // Create string representation of node starting with root.data
        String s = root.data.toString();
        // Separate with commas for same node
        if(root.left != null){
            s += "," + root.left.data;
        }
        else{
            s += "," + null;
        }
        if(root.right != null){
            s += "," + root.right.data;
        }
        else {
            s += "," + null;
        }

        // Separate nodes with dashes for different nodes
        if(root.left != null){
            s += "-" + serialize(root.left);
        }
        if(root.right != null){
            s += "-" + serialize(root.right);
        }
        return s;
    }

    /**
     * Problem 3 part b
     * @param s the string to be deserialized
     * @return a node/tree made from the string
     */
    public static TreeNode<String> deserialize(String s){
        // Runs in I think O(n^2) - create each new node n times and search arrays n times
        String[] nodes = s.split("-");
        String[][] convertedNodes = new String[nodes.length][3];

        // Error check
        if(nodes.length == 0){
            return null;
        }

        // Convert into 2D array with 3 elements (data left right)
        for(int i = 0; i < nodes.length; i++){
            convertedNodes[i] = nodes[i].split(",");
        }

        // Get the first node
        String data = convertedNodes[0][0];
        String left = convertedNodes[0][1];
        String right = convertedNodes[0][2];

        int leftIdx = -1;
        int rightIdx = -1;

        for(int i = 0; i < convertedNodes.length; i++){
            // Find left child unique index
            if(left.equals(convertedNodes[i][0])){
                leftIdx = i;
            }
            if(right.equals(convertedNodes[i][0])){
                rightIdx = i;
            }
        }

        TreeNode<String> newLeft = null;
        TreeNode<String> newRight = null;

        // If we can find the indexes
        if(leftIdx != -1){
            String leftSubtree = String.join("-", Arrays.copyOfRange(nodes, leftIdx, nodes.length));
            newLeft = deserialize(leftSubtree);
        }
        if(rightIdx != -1){
            String rightSubtree = String.join("-", Arrays.copyOfRange(nodes, rightIdx, nodes.length));
            newRight = deserialize(rightSubtree);
        }

        // Initialize a node with either null or recursive call
        TreeNode<String> root = new TreeNode<>(data, newLeft, newRight);
        return root;
    }

    /**
     * Problem 4
     * Find the first missing positive integer in O(n) time and O(1) space
     * Did not really understand this one
     * Needed help on this one
     * @param arr the array with one missing positive integer
     * @return the missing positive integer
     */
    public static int missingPositive(int[] arr){
        // The array can have at most n positive integers
        // Find each integer's correct position and swap it there
        int i = 0;
        while(i < arr.length){
            // Swap if integer is not in position
            if(arr[i] > 0 && arr[i] <= arr.length && arr[arr[i] - 1] != arr[i]){
                swap(arr, i, arr[i] - 1);
                System.out.println(Arrays.toString(arr));
            }
            else{
                i++;
            }
        }
        i = 0;
        while(i < arr.length && arr[i] == i + 1){
            i++;
        }
        return i + 1;
    }

    /**
     * Helper swap method for problem 4
     * @param arr the array
     * @param i first index
     * @param j second index
     */
    public static void swap(int[] arr, int i, int j){
        int temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
    }

    /**
     * Problem 7 - string encoding
     * For mapping 1 = a, 2 = b, ... 26 = z
     * Return the number of ways a string can be encoded
     * @param s the string to be encoded
     */
    public static int encoding(String s){
        // Base case if we eliminate all substrings
        if(s.length() == 0){
            return 1;
        }

        String temp = String.valueOf(s.charAt(0));
        int firstPath = 0;
        int secondPath = 0;
        int firstInt = Integer.parseInt(temp);
        int firstTwo = 0;

        // Can always parse first digit here
        //System.out.println("First substring: " + s.substring(1));
        if(firstInt > 0 && firstInt < 10){
            firstPath = encoding(s.substring(1));
        }

        // Can parse second digit
        if(s.length() > 1){
            //System.out.println("Second substring: " + s.substring(2));
            firstTwo = Integer.parseInt(s.substring(0, 2));
            // Safety check for proper encoding
            if(firstTwo > 9 && firstTwo < 27){
                secondPath = encoding(s.substring(2));
            }
        }
        return firstPath + secondPath;
    }

    /**
     * Problem 8 - unival tree
     * Return number of trees where all nodes under it have the same value
     * @param t
     * @return
     */
    public static int univalTree(TreeNode<Integer> t){
        if(t == null){
            return 0;
        }
        // If the root is a unival tree
        if(isUnival(t)){
            return 1 + univalTree(t.left) + univalTree(t.right);
        }
        else{
            return univalTree(t.left) + univalTree(t.right);
        }
    }

    /**
     * Helper method for problem 8
     * Checks if a tree is a unival tree by traversal
     * @param t
     * @return
     */
    public static boolean isUnival(TreeNode<Integer> t){
        // Edge cases
        if(t == null){
            return true;
        }
        else if(t.left == null && t.right == null){
            return true;
        }
        // Left subtree
        else if(t.left != null && t.right == null){
            return t.data == t.left.data && isUnival(t.left);
        }
        // Right subtree
        else if(t.left == null && t.right != null){
            return t.data == t.right.data && isUnival(t.right);
        }
        // Both subtrees
        else{
            return t.data == t.left.data && t.data == t.right.data && isUnival(t.left) && isUnival(t.right);
        }
    }

    /**
     * Problem 9 - sum of non adj. integers
     * My solution - O(n^2) time and O(n) space
     * @param arr the array of integers
     * @return the largest sum of non adjacent numbers
     */
    public static int nonAdjacentSum(int[] arr) {
        //int sum = 0;
        /*
        int[] values = new int[arr.length];
        int[] indices = new int[arr.length];

        // Initialize the lists - O(n)
        for(int i = 0 ; i < arr.length; i++){
            indices[i] = i;
            values[i] = arr[i];
        }

        // Use selection sort to swap values to sorted order - O(n^2)
        for(int i = 0; i < values.length; i++){
            for(int j = i; j < values.length; j++){
                // Swap if greater
                if(values[j] > values[i]){
                    int temp = values[i];
                    values[i] = values[j];
                    values[j] = temp;

                    int tempIdx = indices[i];
                    indices[i] = indices[j];
                    indices[j] = tempIdx;
                }
            }
        }

        // Sum up - O(n)
        LinkedList<Integer> used = new LinkedList<>();
        for(int i = 0; i < values.length; i++){
            // Check for adjacent indices and continue if so
            if(used.contains(indices[i] - 1) || used.contains(indices[i] + 1)){
                continue;
            }
            else{
                sum += values[i];
                used.add(indices[i]);
            }
        }
         */

        // G4G solution
        int incl = arr[0]; // Maximum sum when last element is included
        int excl = 0; // Maximum sum when last element is excluded
        int newExcl = 0; // Placeholder

        // Loop once in O(n) time
        for(int i = 1; i < arr.length; i++){
            System.out.println(incl);
            System.out.println(excl);

            // Exclude the current element and possibly add its neighbor
            if(incl > excl){
                newExcl = incl;
            }
            else{
                newExcl = excl;
            }

            incl = excl + arr[i];
            excl = newExcl;
        }

        return incl > excl ? incl : excl;
    }
}
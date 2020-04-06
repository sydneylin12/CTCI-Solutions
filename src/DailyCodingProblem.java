// Solutions to daily coding problem emails

import java.util.*;

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
        TreeNode<String> node = new TreeNode("Root", new TreeNode("Left", new TreeNode("Left.Left"), null), new TreeNode("Right"));
        String ser = serialize(node);
        System.out.println(ser);
        TreeNode<String> des = deserialize(ser);
        System.out.println(des.left.left.data);
    }

    /**
     * Problem 1
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
     * Problem 2
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
}

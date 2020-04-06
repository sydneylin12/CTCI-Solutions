
import java.util.*;

/**
 * Binary tree class
 * @param <T> abstract data type
 */
public class BinaryTree<T extends Comparable> {

    public TreeNode<T> root;
    public MyList<MyList<T>> depths;

    /**
     * Binary tree default constructor
     */
    public BinaryTree(){
        root = null;
        depths = new MyList<MyList<T>>();
    }

    /**
     * Binary SEARCH tree add function
     * @param data the data to be added (not a node)
     */
    public void add(T data){
        if(this.root == null){
            this.root = new TreeNode<T>(data);
        }

        TreeNode<T> current = this.root;
        while(current != null){
            // Same data in the tree cannot be added twice
            if(current.data.compareTo(data) == 0){
                return;
            }
            // Current is less, go right
            else if(current.data.compareTo(data) < 0){
                if(current.right == null){
                    current.right = new TreeNode<T>(data);
                }
                else{
                    current = current.right;
                }
            }
            // Current is greater, go left
            else{
                if(current.left == null){
                    current.left = new TreeNode<T>(data);
                }
                else{
                    current = current.left;
                }
            }
        }
    }

    /**
     * Main method for binary tree problems
     * @param args command line arguments
     */
    public static void main(String[] args){
        BinaryTree<Integer> binaryTree = new BinaryTree<>();
        Integer[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        binaryTree.root = binaryTree.minimalTree(arr);
        System.out.println("Balanced: " + binaryTree.isBalanced(binaryTree.root));

        // Testing subtree method
        TreeNode<Integer> t1 = new TreeNode<>(1, new TreeNode(2, new TreeNode(3), null), null);
        TreeNode<Integer> t2 = new TreeNode<>(1, new TreeNode(2, new TreeNode(3), null), null);
        TreeNode<Integer> t3 = new TreeNode<>(1, new TreeNode(2, new TreeNode(4), null), null);
        TreeNode<Integer> t4 = new TreeNode<>(0, new TreeNode<>(1, new TreeNode(2, new TreeNode(3), null), null), null);

        //System.out.println(binaryTree.isSubtree(t1, t2));
        //System.out.println(binaryTree.isSubtree(t1, t3));
        //System.out.println(binaryTree.isSubtree(t4, t1));

        BinaryTree<Integer> b1 = new BinaryTree<>();
        b1.add(5);
        b1.add(2);
        b1.add(7);
        b1.add(6);
        b1.add(9);
        b1.add(1);

        MyList<MyList<Integer>> levels = new MyList<>();
        MyList<MyList<Integer>> list = b1.addToList(b1.root, 1, levels);

        for(int i = 0; i < levels.size(); i++){
            System.out.println(levels.get(i).size());
        }

        System.out.println(b1.validate(b1.root));
    }

    /**
     * Level order traversal from root node
     * @param root the root node
     */
    public void levelOrder(TreeNode root){
        int h = height(root);
        for(int i = 1; i <= h; i++){
            printLevel(root, i);
        }
    }

    /**
     * Calculate height of tree node
     * @param root a node
     * @return
     */
    int height(TreeNode root)
    {
        if (root == null)
            return 0;
        else
        {
            int lHeight = height(root.left);
            int rHeight = height(root.right);
            if (lHeight > rHeight){
                return(lHeight+1);
            }
            else{
                return(rHeight+1);
            }
        }
    }

    /**
     * Print a node at a given level when level = 1
     * @param root the root node
     * @param level the level of the node
     */
    void printLevel (TreeNode root ,int level)
    {
        if (root == null){
            return;
        }
        if (level == 1){
            System.out.println(root.data + " ");
        }
        else if (level > 1)
        {
            printLevel(root.left, level-1);
            printLevel(root.right, level-1);
        }
    }

    /**
     * 4.2 - construct a minimal tree with a sorted array
     * @param arr sorted array of integers
     * @return root node of a minimal tree
     */
    public TreeNode<T> minimalTree(T[] arr){
        if(arr.length == 0){
            return null;
        }
        else if(arr.length == 1){
            //System.out.println("Returning: " + arr[0]);
            return new TreeNode(arr[0]);
        }
        else{
            // Find the middle of the array (balanced tree)
            int midpoint = (arr.length-1)/2;
            TreeNode<T> newNode = new TreeNode<>(arr[midpoint]);

            if(midpoint > 0){
                T[] left = Arrays.copyOfRange(arr, 0, midpoint);
                newNode.left = minimalTree(left);
            }

            if(midpoint < arr.length - 1){
                T[] right = Arrays.copyOfRange(arr, midpoint+1, arr.length);
                newNode.right = minimalTree(right);
            }
            return newNode;
        }
    }

    /**
     * 4.3 - list of depths, return linked list for each level of tree
     * @param root the root node
     * @return 2D linked list of depths and node data
     */
    public MyList<MyList<T>> addToList(TreeNode<T> root, int level, MyList<MyList<T>> levels){
        /*
        if(root == null){
            return null;
        }
        if(levels.size() != level){
            System.out.println("Adding new list");
            LinkedList<T> temp = new LinkedList<>();
            temp.add(root.data);
            levels.add(temp);
        }
        else{
            System.out.println("Getting current level");
            levels.get(level).add(root.data);
        }

        addToList(root.left, level + 1, levels);
        addToList(root.right, level + 1, levels);
        return levels;
        */
        return null;
    }

    /**
     * 4.4 - check if a tree is balanced
     * @param root the root node
     * @return true if the tree is balanced
     */
    public boolean isBalanced(TreeNode root){
        if(root == null){
            return true;
        }
        if(Math.abs(height(root.left) - height(root.right)) > 1){
            return false;
        }
        else{
            return isBalanced(root.left) && isBalanced(root.right);
        }
    }

    /**
     * 4.10 - checks if t2 is a subree of t1
     * @param t1 first tree
     * @param t2 second tree
     */
    public boolean isSubtree(TreeNode<T> t1, TreeNode<T> t2){
        if(t1 == null){
            return false;
        }
        else if(t2 == null){
            return true;
        }

        boolean ret = false;
        ArrayDeque<TreeNode<T>> queue = new ArrayDeque<>();
        queue.add(t1);

        TreeNode<T> current = root;
        while(!queue.isEmpty()){
            current = queue.poll();
            if(current.left != null){
                queue.add(current.left);
            }
            if(current.right != null){
                queue.add(current.right);
            }

            // Begin traversal check if nodes are equal
            if(current.data.equals(t2.data)){
                // If ret is true we can keep it that way with an OR
                System.out.println("Equals found!: " + current.data);
                ret = helperSubtree(current, t2) || ret;
            }
        }
        return ret;
    }

    // Helper method for 4.10 subtree problem
    public boolean helperSubtree(TreeNode<T> t1, TreeNode<T> t2){
        if(t1 == null && t2 == null){
            return true;
        }
        else if(t1 == null && t2 != null){
            return false;
        }
        else if(t1 != null && t2 == null){
            return false;
        }
        else if(!t1.data.equals(t2.data)){
            return false;
        }
        else{
            return helperSubtree(t1.left, t2.left) && helperSubtree(t1.right, t2.right);
        }
    }

    // 4.5 - validate BST
    public boolean validate(TreeNode<T> root){
        // Null checks
        if(root == null){
            return true;
        }
        else if(root.left == null && root.right == null){
            return true;
        }

        // Property violated
        if(root.left != null && root.left.data.compareTo(root.data) >= 0) {
            return false;
        }
        else if(root.right != null && root.right.data.compareTo(root.data) <= 0){
            return false;
        }
        else{
            return validate(root.left) && validate(root.right);
        }
    }
}

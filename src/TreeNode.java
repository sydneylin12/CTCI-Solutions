// Tree node with 2 children
// Abstract type must extend comparable to use compareTo
public class TreeNode<T extends Comparable>{

    public T data;
    public TreeNode left;
    public TreeNode right;

    public TreeNode(T data){
        this.data = data;
        this.left = null;
        this.right = null;
    }

    public TreeNode(T data, TreeNode left, TreeNode right){
        this.data = data;
        this.left = left;
        this.right = right;
    }
}

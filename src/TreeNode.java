/**
 * Custom binary tree node class
 */
public class TreeNode<T extends Comparable>{

    public T data;
    public TreeNode<T> left;
    public TreeNode<T> right;

    /**
     * Constructor for tree node
     * @param data the data of the node
     */
    public TreeNode(T data){
        this.data = data;
        this.left = null;
        this.right = null;
    }

    /**
     * Another constructor for easy tree building
     * @param data node data
     * @param left left node
     * @param right right node
     */
    public TreeNode(T data, TreeNode<T> left, TreeNode<T> right){
        this.data = data;
        this.left = left;
        this.right = right;
    }
}

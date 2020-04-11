/**
 * Linked stack class
 * @param <T> the abstract data type
 */
public class StackNode<T extends Comparable>{
    /**
     * The node data
     */
    public T data;

    /**
     * Pointer to the next node
     */
    public StackNode<T> next;

    /**
     * Constructor with data only
     * @param data the data of the node
     */
    public StackNode(T data){
        this.data = data;
        this.next = null;
    }

    /**
     * Chain constructor for stack nodes
     * @param data the data
     * @param next the next node
     */
    public StackNode(T data, StackNode<T> next){
        this.data = data;
        this.next = next;
    }

    /**
     * Override compare to method
     * @param other the other node
     * @return compare to of the nodes' data
     */
    public int compareTo(StackNode<T> other){
        return this.data.compareTo(other.data);
    }

    /**
     * Return a string representation of the stack
     * @return a string with the list of elements
     */
    public String toString(){
        StackNode current = this;
        String s = "[";
        while(current != null){
            s += current.data;
            if(current.next != null){
                s += ", ";
            }
        }
        s += "]";
        return s;
    }
}

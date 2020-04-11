/**
 * Linked list node class
 * @param <T> abstract data type
 */
public class ListNode<T extends Comparable> {
    /**
     * The data of the node
     */
    public T data;

    /**
     * Pointer to the next node
     */
    public ListNode<T> next;

    /**
     * Constructor with only data
     * @param data the data
     */
    public ListNode(T data){
        this.data = data;
        this.next = null;
    }

    /**
     * Constructor with data and next
     * @param data the node data
     * @param next next node
     */
    public ListNode(T data, ListNode next){
        this.data = data;
        this.next = next;
    }

    /**
     * Generate string from current node
     * @return a string describing the list from the node
     */
    public String toString(){
        ListNode current = this;
        String ret = "[";
        while(current != null){
            ret += current.data;
            if(current.next == null) {
                ret += "]";
            }
            else{
                ret += ", ";
            }
            current = current.next;
        }
        return ret;
    }
}

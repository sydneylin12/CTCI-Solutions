
// Custom linked list node class
public class ListNode<T extends Comparable> {
    public T data;
    public ListNode<T> next;

    public ListNode(T data){
        this.data = data;
        this.next = null;
    }

    public ListNode(T data, ListNode next){
        this.data = data;
        this.next = next;
    }

    // Visualize a linked list
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

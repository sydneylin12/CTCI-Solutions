import java.util.Queue;

/**
 * A custom queue class
 */
public class QueueNode<T extends Comparable> {
    public T data;
    public QueueNode<T> next;

    /**
     * The constructor
     * @param data the abstract data
     */
    public QueueNode(T data){
        this.data = data;
        this.next = null;
    }

    /**
     * Override to compare with other nodes
     * @param other the other node
     * @return compare to of the data
     */
    public int compareTo(QueueNode<T> other){
        return this.data.compareTo(other.data);
    }

    /**
     * Prints the queue from the current node
     */
    public void print(){
        QueueNode current = this;
        System.out.print("[");
        while(current != null){
            System.out.print(current.data);
            if(current.next != null){
                System.out.print(", ");
            }
            current = current.next;
        }
        System.out.print("]");
        System.out.println("");
    }

    /**
     * String representation of the queue starting at the current node
     * @return string representation of the queue
     */
    public String toString(){
        String ret = "[";
        QueueNode current = this;
        while(current != null){
            ret += current.data;
            if(current.next != null){
                ret += ", ";
            }
            current = current.next;
        }
        ret += "]";
        return ret;
    }
}

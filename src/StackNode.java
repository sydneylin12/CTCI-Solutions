// Implementation of a linked stack
public class StackNode<T extends Comparable>{
    public T data;
    public StackNode<T> next;

    public StackNode(T data){
        this.data = data;
        this.next = null;
    }

    // For min stack and future comparision
    public int compareTo(StackNode<T> other){
        return this.data.compareTo(other.data);
    }

    public void printStack(StackNode top){
        StackNode current = top;
        System.out.print("[");
        while(current != null){
            System.out.print(top.data + " ");
        }
        System.out.print("]");
        System.out.println("");
    }
}

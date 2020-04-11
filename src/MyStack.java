import java.util.ArrayDeque;
import java.util.EmptyStackException;

/**
 * Linked stack class
 * @param <T> abstract data type
 */
public class MyStack<T extends Comparable<T>> {

    /**
     * Top of stack pointer
     */
    private StackNode<T> top;

    /**
     * Default java util stack for minimum stack
     */
    private ArrayDeque<T> minStack;

    /**
     * Size of the stack
     */
    private int length;

    public MyStack(){
        this.top = null;
        this.minStack = new ArrayDeque<>();
        this.length = 0;
    }

    /**
     * Push a node onto the stack
     * @param item the data to be pushed
     */
    public void push(T item){
        StackNode<T> newNode = new StackNode<>(item);
        // Support min() in O(1)
        if(top == null){
            minStack = new ArrayDeque<>();
            minStack.push(newNode.data);
        }
        else{
            if(newNode.data.compareTo(minStack.peek()) <= 0){
                // Push min element less than or equal
                minStack.push(newNode.data);
            }
            else{
                //Do not push greater
                minStack.push(minStack.peek());
            }
        }
        newNode.next = top;
        top = newNode;
        length++;
    }

    /**
     * Pop a node off the top of the stack
     * @return the data of the node
     */
    public T pop(){
        if(top == null){
            throw new EmptyStackException();
        }
        T item = top.data;
        top = top.next;
        minStack.pop();
        length--;
        return item;
    }

    /**
     * Look at the top of the stack
     * @return the node data
     */
    public T peek(){
        if(top == null){
            throw new EmptyStackException();
        }
        return top.data;
    }

    /**
     * Minimum of the stack
     * @return the minimum data
     */
    public T min(){
        return minStack.peek();
    }

    /**
     * Check if the stack is empty
     * @return true if empty
     */
    public boolean isEmpty(){
        return top == null;
    }

    /**
     * Return a string representing the stack
     * @return string description of stack
     */
    public String toString(){
        return top.toString();
    }
}

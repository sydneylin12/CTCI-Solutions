import java.util.ArrayDeque;
import java.util.EmptyStackException;

// A linked stack class from CTCI
public class MyStack<T extends Comparable<T>> {

    private StackNode<T> top;
    // Have to use this to avoid nested initialization
    private ArrayDeque<T> minStack;

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
    }

    public T pop(){
        if(top == null){
            throw new EmptyStackException();
        }
        T item = top.data;
        top = top.next;
        minStack.pop();
        return item;
    }

    public T peek(){
        if(top == null){
            throw new EmptyStackException();
        }
        return top.data;
    }

    public T min(){
        return minStack.peek();
    }

    public boolean isEmpty(){
        return top == null;
    }

    public static void main(String[] args){
        MyStack<Integer> stack = new MyStack<>();
        stack.push(1);
        stack.push(2);
        stack.push(0);
        stack.push(10);
        stack.push(-1);
        System.out.println(stack.min());
        // 10 0 2 1 -1
    }
}

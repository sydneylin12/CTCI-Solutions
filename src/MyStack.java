import java.util.ArrayDeque;
import java.util.EmptyStackException;

// A linked stack class from CTCI
public class MyStack<T extends Comparable<T>> {

    private class StackNode<T extends Comparable<T>>{
        private T data;
        private StackNode<T> next;

        public StackNode(T data){
            this.data = data;
        }

        // For min stack and future comparision
        public int compareTo(StackNode<T> other){
            return this.data.compareTo(other.data);
        }
    }

    private StackNode<T> top;
    // Have to use this to avoid nested initialization
    private ArrayDeque<T> minStack;

    public void push(T item){
        StackNode<T> t = new StackNode<>(item);
        // Support min() in O(1)
        if(top == null){
            minStack = new ArrayDeque<>();
            minStack.push(t.data);
        }
        else{
            if(t.data.compareTo(minStack.peek()) <= 0){
                // Push min element less than or equal
                minStack.push(t.data);
            }
            else{
                //Do not push greater
                minStack.push(minStack.peek());
            }
        }
        t.next = top;
        top = t;
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

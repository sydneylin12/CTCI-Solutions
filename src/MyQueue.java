import java.util.NoSuchElementException;

/**
 * A custom queue class
 */
public class MyQueue<T extends Comparable<T>> {

    private QueueNode<T> head;
    private QueueNode<T> tail;
    private int length;

    /**
     * The default constructor
     */
    public MyQueue(){
        head = null;
        tail = null;
        length = 0;
    }

    /**
     * Checks if the queue is empty
     * @return true if empty
     */
    public boolean isEmpty(){
        return head == null;
    }

    /**
     * Length/size of queue
     * @return the length
     */
    public int size(){
        return length;
    }

    /**
     * Helper method to print a queue
     */
    public void printQueue(){
        System.out.println(head.toString());
    }

    /**
     * Check but do not dequeue the head node
     * @return the head node's data
     */
    public T peek(){
        if(this.isEmpty()){
            throw new NoSuchElementException("Queue is empty!");
        }
        else{
            return head.data;
        }
    }

    /**
     * Add an item to the end of the queue
     * @param item the data to be enqueued
     */
    public void enqueue(T item){
        QueueNode<T> temp = new QueueNode<>(item);
        if(isEmpty()){
            head = tail = temp;
        }
        else{
            tail.next = temp;
            tail = temp;
        }
        length++;
    }

    /**
     * Remove the head node and return it
     * @return the removed head node's data
     */
    public T dequeue(){
        if(isEmpty()){
            throw new NoSuchElementException("Cannot dequeue on an empty queue!");
        }
        else{
            QueueNode<T> temp = head;
            head = head.next;
            // Check for empty queu
            if(isEmpty()){
                tail = null;
            }
            return temp.data;
        }
    }

    /**
     * Return string representation of the queue
     * @return a string describing the queue
     */
    public String toString(){
        return head.toString();
    }
}

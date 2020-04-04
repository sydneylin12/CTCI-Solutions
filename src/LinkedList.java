import java.util.HashMap;

/**
 * A linked list custom class for CTCI
 */
public class LinkedList<T extends Comparable> {

    /**
     * Head node of the list (unused)
     */
    public ListNode<T> head;

    /**
     * Empty constructor
     */
    public LinkedList(){
        head = null;
    }

    /**
     * Linked List main method
     */
    public static void main(String[] args){
        LinkedList<Integer> list = new LinkedList<>();
        ListNode<Integer> mid = new ListNode<>(3);
        ListNode<Integer> a = new ListNode<>(7, new ListNode<>(6, new ListNode(7, new ListNode(6, new ListNode(6)))));
        ListNode<Integer> b = new ListNode<>(1, mid);
        mid.next = new ListNode<>(2, new ListNode(4));
        list.dedupe(a);
        delete(mid); // Delete the 3 from 1, 3, 2, 4
        System.out.println(b.toString());
        list.sumLists(a, b);
    }

    /**
     * 2.1 - remove duplicates from a ndoe
     * @param head the head node of a linked list
     */
    public void dedupe(ListNode<T> head){
        HashMap<T, Integer> nodeCount = new HashMap<>();

        // First node cannot be a duplicate
        ListNode<T> trailer = null;
        ListNode<T> current = head;

        // Iterate until the end of list
        while(current != null){
            if(nodeCount.containsKey(current.data)){
                //System.out.println("Dupe found: " + current.data + " " + trailer + " " +  current.next);
                trailer.next = current.next;
            }
            else{
                trailer = current; //PUT THIS HERE
                nodeCount.put(current.data, 1);
            }
            // Current is unaffected
            current = current.next;
        }
        System.out.println(head.toString());
    }


    /**
     * 2.3 - delete middle node given a pointer to a node only
     * @param n the node to be deleted
     */
    public static void delete(ListNode n){
        ListNode trailer = null;
        ListNode current = n;
        while(current != null){
            // Assign current's data to the next node's data
            if(current.next != null){
                current.data = current.next.data;
                trailer = current;
                current = current.next;
            }
            else {
                // Kill the loop
                trailer.next = null;
                current = null;
            }
        }
    }

    /**
     * 2.5 - sum lists in a reverse order
     * @param a first list
     * @param b second list
     * @return a linked list contianing the sum in reverse order
     */
    public static ListNode<Integer> sumLists(ListNode<Integer> a, ListNode<Integer> b){
        int first = 0;
        int second = 0;

        // Iterate through both lists
        ListNode<Integer> current = a;
        int multiplier = 1;
        while(current != null){
            first += current.data * multiplier;
            multiplier *= 10;
            current = current.next;
        }

        current = b;
        multiplier = 1;
        while(current != null){
            second += current.data * multiplier;
            multiplier *= 10;
            current = current.next;
        }

        // Create the third returned list
        int third = first + second;
        int num;

        ListNode head = null;
        ListNode currHead = null;

        // Create nodes while the sum is not 0
        while(third != 0){
            //Get last digit
            num = third % 10;
            if(head == null){
               head = new ListNode(num);
               currHead = head;
            }
            else{
                currHead.next = new ListNode(num);
                currHead = currHead.next;
            }
            third = third / 10;
        }
        System.out.println(head.toString());
        return head;
    }
}

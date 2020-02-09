import java.util.HashMap;
import java.util.LinkedList;

public class LinkedLists {

    static class Node{
        int data;
        Node next;

        public Node(int i){
            this.data = i;
            this.next = null;
        }

        public Node(int i, Node n){
            this.data = i;
            this.next = n;
        }

        public void clear(){
            this.next = null;
        }

        public void setNext(Node n){
            this.next = n;
        }

        public String toString(){
            Node current = this;
            String s = "[";
            while(current != null){
                if(current.next == null){
                    s += String.valueOf(current.data); // End of string
                }
                else{
                    s += String.valueOf(current.data) + ", ";
                }
                current = current.next;
            }
            s += "]";
            return s;
        }
    }

    public static void main(String[] args){
        //Node deleteTest = new Node(4);
        //Node head = new Node(1, new Node(1, new Node(2, new Node(3, new Node(3, deleteTest)))));
        //deleteTest.next = new Node(7, new Node(9));
        //System.out.println(head);
        //dedupe(head);
        //delete(deleteTest);
        //System.out.println(head);

        //Node head = new Node(1, new Node(1, new Node(2, new Node(3, new Node(3, new Node(3, new Node(9, new Node(8, new Node(8, new Node(9, new Node(10)))))))))));
        //System.out.println(head);
        //dedupe(head);
        //System.out.println(head);

        Node a = new Node(7, new Node(1, new Node(6)));
        Node b = new Node(5, new Node(9, new Node(2)));
        sumLists(a, b);

    }

    // 2.1 - remove dupes from a linked list (UNSORTED)
    public static void dedupe(Node head){
        HashMap<Integer, Integer> nodeCount = new HashMap<>();

        Node trailer = null; //First node cannot be a duplicate
        Node current = head;

        while(current != null){
            if(nodeCount.containsKey(current.data)){
                System.out.println("Dupe found: " + current.data + " " + trailer + " " +  current.next);
                trailer.next = current.next;
            }
            else{
                trailer = current; //PUT THIS HERE
                nodeCount.put(current.data, 1);
            }
            // Current is unaffected
            current = current.next;
        }
    }

    // 2.3 delete middle node
    // Cannot pass in start or end, must only use node as argument
    public static void delete(Node n){
        Node previous = null;
        Node current = n;
        while(current.next != null){
            if(current.next != null){
                current.data = current.next.data;
            }
            previous = current;
            current = current.next;
        }
        previous.next = null;
    }

    // 2.5 Sum Lists (stored in reverse order)
    // ex: 7-1-6 is 617, 5-9-2 is 295
    public static Node sumLists(Node a, Node b){
        int first = 0;
        int second = 0;

        // Iterate through both lists
        Node current = a;
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

        int third = first + second;
        int temp;
        Node head = null;
        Node currHead = null;
        while(third != 0){
            //Get last digit
            temp = third % 10;
            if(head == null){
               head = new Node(temp);
               currHead = head;
            }
            else{
                currHead.next = new Node(temp);
                currHead = currHead.next;
            }
            third = third / 10;
        }
        System.out.println(head);
        return head;
    }
}

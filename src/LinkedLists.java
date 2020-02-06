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
        Node head = new Node(1, new Node(1, new Node(2, new Node(3, new Node(3, new Node(5, new Node(7)))))));
        System.out.println(head);
        dedupe(head);
        System.out.println(head);

    }

    // 2.1 - remove dupes from a linked list
    public static void dedupe(Node head){
        Node current = head;
        Node nextNode = null;
        while(current != null){
            nextNode = current.next;
            if(nextNode != null && current.data == nextNode.data){
                current.next = nextNode.next;
                current = nextNode;
            }
            else{
                current = nextNode;
            }
        }
    }
}

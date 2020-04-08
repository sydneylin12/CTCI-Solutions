
/**
 * Daily coding problem 5 class for cons, car, cdr
 */
public class Cons {
    private Object a;
    private Object b;

    public Cons(Object a, Object b){
        this.a = a;
        this.b = b;
    }

    public Object car(){
        return this.a;
    }

    public Object cdr(){
        return this.b;
    }

    public static void main(String[] args){
        Cons c = new Cons("First", new Cons("Second", "Third"));
        System.out.println(c.car() + " " + (Cons) c.cdr());
    }
}
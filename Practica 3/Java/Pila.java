public class Pila{
    private long[] arreglo;
    private int top;
    private int n;
    
    public Pila(int n){
        this.n = n;
        arreglo= new long[n];
        top=-1;
    }
    public void push (long e){
        if(!isFull()){
            arreglo[++top]= e;
        }else{
            System.out.println("La pila está llena, no se puede agregar más elementos.");
        }
    }
    public long pop(){
        if(!isEmpty()){
            return arreglo[top--];
        }else{
            System.out.println("La pila está vacía, no se puede extraer elementos.");
            return -1;
        }
    }
    public long peek(){
        if (!isEmpty()) {
            return arreglo[top];
        } else {
            System.out.println("La pila está vacía, no se puede obtener el elemento superior.");
            return -1;
        }
    }
    public boolean isEmpty() {
        return top == -1;
    }


    public boolean isFull() {
        return top == n - 1;
    }
    public static void main(String[] args) {
        Pila pila = new Pila(5);

    
        pila.push(10);
        pila.push(20);
        pila.push(30);

    
        System.out.println("Elemento superior: " + pila.peek());

        
        System.out.println("Elemento retirado: " + pila.pop());
        System.out.println("Elemento retirado: " + pila.pop());

        
        System.out.println("¿La pila está vacía? " + pila.isEmpty());
    }
}
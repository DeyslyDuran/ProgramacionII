public class Cola {
    private long[] arreglo;
    private int inicio;
    private int fin;
    private int n;

    
    public Cola(int n) {
        this.n = n;
        arreglo = new long[n];
        inicio = 0;
        fin = -1;
    }

    
    public void insert(long e) {
        if (!isFull()) {
            fin = (fin + 1) % n;
            arreglo[fin] = e;
        } else {
            System.out.println("La cola está llena, no se puede agregar más elementos.");
        }
    }

    
    public long remove() {
        if (!isEmpty()) {
            long temp = arreglo[inicio];
            inicio = (inicio + 1) % n;
            return temp;
        } else {
            System.out.println("La cola está vacía, no se puede extraer elementos.");
            return -1; 
        }
    }

    
    public long peek() {
        if (!isEmpty()) {
            return arreglo[inicio];
        } else {
            System.out.println("La cola está vacía, no se puede obtener el primer elemento.");
            return -1; 
        }
    }

    
    public boolean isEmpty() {
        return (fin + 1) % n == inicio;
    }

    
    public boolean isFull() {
        return (fin + 2) % n == inicio;
    }

    
    public int size() {
        if (fin >= inicio) {
            return fin - inicio + 1;
        } else {
            return n - inicio + fin + 1;
        }
    }

    
    public static void main(String[] args) {
        Cola cola = new Cola(5);

        
        cola.insert(10);
        cola.insert(20);
        cola.insert(30);

        
        System.out.println("Primer elemento: " + cola.peek());

        
        System.out.println("Elemento retirado: " + cola.remove());
        System.out.println("Elemento retirado: " + cola.remove());

        
        System.out.println("¿La cola está vacía? " + cola.isEmpty());

        
        System.out.println("¿La cola está llena? " + cola.isFull());

        
        System.out.println("Tamaño de la cola: " + cola.size());
    }
}


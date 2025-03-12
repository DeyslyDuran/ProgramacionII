public class AreaCalculator {



    // Área del círculo
    public double calcularArea(double radio) {
        return Math.PI * radio * radio;
    }

    // Área del rectángulo
    public double calcularArea(double largo, double ancho) {
        return largo * ancho;
    }

    // Área del triángulo
    public double calcularArea(double base, double altura, boolean esTriangulo) {
        if (esTriangulo) {
            return 0.5 * base * altura;
        }
        return -1;
    }

    // Área del cuadrado
    public double calcularArea(int lado) {
        return lado * lado;
    }

    // Área del trapecio
    public double calcularArea(double baseMayor, double baseMenor, double altura) {
        return 0.5 * (baseMayor + baseMenor) * altura;
    }

    // Área del pentágono (usando int para lado para evitar conflicto con el trapecio)
    public double calcularArea(int lado, double apotema) {
        return 0.5 * 5 * lado * apotema;
    }

    public static void main(String[] args) {
        AreaCalculator calculador = new AreaCalculator();
        
        // Ejemplos de uso
        System.out.println("Área del círculo (radio=5): " + calculador.calcularArea(5));
        System.out.println("Área del rectángulo (largo=5, ancho=3): " + calculador.calcularArea(5, 3));
        System.out.println("Área del triángulo (base=4, altura=2): " + calculador.calcularArea(4, 2, true));
        System.out.println("Área del cuadrado (lado=4): " + calculador.calcularArea(4));
        System.out.println("Área del trapecio (base mayor=7, base menor=3, altura=4): " + calculador.calcularArea(7, 3, 4));
        System.out.println("Área del pentágono (lado=3, apotema=2.5): " + calculador.calcularArea(3, 2.5));
    }
}

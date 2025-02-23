import java.awt.*;
import javax.swing.*;

public class Punto {
    public float x;
    public float y;

    public Punto(float x, float y) {
        this.x = x;
        this.y = y;
    }

    public float[] coord_cartesianas() {
        return new float[] { this.x, this.y };
    }

    public float[] coord_polares() {
        float radio = (float) Math.sqrt(this.x * this.x + this.y * this.y);
        float angulo = (float) Math.atan2(this.y, this.x);
        angulo = (float) Math.toDegrees(angulo);
        return new float[] { radio, angulo };
    }

    @Override
    public String toString() {
        return String.format("(%.2f, %.2f)", this.x, this.y);
    }

    public static void main(String[] args) {
        
        // Crear y mostrar la ventana para los gráficos
        JFrame frame = new JFrame("Grafico de Linea y Circulo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 500);
        frame.add(new JComponent() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                ///PUNTO
                Punto punto = new Punto(230,230);
                System.out.println(punto);
                float a[] = punto.coord_cartesianas();
                System.out.println(a[0] + " " + a[1]);
                float b[] = punto.coord_polares();
                System.out.println(b[0] + " " + b[1]);
                

                // Dibujar la linea
                Linea linea = new Linea(punto,new Punto(150,100));
                System.out.println(linea);
                linea.dibujaLinea(g);

                // Dibujar el circulo
                Circulo circulo = new Circulo(punto,100);
                System.out.println(circulo);
                circulo.dibujaCirculo(g);
            }
        });
        frame.setVisible(true);
    }
}

class Linea {
    public Punto p1;
    public Punto p2;

    public Linea(Punto p1, Punto p2) {
        this.p1 = p1;
        this.p2 = p2;
    }

    public Punto getP1() {
        return p1;
    }

    public Punto getP2() {
        return p2;
    }

    @Override
    public String toString() {
        return String.format("Linea[(%.2f, %.2f), (%.2f, %.2f)]", p1.x, p1.y, p2.x, p2.y);
    }

    public void dibujaLinea(Graphics g) {
        g.drawLine((int) p1.x, (int) p1.y, (int) p2.x, (int) p2.y);
    }
}

class Circulo {
    public Punto centro;
    public float radio;

    public Circulo(Punto centro, float radio) {
        this.centro = centro;
        this.radio = radio;
    }

    public Punto getCentro() {
        return centro;
    }

    public float getRadio() {
        return radio;
    }

    @Override
    public String toString() {
        return String.format("Circulo[(%.2f, %.2f), radio=%.2f]", centro.x, centro.y, radio);
    }

    public void dibujaCirculo(Graphics g) {
        g.drawOval((int) (centro.x - radio), (int) (centro.y - radio), (int) (radio * 2), (int) (radio * 2));
    }
}
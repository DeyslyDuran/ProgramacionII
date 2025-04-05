import java.util.Random;
import java.util.Scanner;

class Juego {
    protected int numeroDeVidas = 3;
    protected int record = 0;

    public void reiniciaPartida() {
        numeroDeVidas = 3;
    }

    public void actualizaRecord() {
        if (numeroDeVidas > record) {
            record = numeroDeVidas;
            System.out.println("¡Nuevo récord! Vidas restantes: " + record);
        }
    }

    public boolean quitaVida() {
        numeroDeVidas--;
        if (numeroDeVidas > 0) {
            System.out.println("Te quedan " + numeroDeVidas + " vidas.");
            return true;
        } else {
            System.out.println("¡Has perdido todas tus vidas!");
            return false;
        }
    }
}

class JuegoAdivinaNumero extends Juego {
    protected int numeroAAdivinar;

    public JuegoAdivinaNumero(int numeroDeVidas) {
        this.numeroDeVidas = numeroDeVidas;
    }

    public void juega() {
        reiniciaPartida();
        numeroAAdivinar = new Random().nextInt(11); // Genera un número entre 0 y 10
        System.out.println("Adivina un número entre 0 y 10.");

        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print("Introduce tu número: ");
            int guess;
            try {
                guess = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Por favor, introduce un número válido.");
                continue;
            }

            if (guess == numeroAAdivinar) {
                System.out.println("¡Acertaste!");
                actualizaRecord();
                break;
            } else {
                if (!quitaVida()) {
                    break;
                }
                if (guess < numeroAAdivinar) {
                    System.out.println("El número a adivinar es mayor.");
                } else {
                    System.out.println("El número a adivinar es menor.");
                }
            }
        }
        scanner.close();
    }
}

public class Aplicacion {
    public static void main(String[] args) {
        JuegoAdivinaNumero juego = new JuegoAdivinaNumero(3);
        juego.juega();
    }
}
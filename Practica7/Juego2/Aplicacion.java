package Juego2;

import java.util.Random;
import java.util.Scanner;

class Juego {
    protected int numeroDeVidas;
    protected int record;

    public Juego(int numeroDeVidas) {
        this.numeroDeVidas = numeroDeVidas;
        this.record = 0;
    }

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
        super(numeroDeVidas);
    }

    public boolean validaNumero(int numero) {
        return numero >= 0 && numero <= 10;
    }

    public void juega(Scanner scanner) {
        reiniciaPartida();
        numeroAAdivinar = new Random().nextInt(11); // Genera un número entre 0 y 10
        System.out.println("Adivina un número entre 0 y 10.");

        while (true) {
            System.out.print("Introduce tu número: ");
            int guess;
            try {
                guess = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Por favor, introduce un número válido.");
                continue;
            }

            if (!validaNumero(guess)) {
                System.out.println("El número debe estar entre 0 y 10.");
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
    }
}

class JuegoAdivinaPar extends JuegoAdivinaNumero {
    public JuegoAdivinaPar(int numeroDeVidas) {
        super(numeroDeVidas);
    }

    @Override
    public boolean validaNumero(int numero) {
        if (super.validaNumero(numero) && numero % 2 == 0) {
            return true;
        } else {
            System.out.println("Error: El número debe ser par y estar entre 0 y 10.");
            return false;
        }
    }
}

class JuegoAdivinaImpar extends JuegoAdivinaNumero {
    public JuegoAdivinaImpar(int numeroDeVidas) {
        super(numeroDeVidas);
    }

    @Override
    public boolean validaNumero(int numero) {
        if (super.validaNumero(numero) && numero % 2 != 0) {
            return true;
        } else {
            System.out.println("Error: El número debe ser impar y estar entre 0 y 10.");
            return false;
        }
    }
}

public class Aplicacion {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Crear una única instancia de Scanner
        JuegoAdivinaNumero juegoNumero = new JuegoAdivinaNumero(3);
        JuegoAdivinaPar juegoPar = new JuegoAdivinaPar(3);
        JuegoAdivinaImpar juegoImpar = new JuegoAdivinaImpar(3);

        System.out.println("\n--- Juego Adivina un Número ---");
        juegoNumero.juega(scanner);

        System.out.println("\n--- Juego Adivina un Número Par ---");
        juegoPar.juega(scanner);

        System.out.println("\n--- Juego Adivina un Número Impar ---");
        juegoImpar.juega(scanner);

        scanner.close(); 
    }
}

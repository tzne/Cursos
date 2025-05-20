import java.util.Scanner;

public class ex005 {
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    int numero = (int) (1 + Math.random() * (6 - 1));
    
    System.out.print("Insira um número de 1 a 5: ");
    int chute = entrada.nextInt();

    System.out.printf((chute == numero) ? "Você acertou!\n" : "Você errou! A resposta correta era %d\n", numero);
  }
  
}
import java.util.Scanner;

public class ex010 {
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);

    System.out.print("Início: ");
    int inicio = entrada.nextInt();
    System.out.print("Fim: ");
    int fim = entrada.nextInt();
    System.out.print("Passo: ");
    int passo = entrada.nextInt();

    for (int i = inicio; i <= fim; i += passo)
      System.out.println(i);

  }
}

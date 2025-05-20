import java.util.Scanner;

public class Ex002 {
  public static void main(String[] args) {
    Scanner entradaPadrao = new Scanner(System.in);

    System.out.print("Insira o primeiro número: ");
    float numero1 = entradaPadrao.nextFloat();
    System.out.print("Insira o segundo número: ");
    float numero2 = entradaPadrao.nextFloat();

    float soma = numero1 + numero2;

    System.out.printf("%.2f + %.2f = %.2f", numero1, numero2, soma);

  }
}
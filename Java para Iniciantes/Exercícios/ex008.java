import java.util.Scanner;

public class ex008 {
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);

    int numero = entrada.nextInt(), resultado = 1;

    while (numero != 1) {
      System.out.printf("%d x ", numero);
      resultado *= numero;
      numero--;
    }

  System.out.printf("1 = %d\n",resultado);
  }
}

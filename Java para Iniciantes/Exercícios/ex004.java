import java.util.Scanner;

public class ex004 {
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);

    System.out.print("Informe um valor: ");
    double numero = entrada.nextDouble();

    System.out.printf("Resto da divisão por 2: %d\n", ((int) (numero%2)));
    System.out.printf("Elevado ao cubo: %.2f\n", Math.pow(numero, 3));
    System.out.printf("Raiz quadrada: %.2f\n", Math.sqrt(numero));
    System.out.printf("Raiz cúbica: %.2f\n", Math.cbrt(numero));
    System.out.printf("Valor absoluto: %.2f\n", Math.abs(numero));
    
  }
  
}

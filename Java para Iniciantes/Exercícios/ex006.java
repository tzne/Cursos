import java.util.Scanner;

public class ex006 {
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);

    System.out.print("Insira o coeficiente de a: ");
    float a = entrada.nextFloat();
    System.out.print("Insira o coeficiente de b: ");
    float b = entrada.nextFloat();
    System.out.print("Insira o coeficiente de c: ");
    float c = entrada.nextFloat();

    float delta = b*b - (4 * a * c);
    System.out.printf("Delta = %f\n", delta);
    
    if (delta < 0)
      System.out.println("Não existem raízes reais");
    else
      System.out.println("Existem raízes reais");

  }
}
import java.util.Scanner;

public class ex007 {
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);

    System.out.print("Insira a medida do lado: ");
    float lado1 = entrada.nextFloat();
    System.out.print("Insira a medida do lado: ");
    float lado2 = entrada.nextFloat();
    System.out.print("Insira a medida do lado: ");
    float lado3 = entrada.nextFloat();

    // feito dessa forma por legibilidade
    boolean trianguloExiste = lado1 < (lado2 + lado3) && lado2 < (lado1 + lado3) && lado3 < (lado1 + lado2);

    if (!trianguloExiste)
      System.out.println("Triângulo não existe");
    else if (lado1 == lado2 && lado2 == lado3)
      System.out.println("Triângulo equilátero");
    else if (lado1 != lado2 && lado1 != lado3 && lado2 != lado3)
      System.out.println("Triângulo escaleno");
    else
      System.out.println("Triângulo isósceles");
  }
}

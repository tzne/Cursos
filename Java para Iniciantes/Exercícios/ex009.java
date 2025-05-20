import java.util.Scanner;

public class ex009 {
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);

    int soma = 0, numero = 1, totalValores = 0, totalPares = 0, totalImpares = 0, acima100 = 0, media = 0;

    do {
      numero = entrada.nextInt();

      if (numero != 0) {

        if (numero % 2 == 0)
          totalPares++;
        else
          totalImpares++;

        if (numero > 100)
          acima100++;

        totalValores++;

      }

      soma += numero;

    } while (numero != 0);

    media = soma / totalValores;

    System.out.printf("Resultado: %d\n", soma);
    System.out.printf("Total de valores: %d\n", totalValores);
    System.out.printf("Total de pares: %d\n", totalPares);
    System.out.printf("Total de ímpares: %d\n", totalImpares);
    System.out.printf("Acima de 100: %d\n", acima100);
    System.out.printf("Média: %d\n", media);

  }
}
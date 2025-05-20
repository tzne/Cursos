import java.util.Scanner;
import java.util.Arrays;

public class ex011 {
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);

    int vetor[] = new int[10];
    Arrays.fill(vetor, 0);
    int posicao = 0;


    while (posicao != -1) {
    System.out.print("{");
      for (int i : vetor)
        System.out.printf("%d, ", i);
    System.out.printf("\b\b}");
        
      System.out.println();
      System.out.print("Insira a posição do elemento que deseja alterar (-1 para sair): ");
      posicao = entrada.nextInt();
      if (posicao == -1) break;
      System.out.printf("Insira o elemento que deseja inserir na posição %d: ", posicao);
      int insercao = entrada.nextInt();
      vetor[posicao] = insercao;
    }


  }
}

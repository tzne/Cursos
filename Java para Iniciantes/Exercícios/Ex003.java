import java.util.Scanner;
import java.time.Year;

public class Ex003 {
  public static void main(String args[]) {
    Scanner entrada = new Scanner(System.in);

    System.out.print("Insira o ano que nasceu: ");
    int ano_nascimento = entrada.nextInt();

    int ano_atual = Year.now().getValue();

    int idade = ano_atual - ano_nascimento;

    System.out.printf("Você possui %d anos\n", idade);
  }
}
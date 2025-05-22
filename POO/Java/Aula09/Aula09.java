package Java.Aula09;

public class Aula09 {
  public static void main(String[] args) {
    Pessoa pessoas[] = new Pessoa[2];
    Livro livros[] = new Livro[3];

    pessoas[0] = new Pessoa("Pedro", 22, "M");
    pessoas[1] = new Pessoa("Maria", 25, "F");

    livros[0] = new Livro("Core Java", "Gary Cornell", 384, pessoas[0]);
    livros[1] = new Livro("Java: Como Programa", "Paul Deitel", 968, pessoas[1]);
    livros[2] = new Livro("Algorithms", "Rober Sedgewick", 992, pessoas[1]);
  
    livros[0].abrir();
    livros[0].folhear(230);
    System.out.println(livros[0].detalhes());
  }
}

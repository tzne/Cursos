package Java.Aula13;

public class Mamifero extends Animal{
  /*
   * Atributos
   */
  protected String corPelo;

  /*
   * Métodos personalizados
   */
  @Override
  public void emitirSom() {
    System.out.println("Som de mamífero");
  }

  /*
   * Métodos especiais
   */
public String getCorPelo() {
    return this.corPelo;
  }

  public void setCorPelo(String corPelo) {
    this.corPelo = corPelo;
  }
}
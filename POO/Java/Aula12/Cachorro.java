package Java.Aula12;

public class Cachorro extends Mamifero {
  /* 
   * Métodos personalizados
   */
  public void enterrarOsso() {
    System.out.println("Osso enterrado!");
  }

  public void abanarRabo() {
    System.out.println("Abanando o rabo");
  }

  @Override
  public void emitirSom() {
    System.out.println("AU AU AU AU");
  }
}

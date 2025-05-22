package Java.Aula12;

public class Canguru extends Mamifero {
  /*
   * Métodos personalizados
   */
  public void usarBolsa() {
    System.out.println("Usando bolsa");
  }
  
  @Override
  public void locomover() {
    System.out.println("Pulando");
  }
  
}

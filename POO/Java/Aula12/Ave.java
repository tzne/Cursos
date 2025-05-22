package Java.Aula12;

public class Ave extends Animal {
  /*
   * Atributos
   */
  private String corPena;

  /*
   * Métodos personalizados
   */
  @Override
  public void locomover() {
    System.out.println("Voando");
  }

  @Override
  public void alimentar() {
    System.out.println("Comendo frutas");
  }

  @Override
  public void emitirSom() {
    System.out.println("Som de ave");
  }

  public void fazerNinho() {
    System.out.println("Construir ninho");
  }

  /*
   * Métodos especiais
   */
  public String getCorPena() {
    return this.corPena;
  }

  public void setCorPena(String corPena) {
    this.corPena = corPena;
  }

}

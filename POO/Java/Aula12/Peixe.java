package Java.Aula12;

public class Peixe extends Animal{
  /*
   * Atributos
   */
  private String corEscama;

  /*
   * Métodos personalizados
   */
  public void setCorEscama(String corEscama) {
    this.corEscama = corEscama;
  }

  @Override
  public void locomover() {
    System.out.println("Nadando");
  }

  @Override
  public void alimentar() {
    System.out.println("Comendo substâncias");
  }

  @Override
  public void emitirSom() {
    System.out.println("Peixe não faz som");
  }

  public void soltarBolhas() {
    System.out.println("BLOB BLOB ");
  }


  /*
   * Métodos especiais
   */
  public String getCorEscama() {
    return this.corEscama;
  }

}

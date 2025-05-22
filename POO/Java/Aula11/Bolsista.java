package Java.Aula11;

public class Bolsista extends Aluno {
  /*
   * Atributos
   */
  private float bolsa;

  /*
   * Métodos Personalizados
   */
  public void renovarBolsa() {
    System.out.printf("Renovando bolsa de %s\n", this.getNome());
  }

  @Override
  public void pagarMensalidade() {
    System.out.printf("%s é bolsista! Desconto aplicado\n", this.getNome());
  }

  /*
   * Métodos especiais
   */

  public float getBolsa() {
    return this.bolsa;
  }

  public void setBolsa(float bolsa) {
    this.bolsa = bolsa;
  }

}

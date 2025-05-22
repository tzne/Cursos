package Java.Aula10;

public class Funcionario extends Pessoa {
  /*
   * Atributos
   */
  private boolean trabalhando;
  private String setor;

  /*
   * Métodos personalizados
   */
  public void mudarTrabalho() {
    this.setTrabalhando(!this.getTrabalhando());
  }

  /*
   * Métodos especiais
   */


  public boolean isTrabalhando() {
    return this.trabalhando;
  }

  public boolean getTrabalhando() {
    return this.trabalhando;
  }

  public void setTrabalhando(boolean trabalhando) {
    this.trabalhando = trabalhando;
  }

  public String getSetor() {
    return this.setor;
  }

  public void setSetor(String setor) {
    this.setor = setor;
  }
   
}
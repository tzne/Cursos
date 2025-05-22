package Java.Aula10;

public class Professor extends Pessoa {
  /*
   * Atributos
   */
  private float salario;
  private String especialidade;

  /*
   * Métodos personalizados
   */
  public void receberAumento(float valor) {
  this.setSalario(this.getSalario() + valor);
  }

  
  /*
   * Métodos especiais
   */

  public float getSalario() {
    return this.salario;
  }

  public void setSalario(float salario) {
    this.salario = salario;
  }

  public String getEspecialidade() {
    return this.especialidade;
  }

  public void setEspecialidade(String especialidade) {
    this.especialidade = especialidade;
  }

}
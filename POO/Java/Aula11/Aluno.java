package Java.Aula11;

public class Aluno extends Pessoa {
  /*
   * Atributos
   */
  private int matricula;
  private String curso;

  /*
   * Métodos personalizados
   */
  public void pagarMensalidade() {
    System.out.printf("Mensalidade de %s paga\n", this.getNome());
  }

  /*
   * Métodos especiais
   */
  public int getMatricula() {
    return this.matricula;
  }

  public void setMatricula(int matricula) {
    this.matricula = matricula;
  }

  public String getCurso() {
    return this.curso;
  }

  public void setCurso(String curso) {
    this.curso = curso;
  }

}

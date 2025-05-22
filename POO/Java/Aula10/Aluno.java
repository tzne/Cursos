package Java.Aula10;

public class Aluno extends Pessoa {
  /*
   * Atributos
   */
  private int matricula;
  private String curso;

  /*
   * Métodos personalizados
   */
  public void cancelarMatricula() {
    System.out.println("Matrícula cancelada");
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

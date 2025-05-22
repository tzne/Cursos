package Java.Aula11;

public abstract class Pessoa {
  /*
   * Atributos
   */
  private String nome;
  private String sexo;
  private int idade;

  /*
   * Métodos personalizados
   */
  public void fazerAniversario() {
    this.setIdade(this.getIdade() + 1);
  }

  public String dados() {
    return "Nome: " + this.getNome() + "\nIdade: " + this.getIdade() + "\nSexo: " + this.getSexo();
  }

  /*
   * Métodos especiais
   */

  public String getNome() {
    return this.nome;
  }

  public void setNome(String nome) {
    this.nome = nome;
  }

  public String getSexo() {
    return this.sexo;
  }

  public void setSexo(String sexo) {
    this.sexo = sexo;
  }

  public int getIdade() {
    return this.idade;
  }

  public void setIdade(int idade) {
    this.idade = idade;
  }

}

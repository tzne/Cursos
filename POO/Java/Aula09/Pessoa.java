package Java.Aula09;

public class Pessoa {
  /*
   * Atributos
   */
  private String nome;
  private int idade;
  private String sexo;

  /*
   * Métodos personalizados
   */
  public void fazerAniversario() {
    this.setIdade(this.getIdade() + 1);

  }

  /*
   * Métodos especiais
   */
  public Pessoa(String nomeString, int idade, String sexoString) {
    this.setNome(nomeString);
    this.setIdade(idade);
    this.setSexo(sexoString);
  }

  public String getNome() {
    return this.nome;
  }

  public void setNome(String nome) {
    this.nome = nome;
  }

  public int getIdade() {
    return this.idade;
  }

  public void setIdade(int idade) {
    this.idade = idade;
  }

  public String getSexo() {
    return this.sexo;
  }

  public void setSexo(String sexo) {
    this.sexo = sexo;
  }
  

}

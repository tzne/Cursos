package Java.ProjetoFinal;

public abstract class Pessoa {
  /*
   * Atributos
   */
  protected String nome;
  protected int idade;
  protected String sexo;
  protected float experiencia;

  /*
   * Métodos personalizados
   */
  protected abstract void ganharExperiencia();

  /*
   * Métodos especiais
   */
  public Pessoa(String nomeString, int idade, String sexoString) {
    this.nome = nomeString;
    this.idade = idade;
    this.sexo = sexoString;
    this.experiencia = 0;
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

  public float getExperiencia() {
    return this.experiencia;
  }

  public void setExperiencia(int experiencia) {
    this.experiencia = experiencia;
  }
}

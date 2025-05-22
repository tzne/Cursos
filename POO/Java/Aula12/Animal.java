package Java.Aula12;

public abstract class Animal {
  /*
   * Atributos
   */
  protected float peso;
  protected int idade;
  protected int quantidadeMembros;

  /* 
   * Métodos personalizados
   */
  public abstract void locomover();
  public abstract void alimentar();
  public abstract void emitirSom();

  /*
   * Métodos especiais
   */

  public float getPeso() {
    return this.peso;
  }

  public void setPeso(float peso) {
    this.peso = peso;
  }

  public int getIdade() {
    return this.idade;
  }

  public void setIdade(int idade) {
    this.idade = idade;
  }

  public int getQuantidadeMembros() {
    return this.quantidadeMembros;
  }

  public void setQuantidadeMembros(int quantidadeMembros) {
    this.quantidadeMembros = quantidadeMembros;
  }


}

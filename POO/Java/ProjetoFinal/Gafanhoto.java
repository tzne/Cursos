package Java.ProjetoFinal;

public class Gafanhoto extends Pessoa {

  /*
   * Atributos
   */
  private String login;
  private int totalAssistido;

  /*
   * Métodos personalizados
   */
  @Override
  protected void ganharExperiencia() {
  }

  /*
   * Métodos especiais
   */
  public Gafanhoto(String nomeString, int idade, String sexoString, String loginString) {
    super(nomeString, idade, sexoString);
    this.login = loginString;
    this.totalAssistido = 0;
  }

  public String getLogin() {
    return this.login;
  }

  public void setLogin(String login) {
    this.login = login;
  }

  public int getTotalAssistido() {
    return this.totalAssistido;
  }

  public void setTotalAssistido(int totalAssistido) {
    this.totalAssistido = totalAssistido;
  }

}

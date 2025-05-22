package Java.ProjetoFinal;

public class Visualizacao {
  /*
   * Atributos
   */
  private Gafanhoto espectador;
  private Video filme;

  /*
   * Métodos personalizados
   */
  public void avaliar() {
    this.filme.setAvaliacao(5);
  }

  public void avaliar(int nota) {
    filme.setAvaliacao(nota);
  }

  public void avaliar(float porcentagem) {
    int notaDada = 0;
    if (porcentagem <= 20)
      notaDada = 3;
    else if (porcentagem <= 50)
      notaDada = 5;
    else if (porcentagem <= 90)
      notaDada = 8;
    else
      notaDada = 10;
    this.filme.setAvaliacao(notaDada);
  }

  /*
   * Métodos especiais
   */

  public Visualizacao(Gafanhoto espectador, Video filme) {
    this.espectador = espectador;
    this.filme = filme;
    this.espectador.setTotalAssistido(this.espectador.getTotalAssistido() + 1);
    this.filme.setViews(this.filme.getViews() + 1);
  }

  public Gafanhoto getEspectador() {
    return this.espectador;
  }

  public void setEspectador(Gafanhoto espectador) {
    this.espectador = espectador;
  }

  public Video getFilme() {
    return this.filme;
  }

  public void setFilme(Video filme) {
    this.filme = filme;
  }

}

package Java.ProjetoFinal;

public class Video implements AcoesVideo {
  /*
   * Atributos
   */
  private String titulo;
  private int avaliacao;
  private int views;
  private int curtidas;
  private boolean reproduzindo;

  /*
   * Métodos da interface
   */
  @Override
  public void play() {
  }

  @Override
  public void pause() {
  }

  @Override
  public void like() {
  }

  /*
   * Métodos especiais
   */

  public Video(String titulo) {
    this.titulo = titulo;
    this.avaliacao = 1;
    this.views = 0;
    this.curtidas = 0;
    this.reproduzindo = false;
  }

  public String getTitulo() {
    return this.titulo;
  }

  public void setTitulo(String titulo) {
    this.titulo = titulo;
  }

  public float getAvaliacao() {
    return this.avaliacao;
  }

  public void setAvaliacao(int avaliacao) {
    int novaAvaliacao = (int) (this.getAvaliacao() + avaliacao) / this.getViews();
    this.avaliacao = novaAvaliacao;
  }

  public int getViews() {
    return this.views;
  }

  public void setViews(int views) {
    this.views = views;
  }

  public int getCurtidas() {
    return this.curtidas;
  }

  public void setCurtidas(int curtidas) {
    this.curtidas = curtidas;
  }

  public boolean isReproduzindo() {
    return this.reproduzindo;
  }

  public boolean getReproduzindo() {
    return this.reproduzindo;
  }

  public void setReproduzindo(boolean reproduzindo) {
    this.reproduzindo = reproduzindo;
  }

}

package Java.Aula09;

public class Livro implements Publicacao {
  /*
   * Atributos
   */
  private String titulo;
  private String autor;
  private int totalPaginas;
  private int paginaAtual;
  private boolean aberto;
  private Pessoa leitor;

  /*
   * Métodos personalizados
   */
  public String detalhes() {
    return "Livro{" + "título=" + titulo + ", autor=" + autor + ", totPaginas=" + totalPaginas + ", paginaAtual="
        + paginaAtual + ", aberto=" + aberto + ", leitor=" + leitor.getNome() + '}';
  }

  /*
   * Métodos especiais
   */
  public Livro(String tituloString, String autorString, int quantidadePaginas, Pessoa leitorPessoa) {
    this.setTitulo(tituloString);
    this.setAutor(autorString);
    this.setTotalPaginas(quantidadePaginas);
    this.setLeitor(leitorPessoa);
  }

  public String getTitulo() {
    return this.titulo;
  }

  public void setTitulo(String titulo) {
    this.titulo = titulo;
  }

  public String getAutor() {
    return this.autor;
  }

  public void setAutor(String Autor) {
    this.autor = Autor;
  }

  public int getTotalPaginas() {
    return this.totalPaginas;
  }

  public void setTotalPaginas(int totalPaginas) {
    this.totalPaginas = totalPaginas;
  }

  public int getPaginaAtual() {
    return this.paginaAtual;
  }

  public void setPaginaAtual(int paginaAtual) {
    this.paginaAtual = paginaAtual;
  }

  public boolean isAberto() {
    return this.aberto;
  }

  public boolean getAberto() {
    return this.aberto;
  }

  public void setAberto(boolean aberto) {
    this.aberto = aberto;
  }

  public Pessoa getLeitor() {
    return this.leitor;
  }

  public void setLeitor(Pessoa leitor) {
    this.leitor = leitor;
  }

  /*
   * Métodos abstratos
   */

  @Override
  public void abrir() {
    this.setAberto(true);
  }

  @Override
  public void fechar() {
    this.setAberto(false);
  }

  @Override
  public void folhear(int pagina) {
    if (pagina > this.getTotalPaginas()) {
      System.out.println("A pagina excede o total de páginas do livro");
      this.setPaginaAtual(0);
      return;
    }

    this.setPaginaAtual(pagina);
  }

  @Override
  public void avancarPagina() {
    if (this.getPaginaAtual() >= this.getTotalPaginas()) {
      System.out.println("O livro terminou");
      return;
    }

    this.setPaginaAtual(this.getPaginaAtual() + 1);

  }

  @Override
  public void voltarPagina() {
    if (this.getPaginaAtual() <= 0) {
      System.out.println("O livro está na primeira página!");
      return;
    }

    this.setPaginaAtual(this.getPaginaAtual() - 1);

  }

}

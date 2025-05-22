package Java.Aula07;

public class Lutador {
  /*
   * Atributos
   */
  private String nome;
  private String nacionalidade;
  private int idade;
  private float altura;
  private float peso;
  private String categoria;
  private int vitorias;
  private int derrotas;
  private int empates;

  /*
   * Métodos personalizados
   */
  public void apresentar() {
    System.out.printf("CHEGOU A HORA! Apresentando %s, diretamente de %s, ", this.getNome(), this.getNacionalidade());
    System.out.printf("com %d anos e medindo %.2fm, ", this.getIdade(), this.getAltura());
    System.out.printf("pesa %.1fkg\n", this.getPeso());
    System.out.printf("Conta com %d vitórias, %d derrotas e %d empates\n", this.getVitorias(), this.getDerrotas(),
        this.getEmpates());
  }

  public void status() {
    System.out.printf("%s\n", this.getNome());
    System.out.printf("Peso: %.1fkg\n", this.getPeso());
    System.out.printf("Categoria: %s\n", this.getCategoria());
    System.out.printf("Vitórias: %d\n", this.getVitorias());
    System.out.printf("Derrotas: %d\n", this.getDerrotas());
    System.out.printf("Empates: %d\n", this.getEmpates());
  }

  public void ganharLuta() {
    this.setVitorias(this.getVitorias() + 1);
  }

  public void perderLuta() {
    this.setDerrotas(this.getDerrotas() + 1);

  }

  public void empatarLuta() {
    this.setEmpates(this.getEmpates() + 1);
  }

  /*
   * Métodos especiais
   */
  public Lutador(String nomeString, String nacionalidadeString, int idade, float altura, float peso, int vitorias,
      int derrotas, int empates) {
    this.setNome(nomeString);
    this.setNacionalidade(nacionalidadeString);
    this.setIdade(idade);
    this.setAltura(altura);
    this.setPeso(peso);
    this.setVitorias(vitorias);
    this.setDerrotas(derrotas);
    this.setEmpates(empates);
  }

  public String getNome() {
    return this.nome;
  }

  public void setNome(String nome) {
    this.nome = nome;
  }

  public String getNacionalidade() {
    return this.nacionalidade;
  }

  public void setNacionalidade(String nacionalidade) {
    this.nacionalidade = nacionalidade;
  }

  public int getIdade() {
    return this.idade;
  }

  public void setIdade(int idade) {
    this.idade = idade;
  }

  public float getPeso() {
    return this.peso;
  }

  public void setPeso(float peso) {
    this.peso = peso;
    this.setCategoria();
  }

  public float getAltura() {
    return this.altura;
  }

  public void setAltura(float altura) {
    this.altura = altura;
  }

  public String getCategoria() {
    return this.categoria;
  }

  private void setCategoria() {
    if (this.getPeso() < 52.2)
      this.categoria = "Inválido";
    else if (this.getPeso() <= 70.3)
      this.categoria = "Leve";
    else if (this.getPeso() <= 83.9)
      this.categoria = "Médio";
    else if (this.getPeso() <= 120.2)
      this.categoria = "Pesado";
    else
      this.categoria = "Inválido";

  }

  public int getVitorias() {
    return this.vitorias;
  }

  public void setVitorias(int vitorias) {
    this.vitorias = vitorias;
  }

  public int getDerrotas() {
    return this.derrotas;
  }

  public void setDerrotas(int derrotas) {
    this.derrotas = derrotas;
  }

  public int getEmpates() {
    return this.empates;
  }

  public void setEmpates(int empates) {
    this.empates = empates;
  }

}

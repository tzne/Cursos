package Java.Aula07;

import java.util.Random;

public class Luta {
  /*
   * Atributos
   */
  private Lutador desafiado;
  private Lutador desafiante;
  private int rounds;
  private boolean aprovada;

  /*
   * Métodos personalizados
   */
  public void marcarLuta(Lutador desafiadoLutador, Lutador desafianteLutador) {
    /* Regras
     * Só pode ser marcada entre lutadores da mesma categoria
     * Desafiado e desafiante devem ser lutadores diferentes
     * Só pode acontecer se estiver aprovada
     * Só pode ter como resultado a vitória de um dos lutadores ou o empate
     */
    if (!desafiadoLutador.getCategoria().equals(desafianteLutador.getCategoria())) {
      System.out.println("Os lutadores são de categorias diferentes! A luta não será marcada");
      return;
    }

    if (desafiadoLutador.equals(desafianteLutador)) {
      System.out.println("Não é possível marcar uma luta entre um lutador e ele mesmo!");
      return;
    }
    
    this.setAprovada(true);
    this.setDesafiante(desafianteLutador);
    this.setDesafiado(desafiadoLutador);

  }

  public void lutar() {
    if (!this.getAprovada()) {
      System.out.println("A luta não foi aprovada");
      return;
    }

    this.getDesafiante().apresentar();
    this.getDesafiado().apresentar();

    Random aleatorio = new Random();
    int vencedor = aleatorio.nextInt(3);
    
    switch (vencedor) {
      case 0: // empate
        System.out.println("Empatou");
        this.desafiado.empatarLuta();
        this.desafiante.empatarLuta();
        break;
      case 1: // desafiado venceu
        System.out.printf("VENCE %s\n", this.getDesafiado().getNome());
        this.desafiado.ganharLuta();
        this.desafiante.perderLuta();
      case 2: // desafiante venceu
        System.out.printf("VENCE %s\n", this.getDesafiante().getNome());
        this.desafiante.ganharLuta();
        this.desafiado.perderLuta();
      default:
        return;
    }
  }

  /*
   * Métodos especiais
   */
  public Luta() {
  }

  public Lutador getDesafiado() {
    return this.desafiado;
  }

  public void setDesafiado(Lutador desafiado) {
    this.desafiado = desafiado;
  }

  public Lutador getDesafiante() {
    return this.desafiante;
  }

  public void setDesafiante(Lutador desafiante) {
    this.desafiante = desafiante;
  }

  public int getRounds() {
    return this.rounds;
  }

  public void setRounds(int rounds) {
    this.rounds = rounds;
  }

  public boolean isAprovada() {
    return this.aprovada;
  }

  public boolean getAprovada() {
    return this.aprovada;
  }

  public void setAprovada(boolean aprovada) {
    this.aprovada = aprovada;
  }

}

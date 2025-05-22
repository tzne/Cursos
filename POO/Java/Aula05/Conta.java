package Java.Aula05;

public class Conta {
  /*
   * Atributos
   */
  public int numConta;
  protected String tipo; // "CC" == conta corrente / "CP" == conta poupanca
  private String dono;
  private float saldo;
  private boolean status;

  /* 
  Métodos personalizados
  */
  public void abrirConta(String tipoString) {
    this.setStatus(true);
    this.setTipo(tipoString);

    if (tipoString == "CC")
      this.saldo = 50;
    else if (tipoString == "CP")
      this.saldo = 150;

    System.out.println("Conta aberta com sucesso");
  }

  public void fecharConta() {
    // todo o saldo deve ser sacado
    // não pode haver débito na conta
    if (this.saldo < 0) {
      System.out.println("Não é possível fechar uma conta em débito");
      return;
    }

    if (saldo > 0) {
      System.out.println("A conta deve estar vazia para ser fechada");
    }

    this.status = false;
    System.out.println("Conta fechada com sucesso");
  }

  public void depositar(float valor) {
    // status deve ser verdadeiro
    if (!this.getStatus()) {
      System.out.println("Não é possível depositar em uma conta inativa");
      return;
    }

    this.saldo += valor;
    System.out.println("O valor voi adicionado ao saldo");
  }

  public void sacar(float valor) {
    // status deve ser verdadeiro
    // saldo tem que ser positivo
    if (!this.getStatus()) {
      System.out.println("Não é possível sacar de uma conta inativa");
      return;
    }

    if (valor >= this.saldo) {
      System.out.println("Saldo insuficiente");
      return;
    }

    this.saldo -= valor;
    System.out.println("Saldo atual: " + this.saldo);
  }

  public void pagarMensal() {
    // conta corrente: 12 reais de mensalidade
    // conta poupança: 20 reais de mensalidade
    if (this.tipo == "CC")
      this.saldo -= 12;
    else if (this.tipo == "CC")
      this.saldo -= 20;
  }

  public void estadoAtual() {
    System.out.println("------------------------------------");
    System.out.printf("Conta: %d\n", this.getNumConta());
    System.out.printf("Tipo: %s\n", this.getTipo());
    System.out.printf("Dono: %s\n", this.getDono());
    System.out.printf("Saldo: R$%.2f\n", this.getSaldo());
    System.out.printf("Status: %b\n", this.getStatus());
    System.out.println("------------------------------------");
  }

  /*
   * Métodos especiais
   */
  public Conta() {
    this.status = false;
    this.saldo = 0;
  }

  public int getNumConta() {
    return this.numConta;
  }

  public void setNumConta(int numConta) {
    this.numConta = numConta;
  }

  public String getTipo() {
    return this.tipo;
  }

  public void setTipo(String tipo) {
    this.tipo = tipo;
  }

  public String getDono() {
    return this.dono;
  }

  public void setDono(String dono) {
    this.dono = dono;
  }

  public float getSaldo() {
    return this.saldo;
  }

  public void setSaldo(float saldo) {
    this.saldo = saldo;
  }

  public boolean isStatus() {
    return this.status;
  }

  public boolean getStatus() {
    return this.status;
  }

  public void setStatus(boolean status) {
    this.status = status;
  }

}

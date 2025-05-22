package Java.Aula04;

public class Caneta {
  public String modelo;
  private float ponta;
  private boolean tampada;
  private String cor;

  public String getModelo() {
    return this.modelo;
  }

  public void setModelo(String modeloString) {
    this.modelo = modeloString;
  }

  public float getPonta() {
    return this.ponta;
  }

  public void setPonta(float fponta) {
    this.ponta = fponta;
  }

  public String getCor() {
    return this.cor;
  }

  public void setCor(String corString) {
    this.cor = corString;
  }

  public boolean isTampada() {
    return this.tampada;
  }

  public void tampar() {
    this.tampada = true;
  }

  

  public void status() {
    System.out.println("Sobre a caneta");
    System.out.printf("Modelo: %s\n", this.getModelo());
    System.out.printf("Ponta: %.1f\n", this.getPonta());
    System.out.printf("Cor: %s\n", this.cor);
    System.out.printf("Está tampada: %b\n", this.tampada);
  }

  public Caneta(String modeloString, String corString, float ponta) { // método construtor
    setModelo(modeloString);
    setCor(corString);
    setPonta(ponta);
    tampar();
  }
}
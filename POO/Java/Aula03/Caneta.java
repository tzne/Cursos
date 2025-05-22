package Java.Aula03;

public class Caneta {
  public String modelo;
  public String cor;
  private float ponta;
  protected int carga;
  protected boolean tampada; 

  public void status() {
    System.out.println("Modelo: " + this.modelo);
    System.out.println("Uma caneta " + this.cor);
    System.out.println("Ponta: " + this.ponta);
    System.out.println("Está tampada? " + this.tampada);
  }

  public void escrever() {

  }

  public void rabiscar() {
    if (this.tampada)
      System.out.println("Estou tampada! Não consigo rabiscar");
    else
      System.out.println("Estou rabiscando...");
  }

  public void pintar() {

  }

  private void tampar() {
    this.tampada = true;
  }

  private void destampar() {
    this.tampada = false;
   }

}

package Java.Aula03;

public class Aula03 {
  public static void main(String[] args) {
    Caneta c1 = new Caneta();

    c1.modelo = "Bic Crystal";
    c1.cor = "Azul";
    // c1.ponta = 0.7f;
    c1.tampada = false;
    c1.carga = 80;

    // c1.tampar();
    c1.status();
    c1.rabiscar();
    // c1.destampar();
    c1.status();
    c1.rabiscar();
  }
}

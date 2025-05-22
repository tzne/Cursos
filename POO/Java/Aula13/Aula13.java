package Java.Aula13;

public class Aula13 {
  public static void main(String[] args) {
   Cachorro dog = new Cachorro();
   
   dog.reagir("Olá");
   dog.reagir("Vai apanhar");
   dog.reagir(11, 45);
   dog.reagir(19, 00);
   dog.reagir(true);
   dog.reagir(false);
   dog.reagir(2, 12.5f);
   dog.reagir(17, 4.5f);
  }
  
}
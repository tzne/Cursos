package Java.Aula11;

public class aula11 {
  public static void main(String[] args) {
    Visitante v1 = new Visitante();
    v1.setNome("Juvenal");
    v1.setIdade(77);
    v1.setSexo("M");
    System.out.println(v1.dados());

    Aluno a1 = new Aluno();
    a1.setNome("Pedro");
    a1.setIdade(19);
    a1.setCurso("Ciência da Computação");
    a1.setMatricula(831597);
    a1.pagarMensalidade();

    Bolsista b1 = new Bolsista();
    b1.setNome("Diogo");
    b1.setMatricula(801596);
    b1.setBolsa(80);
    b1.setSexo("M");
    b1.setIdade(23);
    b1.pagarMensalidade();

  }
}

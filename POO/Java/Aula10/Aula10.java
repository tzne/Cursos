package Java.Aula10;

public class Aula10 {
  public static void main(String[] args) {
    Pessoa p1 = new Pessoa();
    Aluno p2 = new Aluno();
    Professor p3 = new Professor();
    Funcionario p4 = new Funcionario();

    p1.setNome("Pedro");
    p2.setNome("Maria");
    p3.setNome("Cláudio");
    p4.setNome("Fabiana");

    p1.setSexo("M");
    p2.setSexo("F");
    p3.setSexo("M");
    p4.setSexo("F");

    p2.setIdade(18);

    p2.setCurso("Ciência da Computação");
    p3.setSalario(1640);
    p4.setSetor("Coordenação");

    p3.receberAumento(12);

    System.out.println(p1.dados());
    System.out.println(p2.dados());
    System.out.println(p3.dados());
    System.out.println(p4.dados());
  }
}

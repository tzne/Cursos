import java.awt.Dimension;
import java.awt.Toolkit;
import java.util.Date;

public class Ex001 {

    public static void main(String[] args) {
        String data = new Date().toString();
        System.out.println("Hora do sistema: ".concat(data));
        
        String lingua = System.getProperty("user.language");
        System.out.println("Idioma do sitema: ".concat(lingua));
        
        Dimension resolucao = Toolkit.getDefaultToolkit().getScreenSize();
        System.out.println("Resolução do sistema: " + resolucao.getWidth() + "x" + resolucao.getHeight());
    }
}

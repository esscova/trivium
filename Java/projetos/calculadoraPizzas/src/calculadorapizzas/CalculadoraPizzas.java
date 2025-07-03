
package calculadorapizzas;

import java.util.Locale;
import java.util.Scanner;

/*
 * @author escova
 */

public class CalculadoraPizzas {

    public static void main(String[] args) {
       Scanner scanner = new Scanner(System.in);
       scanner.useLocale(Locale.forLanguageTag("pt-BR"));
       
       // variaveis
       int pizzas, pessoas, fatias, sobra, totalFatias, fatiasPessoa;
       
       // entrada de dados
       System.out.println("=== Calculadora de Fatias de Pizza ===");
       
       System.out.print("Número de pizzas: ");
       pizzas = scanner.nextInt();
       
       System.out.print("Quantas pessoas?: ");
       pessoas = scanner.nextInt();
       
       System.out.print("Quantas fatias por pizza? ");
       fatias = scanner.nextInt();
       
       // processamento dos dados
       totalFatias = pizzas * fatias;
       fatiasPessoa = totalFatias / pessoas;
       sobra = totalFatias % pessoas;    
       
       // escrita 
        System.out.println("\nResultados:");
        System.out.println("Total de fatias: " + totalFatias);
        System.out.println("Fatias por pessoa: " + fatiasPessoa + " fatia(s).");
        System.out.println("Fatias que sobram: " + sobra);
        
        scanner.close();
    }
      
}

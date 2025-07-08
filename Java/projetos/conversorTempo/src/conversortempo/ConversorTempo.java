/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package conversortempo;

import java.util.Locale;
import java.util.Scanner;

/**
 *
 * @author escova
 */
public class ConversorTempo {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // dependencias
        Scanner scanner = new Scanner(System.in);
        scanner.useLocale(Locale.forLanguageTag("pt-BR"));
        
        // variaveis
        int totalSegundos, hora, minuto, segundo;
        
        // leitura de dados
        System.out.println("=== Conversor de Tempo ===");
        System.out.print("Digite o total de segundos: ");
        totalSegundos = scanner.nextInt();
        
        // processamento
        hora = totalSegundos / 3600;
        minuto = (totalSegundos % 3600) / 60;
        segundo = totalSegundos % 60;
        
        // escrita
        System.out.printf("\nResultado: %d hora, %d minutos e %d segundos%n", hora, minuto, segundo);
        
        scanner.close();
    }
    
}

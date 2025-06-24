/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package calculadoraidade;

import java.time.Year;
import java.util.Scanner;

/**
 *
 * @author escova
 */
public class CalculadoraIdade {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // variaveis
        int anoNascimento;
        int anoAtual;
        int idade;
        
        // entrada - ano de nascimento
        Scanner scanner = new Scanner(System.in);
        System.out.print("Em que ano você nasceu? ");
        anoNascimento = scanner.nextInt();
        
        // processamento - calcula da idade
        anoAtual = Year.now().getValue();
        idade = anoAtual - anoNascimento;
        
        // saida
        System.out.println("Voce tem " + idade + " anos.");
        
    }
    
}

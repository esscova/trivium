/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package sistemanotas;

import java.util.Locale;
import java.util.Scanner;

/**
 *
 * @author escova
 */
public class SistemaNotas {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        scanner.useLocale(Locale.forLanguageTag("pt-BR"));
        
        // variaveis
        String nome;
        double nota1, nota2, nota3, notaParticipacao, media, notaFinal;
    
        // leitura de dados
        System.out.println("\n=== SISTEMA DE NOTAS ===");
        
        System.out.print("Aluno: ");
        nome = scanner.next();
        
        System.out.print("1ª Nota: ");
        nota1 = scanner.nextDouble();
        
        System.out.print("2ª Nota: ");
        nota2 = scanner.nextDouble();
        
        System.out.print("3ª Nota: ");
        nota3 = scanner.nextDouble();
        
        System.out.print("Nota de participação: ");
        notaParticipacao = scanner.nextDouble();
        
        // processamento
        media = (nota1+nota2+nota3)/3;
        notaFinal = (media*0.7)+(notaParticipacao*0.3);
        
        
        // escrita
        System.err.println("\nResultado: ");
        if(notaFinal>=7.0){
            System.out.printf("O aluno %s passou.\n", nome);
        }else{
            System.out.printf("O aluno %s não passou.\n", nome);
        }
        
        scanner.close();
        
    }
    
}

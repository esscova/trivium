/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package conversortemperatura;

import java.util.Scanner;

/**
 *
 * @author escova
 */
public class ConversorTemperatura {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // variaveis
        float celsius, fahr;
        
        // entrada
        Scanner scanner = new Scanner (System.in);
        System.out.print("Digite a temperatura em Celsius: ");
        celsius = scanner.nextFloat();
        scanner.close();
        
        // processamento
        fahr = (celsius * 9/5) + 32;
        
        // saida
        System.out.println(celsius + "ºC" + " equivale a " + fahr + "ºF");
    }
    
}

package calculadoraviagem;

import java.util.Locale;
import java.util.Scanner;

/**
 *
 * @author escova
 */

public class CalculadoraViagem {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        scanner.useLocale(Locale.forLanguageTag("pt-BR")); 
        
        // variaveis
        double distanciaViagem, consumoCarro, precoGasolina, velocidadeMedia, combustivelNecessario, custo, tempoViagem;
        
        // entrada de dados
        System.out.println("=== Calculadora de Viagem ===");
        
        System.out.print("Distância da Viagem (km): ");
        distanciaViagem = scanner.nextDouble();

        System.out.print("Consumo do Carro (km/l): ");
        consumoCarro = scanner.nextDouble();

        System.out.print("Preço da Gasolina (R$/l): ");
        precoGasolina = scanner.nextDouble();

        System.out.print("Velocidade Média (km/h): ");
        velocidadeMedia = scanner.nextDouble();
        
        // processamento de dados
        combustivelNecessario = distanciaViagem / consumoCarro;
        custo = combustivelNecessario * precoGasolina;
        tempoViagem = distanciaViagem / velocidadeMedia;
        
        // escrita de dados
        System.out.println("\nResultado:");
        System.out.printf("Combustível necessário: %.1f litros%n", combustivelNecessario);
        System.out.printf("Custo: R$ %.2f%n", custo);
        System.out.printf("Tempo de viagem: %.2f horas%n", tempoViagem);
        System.out.println();
        
        scanner.close();
    }
    
}

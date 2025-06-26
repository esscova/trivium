/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package cadastroproduto;
import java.util.Locale;
import java.util.Scanner;

/**
 *
 * @author escova
 */
public class CadastroProduto {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        scanner.useLocale(Locale.forLanguageTag("pt-BR")); 

        // Variáveis
        String produto;
        double preco, valor_total;
        int quantidade;
        char categoria;
        boolean promocao;

        // Leitura
        System.out.print("=== CADASTRO DE PRODUTOS ===\nPRODUTO: ");
        produto = scanner.nextLine();

        System.out.print("PREÇO: ");
        preco = scanner.nextDouble();
        scanner.nextLine(); // Limpar o buffer

        System.out.print("QUANTIDADE: ");
        quantidade = scanner.nextInt();
        scanner.nextLine(); // Limpar o buffer

        System.out.print("CATEGORIA (primeira letra): ");
        categoria = scanner.nextLine().charAt(0); // Apenas a primeira letra

        System.out.print("ESTÁ EM PROMOÇÃO? (true/false): ");
        promocao = scanner.nextBoolean();
        scanner.nextLine(); // Limpar o buffer

        // Processamento
        valor_total = preco * quantidade;

        // Escrita
        System.out.println("\n=== PRODUTOS ===");
        System.out.println("Nome do produto: " + produto);
        System.out.println("Preço unitário: " + preco);
        System.out.println("Quantidade em estoque: " + quantidade);
        System.out.println("Categoria: " + categoria);
        System.out.println("Está em promoção?: " + promocao);
        System.out.println("Valor total em estoque: $" + valor_total);

        scanner.close();
    }
    
}

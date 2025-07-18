
package calculosalario;

import java.util.Locale;
import java.util.Scanner;

/**
 *
 * @author escova
 * @date 2025-07-18
 * @description Calcular salario liquido de um funcionario.
 */
public class CalculoSalario {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        scanner.useLocale(Locale.forLanguageTag("pt-BR"));

        // Variáveis
        String nomeFuncionario;
        double salarioBruto, valorHoraExtra, totalHorasExtras, salarioExtras, desconto, salarioLiquido;
        int horasExtras;

        // Leitura
        System.out.println("\n=== CALCULADORA DE SALÁRIO LÍQUIDO ===");
        System.out.print("Digite o nome do funcionário: ");
        nomeFuncionario = scanner.nextLine();

        System.out.print("Digite o salário bruto: ");
        salarioBruto = scanner.nextDouble();

        System.out.print("Quantas horas extras trabalhadas? ");
        horasExtras = scanner.nextInt();

        System.out.print("Qual valor da hora extra? ");
        valorHoraExtra = scanner.nextDouble();

        // Processamento
        totalHorasExtras = horasExtras * valorHoraExtra;
        salarioExtras = salarioBruto + totalHorasExtras;
        desconto = salarioExtras * 0.08;
        salarioLiquido = salarioExtras - desconto;

        // Escrita
        System.out.printf("\n=== SALÁRIO LÍQUIDO DE: %s ===\n", nomeFuncionario);
        System.out.printf("Horas Extras: R$%.2f\n", totalHorasExtras);
        System.out.printf("Salário Total: R$%.2f\n", salarioExtras);
        System.out.printf("Desconto INSS (8%%): R$%.2f\n", desconto);
        System.out.printf("Salário Líquido: R$%.2f\n", salarioLiquido);

        scanner.close();
    }
}
# Fazendo Contas com Java: Expressões e Operadores Matemáticos

## Introdução

Sabe quando você está no supermercado e faz a conta de quantos produtos pode comprar com o dinheiro que tem? Ou quando calcula quantos minutos faltam para um compromisso? Esses raciocínios envolvem **expressões matemáticas** — e os programas também fazem isso!

Em Java, usamos **operadores matemáticos** para realizar contas simples e combinar valores que estão nas variáveis. Neste material, vamos entender como isso funciona de maneira bem prática.

---

## O Que São Operadores?

**Operadores** são símbolos que indicam qual operação matemática queremos fazer. Assim como usamos o símbolo `+` para somar ou `-` para subtrair em papel, usamos esses mesmos sinais no código.

### Principais Operadores em Java:

| Operador | Significado      | Exemplo     |
| -------- | ---------------- | ----------- |
| `+`      | Soma             | `5 + 3 = 8` |
| `-`      | Subtração        | `5 - 2 = 3` |
| `*`      | Multiplicação    | `4 * 2 = 8` |
| `/`      | Divisão          | `8 / 2 = 4` |
| `%`      | Resto da divisão | `7 % 2 = 1` |

---

## O Que São Expressões?

Uma **expressão** é como uma conta matemática que combina variáveis, valores e operadores para chegar a um resultado.

### Exemplo do cotidiano:

Se você tem 2 pacotes com 4 maçãs em cada um, você faz a conta: `2 * 4 = 8`.
Essa é uma expressão que representa uma ideia simples: multiplicar.

---

## Exemplo Prático com Variáveis

Vamos imaginar que você está organizando uma pequena festa e quer calcular:

* Quantas pessoas você convidou
* Quantos refrigerantes comprar
* Qual será o custo total

```java
int convidados = 10;
int refrigerantesPorPessoa = 1;
double precoPorRefrigerante = 5.0;

int totalRefrigerantes = convidados * refrigerantesPorPessoa;
double custoTotal = totalRefrigerantes * precoPorRefrigerante;

System.out.println("Total de refrigerantes: " + totalRefrigerantes);
System.out.println("Custo total da compra: R$ " + custoTotal);
```

Neste exemplo:

* Usamos `*` para multiplicar o número de pessoas pelo número de bebidas.
* Calculamos o valor total com outra multiplicação.

---

## Cuidado com a Divisão

Se você dividir dois números inteiros, o resultado será um número **inteiro** (sem casas decimais). Isso pode causar confusão.

```java
int resultado = 5 / 2; // O resultado será 2 (e não 2.5!)
```

Se quiser um resultado com vírgula (ponto), use `double`:

```java
double resultado = 5.0 / 2; // Agora o resultado será 2.5
```

---

## Usando o Operador de Resto (%)

Esse operador mostra **o que sobra** de uma divisão. Ele é útil para várias situações:

### Exemplo:

Você tem 10 balas para dividir entre 3 crianças. Cada uma recebe 3 balas, e sobra 1.

```java
int sobra = 10 % 3; // sobra = 1
```

---

## Expressão Completa em Situação Real

Vamos juntar tudo em um exemplo final:

### Situação:

Você quer saber quantos dias, semanas e o que sobra ao converter 45 dias de férias.

```java
int diasFérias = 45;

int semanas = diasFérias / 7;
int diasSobrando = diasFérias % 7;

System.out.println("Você tem " + semanas + " semanas completas e " + diasSobrando + " dias de férias restantes.");
```

> Resultado:
> Você tem 6 semanas completas e 3 dias de férias restantes.

---

## Resumo Simples

* Operadores são símbolos usados para fazer contas (`+`, `-`, `*`, `/`, `%`)
* Expressões combinam operadores e variáveis para gerar resultados.
* Divisões entre inteiros descartam as casas decimais.
* O operador `%` mostra o que sobra de uma divisão.

---

## Próximos Passos

Agora que você já sabe criar variáveis e fazer contas com elas, o próximo passo é aprender a **tomar decisões no programa**, como:

> “Se o aluno tirou mais de 7, ele passou?”
> Esse é o papel das **estruturas de decisão**, tema do próximo material.

---

*Dica: sempre que você estiver resolvendo uma conta no dia a dia, tente imaginar como faria isso usando variáveis e operadores. Com a prática, você vai transformar qualquer problema em código com facilidade!*

# Guardando Informações: O Que São Variáveis?

## Introdução

Imagine que você tem várias **caixinhas com etiquetas** na sua casa. Em uma delas, você guarda canetas; em outra, moedas; em outra, papéis importantes. Cada caixinha tem um tipo específico de coisa que pode ser guardada.

Na programação, usamos um conceito parecido: as **variáveis**. Elas são como caixinhas com nome, que guardam algum valor que pode ser usado e até alterado durante o programa.

Vamos entender melhor como isso funciona em Java?

---

## O Que São Variáveis?

Uma **variável** é um espaço na memória do computador onde guardamos alguma informação. Pode ser um número, uma palavra, uma letra ou um valor lógico (verdadeiro ou falso). O importante é: cada variável tem um **tipo** (o que ela pode guardar) e um **nome** (para sabermos como acessá-la).

### Analogias do dia a dia:

* Uma etiqueta em um pote de arroz: o pote é a variável, a etiqueta é o nome, e o arroz é o conteúdo (valor).
* O contato “mãe” no seu celular: o nome é “mãe”, e o conteúdo pode ser o número de telefone dela.
* A memória de um GPS: guarda a posição atual, o destino, a velocidade.

---

## Como Criamos Variáveis em Java?

Para criar uma variável em Java, usamos uma estrutura parecida com esta:

```java
tipo nomeDaVariavel = valor;
```

Ou seja: dizemos qual o tipo de informação, damos um nome à caixinha e colocamos um valor dentro dela.

### Exemplos Simples:

```java
int idade = 25;           // Guarda um número inteiro
double altura = 1.70;     // Guarda um número com vírgula (ponto)
char inicial = 'A';       // Guarda um único caractere
String nome = "Ana";      // Guarda um texto
boolean estudante = true; // Guarda verdadeiro ou falso
```

Cada variável tem:

* **Um tipo:** para saber que tipo de dado ela pode guardar.
* **Um nome:** para podermos chamá-la quando precisarmos.
* **Um valor:** que é o conteúdo guardado.

> **Observação**: No caso do `char`, usamos aspas simples e guardamos apenas **uma letra**. Ele é diferente do `String`, que guarda textos mais longos com aspas duplas.

---

## Como Usamos Variáveis?

Uma vez que a informação está guardada, podemos usá-la para mostrar mensagens, fazer contas ou tomar decisões.

```java
String nome = "João";
System.out.println("Bem-vindo, " + nome);
```

Aqui, o programa mostra:
**Bem-vindo, João**

Ou seja, ele usou o conteúdo da variável `nome` para completar a frase.

---

## Boas Práticas para Nomear Variáveis

Assim como organizamos melhor as coisas quando usamos nomes claros nas etiquetas das caixas, também organizamos melhor nossos códigos com boas práticas:

* Use **nomes claros**: `idadePessoa`, `precoProduto`, `notaFinal`
* Escreva usando o **padrão camelCase**: a primeira palavra com letra minúscula, e as próximas com maiúscula.
* **Não use espaços**: nomes de variáveis não podem ter espaço.
* Evite abreviações confusas: `valorDesconto` é melhor que `vlrDscnto`.

---

## Exemplo Prático Unificado

Vamos ver um exemplo simples, usando variáveis para calcular o tempo de viagem de um carro:

### Situação:

Você quer saber quanto tempo vai levar para viajar de uma cidade para outra, sabendo a distância e a velocidade média do carro.

```java
// Informações
double distanciaKm = 150.0; // A distância da viagem, em km
double velocidadeKmH = 75.0; // A velocidade média, em km/h

// Cálculo
double tempoHoras = distanciaKm / velocidadeKmH;

// Resultado
System.out.println("Tempo estimado de viagem: " + tempoHoras + " horas");
```

O programa usa três variáveis para resolver a situação. Perceba como os nomes ajudam a entender o que está acontecendo.

---

## Resumo Simples

* Variáveis são como caixinhas que guardam informações temporárias durante a execução do programa.
* Cada variável tem um tipo (int, double, char, String, boolean) e um nome.
* Usamos variáveis para armazenar dados, realizar operações e gerar respostas.
* Boas práticas de nomeação tornam o código mais claro e organizado.

---

## Próximos Passos

Agora que você sabe guardar e usar informações, é hora de aprender como fazer **contas e expressões com essas variáveis**, usando os **operadores matemáticos**. Esse será o nosso próximo tema, e ele é fundamental para todo tipo de cálculo ou lógica em programação.

---

*Dica: Sempre que quiser organizar algo no programa — um nome, um número, uma letra, uma escolha — pense: “isso pode ser uma variável?” Se a resposta for sim, você já sabe como criar e usar uma!*

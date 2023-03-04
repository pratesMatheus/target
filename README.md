<h1 align="center">target</h1>

## Questão 1:

Observe o trecho de código abaixo:

```
int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça
{
K = K + 1;
SOMA = SOMA + K;
}

imprimir(SOMA);
```

Ao final do processamento, qual será o valor da variável SOMA? A resolução foi feita em JS e foi algo bem simples, retornando o resultado **91**

## Questão 2

Dado a **sequência de Fibonacci**, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

A resolução foi feita em Python, optei pela linguagem por conta da sintaxe e sua legibilidade. Esse foi o retorno:

```
==================================================
Sequência de Fibonacci
==================================================
Digite para mim quantos termos você deseja mostrar? 10
-------------------------
0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8 -> 13 -> 21 -> 34 -> the end...
```

## Questão 3

Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:

- O menor valor de faturamento ocorrido em um dia do mês;
- O maior valor de faturamento ocorrido em um dia do mês;
- Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:

- a - Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
- b - Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

Novamente, optei pelo Python pela sintaxe e legibilidade do código alto nível, esses foram os valores retornados:

```
- Menor valor de faturamento ocorrido em um dia do mês: 0.0
- Maior valor de faturamento ocorrido em um dia do mês: 46251.1749
- N° de dias/M onde o faturamento p/dia superou a média mensal: 9
```

## Questão 4

Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

- SP – R$67.836,43
- RJ – R$36.678,66
- MG – R$29.229,88
- ES – R$27.165,48
- Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

```
==================================================
Calculando o parcelamento mensal de uma distribuidora
==================================================
Faturamento de SP em &: 37.53%
-------------------------
Faturamento de RJ em &: 20.29%
-------------------------
Faturamento de MG em &: 16.17%
-------------------------
Faturamento de ES em &: 15.03%
-------------------------
Outros faturamentos em %: 10.98%
==================================================
```

## Questão 5

Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:

- a - Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
- b - Evite usar funções prontas, como, por exemplo, reverse;

**NOTA**: Fiz questão de me desafiar e resolvi fazer a quinta questão em JS, por ter uma função integrada (built-in function) chamada `reverse()` que já usei em um projeto anterior (para verficar se o nome de um usuário era ou não um palíndromo). Esse foi o retorno.

Segue o script usado:

```JS
const reverseStr = (txt) => {
  let newStr = "";

  for (let i = txt.length - 1; i >= 0; i--) {
      newStr += txt[i];
  }

  return newStr;
}

reverseStr('hello world');//'dlrow olleh'
reverseStr('matheus'); //'suehtam'
reverseStr('sql'); //'lqs'
reverseStr('target'); //'tegrat'
```

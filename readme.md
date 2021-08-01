# Projeto de P2 (programação orientada à objeto)

O objetivo do trabalho é seguir as especificações do arquivo [Folha_de_pagamento.pdf] para poder escrever as classes necessárias apra implementar o sistema.

[Folha_de_pagamento.pdf]: <Folha_de_pagamento.pdf>

## Sistema de folha de pagamento

Consiste em gerenciar os dados dos empregados e os pagamentos à estes empregados, como cartões de ponto. Os empregados devem receber o salário no momento correto, ao modo que escolherem e obedecer várias taxas e impostos no salário.

* Os empregados que recebem por hora trabalhada
   * Submetem de 'cartões de ponto' todo dia para informar número de horas trabalhadas naquele dia
   * Se empregados trabalhar mais que 8 horas, deve receber 1.5 vezes a taxa por hora. 
   * São pagos toda sexta-feira

* Os empregados assalariados
  *  Recebem salário fixo mensal que
  *  São pagos no último dia do mês.

* Os empregados comissionados recebem um percentual das vendas que realizam.
  * Submetem o resultado das vendas
    * Valor da venda
    * Data da venda
  * O valor da percentagem da comissão varia de empregados para empregado
  * São pagos a cada 2 sexta-feiras
    * Nesse período devem receber o equivalente a 2 semanas de salário fixo somados às comissões do período

  * Escolher o método de pagamento
    * Receber um cheque pelo correio
    * Cheque em mãos
  * Depósito em conta bancária

* Alguns funcionários pertencem ao sindicato, o sindicato:
  * Cobra taxa mensal ao funcionário
    * Varia entre empregados
  * A taxa sindical é reduzida do salário
  * Pode cobrar taxas de serviços adicionais a um empregado
    * São submetidas mensalmente e são reduzidas no próximo contracheque do empregado
  * Deve haver um sistema à parte do empregados ao sindicato
  
* A folha de pagamento é rodada todo dia
  * Deve pagar os funcionários cujos salários vencem naquele dia
  * O sistema receberá a data até qual o pagamento deve ser feito e calculará o pagamento para cada empregado desde a última vez em que este foi pago


## As funções que existem no sistema

1. Adição de um empregado
   * Nome, Endereço, Tipo de empregado (hourly, salaried, commissioned), Atributos associados (salário por horário, salário mensal ou comissão)
   * Um número de empregado deve ser escolhido pelo sistema

1. Remoção de um empregado
   * Remover um empregado do sistema

1. Lançar um cartão de ponto
   * Associará cartão de ponto ao empregado correto

1. Lançar resultado de venda
   * Associará informação de venda ao funcionário correto

1. Lançar taxa de serviço
   * Anotará taxa de serviço e associará ao funcionário correto

1. Alterar detalhes de um empregado
   * Os seguinte atributos podem ser alterados
     * Nome, Endereço, Tipo, Método de pagamento, Se pertence ao sindicato ou não, indentificação no sindicato, taxa sindical

2. Rodar folha de pagamento para hoje
   * O sistema deve achar todos os empregados que devem ser pagos no dia
     * Deve calcular o valor do salário
     * Providenciar pagamento de acordo com método de pagamento escolhido pelo empregado

3. Undo/Redo
   * Qualquer funcionalidade feita entre as relações 1 - 7
     * Undo - Desfeitas
     * Redo - Refeita

4. Agenda de pagamento
   * Empregados podem selecionar a agenda de pagamento que desejarem
   * Por default as agendas "semanalmente", "mensalmente" e "bi-semanalmente" são usadas
   * Um empregados pode pedir para ser pago com qualquer uma dessas agendas

5. Criação de novas agendas de pagamento
   * Criar uma agenda de pagamento para ser disponibilizada para os empregados
   * Uma agenda é especificada através de uma string
     * Exemplo de novas agendas de pagamento
       * 'mensal 1', dia 1 de todo mês, 'mensal $', útlimo dia de todo mês
       * 'semanal 1 segunda', toda semana às segundas-feiras
       * 'semanal 2 sexta', a cada 2 semanas às sextas-feiras
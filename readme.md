# Projeto de P2 (programação orientada à objeto)

O objetivo do trabalho é seguir as especificações do arquivo [Folha_de_Pagamento.pdf] para poder escrever as classes necessárias apra implementar o sistema.

[Folha_de_Pagamento.pdf]: <./Folha_de_Pagamento.pdf>

## Funções adicionadas ao sistema

O sistema é inicializado utilizando o objeto `QueueSystem()` que é atribuído a uma variável, que no exemplo é chamada de `system`.

1. Para poder adicionar um empregado, utiliza-se o método `add_employee`
   1. Os atribuos `name, address, type e param` são necessários. 
   2. O atributo **name** é o nome do empregado
   3. O atributo **address** é o endereço do empregado
   4. O atributo **param** é o parâmetro do tipo do empregado (ex. quando o empregado for *salaried*, **param** é o salário do empregado).

Todos os empregados, ao serem adicionados são atribuídos uma identificação, um id. Cada empregado detém um id diferente dos que já existem no banco de dados dos empregados.

2. Para remover um empregado utiliza-se o **id do mesmo** e a chamada do método `del_employee`, que automaticamente remove um empregado que possúi o dado id.

3. Para lançar o cartão de ponto utiliza-se a chamada do método `launch_timecard`. 
   1. Os atributos `id, hours` são necessãrios.
   2. O **id** é o id do empregado que será adicionado o cartão de ponto 
   3. E as **hours** são as horas que foram trabalhadas no dia.

4. Para lançar um resultado de venda, utiliza-se o método `launch_selling`
   1. No método, são necessárias os atributos `id, price, date`
   2. O **id** é o id do empreagdo que se deseja lançar o resultado de venda
   3. O **price** é o preço do produto que foi vendido
   4. A **date** é a data à qual foi vendida o produto

5. Para lançar uma taxa de serviço, utiliza-se o método `launch_service_charge`
   1. São necessários os atributos `id, charge`
   2. O **id** é o id do empregado
   3. O atributo **charge** é a cobrança adicional que será realizada

6. Para alterar os detalhes dos empregados, utiliza-se o método `change_employee_data`
   1. Nele, é necessário adicionar os atributos `id, dict`
   2. O **id** é o id do empregado que se necessita alterar os dados
   3. O **dict** é o dicionário em python dos atributos que se necessita alterar os dados, os possíveis parâmetros são:
      * `name, address, payment_method, syndicate, syndicate_id, syndicate_charge`
      * O **name** é para mudar o nome
      * O **address** é para mudar o endereço
      * O **payment_method** é para mudar o método de pagamento
      * O **syndicate** é para mudar se pertence ao sindicato ou não
      * O **syndicate_id** é para mudar a identificação sindical
      * O **syndicate_charge** é para mudar a cobrança sindical 

7. Para modificar o tipo de empregado, utiliza-se a chamada de função `change_employee_type`
   1. Colocam-se os parâmetros `id, type`
   2. O parâmetro **id** é o id do funcionário que se deseja mudar o tipo
   3. O parâmetro **type** é o tipo do empregado que se deseja modificar para, os tipos são: **Salaried**, **Commissioned**, **Hourly**

8. Para mudar o tipo da agenda de pagamento, é necessário chamar o método `change_payment_schedule`
   1. Os atributos `id, new_schedule` são necessários
   2. O atributo **id** é o id do pagamento que será modificado
   3. O atributo **new_schedule** é a nova agenda de pagamento
      1. As agendas de pagamentos podem ser mensais, como exemplo:
         1. `mensal 1` - todo o primeiro dia do mês
         2. `mensal 3` - todo o terceiro dia do mês
         3. `mensal $` - todo o último dia do mês
         4. Pode ser em inglês também, ex.: `monthly 1`
      2. Ter pagamentos semanais, como exemplo:
         1. `semanal 2 sexta` - toda sexta a cada duas semanas
         2. `semanal 1 quarta` - toda quarta todas as semanas
         3. Também poder se a agenda em inglês, ex.: `weekly 2 friday`

9.  Para atualizar a numeração do dia, ir para o dia seguinte, utiliza-se a chamada de função `update_day`. Essa função é necessária para que os dias sigam no sistema.

10. Para rodar a folha de pagamento para hoje é necessário realizar a chamada de função `run_today_payroll`, com ela se realizará o pagamento de todos os funcionários do dia.

11. Sistema de undo/redo que poderá desfazer ou refazer alterações feitas no banco de dados
    1. Com o método `undo`, desfaz a última alteração feita no sistema
    2. Com o método `redo`, refaz a última alteração desfeita no sistema

12. Existe o método `write`. O sistema que se pode utilizar é o `QueueSystem`, nele as ações realizadas por meios de funções são somente adicionadas a uma fila que será escrita no sistema, por meio da chamada de função `write`. Com a função write, cria-se um novo sistema de pagamento que irá sobrepor o antigo, e adicionará à lista de escrita.
    1. Com isso, o que ocorre é que para escrever as mudanças no sistema, é necessário chamar a função write para que se possa alterar os atributos atuais.

13. Existe a função `print` que imprime na tela as funções que estão na fila, a função `print_payroll` que imprime o último estado escrito no sistema de pagamento, e a função `print_payroll_calendar` que imprime o calendário do último estado escrito do sistema de pagamento.

14. Existe ainda o método `search_by_name` que dispõe para o usuário o **id** do empregado através do **nome**. Ele procura somente no último estado escrito do sistema, portanto é necessário a chamad do método `write`, anteriormente.


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

2. Remoção de um empregado
   * Remover um empregado do sistema

3. Lançar um cartão de ponto
   * Associará cartão de ponto ao empregado correto

4. Lançar resultado de venda
   * Associará informação de venda ao funcionário correto

5. Lançar taxa de serviço
   * Anotará taxa de serviço e associará ao funcionário correto

6. Alterar detalhes de um empregado
   * Os seguinte atributos podem ser alterados
     * Nome, Endereço, Tipo, Método de pagamento, Se pertence ao sindicato ou não, indentificação no sindicato, taxa sindical

7. Rodar folha de pagamento para hoje
   * O sistema deve achar todos os empregados que devem ser pagos no dia
     * Deve calcular o valor do salário
     * Providenciar pagamento de acordo com método de pagamento escolhido pelo empregado

8. Undo/Redo
   * Qualquer funcionalidade feita entre as relações 1 - 7
     * Undo - Desfeitas
     * Redo - Refeita

9. Agenda de pagamento
   * Empregados podem selecionar a agenda de pagamento que desejarem
   * Por default as agendas "semanalmente", "mensalmente" e "bi-semanalmente" são usadas
   * Um empregados pode pedir para ser pago com qualquer uma dessas agendas

10. Criação de novas agendas de pagamento
   * Criar uma agenda de pagamento para ser disponibilizada para os empregados
   * Uma agenda é especificada através de uma string
     * Exemplo de novas agendas de pagamento
       * 'mensal 1', dia 1 de todo mês, 'mensal $', útlimo dia de todo mês
       * 'semanal 1 segunda', toda semana às segundas-feiras
       * 'semanal 2 sexta', a cada 2 semanas às sextas-feiras

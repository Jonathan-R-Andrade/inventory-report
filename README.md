# Inventory Reports

Projeto desenvolvido por [Jonathan R. Andrade](https://www.linkedin.com/in/jonathan-r-andrade/) na [Trybe](https://www.betrybe.com/).

## Sobre

Gerador de relatórios escrito em Python que recebe como entrada arquivos de vários formatos contendo dados de um estoque e gera, como saída, um relatório sobre estes dados.

Os formatos de entrada dos arquivos suportados são: `.xml`, `.csv` e `.json`. É possível adicionar novos formatos de entrada facilmente graças ao uso do padrão de projeto [Strategy](https://refactoring.guru/pt-br/design-patterns/strategy), utilizado nas classes de importação de dados. Outro padrão de projeto, utilizado na classe ColoredReport, foi o [Decorator](https://refactoring.guru/pt-br/design-patterns/decorator) para adicionar cor ao relatório sem precisar fazer grandes alterações no código.

## Habilidades desenvolvidas

* Aplicar conceitos de Orientação a Objetos em Python;
* Aplicar padrões de projeto;
* Ler e escrever arquivos XML, CSV e JSON;
* Escrever testes unitários em Python.

## Ferramentas/Tecnologias utilizadas

* Python v3.10.6
* Docker v24.0.2

## Como executar

Siga os passos abaixo executando os comandos no terminal.

1. Clone o repositório.

    * Exemplo com Git + HTTPS
      ```bash
      git clone https://github.com/Jonathan-R-Andrade/inventory-report.git
      ```
    * Exemplo com Git + SSH
      ```bash
      git clone git@github.com:Jonathan-R-Andrade/inventory-report.git
      ```
    * Usando GitHub CLI
      ```bash
      gh repo clone Jonathan-R-Andrade/inventory-report
      ```

2. Entre na pasta do projeto.

      ```bash
      cd inventory-report
      ```

3. Prepare o ambiente usando o Python instalado localmente ou o Docker.

   * <details>
       <summary>Usando o Python instalado localmente.</summary>

       1. Crie o ambiente virtual.
       ```bash
       python3 -m venv .venv
       ```

       2. Ative o ambiente virtual.
       ```bash
       source .venv/bin/activate
       ```

       3. Instale as dependências.
       ```bash
       python3 -m pip install -r dev-requirements.txt
       ```

       4. Instale o projeto.
       ```bash
       python3 -m pip install .
       ```
     </details>

   * <details>
       <summary>Usando o Docker.</summary>

       1. Crie a imagem.
       ```bash
       docker image build -t inventory-report .
       ```

       2. Inicie o contêiner.
       ```bash
       docker run --name inventory-report -it inventory-report bash
       ```
       > O comando acima cria um contêiner com o nome `inventory-report` e abre um terminal interativo dentro dele, execute os próximos comandos neste terminal.
     </details>

4. Execute o gerador de relatórios.

    > __O comando usado para executar o gerador de relatórios é `inventory_report`, ele recebe como argumento o caminho para um arquivo e uma string (`simples` ou `completo`) que representa o tipo de relatório a ser gerado.__

  * Exemplo de um relatório simples usando um arquivo CSV.
    ```bash
    inventory_report inventory_report/data/inventory.xml simples
    ```

  * Exemplo de um relatório completo usando um arquivo JSON.
    ```bash
    inventory_report inventory_report/data/inventory.json completo
    ```

5. Execute os testes.

    > Poucos testes foram escritos para este projeto, apenas para demonstrar o uso de testes unitários em Python.

    ```bash
    python3 -m pytest
    ```

    Ou simplesmente.

    ```bash
    pytest
    ```

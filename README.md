# Datarisk Data Engineering Challenge

## Apresentação

Olá candidato(a), esse é o desafio prático para o time de **Engenharia de dados** da Datarisk!

O objetivo desse desafio é entendermos melhor o seu nível técnico, então sugerimos um projeto que utiliza ferramentas bastante comuns na vida de um engenheiro de dados.

O desafio segue uma ideia simples à princípio, mas você pode encontrar algumas dificuldades no meio do caminho. Por isso, **não hesite** em propor qualquer solução diferente para chegar em seu objetivo final.

O importante é **entregar o que você conseguir fazer**, com a devida documentação.

## Desafio

Segue abaixo uma lista de desafios abrangendo vários pontos presentes no dia a dia de um engenheiro de dados. **Sinta-se livre para ir além** das ferramentas pré-determinadas e construir a solução que melhor se aplica ao seu ver.

- Fazer a configuração do **Apache Airflow** e **PostgreSQL** em seu computador com Docker.
    - Sugestão: [Docker Compose](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html).
- Criar um processo de **ETL** (Extract, Transform, Load) no **Apache Airflow**, utilizando dados de **corridas de táxi** de Nova York.
    - Disponível em: [nyc-tlc-data](https://github.com/datarisk-io/data-engineering-challenge/tree/master/nyc-tlc-data).
- Armazenar os dados no banco de dados **PostgreSQL**.
    - Sugestão: organizar os dados em camadas de processamento (raw, trusted, refined).
- Responder às seguintes questões:
    1. Qual o total de registros na tabela final?
    2. Qual o total de viagens iniciadas e finalizadas no dia 17 de junho?
    3. Qual foi o dia da viagem mais longa percorrida?
    4. Qual a média, o desvio padrão, o mínimo, o máximo e os quartis da distribuição de distância percorrida nas viagens totais?
- Criar um **README** contendo os passos do processo, decisões tomadas e as respostas das questões passadas junto com as queries SQL utilizadas.
    - Sugestão: Markdown.

## Solução

Para realizar a entrega desse desafio, você deve fazer um fork desse repositório para sua conta pessoal e armazenar o código e documentação do projeto neste repositório, no diretório `challenge`.

## Dúvidas

Caso tenha alguma dúvida ou sugestão, sinta-se a vontade para abrir uma `issue` nesse repositório.
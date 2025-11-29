# Sistema de Cadastro de Clientes 💻
Este projeto implementa um sistema CRUD completo para gerenciamento de clientes usando Python, funcionando totalmente no terminal.
O sistema permite cadastrar, visualizar, atualizar, remover e analisar registros.

## Funcionalidades

### 1. Cadastrar cliente

Permite inserir um novo cliente informando nome, telefone e serviço contratado.

Obs: Os registros são armazenados em uma lista de dicionários e recebem um ID sequencial automático.


### 2. Listar clientes

Exibe todos os clientes em formato tabular, incluindo:

• ID;

• Nome;

• Telefone;

• Serviço contratado.

### 3. Atualizar cliente

Permite alterar os dados de um cliente existente.

O usuário informa o ID, e então pode editar nome, telefone e serviço (ou deixar em branco para manter).


### 4. Remover cliente

Exclui um cliente da lista usando o ID.

O programa solicita confirmação antes de remover.



### 5. Relatório

Gera uma análise rápida, mostrando:

• Total de clientes cadastrados;

• Quantidade de clientes por serviço;

• Identificação do serviço mais contratado.


Obs: O relatório utiliza collections.Counter para estatísticas.



### 6. Sair

Encerra o programa de forma segura.



#### • Armazenamento Persistente.

#### • O sistema grava os dados automaticamente no arquivo "clientes.json".

Isso permite que os registros permaneçam salvos mesmo após fechar o programa.


### Tecnologias Utilizadas


#### Python:

• Biblioteca padrão (json, os, collections.Counter);

• Estruturas fundamentais: funções, listas, dicionários, loops e condicionais.


## Exemplo de Uso


### Passo 1 – Iniciar o sistema

O programa é executado e exibe o menu principal com seis opções.

O usuário observa o menu e decide qual ação deseja realizar.


### Passo 2 – Cadastrar um cliente

1. O usuário escolhe a opção 1 – Cadastrar cliente.

2. O sistema solicita o nome do cliente.

O usuário digita: “João da Silva”.

3. O sistema solicita o telefone.

O usuário insere: (86) 98888-7777.

4. O sistema solicita o serviço contratado.

O usuário informa: Internet Fibra 500Mb.

5. O sistema confirma o cadastro e gera automaticamente o ID 1.


### Passo 3 – Listar todos os clientes

1. O usuário retorna ao menu principal.

2. Seleciona a opção 2 – Listar clientes.

3. O sistema exibe uma tabela contendo:

ID: 1

Nome: João da Silva

Telefone: (86) 98888-7777

Serviço: Internet Fibra 500Mb


### Passo 4 – Atualizar um cliente

1. No menu, o usuário seleciona 3 – Atualizar cliente.

2. O sistema solicita o ID.

O usuário informa: 1.

3. O sistema exibe os dados atuais e permite alterar cada campo.

4. O usuário atualiza:

Nome: João da Silva Filho

Telefone: (mantém o mesmo)

Serviço: Internet Fibra 700Mb

5. O sistema confirma a atualização.


### Passo 5 – Remover um cliente

1. No menu, o usuário escolhe 4 – Remover cliente.

2. O sistema solicita o ID.

O usuário insere: 1.

3. O sistema pede confirmação.

O usuário digita: s.

4. O registro é removido com sucesso.


### Passo 6 – Gerar relatório

1. O usuário seleciona a opção 5 – Relatório.

2. O sistema exibe:

Total de clientes cadastrados

Quantidade por serviço

Serviço mais contratado

Se não houver clientes, o sistema informa que a lista está vazia.


### Passo 7 – Encerrar o sistema

1. O usuário seleciona 6 – Sair.

2. O sistema encerra e mostra a mensagem:
“Saindo… Até mais!”


## Autores:

Projeto desenvolvido como requisito da disciplina Programação – Python

Curso: Engenharia de Software

Instituição: Centro Universitário Santo Agostinho

Dupla: João Vitor Rodrigues Santos e Júlia Beatriz Borges




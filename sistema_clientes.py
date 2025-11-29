import json
import os
from collections import Counter

DATA_FILE = "clientes.json"

# Lista que armazena os clientes
clientes = []

# Funções 

def carregar_dados():
    """Carrega os clientes de um arquivo JSON (se existir)."""
    global clientes
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                clientes = json.load(f)
        except Exception as e:
            print(f"Aviso: não foi possível ler {DATA_FILE}: {e}")
            clientes = []
    else:
        clientes = []


def salvar_dados():
    """Salva os clientes no arquivo JSON."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(clientes, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")


def gerar_id():
    """Gera um id único sequencial baseado no maior id existente."""
    if not clientes:
        return 1
    try:
        max_id = max(item.get("id", 0) for item in clientes)
        return max_id + 1
    except Exception:
        return 1

# Operações do CRUD (Create, read, update, delete) 

def cadastrar_cliente():
    """Solicita dados do cliente, valida e adiciona à lista."""
    print("\n--- Cadastro de Cliente ---")
    while True:
        nome = input("Nome: ").strip()
        if nome:
            break
        print("Por favor, insira um nome.")

    while True:
        telefone = input("Telefone (ex: (86) 99999-9999): ").strip()
        if telefone:
            break
        print("Por favor, insira um telefone.")

    while True:
        servico = input("Serviço contratado: ").strip()
        if servico:
            break
        print("Por favor, insira o serviço contratado.")
        

    novo = {
        "id": gerar_id(),
        "nome": nome,
        "telefone": telefone,
        "servico": servico
    }
    clientes.append(novo)
    salvar_dados()
    print(f"Cliente cadastrado com sucesso! ID = {novo['id']}")

# Listar os clientes e as informações ligadas a cada um deles.
def listar_clientes():
    """Exibe todos os clientes cadastrados em formato tabular simples."""
    print("\n----------- Lista de Clientes -----------")
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
# Informações orgaizadas em formato de "tabela".
    print(f"{'ID':<4} {'Nome':<50} {'Telefone':<18} {'Serviço':<20}")
    print("-" * 90)
    for c in clientes:
        print(f"{c.get('id', ''):<4} {c.get('nome','')[:50]:<50} {c.get('telefone',''):<18} {c.get('servico','')[:20]:<20}")


def buscar_cliente_por_id(id_busca):
    """Retorna o cliente com o id informado ou None se não existir."""
    for c in clientes:
        if c.get("id") == id_busca:
            return c
    return None


def atualizar_cliente():
    """Atualiza os campos de um cliente existente."""
    print("\n--- Atualizar Cliente ---")
    
    # Loop de validação
    while True:
        id_str = input("Informe o ID do cliente a ser atualizado: ").strip()
        
        # Verifica se o campo está vazio
        if not id_str:
            print("Por favor, digite um ID.")
            continue  # Volta ao início do loop
            
        # Verifica se a entrada pode ser convertida para inteiro
        try:
            id_busca = int(id_str)
            break  # Sai do loop se a conversão for bem-sucedida
        except ValueError:
            print("ID inválido. Por favor, digite um número inteiro.")
            continue # Volta ao início do loop
    

    cliente = buscar_cliente_por_id(id_busca)
    if not cliente:
        print(f"Cliente com ID {id_busca} não encontrado.")
        return
    
    # Cliente encontrado para fazer as atualizações

    print("Deixe em branco para manter o valor atual.")
    novo_nome = input(f"Nome [{cliente['nome']}]: ").strip()
    if novo_nome:
        cliente['nome'] = novo_nome

    novo_tel = input(f"Telefone [{cliente['telefone']}]: ").strip()
    if novo_tel:
        cliente['telefone'] = novo_tel

    novo_serv = input(f"Serviço [{cliente['servico']}]: ").strip()
    if novo_serv:
        cliente['servico'] = novo_serv

    salvar_dados()
    print("Cliente atualizado com sucesso.")


def remover_cliente():
    """Remove um cliente com base no ID informado pelo usuário."""
    print("\n--- Remover Cliente ---")
    try:
        id_str = input("Informe o ID do cliente a ser removido: ").strip()
        id_busca = int(id_str)
    except ValueError:
        print("ID inválido. Operação cancelada.")
        return

    cliente = buscar_cliente_por_id(id_busca)
    if not cliente:
        print(f"Cliente com ID {id_busca} não encontrado.")
        return

    confirm = input(f"Tem certeza que deseja remover '{cliente['nome']}'? (s/n): ").strip().lower()
    if confirm != 's':
        print("Operação cancelada.")
        return

    # remover
    clientes.remove(cliente)
    salvar_dados()
    print("Cliente removido com sucesso.")

# Gerar relatório.

def gerar_relatorio():
    """Gera um pequeno relatório com total de clientes e contagem por serviço."""
    print("\n--- Relatório de Clientes ---")
    total = len(clientes)
    print(f"Total de clientes cadastrados: {total}")

    if total == 0:
        return

    # Contagem por serviço
    servicos = [c.get('servico', 'Não informado') for c in clientes]
    contagem = Counter(servicos)

    print("\nQuantidade por serviço:")
    for serv, qtd in contagem.most_common():
        print(f"- {serv}: {qtd}")

    # Identificar serviço mais contratado
    mais_contratado, qtd = contagem.most_common(1)[0]

    # Verifica se todos têm a mesma quantidade
    quantidades = list(contagem.values())
    if len(set(quantidades)) == 1:
        print("\nServiço mais contratado: todos têm a mesma quantidade")
    else:
        print(f"\nServiço mais contratado: {mais_contratado} ({qtd} clientes)")


# Menu.

def menu():
    """Exibe o menu principal e retorna a opção escolhida pelo usuário."""
    print("\n=== SISTEMA DE CLIENTES ===")
    print("1. Cadastrar cliente")
    print("2. Listar clientes")
    print("3. Atualizar cliente")
    print("4. Remover cliente")
    print("5. Relatório")
    print("6. Sair")

    escolha = input("Escolha uma opção (1-6): ").strip()
    return escolha


def main():
    carregar_dados()
    while True:
        opc = menu()
        if opc == '1':
            cadastrar_cliente()
        elif opc == '2':
            listar_clientes()
        elif opc == '3':
            atualizar_cliente()
        elif opc == '4':
            remover_cliente()
        elif opc == '5':
            gerar_relatorio()
        elif opc == '6':
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == '__main__':
    main()

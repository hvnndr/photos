import os

def renomear_arquivos(diretorio, prefixo, numero_inicial=None):
    try:
        # Verifica se o diretório existe
        if os.path.exists(diretorio):

            # Lista e ordena os arquivos no diretório
            arquivos = sorted([arquivo for arquivo in os.listdir(diretorio) if arquivo.lower().endswith('.JPG')])

            # Determina o número inicial
            if numero_inicial is not None:
                try:
                    numero_inicial = int(numero_inicial)
                except ValueError:
                    raise ValueError("O número inicial deve ser um valor numérico.")
            else:
                numero_inicial = 1

            # Renomeia os arquivos
            for i, arquivo in enumerate(arquivos, start=numero_inicial):
                numero_formatado = str(i).zfill(4)  # Preenche com zeros à esquerda até 4 dígitos
                novo_nome = f"{prefixo}_{numero_formatado}.JPG"
                caminho_antigo = os.path.join(diretorio, arquivo)
                caminho_novo = os.path.join(diretorio, novo_nome)
                os.rename(caminho_antigo, caminho_novo)
                print(f"Arquivo renomeado: {caminho_antigo} -> {caminho_novo}")

            print("Renomeação concluída.")
        else:
            print(f"O diretório '{diretorio}' não existe.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso
diretorio_parametro = './fotos'
prefixo_parametro = 'corrida'
#numero_inicial_parametro = input("Digite o número inicial (opcional): ")

renomear_arquivos(diretorio_parametro, prefixo_parametro)

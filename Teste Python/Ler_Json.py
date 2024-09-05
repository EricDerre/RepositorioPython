import json
import os

def calcular_faturamento_json(caminho_arquivo_json):

    # abre o arquivo definido no caminho em modo de "Leitura" e o fecha automáticamente após o uso
    with open(caminho_arquivo_json, 'r') as arquivo:

        # carrega as informações do arquivo para uma variável, convertendo o conteúdo para uma lista de dicionários
        dados = json.load(arquivo)
    
    # ignora todos os dias sem faturamento
    faturamentos = [item['valor'] for item in dados if item['valor'] > 0]

    # caso o Json esteja vazio ou com apenas valores sem faturamento, ele retorna os dados como None ou 0
    if not faturamentos:
        return None, None, 0  

    # percorre a lista para encontrar seu menor valor 
    menor = min(faturamentos)

    # percorre a lista para encontrar seu maior valor 
    maior = max(faturamentos)
    
    # calcula e armazena a soma total dos faturamentos
    total_faturamento = sum(faturamentos)

    # conta quantos dias tiveram faturamento, apenas verificando o tamanho da lista, visto que os dias sem faturamento já foram ignorados
    dias_com_faturamento = len(faturamentos)

    # faz a média mensal dos faturamentos, sempre evitando realizar alguma divisão por 0
    media_mensal = total_faturamento / dias_com_faturamento if dias_com_faturamento > 0 else 0
    
    # faz a contagem de quantos dias o faturamento foi maior do que a média calculada à cima
    dias_acima_media = len([f for f in faturamentos if f > media_mensal])
    
    return menor, maior, dias_acima_media



# verifica onde o código fonte Python está localizado na máquina e retorna seu endereço
diretorio_atual = os.path.dirname(__file__)

# com o endereço à cima, o arquivo json deve sempre estar acompanhado do código fonte, para evitar não conseguir encontrar
# pode ocasionar erros
caminho_json = os.path.join(diretorio_atual, 'dados.json')


# chama a função dando como argumento o caminho para o json e salva os valores calculados nas variáveis
menor_json, maior_json, dias_acima_media_json = calcular_faturamento_json(caminho_json)


# mostra o valor de cada variável calculada
print("JSON:")
print(f"Menor valor: {menor_json}")
print(f"Maior valor: {maior_json}")
print(f"Numero de dias acima da media: {dias_acima_media_json}")

from seleniumbase import SB
import pandas as pd
from io import StringIO
import os

#===================#
#    Variaveis      #
#===================#

PASTA_DESTINO = "./Download"
if not os.path.exists(PASTA_DESTINO):
    os.makedirs(PASTA_DESTINO)

NOME_ARQUIVO = "DataHockey.xlsx"
CAMINHO_FINAL = os.path.join(PASTA_DESTINO, NOME_ARQUIVO)
todos_os_dados = []
#===================#
#        Main       #
#===================#

if __name__ == "__main__":

    with SB(uc=True, headless=False) as sb:
        try:
            # Configura o diretório de download internamente
            sb.execute_cdp_cmd("Page.setDownloadBehavior", {
                "behavior": "allow",
                "downloadPath": PASTA_DESTINO
            })
        except:
            print('Configuração de download falhou, seguindo...')
            pass        
        
        try:
            # Acessar URL
            sb.maximize_window()
            sb.open("https://www.scrapethissite.com/pages/forms/")
            # Aumentar o limite de linhas por pagina
            sb.select_option_by_value('#per_page', '100')
            sb.sleep(2) 

            # Loop para passar por todas as páginas
            while True:
                # Baixar o Conteúdo da página atual
                sb.wait_for_element('#hockey > div > table')
                HTML_table = sb.get_attribute('#hockey', 'outerHTML')
                
                # Lê a tabela e adiciona na lista
                df = pd.read_html(StringIO(HTML_table))[0]
                todos_os_dados.append(df)
                
                print(f"Total de linhas: {sum([len(d) for d in todos_os_dados])}")

                seletor_proximo = 'ul.pagination li:not(.disabled) a[aria-label="Next"]'
                
                if sb.is_element_visible(seletor_proximo):
                    sb.click(seletor_proximo)
                    sb.sleep(2) # Pausa fundamental para a nova página carregar antes de extrair novamente
                else:
                    # Se não achou o botão de próximo, chegamos na última página. Quebra o loop.
                    print("Última página alcançada.")
                    break

            # Junta todos os DataFrames da lista em um único DataFrame
            print("Consolidando os dados...")
            df_final = pd.concat(todos_os_dados, ignore_index=True)
            
            # Salva o arquivo único
            df_final.to_excel(CAMINHO_FINAL, index=False)

            print(f">> Sucesso! {len(df_final)} linhas extraídas e salvas em: {CAMINHO_FINAL}")

        except Exception as e:
            print(f'Deu erro: {e}')
from seleniumbase import SB
import pandas as pd
from io import StringIO
import os
#===================#
#    Variaveis      #
#===================#

PASTA_DESTINO = r"C:\Users\kaua\OneDrive\Documentos\rpa-data-extraction-seleniumbase\Download"
if not os.path.exists(PASTA_DESTINO):
    os.makedirs(PASTA_DESTINO)
    
NOME_ARQUIVO = "DataHockey.xlsx"
CAMINHO_FINAL = os.path.join(PASTA_DESTINO, NOME_ARQUIVO)

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
            print('teste falhou')
            pass        
        try:
            # Acessar URL
            sb.open("https://www.scrapethissite.com/pages/forms/")
            sb.maximize_window()
            sb.wait_for_element('#hockey > div > table')

            HTML_table = sb.get_attribute('#hockey' , 'outerHTML')
            df = pd.read_html(StringIO(HTML_table))[0]
            df.to_excel(CAMINHO_FINAL, index=False)
            print(f">> Dados extraídos e salvos em: {CAMINHO_FINAL}")



            input()
        except Exception as e:
            print(F'deu erro:{e}')
# RPA Data Extraction - SeleniumBase

## Cenário e Problema de Negócio
A coleta manual de dados estruturados espalhados por múltiplas páginas web é um processo operacional lento e propenso a erros. Este projeto resolve esse problema através de uma automação de extração de dados (Web Scraping/RPA). O script acessa o portal de testes [Scrape This Site](https://www.scrapethissite.com/pages/forms/), varre o catálogo de times de hóquei, gerencia a paginação de forma dinâmica e consolida todas as informações em um relatório único e limpo no formato Excel.

---

## Funcionalidades

* **Navegação Automatizada:** Utiliza o SeleniumBase com o modo Undetected ChromeDriver (`uc=True`) para interagir com a página de forma contínua e imitar comportamento humano.
* **Paginação Inteligente:** O script otimiza a extração ao maximizar a visualização para 100 itens por página e avança automaticamente até identificar que não há mais botões "Next" disponíveis.
* **Processamento de Dados em Memória:** Captura o HTML bruto da tabela e utiliza a biblioteca Pandas para transformar diretamente em DataFrames estruturados, eliminando a necessidade de tratar linha por linha manualmente.
* **Exportação Centralizada:** Todos os dados extraídos em cada página são aglomerados e salvos automaticamente no arquivo `DataHockey.xlsx` dentro do diretório `./Download`.

## Tecnologias Utilizadas

* **[Python](https://www.python.org/)**
* **[SeleniumBase](https://seleniumbase.io/)** - Para automação web, manipulação do navegador e bypass de bloqueios.
* **[Pandas](https://pandas.pydata.org/)** - Para leitura das tabelas, consolidação (`concat`) e exportação dos dados.
* **[OpenPyXL](https://openpyxl.readthedocs.io/)** - Motor de dependência do Pandas para gerar e escrever o arquivo Excel.

## Pré-requisitos e Instalação

1. Clone o repositório ou baixe os arquivos do projeto.
2. Crie e ative um ambiente virtual (recomendado):
   ```bash
   python -m venv venv
   # No Windows: venv\Scripts\activate
   # No Linux/Mac: source venv/bin/activate
3. Instale as dependencias pelo terminal
   pip install -r requirements.txt
4. execute o seguinte comando no terminal para executar o projeto
   python Main.py
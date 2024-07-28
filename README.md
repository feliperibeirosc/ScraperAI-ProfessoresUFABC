# WebScraper AI

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen.svg)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-brightgreen.svg)

> **Projeto desenvolvido para a disciplina de Comunicação e Redes da UFABC.**  
> **Objetivo:** Capturar dados dos professores do [site dos docentes](https://www.ufabc.edu.br/ensino/docentes) e catalogá-los conforme universidade de formação (Doutorado) e áreas de interesse, para posterior construção de um grafo.

## Sobre o Projeto

Para capturar e catalogar os dados dos docentes da UFABC, o programa segue 4 etapas principais:

1. **scraper.py**: 
   - **Função:** Lê dados de um arquivo `.txt` com links para as páginas dos professores.
   - **Processo:** Verifica cada página e coleta informações entre `<h1 class="documentFirstHeading">` e `<div class="boxAutor">` com dados de contato do professor.
   - **Resultado:** Gera um arquivo `.txt` na pasta `raw`, chamado `TeacherData`, contendo as informações extraídas.
   
2. **analyzer.py**: 
   - **Função:** Utiliza a API do Google Gemini para processar os dados brutos.
   - **Processo:** Analisa cada professor individualmente, considera o contexto das áreas de interesse e, caso sejam muito específicas, as generaliza em uma área maior, retornando um arquivo `.txt` com os dados necessários para análise.
   - **Resultado:** Produz um arquivo tratado com informações relevantes para a pesquisa.

3. **converter.py**: 
   - **Função:** Converte os dados processados em um arquivo `.csv`.
   - **Processo:** Transforma os dados do `.txt` tratado em colunas organizadas (nome, universidade, áreas de interesse).
   - **Resultado:** Gera um arquivo `.csv` estruturado e pronto para análise.

4. **training.py**: 
   - **Função:** Realiza o fine-tuning do modelo Google Gemini 1.0 Pro.
   - **Processo:** Utiliza um dataset com cerca de 500 exemplos para padronizar a saída dos textos.
   - **Resultado:** Modelo aprimorado para fornecer resultados consistentes.


## Estrutura de arquivos
    scraper/
    │ ├── data/
    │ │ ├── raw/
    │ │ │ ├── links.txt
    │ │ │ └── teacherData.txt
    │ │ └── processed/
    │ │ ├── teacherData.txt
    │ │ └── teacherData.csv
    │
    ├── analyzer.py
    ├── converter.py
    ├── scraper.py
    └── training.py

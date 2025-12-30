# Demonstrações Financeiras a partir de Balancete

Projeto em Python para praticar **raspagem de dados**, **tratamento de informações contábeis** e **geração de demonstrações financeiras**.

## Objetivo

- Raspar o balancete de uma empresa SESC RJ a partir de um site.
- Tratar e padronizar os dados
- Gerar demonstrações financeiras a partir do balancete

## Estrutura do Projeto

```
demonstracoes_financeiras/
│
├── data/
│ ├── raw/ # Dados brutos (raspados)
│ ├── processed/ # Dados tratados
│ └── outputs/ # Demonstrações financeiras
│
├── src/
│ ├── scrape.py # Raspagem do balancete
│ ├── transform.py # Tratamento e padronização dos dados
│ └── reports.py # Geração das demonstrações financeiras
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Etapas do Pipeline

1. **Raspagem (`scrape.py`)**
   - Acessa o site da empresa
   - Baixa o balancete
   - Salva em `data/raw/`

2. **Tratamento (`transform.py`)**
   - Limpeza de dados
   - Conversão de tipos
   - Padronização de contas e valores
   - Salva em `data/processed/`

3. **Demonstrações (`reports.py`)**
   - Geração de BP e DRE
   - Resultados salvos em `data/outputs/`

## Execução

Exemplo de execução do script de raspagem:

```bash
python src/scrape.py

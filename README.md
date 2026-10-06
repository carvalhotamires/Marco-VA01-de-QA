# Marco VA01 de QA - Tech UniDiasUp

Projeto de Testes Unitários Automatizados para o sistema de E-commerce, cobrindo a User Story de cálculo de descontos progressivos por categoria de fidelidade.

## Estrutura do Projeto

```
Marco-VA01-de-QA/
│
├── .gitignore                          # Arquivos ignorados pelo Git
├── pytest.ini                          # Configuração do Pytest (pythonpath e caminhos de teste)
├── requirements.txt                    # Dependências do projeto (pytest, pytest-cov)
├── README.md                           # Documentação do projeto
│
├── .vscode/
│   └── settings.json                   # Configuração de execução de testes no VS Code
│
└── src/
    ├── __init__.py
    ├── tech/
    │   ├── __init__.py
    │   └── tamires/                    # Identificação do aluno/QA
    │       ├── __init__.py
    │       └── ecommerce/
    │           ├── __init__.py
    │           └── operacoes/
    │               ├── __init__.py
    │               └── calcular_desconto.py    # Função de cálculo de descontos
    │
    └── tests/
        ├── cenarios/
        │   └── cenarios_desconto.txt           # Documentação dos cenários de teste pensados
        └── test_calcular_desconto.py           # Testes unitários com Pytest
```

## Requisitos e Instalação

Certifique-se de ter o Python 3 instalado. Para instalar as dependências de teste:

```bash
pip install -r requirements.txt
```

## Como Executar os Testes

Para rodar todos os testes com relatório detalhado:

```bash
pytest -v
```

Para rodar com relatório de cobertura de código:

```bash
pytest -v --cov=src/tech/tamires/ecommerce/operacoes
```

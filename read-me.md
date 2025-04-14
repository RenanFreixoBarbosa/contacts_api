# API Flask de Contatos

Esta API foi desenvolvida utilizando o framework web Flask (Python). Para documentação e testes interativos, estamos utilizando a biblioteca Flask-OpenAPI3, que gera automaticamente a especificação OpenAPI (Swagger).

## Tecnologias Utilizadas

* **Flask:** Framework web micro para Python.
* **Flask-OpenAPI3:** Extensão Flask para integrar a especificação OpenAPI 3.0 (Swagger).

## Como Rodar a Aplicação

Siga os passos abaixo para executar a API no seu ambiente local:

1.  **Pré-requisitos:**
    * **Python 3:** Certifique-se de ter o Python 3 instalado na sua máquina. Você pode verificar a versão executando o comando `python --version` ou `python3 --version` no seu terminal.
    * **pip:** O gerenciador de pacotes do Python. Geralmente vem instalado com o Python.

2.  **Clonar o Repositório (Opcional):**
   clone-o para sua máquina:
    ```bash
    git clone https://github.com/RenanFreixoBarbosa/contacts_api
    cd [NOME_DO_SEU_REPOSITORIO]
    ```

3.  **Criar um Ambiente Virtual (Recomendado):**
    É uma boa prática criar um ambiente virtual isolado para as dependências do seu projeto.
    ```bash
    python -m venv venv
    # Ou
    python3 -m venv venv
    ```

4.  **Ativar o Ambiente Virtual:**
    * **No Linux/macOS:**
        ```bash
        source venv/bin/activate
        ```
    * **No Windows (cmd):**
        ```bash
        venv\Scripts\activate
        ```
    * **No Windows (PowerShell):**
        ```powershell
        .\venv\Scripts\Activate.ps1
        ```

5.  **Instalar as Dependências:**
    Utilize o arquivo `requirements.txt` (se existir) para instalar todas as bibliotecas necessárias, incluindo Flask e Flask-OpenAPI3. Certifique-se de que `flask` e `flask-openapi3` estejam listados neste arquivo.
    ```bash
    pip install -r requirements.txt
    ```
    Se o arquivo `requirements.txt` não existir, você pode instalar as dependências manualmente:
    ```bash
    pip install Flask Flask-OpenAPI3
    # Instale outras dependências que sua aplicação possa ter (ex: Pydantic)
    pip install Pydantic
    ```

6.  **Configurar Variáveis de Ambiente (Se Necessário):**
    Sua aplicação pode depender de variáveis de ambiente para configurações como banco de dados, chaves secretas, etc. Configure essas variáveis conforme as instruções do seu projeto (podem ser arquivos `.env` ou configurações diretamente no sistema).

7.  **Executar a Aplicação Flask:**
    A forma de executar a aplicação Flask geralmente envolve definir a variável de ambiente `FLASK_APP` e usar o comando `flask run`. Assumindo que o arquivo principal da sua aplicação se chama `app.py` ou algo similar:
    ```bash
    export FLASK_APP=nome_do_seu_arquivo.py
    flask run
    ```
    Ou, se você estiver em modo de desenvolvimento com recarregamento automático:
    ```bash
    flask run --debug
    ```
    A aplicação será iniciada em um endereço local (geralmente `http://127.0.0.1:5000`).

## Acessando a Documentação Swagger UI

Após executar a aplicação, você pode acessar a interface do Swagger UI para visualizar a documentação da sua API e realizar testes interativos através do seu navegador. A URL padrão para a interface do Swagger UI quando se usa Flask-OpenAPI3 é geralmente:

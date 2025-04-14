# API Flask de Contatos
Esta API foi desenvolvida como trabalho de conclusão da disciplina Full Stack Básico utilizando o framework web Flask (Python). Para documentação e testes interativos, estamos utilizando a biblioteca Flask-OpenAPI3, que gera automaticamente a especificação OpenAPI (Swagger).

## Tecnologias Utilizadas

* **Flask:** Framework web micro para Python.
* **Flask-OpenAPI3:** Extensão Flask para integrar a especificação OpenAPI 3.0 (Swagger).
* **Db-Sqlite:** Banco de dados

## Como Rodar a Aplicação

Siga os passos abaixo para executar a API no seu ambiente local:

1.  **Pré-requisitos:**
    * **Python 3:** Certifique-se de ter o Python 3 instalado na sua máquina. Você pode verificar a versão executando o comando `python --version` ou `python3 --version` no seu terminal.
    * **pip:** O gerenciador de pacotes do Python. Geralmente vem instalado com o Python.

2.  **Clonar o Repositório:**
   clone-o para sua máquina:
       ```bash
    https://github.com/RenanFreixoBarbosa/contacts_api.git
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
    Utilize o arquivo `requirements.txt` para instalar todas as bibliotecas necessárias para esta aplicação.
    ```bash
    pip install -r requirements.txt
    ```

7.  **Executar a Aplicação Flask:**
    Após executar os passos anteriores e criar o ambiente virtual, podemos rodar o seguinte comando para executar a api
    
    ```bash
    python app.py
    ```
    A aplicação será iniciada em um endereço local (`http://127.0.0.1:5000`).

## Acessando a Documentação Swagger UI

Após executar a aplicação, você pode acessar a interface do Swagger UI para visualizar a documentação da sua API e realizar testes interativos através do link: 
```bash
http://127.0.0.1:5000/openapi/swagger#/
```

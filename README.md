# Calculadora

Este repositório contém uma aplicação web de calculadora simples, desenvolvida em Python utilizando o framework Flask.

## Descrição do Projeto

O projeto implementa uma calculadora básica que permite realizar operações aritméticas fundamentais (adição, subtração, multiplicação e divisão) através de uma interface web. A aplicação é construída com Flask no backend para processar as requisições e renderizar a interface, e HTML/CSS/JavaScript no frontend para a interação do usuário.

## Funcionalidades

*   Adição
*   Subtração
*   Multiplicação
*   Divisão (com tratamento para divisão por zero)

## Tecnologias Utilizadas

*   **Python:** Linguagem de programação principal.
*   **Flask:** Microframework web para Python.
*   **HTML5:** Estrutura da interface do usuário.
*   **CSS3:** Estilização da interface.
*   **JavaScript:** Interatividade no frontend (se aplicável, embora o exemplo pareça mais focado no Flask para renderização).

## Como Configurar e Rodar o Projeto

Para configurar e executar este projeto localmente, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/DAVIWENDELL/Calculadora.git
    cd Calculadora
    ```
2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows: `venv\Scripts\activate`
    ```
3.  **Instale as dependências:**
    ```bash
    pip install Flask
    ```
4.  **Execute a aplicação:**
    ```bash
    python calculadora.py
    ```
5.  **Acesse a aplicação:**
    Abra seu navegador e acesse `http://127.0.0.1:5000/` (ou o endereço indicado no terminal).

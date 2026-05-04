# 💧 Controle de Níveis de Água 💧

## 📖 Sobre o projeto
Este programa simula o controle de níveis de água em um reservatório.  
O usuário pode visualizar os diferentes níveis (de 1 a 5), cada um com uma cor correspondente para facilitar a identificação:
- 🔴 Nível 1: Muito baixo (crítico)
- 🟡 Nível 2: Baixo
- 🟢 Nível 3: Médio
- 🧊 Nível 4: Alto
- 🔵 Nível 5: Muito alto (alerta)

Ao final, o programa solicita ao usuário que informe o nível atual do reservatório e apresenta a situação correspondente com destaque em cores.

## Linguagem utilizada
![Python](https://img.shields.io/badge/Python-3.14-blue?style=plastic&logo=python&logoColor=3776AB&labelColor=white&color=3776AB)

## ⚙️ Estruturas utilizadas
- **Colorama:** biblioteca utilizada para aplicar cores no terminal.
- **listas:** para armazenar as mensagens de cada nível.
- **for:** para percorrer e exibir todos os níveis do reservatório.
- **if / elif:** para definir a cor de cada nível.
- **while:** para validar a entrada do usuário (nível entre 1 e 5).


## ▶️ Como executar este programa
- Clone este repositório:
    ```bash
    git clone https://github.com/arwintuco/Projetos.git

- Acesse a pasta do projeto:
    ```bash
    cd controle-de-niveis-de-agua

- Execute o programa:
    ```bash
    python app.py
🚀 Como Executar o Projeto

1️⃣ Instalar o Python

Caso ainda não tenha o Python instalado, baixe e instale a versão mais recente em: Python Official Website

2️⃣ Criar um Ambiente Virtual (Recomendado)

Para manter a organização das dependências, recomenda-se criar um ambiente virtual:

python -m venv venv  # Criar ambiente virtual
source venv/bin/activate  # Ativar no Linux/macOS
venv\Scripts\activate  # Ativar no Windows

3️⃣ Instalar as Dependências

Antes de executar o projeto, instale as bibliotecas necessárias:

pip install -r requirements.txt

Caso não tenha o arquivo requirements.txt, instale manualmente:

pip install streamlit pandas matplotlib seaborn

4️⃣ Executar o Dashboard

Dentro do diretório do projeto, execute:

streamlit run app.py

Isso abrirá o dashboard automaticamente no navegador.

📂 Estrutura do Projeto

projeto/
│── app.py               # Código principal do Streamlit
│── requirements.txt     # Lista de dependências
│── data/
│   ├── ml_sale_houses_cleaned.csv  # Base de dados utilizada
│── README.md            # Documentação do projeto

📌 Principais Funcionalidades

✅ Exibição de métricas sobre os imóveis (Preço médio por metro quadrado, área média, etc.)✅ Gráficos interativos de análise exploratória✅ Filtros dinâmicos por estado e categoria de imóvel✅ Suporte para diferentes formatos de dados

🛠 Possíveis Erros e Soluções

🔹 Erro: streamlit: command not found

Certifique-se de que o ambiente virtual está ativado (venv\Scripts\activate no Windows ou source venv/bin/activate no Linux/macOS).

Se o Streamlit não estiver instalado, rode pip install streamlit novamente.

🔹 Erro: KeyError: 'Preço/m²'

O nome da coluna pode ter espaços ou caracteres especiais. Verifique as colunas disponíveis com print(df.columns).

Certifique-se de que o arquivo CSV está corretamente carregado.

📢 Contato

Caso tenha dúvidas ou sugestões, entre em contato pelo GitHub ou e-mail. 🚀

me de esse texto no formado md para colocar no readme
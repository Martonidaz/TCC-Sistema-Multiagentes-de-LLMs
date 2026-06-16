Lab02/
├── env/                        # (Já criado) Seu ambiente virtual Python isolado
├── data/                       # Armazenamento de dados locais (ignorados no Git)
│   ├── raw/                    # Documentos originais (PDFs, TXT) para ingestão
│   └── vector_db/              # Banco de dados vetorial local (ChromaDB ou FAISS)
├── src/                        # O coração do seu software
│   ├── __init__.py
│   ├── config.py               # Central de variáveis: portas, nomes dos modelos e caminhos
│   ├── ingestao.py             # Lógica de extração de texto, chunking e embeddings
│   └── agentes/                # Módulo da arquitetura Multi-Agente
│       ├── __init__.py
│       ├── estado.py           # Definição das variáveis de estado (State) do LangGraph
│       ├── gerador.py          # Agente responsável por consultar o RAG e gerar o texto
│       ├── avaliador.py        # Agente que aplica a Entropia Semântica e Métricas RAGAS
│       └── grafo.py            # Onde os nós e as arestas do LangGraph são conectados
├── tests/                      # Bateria de testes unitários e de integração
│   ├── __init__.py
│   ├── test_conexao_llm.py     # Nosso ponto de partida: validar a ponte com o Ollama
│   ├── test_ingestao.py        # Valida se os chunks estão sendo criados corretamente
│   └── test_agentes.py         # Valida o fluxo de decisão do LangGraph de forma isolada
├── requirements.txt            # Lista exata das bibliotecas e suas versões
├── .gitignore                  # Impede que o 'env' e o banco de dados subam para o GitHub
└── main.py                     # Ponto de entrada (Entrypoint) que inicializa o sistema
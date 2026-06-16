# src/config.py

# Configurações do Motor de Inferência (Ollama)
OLLAMA_BASE_URL = "http://localhost:11434"

# IMPORTANTE: Altere para o nome exato do modelo que você baixou no servidor (ex: llama3, phi3)
MODELO_LLM = "llama3.2:1b" 

# Configurações do RAG e Embeddings (usaremos este modelo leve e eficiente)
MODELO_EMBEDDING = "all-MiniLM-L6-v2"
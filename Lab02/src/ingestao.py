# src/ingestao.py
import os
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from src.config import MODELO_EMBEDDING

class IngestorDados:
    def __init__(self):
        print(f"📦 Carregando modelo de embeddings '{MODELO_EMBEDDING}' na CPU...")
        self.model = SentenceTransformer(MODELO_EMBEDDING, device='cpu')
        self.caminho_db = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'vector_db'))
        os.makedirs(self.caminho_db, exist_ok=True)

    def fatiar_texto(self, texto, tamanho_chunk=300, sobreposicao=50):
        """Divide o texto em blocos menores baseados em caracteres para manter o contexto."""
        palavras = texto.split()
        chunks = []
        i = 0
        while i < len(palavras):
            chunk = " ".join(palavras[i:i + tamanho_chunk])
            chunks.append(chunk)
            i += (tamanho_chunk - sobreposicao)
        return chunks

    def processar_e_salvar(self, nome_arquivo, texto):
        """Gera os embeddings dos chunks e salva a base de conhecimento localmente."""
        chunks = self.fatiar_texto(texto)
        if not chunks:
            return False
        
        print(f"✂️ Texto fatiado em {len(chunks)} pedaços.")
        
        # Gerando os vetores matemáticos
        embeddings = self.model.encode(chunks)
        
        # Estrutura do nosso banco vetorial nativo
        base_conhecimento = {
            "chunks": chunks,
            "embeddings": embeddings
        }
        
        # Salvando em disco via pickle
        caminho_arquivo_saida = os.path.join(self.caminho_db, f"{nome_arquivo}.pkl")
        with open(caminho_arquivo_saida, 'wb') as f:
            pickle.dump(base_conhecimento, f)
            
        print(f"💾 Base vetorial salva com sucesso em: {caminho_arquivo_saida}")
        return True

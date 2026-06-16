# tests/test_conexao_llm.py
import sys
import os

# Ajuste de rota: Permite que o teste enxergue a pasta 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ollama import Client
from src.config import MODELO_LLM, OLLAMA_BASE_URL

def testar_conexao():
    print(f"🔄 Iniciando teste de conexão com '{MODELO_LLM}' via {OLLAMA_BASE_URL}...")
    
    # Instanciando o cliente apontando explicitamente para o Docker
    cliente = Client(host=OLLAMA_BASE_URL)
    
    try:
        resposta = cliente.chat(model=MODELO_LLM, messages=[
            {
                'role': 'user',
                'content': 'Responda com uma única frase curta: Você está online e pronto para processar dados?'
            }
        ],
             options={
                       'num_gpu': 0
                    }
         )
        
        print("\n✅ Conexão estabelecida com sucesso! Resposta da IA:")
        print(f"🤖 {resposta['message']['content']}\n")
        
    except Exception as e:
        print(f"\n❌ ERRO FATAL: Não foi possível conectar ao modelo.")
        print(f"Detalhes técnicos: {e}")

if __name__ == "__main__":
    testar_conexao()
    

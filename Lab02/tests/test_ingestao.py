# tests/test_ingestao.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ingestao import IngestorDados

def executar_teste_ingestao():
    print("🧪 Iniciando teste unitário do módulo de ingestão...")
    
    caminho_txt = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'referencial_tcc.txt'))
    
    if not os.path.exists(caminho_txt):
        print(f"❌ Erro: Arquivo de teste não encontrado em {caminho_txt}")
        return

    with open(caminho_txt, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    # Inicializando o motor de processamento vetorial
    ingestor = IngestorDados()
    sucesso = ingestor.processar_e_salvar("base_tcc", conteudo)
    
    if sucesso:
        print("✅ Teste Unitário de Ingestão: PASSOU!")
    else:
        print("❌ Teste Unitário de Ingestão: FALHOU!")

if __name__ == "__main__":
    executar_teste_ingestao()

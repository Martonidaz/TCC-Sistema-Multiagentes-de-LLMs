# 🤝 Multi-Agent Builder: Democratizando Soluções Tecnológicas com Entropia Semântica

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Estatística](https://img.shields.io/badge/Validação-Entropia%20Semântica-purple.svg)](#)
[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-success.svg)](#)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Conectar-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/daniel-marton-barbosa/)

> **Resumo do Projeto:** Uma plataforma inteligente que capacita profissionais de fora da área de Tecnologia da Informação (TI) a desenvolverem suas próprias soluções tecnológicas de forma autônoma e segura, utilizando seus manuais técnicos como base de conhecimento.

Este repositório contém o código-fonte desenvolvido para o Trabalho de Conclusão de Curso em **Engenharia de Computação** no **Centro Universitário Salesiano de São Paulo (Unisal)**.

O grande diferencial deste sistema é a união da acessibilidade proporcionada por agentes de Inteligência Artificial com o rigor de ferramentas de validação estatística. A **Entropia Semântica** é utilizada no back-end para garantir que as soluções geradas sejam precisas, coerentes com os manuais fornecidos e livres de alucinações.

---

## ⚙️ Arquitetura e Proposta de Valor

O sistema atua como uma ponte entre o conhecimento de domínio do usuário (manuais técnicos) e a construção de software, orquestrado pela seguinte dinâmica multiagente:

* **Agentes Facilitadores:** Interagem em linguagem natural com o profissional não-TI, compreendendo suas necessidades de negócio e traduzindo-as em requisitos lógicos.
* **Agentes de Processamento de Conhecimento:** Extraem, vetorizam e interpretam as regras de negócio contidas nos manuais técnicos fornecidos pelo próprio usuário.
* **Validação por Entropia Semântica (Estatística):** Em vez de confiar cegamente na geração do LLM, o sistema utiliza métodos estatísticos para calcular a dispersão de significados (incerteza) nas respostas geradas. Se a entropia semântica for alta, o sistema bloqueia a sugestão tecnológica, garantindo que o profissional não-TI receba apenas arquiteturas e lógicas validadas e estritamente aderentes ao manual.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem Principal:** Python
* **Orquestração Multiagente:** [Ex: LangChain / LlamaIndex / AutoGen]
* **Cálculo Estatístico e Métricas:** Bibliotecas Python para cálculo de entropia e modelagem probabilística (ex: `scipy`, `numpy`)
* **Processamento de Linguagem Natural (NLP):** Extração de dados de PDFs/Documentos e *Embeddings*

---

## 👨‍💻 Autor

**Daniel Marton Barbosa**
*Engenharia de Computação - Unisal*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Acessar_Perfil-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/daniel-marton-barbosa/)

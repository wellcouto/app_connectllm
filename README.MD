
# Projeto: LLM CLI - Integração com ChatGPT e RoBERTa (Hugging Face)

Este projeto é uma aplicação Python que se conecta com dois Large Language Models (LLMs): ChatGPT (via API da OpenAI) e RoBERTa (via Hugging Face), utilizando padrões de projeto para estruturação robusta e extensível.

Demo de Uso: https://youtu.be/Mob6fL4AWh8

## 📦 Funcionalidades

- Perguntas via linha de comando a um ou ambos os modelos.
- Avaliação das respostas com estratégia baseada em similaridade semântica.
- Padrões de projeto aplicados:
  - Factory
  - Command
  - Strategy
  - Observer
- Comparação de respostas entre modelos.
- Interface de linha de comando intuitiva.
- Tratamento de erros e logs informativos.

---

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seuusuario/llm-cli-projeto.git
cd llm-cli-projeto
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuração

### 1. Chave da API da OpenAI

Crie um arquivo `.env` (ou defina manualmente no código) com a sua chave:

```
OPENAI_API_KEY=sua_chave_aqui
```

Ou altere diretamente no `main.py` se necessário:

```python
CHATGPT_API_KEY = "sua_chave"
```

---

## 🚀 Execução

### Usos Básicos

```bash
# Consultar apenas o Hugging Face
python src/main.py hf "Qual é a capital da França?"

# Consultar o ChatGPT (requer chave válida)
python src/main.py chatgpt "Qual é a capital da França?" --context "A França está localizada na Europa e sua capital é Paris."
```

### Comparar ambos os modelos

```bash
python src/main.py hf "Qual é a capital da França?" --context "A França está localizada na Europa e sua capital é Paris." --compare
```

---

## 📖 Parâmetros CLI

| Parâmetro      | Tipo     | Obrigatório | Descrição                                                         |
|----------------|----------|-------------|-------------------------------------------------------------------|
| `model_choice` | string   | ✅          | `'chatgpt'` ou `'hf'` (Hugging Face)                              |
| `question`     | string   | ✅          | A pergunta a ser feita ao modelo                                  |
| `context`      | string   | ✅          | Um texto base para perguntas no estilo Q&A (RoBERTa)              |

---

## 🧠 Padrões de Projeto Utilizados

### 🏭 Factory

- **Objetivo**: Criar objetos de forma flexível e desacoplada.
- **Aplicado em**: Criação de serviços de conexão com APIs (`ChatGPTFactory`, `HuggingFaceFactory`).

### 🧾 Command

- **Objetivo**: Encapsular requisições como objetos.
- **Aplicado em**: `AskCommand`, que executa uma pergunta ao modelo.

### 🧮 Strategy

- **Objetivo**: Permitir múltiplos algoritmos intercambiáveis.
- **Aplicado em**: `EmbeddingSimilarityStrategy` avalia respostas com base em embeddings.

### 🔔 Observer

- **Objetivo**: Notificar partes do sistema quando algo muda.
- **Aplicado em**: `CLIObserver` que exibe a resposta escolhida no console.

---

## 💡 Demonstração

Grave um vídeo mostrando:

1. Instalação do ambiente
2. Execução de exemplos com CLI
3. Explicação da arquitetura e dos padrões

---

## 📁 Estrutura do Projeto

```
src/
├── factories/
├── commands/
├── strategies/
├── observers/
├── services/
└── main.py
```

---

## 📌 Requisitos

- Python 3.9+
- API Key válida da OpenAI (para ChatGPT)
- Internet para acesso aos modelos do Hugging Face

---

## 🧊 Exemplo de Execução

```bash
python src/main.py hf "Qual é a capital da França?" "A França é um país europeu. Sua capital é Paris." 
```

Saída esperada:

```
[Resposta do modelo hf]
Paris

[Resposta do modelo chatgpt]
A capital da França é Paris.

[Observer] Nova resposta escolhida pelo sistema:
Paris
```

---

## 📝 Licença

Este projeto é apenas para fins demonstrativos e educacionais.

---

Desenvolvido com ❤️ e Python.

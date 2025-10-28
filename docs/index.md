# 🐍 PyBrige — Toolkit de Produtividade Python

Bem-vindo ao **PyBrige**, um toolkit moderno e leve criado para **aumentar a produtividade dos desenvolvedores Python**.  
Ele combina automação, logging avançado, configuração inteligente e utilitários úteis — tudo em um só pacote.

---

## ✨ O que é o PyBrige?

O **PyBrige** nasceu com o objetivo de eliminar repetições de código e facilitar tarefas do dia a dia no desenvolvimento Python.  
Com uma estrutura modular e extensível, ele fornece ferramentas para:

- 🧩 **Automação de builds e uploads** (CLI inclusa)
- ⚙️ **Configuração e variáveis de ambiente seguras**
- 🧾 **Logging colorido e personalizável**
- 🪄 **Decorators úteis** (`retry`, `timer`, etc.)
- 📂 **Manipulação de ficheiros e JSON**
- 🧠 **Validação e utilidades de texto**

---

## 🚀 Instalação

```bash
pip install pybrige
```

Para instalar com extras de documentação:

```bash
pip install "pybrige[docs]"
```

---

## ⚡ Exemplo Rápido

Veja como o PyBrige pode simplificar seu fluxo:

```python
from pybrige import setup_logging, retry, timer

setup_logging(colors=True)

@retry(tries=3, delay=2)
@timer()
def exemplo():
    print("Executando tarefa...")

exemplo()
```

Saída esperada:
```
[INFO] Executando tarefa...
[PERF] 'exemplo' executado em 0.02s
```

---

## 📚 Estrutura da Documentação

- **Instalação:** Como configurar o PyBrige.  
- **Guias:** Tutoriais práticos (Logging, CLI, Configuração).  
- **Referência da API:** Documentação detalhada das funções e módulos.  
- **Roadmap:** O que vem nas próximas versões.  
- **Contribuir:** Como ajudar a construir o PyBrige.  

---

## 🧭 Filosofia do Projeto

> “Produtividade é mais do que escrever código rápido — é escrever código limpo, reutilizável e confiável.”

O PyBrige foi criado para desenvolvedores que valorizam **clareza**, **organização** e **eficiência**.  
Nosso foco é tornar o desenvolvimento Python mais fluido e intuitivo, sem comprometer a simplicidade.

---

## 🔗 Recursos

- 🏠 [Repositório no GitHub](https://github.com/juliobrige/pybrige)
- 📦 [PyPI](https://pypi.org/project/pybrige/)
- 🧩 [Documentação Oficial](https://juliobrige.github.io/pybrige/)

---

## 💬 Contribua

Quer ajudar o projeto a crescer?  
Veja o guia [Como Contribuir](contributing.md) e junte-se à comunidade.

---

📘 **Licença:** MIT  
Criado e mantido por **Julio Benjamim Bernardo Brige**

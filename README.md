# 🐍 PyBrige

[![PyPI](https://img.shields.io/pypi/v/pybrige.svg?color=blue&label=pypi)](https://pypi.org/project/pybrige/)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://pypi.org/project/pybrige/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/juliobrige/pybrige/blob/main/LICENSE)
[![Build](https://github.com/juliobrige/pybrige/actions/workflows/python-tests.yml/badge.svg)](https://github.com/juliobrige/pybrige/actions/workflows/python-tests.yml)
[![Coverage](https://img.shields.io/badge/coverage-92%25-brightgreen.svg)](https://github.com/juliobrige/pybrige)
[![Docs](https://img.shields.io/badge/docs-online-blue.svg)](https://juliobrige.github.io/pybrige/)

---

<div align="center">

### 🇧🇷 Português · [🇺🇸 English](#english-version)

Um **toolkit de produtividade para desenvolvedores Python**, com utilitários para logging elegante, manipulação de JSON, validação, decorators inteligentes e automação de tarefas.

</div>

---

## ✨ Visão Geral

**PyBrige** é um toolkit moderno criado para eliminar código repetitivo em projetos Python, oferecendo funções reutilizáveis para logging, configuração, análise de tempo e manipulação de dados.

Com `pybrige`, você ganha **velocidade**, **clareza** e **organização** no desenvolvimento — sem perder o controle.

---

## 🚀 Instalação

```bash
pip install pybrige
```

---

## ⚡ Exemplo Rápido

```python
from pybrige import setup_logging, timer, retry, load_env, EnvSpec, VarSpec

setup_logging(colors=True)

config = load_env(EnvSpec(vars=[
    VarSpec("API_URL", help="URL da API"),
    VarSpec("RETRIES", type="int", default=3)
]))

@retry(tries=config["RETRIES"], delay=1)
@timer(template="[PERF] '{func_name}' executou em {elapsed:.2f}s")
def buscar_dados():
    import requests
    resp = requests.get(config["API_URL"])
    resp.raise_for_status()
    return resp.json()

dados = buscar_dados()
print(dados)
```

---

## 🔧 Funcionalidades Principais

| Categoria | Recursos |
|------------|-----------|
| ⚙️ **Configuração** | `load_env`, `EnvSpec`, `VarSpec` |
| 🧠 **Logging** | `setup_logging` com cores e formatação avançada |
| ⏱️ **Decorators** | `@retry`, `@timer` |
| 🧩 **JSON Utils** | `read_json`, `write_json`, `append_json_line`, `pretty_print_json` |
| 🧵 **Texto & Strings** | `slugify`, `camel_to_snake`, `extract_emails`, `extract_urls`, `validate_bi` |
| 🎨 **Extras Visuais** | `ascii_banner_hacker`, `matrix_rain_preview` |

---

## 🧪 Exemplo de Uso: `validate_bi`

```python
from pybrige import validate_bi

print(validate_bi("123456789012A"))   # ✅ True
print(validate_bi("123456-789012-B")) # ✅ True
print(validate_bi("invalido"))        # ❌ False
```

---

## 🗺️ Roadmap

- [ ] Suporte a YAML (`io_utils`)  
- [ ] Novas transformações de texto (kebab-case, title case)  
- [ ] CLI interativo (`pybrige build`, `pybrige upload`)  

---

## 🤝 Contribuindo

Quer contribuir? ❤️  
Siga estes passos simples:

```bash
# 1. Fork o repositório
# 2. Crie sua branch
git checkout -b minha-feature

# 3. Commit e push
git commit -m "Nova feature"
git push origin minha-feature
```

Depois, abra um **Pull Request** 🚀

---

## 📄 Licença

Distribuído sob a licença **MIT**.  
Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🌍 Links

- 📦 **PyPI:** [pypi.org/project/pybrige](https://pypi.org/project/pybrige)
- 💻 **GitHub:** [github.com/juliobrige/pybrige](https://github.com/juliobrige/pybrige)
- 📘 **Documentação:** [juliobrige.github.io/pybrige](https://juliobrige.github.io/pybrige)

---

# 🇺🇸 English Version

[![PyPI](https://img.shields.io/pypi/v/pybrige.svg?color=blue&label=pypi)](https://pypi.org/project/pybrige/)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://pypi.org/project/pybrige/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/juliobrige/pybrige/blob/main/LICENSE)
[![Docs](https://img.shields.io/badge/docs-online-blue.svg)](https://juliobrige.github.io/pybrige/)

---

<div align="center">

A **developer productivity toolkit for Python**, featuring elegant logging, retry decorators, JSON utilities, environment handling, and automation helpers.

</div>

---

## ✨ Overview

**PyBrige** is a lightweight productivity toolkit designed to simplify repetitive tasks in Python projects — from environment management to data handling and logging.

You get **cleaner code**, **faster setup**, and **powerful tools** ready to use.

---

## 🚀 Installation

```bash
pip install pybrige
```

---

## ⚡ Quick Example

```python
from pybrige import setup_logging, retry, timer

setup_logging(colors=True)

@retry(tries=3, delay=1)
@timer()
def fetch_data():
    print("Fetching data...")
    return {"ok": True}

fetch_data()
```

---

## 🔧 Key Features

| Category | Features |
|-----------|-----------|
| ⚙️ **Config** | Environment validation (`load_env`, `EnvSpec`, `VarSpec`) |
| 🧠 **Logging** | Simple colorized logging (`setup_logging`) |
| ⏱️ **Decorators** | `@retry`, `@timer` |
| 🧩 **JSON Utils** | `read_json`, `write_json`, `append_json_line` |
| 🔠 **Text Utils** | `slugify`, `camel_to_snake`, `extract_emails`, `extract_urls` |
| 💻 **CLI (coming soon)** | `pybrige build`, `pybrige upload`, `pybrige version` |

---

## 🤝 Contributing

We welcome contributions!  
Fork, create your branch, commit, push, and open a PR 🚀

---

## 📄 License

Distributed under the **MIT License**.  
See [LICENSE](LICENSE) for details.

---

## 🌐 Links

- PyPI → [pypi.org/project/pybrige](https://pypi.org/project/pybrige)  
- GitHub → [github.com/juliobrige/pybrige](https://github.com/juliobrige/pybrige)  
- Docs → [juliobrige.github.io/pybrige](https://juliobrige.github.io/pybrige)

---

💡 *Inspired by the clean documentation style of [FastAPI](https://fastapi.tiangolo.com/) — modern, organized, and developer-friendly.*

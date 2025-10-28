# 📘 Referência da API

Esta secção contém a documentação detalhada da API do **PyBrige**.  
Aqui você encontrará informações sobre todas as **funções**, **classes** e **métodos** disponíveis, gerados automaticamente a partir das docstrings do código-fonte.

---

## 🧭 Utilização

Para navegar pela API, utilize o **menu lateral** ou a **barra de pesquisa** no topo da página.

A documentação cobre os seguintes módulos principais:

- `pybrige.core.automation`
- `pybrige.core.config`
- `pybrige.core.logging`
- `pybrige.decorators`
- `pybrige.utils.io`
- `pybrige.utils.dicts`
- `pybrige.utils.formatting`
- `pybrige.utils.text`

---

## 🧱 Estrutura da API

Cada módulo do PyBrige foi projetado com **simplicidade e reutilização** em mente.  
Abaixo, um resumo das principais funcionalidades expostas:

### 🔧 `pybrige.core.config`
Manipula variáveis de ambiente e configuração de aplicações.

```python
from pybrige.core.config import load_env, EnvSpec, VarSpec

# Carrega variáveis do .env e valida
config = load_env(EnvSpec(vars=[
    VarSpec("API_KEY", help="Chave da API"),
    VarSpec("DB_URL", help="URL do banco de dados"),
]))
```

### 🧩 `pybrige.decorators`
Decorators prontos para produtividade.

```python
from pybrige.decorators import retry, timer

@retry(tries=3, delay=2)
@timer()
def call_api():
    pass
```

### 📦 `pybrige.utils.io`
Funções para manipulação de ficheiros, JSON e CSV.

```python
from pybrige.utils.io import read_json, write_json

write_json("data.json", {"id": 1})
print(read_json("data.json"))
```

### 💬 `pybrige.utils.text`
Manipulação de texto e validações.

```python
from pybrige.utils.text import slugify, validate_bi

print(slugify("Título de Exemplo"))  # "titulo-de-exemplo"
print(validate_bi("123456789012A"))  # True
```

### ⚙️ `pybrige.core.automation`
Automação de tarefas de build, upload e versionamento.

```python
from pybrige.core.automation import build_package, upload_package

build_package()
upload_package(repository="pypi")
```

---

## 🔍 Documentação Automática

> ⚠️ Esta secção será **preenchida automaticamente** após a integração do plugin `mkdocstrings` (planejada para a versão `v0.8`).

A partir da v0.8, a documentação será gerada dinamicamente com base nas **docstrings** do código-fonte, utilizando:

```yaml
plugins:
  - mkdocstrings:
      handlers:
        python:
          options:
            show_root_heading: true
            show_object_full_path: false
            heading_level: 2
            docstring_style: google
```

---

## 🧭 Próximos Passos

- [Primeiros Passos](guides/getting-started.md)
- [Guia de Configuração](guides/configuration.md)
- [CLI e Automação](guides/cli.md)

---

📘 *Dica:* para contribuir com a documentação da API, adicione **docstrings completas** aos módulos e funções do PyBrige.  
Use o formato Google ou NumPy para uma melhor integração com `mkdocstrings`.

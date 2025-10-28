# 🚀 Primeiros Passos com o PyBrige

O **PyBrige** é um toolkit leve e modular criado para ajudar desenvolvedores Python a escrever código mais rápido, limpo e produtivo.  
Aqui está um guia rápido para começar a usá-lo.

---

## 📦 Instalação

Instale o pacote diretamente do PyPI:

```bash
pip install pybrige
```

Verifique se foi instalado corretamente:

```bash
python -m pip show pybrige
```

Saída esperada:
```
Name: pybrige
Version: 0.5.1
Summary: Toolkit de produtividade para desenvolvedores Python.
```

---

## 🧠 Ideia Principal

O PyBrige reúne utilitários comuns que normalmente precisaríamos reescrever em cada projeto:
- Logging elegante e configurável 🎨  
- Carregamento e validação de variáveis de ambiente 🌍  
- Decorators úteis (`@retry`, `@timer`) ⚙️  
- Manipulação de JSON e texto 🧩

---

## 💡 Exemplo Rápido

```python
import logging
from pybrige import setup_logging, retry, timer

# Configura logs coloridos
setup_logging(colors=True)

@retry(tries=3, delay=2)
@timer()
def fetch_data():
    logging.info("Simulando chamada de API...")
    return {"status": "ok", "message": "Dados obtidos com sucesso"}

if __name__ == "__main__":
    data = fetch_data()
    print(data)
```

Saída esperada:
```
[INFO] Simulando chamada de API...
[PERF] 'fetch_data' executou em 0.02s
{'status': 'ok', 'message': 'Dados obtidos com sucesso'}
```

---

## ⚙️ Estrutura de Projeto Recomendada

Ao usar o PyBrige, é comum organizar os ficheiros da seguinte forma:

```
my_project/
├── .env
├── pyproject.toml
├── src/
│   └── main.py
└── requirements.txt
```

**.env**
```
API_URL=https://api.exemplo.com
RETRIES=3
```

**main.py**
```python
from pybrige import load_env, EnvSpec, VarSpec

config = load_env(EnvSpec(vars=[
    VarSpec("API_URL"),
    VarSpec("RETRIES", type="int", default=3)
]))

print(config)
```

---

## 🧩 Recursos Disponíveis

### Logging
```python
from pybrige import setup_logging
setup_logging(level="DEBUG", colors=True)
```

### Retry
```python
from pybrige import retry

@retry(tries=5, delay=1)
def unstable():
    pass
```

### Timer
```python
from pybrige import timer

@timer()
def slow_task():
    pass
```

### JSON Utils
```python
from pybrige import write_json, read_json
write_json("data.json", {"name": "Alice"})
print(read_json("data.json"))
```

---

## 🧭 Próximos Passos

- [CLI e Automação](cli.md)
- [Configuração](configuration.md)
- [Logging](logging.md)
- [Referência da API](../api-reference.md)

---

✨ **Dica:** Combine o PyBrige com ferramentas como **Rich**, **Typer** e **Pydantic** para criar pipelines poderosos e aplicações Python mais produtivas.

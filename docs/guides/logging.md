# 🧾 Logging com PyBrige

O **PyBrige** fornece um sistema de logging elegante e personalizável baseado no módulo `logging` da biblioteca padrão do Python — mas com **cores**, **níveis aprimorados** e **configuração simplificada**.

---

## 🚀 Introdução

Para ativar o logging colorido e pronto para uso:

```python
from pybrige import setup_logging
import logging

setup_logging(colors=True)

logging.info("Aplicação iniciada com sucesso!")
logging.warning("Aviso: conexão lenta detectada.")
logging.error("Erro ao carregar configuração.")
```

Saída esperada no terminal:

```
[INFO] Aplicação iniciada com sucesso!
[WARNING] Aviso: conexão lenta detectada.
[ERROR] Erro ao carregar configuração.
```

---

## ⚙️ Opções Disponíveis

A função `setup_logging()` aceita diversos parâmetros opcionais:

| Parâmetro | Tipo | Descrição |
|------------|------|------------|
| `level` | `str` | Define o nível mínimo de logs exibidos (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`). |
| `colors` | `bool` | Ativa logs coloridos (usando o módulo `rich`). |
| `file` | `str | Path` | Caminho para gravar logs em ficheiro. |
| `logger_name` | `str` | Define o nome do logger principal. |

Exemplo completo:

```python
from pybrige import setup_logging
setup_logging(level="DEBUG", colors=True, file="logs/app.log", logger_name="pybrige-demo")
```

---

## 🎨 Exemplo de Saída Colorida

O PyBrige usa **Rich** para formatar mensagens de forma clara e visualmente agradável.

```
[12:01:05] INFO     Servidor iniciado na porta 8080
[12:01:05] DEBUG    Configuração carregada de .env
[12:01:07] WARNING  Latência acima do esperado
[12:01:10] ERROR    Falha ao conectar ao banco de dados
[12:01:12] CRITICAL Aplicação encerrada inesperadamente
```

---

## 🧩 Logando em Ficheiro

Você pode salvar logs num ficheiro e manter a saída colorida no terminal:

```python
setup_logging(file="logs/system.log", colors=True)
```

Isso cria automaticamente o diretório `logs/` se ele não existir.

---

## 🧠 Boas Práticas

- Defina níveis apropriados (`DEBUG` para dev, `INFO` para produção).  
- Evite `print()` — use sempre `logging`.  
- Combine com `timer` e `retry` para logs automáticos de performance e falhas.  

Exemplo:

```python
from pybrige import setup_logging, retry, timer
import logging, random

setup_logging(colors=True)

@retry(tries=3, delay=1)
@timer()
def process_data():
    if random.random() < 0.5:
        raise ValueError("Erro de processamento")
    return "Processado com sucesso!"

logging.info(process_data())
```

---

## 🔧 Integração com CLI

Os comandos da CLI do PyBrige também utilizam o mesmo sistema de logging, garantindo uma saída uniforme e informativa.

---

## 🧭 Próximos Passos

- [Guia de Configuração](configuration.md)
- [CLI e Automação](cli.md)
- [Referência da API](../api-reference.md)

---

📘 *Dica:* Combine o `setup_logging()` com `EnvSpec` e `.env` para configurar níveis de log dinamicamente, por exemplo:

```python
LOG_LEVEL=DEBUG
```

```python
from pybrige import load_env, setup_logging

config = load_env()
setup_logging(level=config.get("LOG_LEVEL", "INFO"))
```

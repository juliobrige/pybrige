# ⚙️ Configuração

O **PyBrige** oferece um sistema flexível e seguro para gerenciar as configurações da sua aplicação —  
desde variáveis de ambiente (`.env`) até ficheiros de configuração (`pyproject.toml`).

---

## 🌍 Carregamento de Variáveis de Ambiente (.env)

Use `pybrige.core.config.load_env()` para carregar variáveis de ambiente de um ficheiro `.env` para `os.environ`.

```python
# Exemplo de ficheiro .env
# DB_HOST=localhost
# DB_PORT=5432
# API_KEY=abc123def456

from pybrige.core.config import load_env, require_vars

# Carrega variáveis do .env no diretório atual
load_env()

# Requer variáveis obrigatórias
try:
    required = require_vars(["DB_HOST", "API_KEY"])
    print(f"DB_HOST: {required['DB_HOST']}")
    print(f"API_KEY: {required['API_KEY']}")
except Exception as e:
    print(f"Erro de configuração: {e}")
```

A partir daí, pode aceder diretamente via:

```python
import os
print(f"DB_PORT: {os.getenv('DB_PORT')}")
```

---

## 📘 Configurações do Projeto (pyproject.toml)

Desde a versão **v0.6**, o PyBrige consegue ler e interpretar configurações básicas do ficheiro `pyproject.toml`.  
No futuro, esse suporte será expandido para um sistema completo de configuração hierárquica.

Exemplo:

```toml
[tool.pybrige]
log_level = "INFO"
database_url = "sqlite:///./dev.db"
```

---

## 🧩 Validação de Configuração com VarSpec e EnvSpec

Com `VarSpec` e `EnvSpec`, você pode definir esquemas para validar suas variáveis de ambiente —  
garantindo tipos corretos, valores padrão e faixas permitidas.

```python
from pybrige.core.config import EnvSpec, VarSpec

class AppConfig(EnvSpec):
    DATABASE_URL: VarSpec[str] = VarSpec("DATABASE_URL", default="sqlite:///./test.db")
    DEBUG_MODE: VarSpec[bool] = VarSpec("DEBUG_MODE", default=False)
    WORKERS: VarSpec[int] = VarSpec("WORKERS", default=4, min_value=1)

# Carrega e valida
config = AppConfig.load()

print(f"Database URL: {config.DATABASE_URL}")
print(f"Debug Mode: {config.DEBUG_MODE}")
print(f"Workers: {config.WORKERS}")
```

Se uma variável estiver ausente ou inválida, o PyBrige levantará um erro com explicação detalhada.

---

## 🔒 Boas Práticas

- Nunca exponha dados sensíveis no código (como `API_KEY`).
- Use `.env.example` para partilhar o modelo de configuração.
- Adicione `.env` ao `.gitignore`.
- Valide tudo com `EnvSpec` e `VarSpec`.

---

## 🧭 Próximos Passos

A versão **v0.8** introduzirá:

- Configuração hierárquica completa (YAML, TOML e Env).  
- Validação com **Pydantic**.  
- Perfis de ambiente (`dev`, `prod`, `test`).  
- Integração com CLI: `pybrige config show`.

---

📘 Consulte também:
- [Guia de Logging](logging.md)
- [CLI e Automação](cli.md)
- [Primeiros Passos](getting-started.md)

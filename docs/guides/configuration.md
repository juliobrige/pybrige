# ⚙️ Configuração

O **PyBrige** oferece um sistema flexível para gerenciar as configurações da sua aplicação — desde variáveis de ambiente (`.env`) até ficheiros de configuração (`pyproject.toml`).

---

## 🌍 Carregamento de Variáveis de Ambiente (.env)

Utilize `pybrige.core.config.load_env()` para carregar variáveis de ambiente de um ficheiro `.env` diretamente para o `os.environ`.

### Exemplo

```python
# Exemplo de ficheiro .env
# DB_HOST=localhost
# DB_PORT=5432
# API_KEY=abc123def456

from pybrige.core.config import load_env, require_vars

# Carrega variáveis do .env no diretório atual
load_env()

# Requere que certas variáveis estejam definidas, ou levanta um erro
try:
    required = require_vars(["DB_HOST", "API_KEY"])
    print(f"DB_HOST: {required['DB_HOST']}")
    print(f"API_KEY: {required['API_KEY']}")
except Exception as e:
    print(f"Erro de configuração: {e}")

# Acessar variáveis diretamente
import os
print(f"DB_PORT: {os.getenv('DB_PORT')}")

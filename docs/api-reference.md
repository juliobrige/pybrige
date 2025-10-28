# 🧩 Referência da API

Esta secção contém a **documentação detalhada da API do PyBrige**.

Aqui você encontrará informações sobre todas as **funções, classes e métodos disponíveis**, que serão **geradas automaticamente** a partir das *docstrings* do código-fonte.

---

## 📘 Utilização

Para navegar pela API, use o **menu lateral** ou a **barra de pesquisa** no topo.  
A referência será atualizada automaticamente conforme novas versões forem lançadas.

---

## 🧠 Módulos Principais

### 🔹 `pybrige.core.automation`
Gerencia automações, build, upload e versionamento de pacotes Python.

Funções planejadas:
- `build_package()`
- `upload_package(repo='pypi')`
- `increment_version(part='patch' | 'minor' | 'major')`
- `run_command(cmd)`

---

### 🔹 `pybrige.core.config`
Manipula variáveis de ambiente e arquivos `.env` de forma tipada e validada.

Funções principais:
- `load_env(EnvSpec)`
- `require_vars(vars)`
- `setup_logging(level, colors, file, logger_name)`

---

### 🔹 `pybrige.core.logging`
Configuração avançada de logs coloridos e padronizados.

Recursos:
- Formatação enriquecida com `rich`
- Suporte a arquivos de log
- Integração com decorators (`@retry`, `@timer`)

---

### 🔹 `pybrige.decorators`
Decorators utilitários para produtividade e resiliência de código.

Funções principais:
- `@retry` — repete a execução de funções em caso de falha.
- `@timer` — mede o tempo de execução e mostra logs automáticos.

---

### 🔹 `pybrige.utils.io`
Funções de leitura e escrita de ficheiros JSON, CSV e JSON Lines.

Exemplos:
- `read_json(path)`
- `write_json(path, data)`
- `append_json_line(path, record)`
- `pretty_print_json(data)`
- `merge_json_files(dir)`
- `validate_json(data)`

---

### 🔹 `pybrige.utils.dicts`
Funções para manipulação avançada de dicionários.

Exemplos:
- `merge_dicts_deep(dict1, dict2)`
- `get_nested_value(d, keys, default=None)`

---

### 🔹 `pybrige.utils.formatting`
Funções para formatação de tempo, tamanhos e strings de exibição.

Exemplos:
- `format_size(bytes)`
- `format_time(seconds)`

---

### 🔹 `pybrige.utils.text`
Manipulação e extração de texto.

Funções principais:
- `slugify(text)`
- `camel_to_snake(text)`
- `snake_to_camel(text)`
- `normalize_whitespace(text)`
- `remove_html_tags(text)`
- `extract_emails(text)`
- `extract_urls(text)`
- `validate_bi(bi_number)` — valida bilhetes de identidade moçambicanos.

---

## ⚙️ Integração com MkDocs

Na versão **v0.8**, esta secção será **gerada automaticamente** pelo plugin [`mkdocstrings`](https://mkdocstrings.github.io/):

```yaml
plugins:
  - mkdocstrings:
      handlers:
        python:
          selection:
            docstring_style: google
          options:
            show_root_heading: true
            show_category_heading: true
            show_full_path: false

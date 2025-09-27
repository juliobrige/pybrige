# Changelog

Todas as mudanças notáveis neste projeto serão documentadas aqui.  
O formato segue as recomendações do [Keep a Changelog](https://keepachangelog.com/).

---

## [0.3.0] - 2025-09-26
### Added
- **Módulo `io_utils`**:
  - `write_json`: escreve dicionários/listas em JSON com indentação e UTF-8.
  - `read_json`: leitura de JSON com modo seguro (`safe=True`).
  - `append_json_line`: suporte a JSON Lines (logs).
  - `pretty_print_json`: imprime objetos Python em JSON formatado.

- **Módulo `text_utils`**:
  - `slugify`: agora com suporte a Unicode (`allow_unicode=True`).
  - `camel_to_snake`: conversor de `CamelCase` → `snake_case`.
  - `snake_to_camel`: conversor de `snake_case` → `CamelCase` (com suporte opcional a siglas).
  - `normalize_whitespace`: remove espaços extras.
  - `remove_html_tags`: sanitiza texto removendo tags HTML.
  - `extract_emails`: extrai endereços de e-mail de strings.
  - `extract_urls`: extrai URLs (incluindo paths e queries).

### Changed
- Regexes refinadas para maior confiabilidade em `extract_emails` e `extract_urls`.

---

## [0.2.0] - 2025-09-25
### Added
- **Módulo `robustness`**:
  - `retry`: decorator para repetir execução de funções em caso de erro.
  - Novos parâmetros:
    - `exceptions`: definir quais exceções disparam retries.
    - `sleep_func`: função de sleep injetável (útil em testes).
    - `log_success`: loga sucesso após retries.

---

## [0.1.1] - 2025-09-24
### Added
- Logging colorido (`setup_logging`).
- `timer`: agora com suporte a timestamp e template customizado.

### Fixed
- Cobertura de testes completa para `logging` e `timing`.

---

## [0.1.0] - 2025-09-23
### Added
- Versão inicial:
  - `require_vars` para validação de variáveis de ambiente.
  - `print_table` para exibição de tabelas.
  - Estrutura de testes e publicação no TestPyPI.

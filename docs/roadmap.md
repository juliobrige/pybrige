# Roadmap do PyBrige

O `pybrige` está em constante evolução. Aqui está o nosso roadmap para as próximas versões, detalhando as funcionalidades planeadas para impulsionar a produtividade do desenvolvedor Python.

---

## v0.6 – Núcleo Estável (Fundação)

Foco na construção de uma base sólida com utilitários essenciais para automação e gestão de projetos.

* **`pybrige.core.automation`**: Implementação das funções `run_command`, `build_package`, `upload_package`.
* **`pybrige.core.logging`**: `setup_root_logger(json=False)`, com handlers opcionais para ficheiro e console.
* **`pybrige.utils.io`**: Funções `read_text`/`write_text`, `temp_file()`, `get_project_root()`.
* **`pybrige.core.config`**: Carregamento de variáveis de ambiente de `.env` e configurações de `pyproject.toml` (com fallback).
* **CLI inicial (`pybrige.cli`, Typer)**: Comandos `pybrige build`, `pybrige upload`, `pybrige version --bump patch`.

---

## v0.7 – Integrações

Expansão para integrar o `pybrige` com serviços externos e melhorar as capacidades de relatório.

* **`pybrige.services.pypi`**: Funções para `get_package_info`, `search_pypi`.
* **`pybrige.services.github`**: Funções para `get_latest_tag`, `create_github_release`.
* **`pybrige.services.notify`**: Funções para `send_slack_message`, `send_discord_message`.
* **`pybrige.reporting`**: Implementação de `create_markdown_report`, `summarize_logs`.

---

## v0.8 – Qualidade & DX (Developer Experience)

Melhorias focadas na experiência do desenvolvedor, qualidade de código e gestão avançada de configuração.

* **Decorators**: Novos decorators como `@cache_result`, `@validate_args`.
* **Configuração Hierárquica**: Sistema de configuração robusto com prioridade (Variáveis de Ambiente > YAML/TOML > Valores Padrão) e validação com Pydantic.
* **`pybrige.reporting`**: `generate_coverage_report(html_out)` para relatórios de cobertura de código.
* **Formatação e Utilitários**: Novas funções utilitárias como `format_bytes`, `format_duration`, `slugify`, `truncate_string`.

---

## v1.0 – CI/CD e Estabilidade

Foco na automação completa do ciclo de vida do desenvolvimento e na garantia da estabilidade e maturidade do projeto.

* **Pipeline GitHub Actions**: Implementação de um workflow completo para `build`, `test`, `publish PyPI` e `release GitHub`.
* **Versionamento Semântico**: Consistência rigorosa no versionamento.
* **Documentação e Exemplos**: Documentação completa e bem detalhada, com muitos exemplos práticos de uso.
* **Testes de Contrato/CLI Snapshots**: Melhoria da robustez dos testes com testes de contrato para APIs e snapshots para a saída da CLI.
* **Deprecações Documentadas**: Gestão clara e documentada de funcionalidades depreciadas para garantir a compatibilidade futura.

---

Este roadmap é um guia e pode ser ajustado com base no feedback da comunidade e nas prioridades do desenvolvimento. Estamos ansiosos para construir o `pybrige` com você\!
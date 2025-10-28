# 🗺️ Roadmap do PyBrige

O **PyBrige** está em constante evolução.  
Este roadmap descreve as versões planejadas e as funcionalidades que serão introduzidas para impulsionar a produtividade dos desenvolvedores Python.

---

## 🧩 v0.6 — Núcleo Estável (Fundação)

Foco: **Base sólida com utilitários essenciais** para automação e gestão de projetos.

### Principais funcionalidades:
- `pybrige.core.automation`: Implementação das funções `run_command`, `build_package`, `upload_package`.
- `pybrige.core.logging`: Novo `setup_root_logger(json=False)` com suporte a múltiplos handlers (console e ficheiro).
- `pybrige.utils.io`: Funções `read_text`, `write_text`, `temp_file()`, `get_project_root()`.
- `pybrige.core.config`: Leitura e carregamento de configurações do `.env` e `pyproject.toml`.
- **CLI inicial (`pybrige.cli`)**: Com comandos `pybrige build`, `pybrige upload`, `pybrige version --bump patch`.

---

## 🔗 v0.7 — Integrações

Foco: **Conectividade com serviços externos e relatórios avançados.**

### Principais funcionalidades:
- `pybrige.services.pypi`: Funções `get_package_info`, `search_pypi`.
- `pybrige.services.github`: Funções `get_latest_tag`, `create_github_release`.
- `pybrige.services.notify`: Notificações automáticas com `send_slack_message`, `send_discord_message`.
- `pybrige.reporting`: Relatórios automáticos com `create_markdown_report`, `summarize_logs`.

---

## ⚙️ v0.8 — Qualidade e Experiência do Desenvolvedor (DX)

Foco: **Melhorias na experiência do desenvolvedor e gestão avançada de configuração.**

### Principais funcionalidades:
- Novos decorators: `@cache_result`, `@validate_args`.
- **Configuração hierárquica**: Prioridade entre `.env`, YAML/TOML e variáveis de ambiente, com validação via **Pydantic**.
- `pybrige.reporting`: Novo `generate_coverage_report(html_out)` para relatórios de cobertura.
- Funções utilitárias novas: `format_bytes`, `format_duration`, `slugify`, `truncate_string`.

---

## 🚀 v1.0 — CI/CD e Estabilidade

Foco: **Automação completa do ciclo de vida e estabilidade do projeto.**

### Principais funcionalidades:
- **Pipeline GitHub Actions completo** para `build`, `test`, `publish PyPI` e `release GitHub`.
- **Versionamento Semântico** rigoroso.
- **Documentação abrangente** com exemplos reais e demonstrações.
- **Testes de Contrato/CLI Snapshots** para garantir a integridade do comportamento.
- **Gestão de deprecações** com clareza e compatibilidade futura.

---

## 💬 Nota Final

> Este roadmap é um guia evolutivo e poderá ser ajustado com base no feedback da comunidade e nas prioridades do desenvolvimento.  
> O objetivo do PyBrige é crescer **junto com os desenvolvedores Python**, simplificando tarefas, otimizando fluxos e promovendo código de qualidade.

---

📘 *Próximos passos*:  
- [Referência da API](api-reference.md)  
- [Como Contribuir](contributing.md)

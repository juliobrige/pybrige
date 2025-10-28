# 🧮 Interface de Linha de Comando (CLI)

O **PyBrige CLI** fornece uma forma rápida e poderosa de executar tarefas de automação diretamente pelo terminal.  
Ele é construído com o framework [Typer](https://typer.tiangolo.com/), o mesmo usado pela FastAPI, garantindo simplicidade e robustez.

---

## 🚀 Introdução

Após instalar o pacote, o comando `pybrige` estará disponível globalmente (ou via `python -m pybrige.cli.main`).  
Você pode verificar se está tudo funcionando com:

```bash
pybrige --help
```

Saída esperada:

```
Ferramenta de linha de comando para automação e utilitários de desenvolvimento Python.

Usage: pybrige [OPTIONS] COMMAND [ARGS]...
```

---

## ⚙️ Comandos Disponíveis

### 🔹 `--version`

Exibe a versão atual instalada do PyBrige.

```bash
pybrige --version
```

Saída esperada:

```
pybrige CLI Version: 0.5.1
```

---

### 🔹 `build`

Constrói os pacotes de distribuição (`wheel` e `sdist`) do projeto.

```bash
pybrige build
```

**Opções:**

| Opção | Descrição |
|-------|------------|
| `--clean, -c` | Limpa o diretório `dist/` antes de construir. |

Exemplo:

```bash
pybrige build --clean
```

Saída esperada:
```
Executando comando 'build' (clean=True)...
Limpando o diretório 'dist/'...
Construindo pacotes de distribuição...
Pacotes construídos com sucesso na pasta 'dist/'.
```

---

### 🔹 `upload`

Faz upload dos pacotes para o **PyPI** ou **TestPyPI**.

```bash
pybrige upload
```

**Opções:**

| Opção | Descrição |
|-------|------------|
| `--repo, -r` | Define o repositório de destino (`pypi` ou `testpypi`). |
| `--dry-run` | Executa o processo sem enviar os ficheiros. |

Exemplo:

```bash
pybrige upload --repo testpypi --dry-run
```

Saída esperada:
```
Executando comando 'upload' para 'testpypi' (dry_run=True)...
Modo 'dry-run' ativado. Nenhum ficheiro será enviado.
Upload concluído (ou simulado) com sucesso.
```

---

### 🔹 `version`

Incrementa a versão do projeto conforme o padrão **semântico** (`patch`, `minor`, `major`).

```bash
pybrige version patch
```

**Parâmetros válidos:**  
- `patch` → 0.5.1 → 0.5.2  
- `minor` → 0.5.1 → 0.6.0  
- `major` → 0.5.1 → 1.0.0

Exemplo:

```bash
pybrige version minor
```

Saída esperada:
```
Incrementando a versão do projeto em 'minor'...
Versão incrementada com sucesso.
```

---

## 🧠 Dicas Avançadas

- Combine comandos para pipelines automatizados (ex: build → upload → version bump).  
- Use o comando `--help` em qualquer subcomando para ver detalhes adicionais:

```bash
pybrige upload --help
```

---

## 🧭 Roadmap Futuro (v0.6+)

- `pybrige test` → Executar testes com cobertura.  
- `pybrige lint` → Executar ruff + mypy automaticamente.  
- `pybrige docs` → Gerar e publicar documentação MkDocs no GitHub Pages.

---

📘 *Dica:* Todos os comandos são extensíveis. Novos subcomandos podem ser adicionados facilmente dentro do módulo `src/pybrige/cli/main.py`.

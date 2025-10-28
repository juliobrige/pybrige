# src/pybrige/cli/main.py
from __future__ import annotations

import typer
from importlib.metadata import PackageNotFoundError, version as pkg_version

try:
    from typing import Annotated  # 3.10+
except Exception:  # 3.8/3.9
    from typing_extensions import Annotated

app = typer.Typer(
    name="pybrige",
    help="Ferramenta de linha de comando para automação e utilitários de desenvolvimento Python.",
    pretty_exceptions_enable=True,
)

def __version_callback(value: bool):
    """Callback para --version/-v."""
    if value:
        try:
            ver = pkg_version("pybrige")
        except PackageNotFoundError:
            # fallback se ainda não estiver instalado como pacote
            try:
                from pybrige import __version__ as ver  # definir em src/pybrige/__init__.py
            except Exception:
                ver = "desenvolvimento"
        typer.echo(f"pybrige CLI Version: {ver}")
        raise typer.Exit()

@app.callback()
def main(
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            "-v",
            help="Mostra a versão da ferramenta pybrige.",
            callback=__version_callback,
            is_eager=True,
        ),
    ] = False,
):
    """Gestor de automação e utilitários para projetos Python."""
    # Nada a fazer aqui: o callback de versão já trata a saída.
    return

# --- Comandos ---

@app.command()
def build(
    clean: Annotated[
        bool,
        typer.Option("--clean", "-c", help="Limpa o diretório 'dist/' antes de construir.")
    ] = False,
):
    """Constrói wheel e sdist do projeto."""
    from rich import print
    print(f"[bold]Executando 'build' (clean={clean})...[/]")

    if clean:
        # TODO: implementar utils.io.remove_dist_directory()
        print("Limpando o diretório 'dist/'...")

    # TODO: ligar com pybrige.core.automation.build_package()
    # from pybrige.core.automation import build_package
    # build_package()
    print("[green]Pacotes construídos em 'dist/'.[/]")

@app.command()
def upload(
    repo: Annotated[
        str,
        typer.Option("--repo", "-r", help="Repositório de destino: pypi ou testpypi.")
    ] = "pypi",
    dry_run: Annotated[
        bool,
        typer.Option("--dry-run", help="Executa sem enviar os ficheiros.")
    ] = False,
):
    """Faz upload dos pacotes para PyPI ou TestPyPI."""
    from rich import print
    repo = repo.lower()
    if repo not in {"pypi", "testpypi"}:
        typer.secho("Erro: --repo deve ser 'pypi' ou 'testpypi'.", err=True, fg=typer.colors.RED)
        raise typer.Exit(code=2)

    print(f"[bold]Executando 'upload'[/] para '{repo}' (dry_run={dry_run})...")
    if dry_run:
        print("[yellow]Dry-run ativo. Nenhum arquivo será enviado.[/]")
    else:
        # TODO: ligar com pybrige.core.automation.upload_package(repo)
        # from pybrige.core.automation import upload_package
        # upload_package(repo)
        print(f"[green]Upload concluído para {repo}.[/]")


@app.command("version")
def bump_version(
    part: Annotated[str, typer.Argument(help="Parte da versão: patch | minor | major")] = "patch"
):
    """Incrementa a versão do projeto (ex.: pybrige version patch)."""
    part = part.lower()
    if part not in {"patch", "minor", "major"}:
        typer.secho("Erro: use 'patch', 'minor' ou 'major'.", err=True, fg=typer.colors.RED)
        raise typer.Exit(code=2)

    from rich import print
    print(f"Incrementando versão: [cyan]{part}[/] ...")
    # TODO: ligar com pybrige.core.automation.increment_version(part)
    # from pybrige.core.automation import increment_version
    # new_v = increment_version(part)
    # print(f"[green]Nova versão: {new_v}[/]")
    print("[green]Versão incrementada (simulada).[/]")

if __name__ == "__main__":
    app()

from __future__ import annotations

"""
pybrige - Um toolkit de produtividade para desenvolvedores em Python.
"""

# Core (módulo principal)
from .core import (
    MissingEnvVarsError, VarSpec, EnvSpec,
    load_env, require_vars, setup_logging,
)

# Decorators
from .decorators import (
    retry, timer,
)

# Utils (I/O, JSON, CSV, etc.)
from .utils.io import (
    parse_csv, write_json, read_json,
    append_json_line, pretty_print_json,
    iter_json_lines, read_json_lines, tail_json_lines,
    count_file_lines, merge_json_files, validate_json,
)

# Stubs (para evitar erro se ainda não implementou)
def extract_urls(*args, **kwargs): ...
def validate_bi(*args, **kwargs): ...

# --- Versão oficial ---
__version__ = "0.6.0"

__all__ = [
    "MissingEnvVarsError", "VarSpec", "EnvSpec",
    "load_env", "require_vars", "setup_logging",
    "retry", "timer",
    "parse_csv", "write_json", "read_json",
    "append_json_line", "pretty_print_json",
    "iter_json_lines", "read_json_lines", "tail_json_lines",
    "count_file_lines", "merge_json_files", "validate_json",
    "extract_urls", "validate_bi",
]

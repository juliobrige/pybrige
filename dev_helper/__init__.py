# --- Namespaces principais ---
from . import core
from . import formatting
from . import io_utils as io
from . import logging_utils as logging_utils
from . import robustness
from . import text
from . import timing

# --- Atalhos para os módulos mais usados ---
from .core import require_vars, MissingEnvVarsError, load_env, EnvSpec, VarSpec
from .logging_utils import setup_logging
from .timing import timer
from .robustness import retry
from .io_utils import write_json, read_json, append_json_line, pretty_print_json
from .formatting import print_table
from .text import (
    slugify, camel_to_snake, snake_to_camel,
    normalize_whitespace, remove_html_tags,
    extract_emails, extract_urls
)

# --- Versão ---
__version__ = "0.3.0"

# --- Exportação organizada ---
__all__ = [
    # Namespaces
    "core", "formatting", "io", "logging_utils", "robustness", "text", "timing",
    
    # Funções/Classes de alto nível
    "require_vars", "MissingEnvVarsError", "load_env", "EnvSpec", "VarSpec",
    "setup_logging", "timer", "retry",
    "write_json", "read_json", "append_json_line", "pretty_print_json",
    "print_table",
    "slugify", "camel_to_snake", "snake_to_camel",
    "normalize_whitespace", "remove_html_tags",
    "extract_emails", "extract_urls",
]

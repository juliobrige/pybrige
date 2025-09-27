import pytest
from dev_helper.core.config import (
    load_env,
    EnvSpec,
    VarSpec,
    MissingEnvVarsError
)

def test_load_env_success_basic(monkeypatch):
    """Testa o caminho feliz: todas as variáveis estão corretas."""
    monkeypatch.setenv("APP_DATABASE_URL", "postgresql://user:pass@host:5432/db")
    monkeypatch.setenv("APP_DEBUG", "true")
    monkeypatch.setenv("APP_PORT", "8080")
    monkeypatch.setenv("APP_ALLOWED_HOSTS", "localhost, 127.0.0.1")

    spec = EnvSpec(
        vars=[
            VarSpec("DATABASE_URL"),
            VarSpec("DEBUG", type="bool"),
            VarSpec("PORT", type="int"),
            VarSpec("ALLOWED_HOSTS", type="list"),
        ],
        prefix="APP_"
    )
    
    config = load_env(spec)

    assert config["DATABASE_URL"] == "postgresql://user:pass@host:5432/db"
    assert config["DEBUG"] is True
    assert config["PORT"] == 8080
    assert config["ALLOWED_HOSTS"] == ["localhost", "127.0.0.1"]

def test_load_env_uses_defaults(monkeypatch):
    """Testa se os valores padrão são usados quando as variáveis não estão definidas."""
    monkeypatch.delenv("APP_DEBUG", raising=False)
    monkeypatch.delenv("APP_PORT", raising=False)

    spec = EnvSpec(
        vars=[
            VarSpec("DEBUG", type="bool", required=False, default=False),
            VarSpec("PORT", type="int", required=False, default=9000),
        ],
        prefix="APP_"
    )
    config = load_env(spec)
    assert config["DEBUG"] is False
    assert config["PORT"] == 9000

def test_load_env_missing_required_var():
    """Testa se levanta um erro para uma variável obrigatória em falta."""
    spec = EnvSpec([VarSpec("API_KEY_SECRET", required=True)])
    with pytest.raises(MissingEnvVarsError) as excinfo:
        load_env(spec)
    assert "API_KEY_SECRET" in excinfo.value.missing



def test_load_env_invalid_type(monkeypatch):
    """Deve levantar MissingEnvVarsError quando o casting de tipo falha."""
    monkeypatch.setenv("PORT", "not-a-number")

    spec = EnvSpec(vars=[VarSpec(name="PORT", type=int)])

    with pytest.raises(MissingEnvVarsError) as excinfo:
        load_env(spec)

    # Verifica que a variável aparece na lista de inválidos
    assert "PORT" in str(excinfo.value)
    assert "invalid" in str(excinfo.value).lower()



    
def test_load_env_custom_validator_fails(monkeypatch):
    """Testa se um validador personalizado falha corretamente."""
    def port_must_be_privileged(p):
        if p >= 1024:
            raise ValueError("Port must be < 1024")

    monkeypatch.setenv("PORT", "8000")
    spec = EnvSpec([VarSpec("PORT", type="int", validator=port_must_be_privileged)])
    
    with pytest.raises(MissingEnvVarsError) as excinfo:
        load_env(spec)
    assert "PORT" in excinfo.value.invalid
    assert "Validation failed: Port must be < 1024" in excinfo.value.details["PORT"]
# 📦 Instalação

O **PyBrige** pode ser instalado diretamente a partir do [PyPI](https://pypi.org/project/pybrige/).  
Siga os passos abaixo para configurar o toolkit no seu ambiente.

---

## 💻 Requisitos

- Python **3.8 ou superior**
- pip atualizado (`pip install --upgrade pip`)

---

## 🚀 Instalação Rápida

Execute o seguinte comando no terminal:

```bash
pip install pybrige
```

Após a instalação, verifique se o PyBrige foi instalado corretamente:

```bash
python -m pip show pybrige
```

---

## 🧰 Instalação para Desenvolvimento

Se planeja contribuir com o projeto, instale o PyBrige com as dependências de desenvolvimento:

```bash
git clone https://github.com/juliobrige/pybrige.git
cd pybrige
pip install -e ".[dev]"
```

> 💡 Isso instala o pacote em modo editável, permitindo modificar o código localmente enquanto o utiliza.

---

## 🧩 Instalação com Extras

O PyBrige possui grupos opcionais de dependências (*extras*) para documentação e testes.

### 📘 Documentação
```bash
pip install "pybrige[docs]"
```

### 🧪 Testes
```bash
pip install "pybrige[test]"
```

---

## 🧱 Verificação da Instalação

Para testar se tudo está funcionando corretamente:

```python
from pybrige import setup_logging, __version__

setup_logging()
print(f"PyBrige instalado com sucesso! Versão: {__version__}")
```

Se você vir algo como:
```
PyBrige instalado com sucesso! Versão: 0.5.1
```
significa que a instalação foi concluída com êxito. 🎉

---

## 🧭 Próximos Passos

- [Primeiros Passos](guides/getting-started.md)  
- [CLI e Automação](guides/cli.md)  
- [Logging](guides/logging.md)  
- [Configuração](guides/configuration.md)

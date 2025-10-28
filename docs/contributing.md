# 🤝 Contribuir para o PyBrige

Agradecemos o seu interesse em contribuir para o **PyBrige**!  
Sua ajuda é fundamental para tornar esta ferramenta ainda mais poderosa e útil à comunidade Python.  
Seja para **relatar um bug**, **sugerir uma funcionalidade**, ou **enviar código**, todas as contribuições são bem-vindas. 💪

---

## 🐛 Relatar Bugs

Se encontrar um problema, por favor abra uma **Issue** no [GitHub](https://github.com/juliobrige/pybrige/issues).

Inclua:
- Uma descrição clara do erro.
- Os **passos para reproduzir** o problema.
- Informações sobre o seu ambiente:
  - Sistema operacional (Windows, Linux, macOS)
  - Versão do Python
  - Versão do PyBrige (`pip show pybrige`)

Exemplo:
```
**Descrição:** Erro ao carregar .env em Windows.
**Reprodução:** Executar load_env com variável inválida.
**Ambiente:** Python 3.12, Windows 11, PyBrige 0.5.1
```

---

## 💡 Sugerir Funcionalidades

Tem uma ideia que pode melhorar o PyBrige?  
Abra uma **Issue de sugestão** no GitHub e descreva:

- O problema que a funcionalidade resolve.
- Como você imagina que ela funcionaria.
- Exemplos de uso, se possível.

✨ Funcionalidades úteis e bem documentadas têm mais chance de serem implementadas rapidamente.

---

## 🧩 Contribuir com Código

1. Faça um **fork** do repositório [PyBrige](https://github.com/juliobrige/pybrige).
2. Clone o seu fork localmente:
   ```bash
   git clone https://github.com/<seu-usuario>/pybrige.git
   cd pybrige
   ```
3. Crie um branch descritivo:
   ```bash
   git checkout -b feature/minha-nova-feature
   # ou
   git checkout -b fix/erro-no-logging
   ```
4. Implemente suas alterações.
5. Escreva testes automatizados garantindo que tudo funciona.
6. Execute os testes:
   ```bash
   pytest
   ```
7. Verifique o estilo e os tipos:
   ```bash
   ruff check .
   mypy src/
   ```
8. Faça commit das mudanças:
   ```bash
   git commit -m "feat: adiciona suporte a configuração hierárquica"
   ```
9. Envie para o seu fork:
   ```bash
   git push origin feature/minha-nova-feature
   ```
10. Abra uma **Pull Request** (PR) no repositório principal.

---

## 🧱 Ambiente de Desenvolvimento

Para configurar o ambiente de desenvolvimento:

```bash
pip install "pybrige[dev]"
```

---

## 🧪 Testes

Para executar todos os testes:

```bash
pytest
```

Para gerar o relatório de cobertura de código:

```bash
pytest --cov=pybrige --cov-report=term-missing
```

---

## 🧭 Boas Práticas de Código

Siga estas diretrizes:

✅ **PEP 8** — estilo e formatação de código.  
✅ **Type hints** — facilite a leitura e o linting.  
✅ **Docstrings** — documente funções, classes e métodos.  
✅ **Commits descritivos** — explique *por que* e *o que* foi alterado.

Exemplo de docstring:

```python
def merge_dicts(a: dict, b: dict) -> dict:
    """
    Mescla dois dicionários recursivamente.
    
    Args:
        a: Dicionário base.
        b: Dicionário a ser mesclado.
    
    Returns:
        Um novo dicionário com os dados combinados.
    """
```
---

## 💬 Agradecimento

Agradecemos por contribuir para o sucesso do PyBrige!  
Cada sugestão, teste ou linha de código ajuda a fortalecer este projeto e a comunidade que o apoia. 🙌

> 💙 “O código é melhor quando é construído em conjunto.”

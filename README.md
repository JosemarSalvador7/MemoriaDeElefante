# build.sh

# Sincronizar_dependências

uv sync
# Compilar com Nuitka

uv run python -m nuitka --onefile --follow-imports --enable-plugin=tk-inter --include-data-dir=./img=img --output-dir=dist main.py

# Verificar o executável
ls -la dist/

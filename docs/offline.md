# Offline Setup

## uv
```bash
uv pip download -r requirements.txt -d packages/
uv sync --offline
```

## pip
```bash
python -m pip install --no-index --find-links=packages/
```

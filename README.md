# EMAI-COPD Documentation Build Notes

This repository uses Sphinx to build the documentation site under the `_build` folder.

## Location

- Project root: `EMAI-COPD/`
- Build script: `EMAI-COPD/run.sh`
- HTML output: `EMAI-COPD/_build/html/`

## Install Requirements (uv)

Install uv once (if needed):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Or 
```bash 
pip install uv
```

Then create the environment and install docs dependencies:

```bash
uv venv
source .venv/bin/activate
uv pip install sphinx furo
```

## Build the Docs

```bash
chmod +x run.sh
./run.sh
```

Optional one-shot (without activating .venv):

```bash
cd EMAI-COPD
uv run --with sphinx --with furo ./run.sh
```

Current script content:

```bash
sphinx-build -b html . _build/html
```

After a successful run, open:

- `_build/html/index.html`

## Clean Rebuild (Optional)

```bash
rm -rf _build
./run.sh
```

## Common Errors

1. `no theme named 'furo' found`
- Install the theme in the same active environment:
```bash
uv pip install furo
```

2. Python environment mismatch
- Make sure your shell is using the same environment where Sphinx was installed:
```bash
which python
uv pip show sphinx furo
```


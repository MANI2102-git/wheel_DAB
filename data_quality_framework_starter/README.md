# Data Quality Framework

A small Python package that checks whether required fields are present in records.

## Run the example

From the project root:

```bash
python -m pip install -e .
python examples/run_validation.py
```

## Build a wheel

```bash
python -m pip install build
python -m build --wheel
```

The wheel will be created under `dist/`.

## Run the test

```bash
python -m pip install pytest
python -m pytest
```

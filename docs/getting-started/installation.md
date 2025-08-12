# Installation

## Requirements

- Python 3.8 or higher
- pip package manager

## Installation Methods

### From GitHub

```bash
pip install git+https://github.com/prakashgbid/smart-planner.git
```

### From Source

```bash
git clone https://github.com/prakashgbid/smart-planner.git
cd smart-planner
pip install -e .
```

### Development Installation

```bash
git clone https://github.com/prakashgbid/smart-planner.git
cd smart-planner
pip install -e ".[dev]"
```

## Verify Installation

```python
import smart_planner
print(smart_planner.__version__)
```

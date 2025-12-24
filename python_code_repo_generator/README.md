# 🚀 {{project_name}}

## Overview
A Python project scaffold generated automatically.

## Project Structure

```
{{project_name}}/
├── config/
|   ├── __init__.py
|   ├── config.yaml
|   └── logging.yaml 
├── tests/
├── modules/
│   └── logger.py
├── logs/
├── venv/
├── .gitignore
├── requirements.txt
├── run.py
└── README.md
```

## 📦 Installation (Ubuntu or WSL)

If you're on Windows, open your project inside **WSL Ubuntu** and run:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python run.py
```

## Notes
- Logging configuration lives in `config/logging.yaml`
- Application configuration lives in `config/app.yaml`

## 🧪 Running Tests

```bash
pytest
```

---

## 🤝 Contributing
Pull requests are welcome. For major changes, open an issue first.

---
from pathlib import Path
import ast


def test_python_sources_parse():
    for file in Path("src").glob("*.py"):
        ast.parse(file.read_text(encoding="utf-8"))


def test_sample_env_contains_no_live_credentials():
    sample = Path(".env.example").read_text(encoding="utf-8")
    assert "REPLACE_WITH_SECRET" in sample
    assert "example.invalid" in sample

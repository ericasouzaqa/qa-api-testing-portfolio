from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[2]
REQUIRED_FILES = {
    "index.html",
    "curso_api_testing.html",
    "postman_pratica.html",
    "cypress_api_testing.html",
    "terms.html",
    "README.md",
    "LICENSE",
    "desktop/QA-API-Testing-Portfolio.bat",
    "desktop/README.txt",
}
FORBIDDEN_NAMES = {
    "qa_triagem.html",
    "curriculo_automacao_api.pdf",
}
FORBIDDEN_SUFFIXES = {".tmp", ".bak", ".swp", ".orig"}


class DocumentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []
        self.has_doctype = False
        self.has_html = False
        self.has_head = False
        self.has_body = False

    def handle_decl(self, decl: str) -> None:
        if decl.lower() == "doctype html":
            self.has_doctype = True

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if tag == "html":
            self.has_html = True
        elif tag == "head":
            self.has_head = True
        elif tag == "body":
            self.has_body = True
        if tag == "a":
            attributes = dict(attrs)
            href = attributes.get("href")
            if href:
                self.hrefs.append(href)


def relative_files() -> set[str]:
    return {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts
    }


def validate_structure(errors: list[str]) -> None:
    files = relative_files()
    for required in sorted(REQUIRED_FILES):
        if required not in files:
            errors.append(f"arquivo obrigatório ausente: {required}")
    for path in files:
        candidate = Path(path)
        if candidate.name in FORBIDDEN_NAMES:
            errors.append(f"arquivo indevido presente: {path}")
        if candidate.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"arquivo temporário presente: {path}")
        if "__pycache__" in candidate.parts or candidate.name == ".DS_Store":
            errors.append(f"artefato temporário presente: {path}")


def validate_html_and_links(errors: list[str]) -> None:
    for path in sorted(ROOT.glob("*.html")):
        text = path.read_text(encoding="utf-8")
        parser = DocumentParser()
        try:
            parser.feed(text)
            parser.close()
        except Exception as exc:  # pragma: no cover - parser-specific failure
            errors.append(f"HTML inválido em {path.name}: {exc}")
            continue
        if not parser.has_doctype:
            errors.append(f"DOCTYPE ausente em {path.name}")
        if not parser.has_html or not parser.has_head or not parser.has_body:
            errors.append(f"estrutura HTML incompleta em {path.name}")
        for href in parser.hrefs:
            parsed = urlsplit(href)
            if parsed.scheme or href.startswith("#") or not parsed.path:
                continue
            target = (path.parent / parsed.path).resolve()
            if not target.exists() or ROOT not in target.parents and target != ROOT:
                errors.append(f"link local quebrado em {path.name}: {href}")


def validate_readme_and_desktop(errors: list[str]) -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
    for term in ("versão web", "versão desktop", "contribuição", "licença mit", "github pages"):
        if term not in readme:
            errors.append(f"README sem seção obrigatória: {term}")
    launcher = (ROOT / "desktop/QA-API-Testing-Portfolio.bat").read_text(encoding="utf-8")
    if "index.html" not in launcher or "start" not in launcher.lower():
        errors.append("launcher Desktop não abre index.html com start")


def main() -> int:
    errors: list[str] = []
    validate_structure(errors)
    validate_html_and_links(errors)
    validate_readme_and_desktop(errors)
    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"VALIDATION OK: {len(list(ROOT.glob('*.html')))} HTML files, required structure, local links and documentation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

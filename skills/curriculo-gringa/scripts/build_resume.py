"""Gera o PDF do currículo a partir de um Markdown no formato do template.

Uso:
    python build_resume.py resume.md [saida.pdf]

Requer: reportlab (pip install reportlab)

Formato esperado do Markdown (veja templates/resume.md):

    # Nome Completo
    +55 11 90000-0000 • email@exemplo.com • linkedin.com/in/voce

    ## Cargo-alvo
    Resumo profissional em um parágrafo.

    ## Work Experience
    ### Cargo | Empresa | Mar 2024 - Present
    - Bullet com **negrito** opcional.

    ## Skills
    - **Categoria:** item, item, item

    ## Education
    ### Diploma | Instituição | Dez 2018

O PDF sai com uma coluna, texto selecionável e fonte padrão (Helvetica),
que é o que importa pra passar no ATS.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

FONT = "Helvetica"
FONT_BOLD = "Helvetica-Bold"
TEXT = 9.5
INK = colors.HexColor("#111111")

# Caracteres fora do WinAnsi (fonte padrão do PDF) viram equivalentes seguros.
REPLACEMENTS = {"→": "->", "≈": "~", "≥": ">=", "≤": "<=", "×": "x", " ": " "}


@dataclass
class Entry:
    title: str
    org: str = ""
    date: str = ""
    bullets: list[str] = field(default_factory=list)


@dataclass
class Section:
    name: str
    entries: list[Entry] = field(default_factory=list)
    lines: list[str] = field(default_factory=list)  # itens soltos (ex.: Skills)


@dataclass
class Resume:
    name: str = ""
    contact: str = ""
    headline: str = ""
    summary: list[str] = field(default_factory=list)
    sections: list[Section] = field(default_factory=list)


def clean(text: str) -> str:
    for a, b in REPLACEMENTS.items():
        text = text.replace(a, b)
    return text


def inline(text: str) -> str:
    """Converte o Markdown inline suportado (negrito, itálico, links) pra markup do reportlab."""
    text = clean(text)
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"<i>\1</i>", text)
    return text


def parse(md: str) -> Resume:
    r = Resume()
    section: Section | None = None
    entry: Entry | None = None
    in_summary = False

    for raw in md.splitlines():
        line = raw.strip()
        if not line or line.startswith("<!--"):
            continue
        if line.startswith("# "):
            r.name = line[2:].strip()
        elif line.startswith("## "):
            title = line[3:].strip()
            if not r.headline:
                r.headline, in_summary = title, True
            else:
                in_summary, entry = False, None
                section = Section(title)
                r.sections.append(section)
        elif line.startswith("### ") and section is not None:
            parts = [p.strip() for p in line[4:].split("|")]
            parts += [""] * (3 - len(parts))
            entry = Entry(parts[0], parts[1], parts[2])
            section.entries.append(entry)
        elif line.startswith(("- ", "* ")):
            item = line[2:].strip()
            if entry is not None:
                entry.bullets.append(item)
            elif section is not None:
                section.lines.append(item)
        elif in_summary:
            r.summary.append(line)
        elif not r.contact and r.name and not r.headline:
            r.contact = line
        elif section is not None:
            section.lines.append(line)
    return r


def build(resume: Resume, out: Path) -> None:
    s = {
        "name": ParagraphStyle("name", fontName=FONT_BOLD, fontSize=22, leading=26, alignment=TA_CENTER, textColor=INK),
        "contact": ParagraphStyle("contact", fontName=FONT, fontSize=TEXT, leading=13, alignment=TA_CENTER, textColor=INK),
        "headline": ParagraphStyle("headline", fontName=FONT_BOLD, fontSize=12, leading=15, textColor=INK),
        "body": ParagraphStyle("body", fontName=FONT, fontSize=TEXT, leading=14, textColor=INK),
        "section": ParagraphStyle("section", fontName=FONT, fontSize=10, leading=12, textColor=INK),
        "title": ParagraphStyle("title", fontName=FONT_BOLD, fontSize=11.5, leading=14, textColor=INK),
        "org": ParagraphStyle("org", fontName=FONT_BOLD, fontSize=TEXT, leading=12, textColor=INK),
        "date": ParagraphStyle("date", fontName=FONT, fontSize=TEXT, leading=12, alignment=2, textColor=INK),
        "bullet": ParagraphStyle(
            "bullet", fontName=FONT, fontSize=TEXT, leading=13.5, textColor=INK, leftIndent=16, bulletIndent=5, spaceAfter=1
        ),
    }
    doc = SimpleDocTemplate(
        str(out),
        pagesize=LETTER,
        leftMargin=0.7 * inch,
        rightMargin=0.7 * inch,
        topMargin=0.5 * inch,
        bottomMargin=0.5 * inch,
        title=f"Resume - {clean(resume.name)}",
        author=clean(resume.name),
    )
    width = doc.width - 12  # o frame padrão tem 6pt de padding de cada lado
    story: list = [
        Paragraph(inline(resume.name), s["name"]),
        Spacer(1, 4),
        Paragraph(inline(resume.contact), s["contact"]),
        Spacer(1, 6),
        HRFlowable(width="100%", thickness=1.2, color=INK, spaceAfter=14),
        Paragraph(inline(resume.headline), s["headline"]),
        Spacer(1, 8),
    ]
    for para in resume.summary:
        story += [Paragraph(inline(para), s["body"]), Spacer(1, 4)]

    def org_date_row(org: str, date: str) -> Table:
        t = Table(
            [[Paragraph(inline(org), s["org"]), Paragraph(inline(date), s["date"])]],
            colWidths=[width * 0.7, width * 0.3],
        )
        t.setStyle(
            TableStyle(
                [
                    ("LEFTPADDING", (0, 0), (-1, -1), 0),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                    ("TOPPADDING", (0, 0), (-1, -1), 0),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                    ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
                ]
            )
        )
        t.hAlign = "LEFT"
        return t

    for sec in resume.sections:
        story += [
            Spacer(1, 12),
            Paragraph(inline(sec.name.upper()), s["section"]),
            Spacer(1, 3),
            HRFlowable(width="100%", thickness=1, color=INK, spaceAfter=6),
        ]
        for e in sec.entries:
            # "Cargo • Freelancer": a parte depois do • sai em fonte normal, menor.
            main, _, tag = e.title.partition("•")
            title = f"{inline(main.strip())}"
            if tag.strip():
                title += f' <font name="{FONT}" size="{TEXT}">• {inline(tag.strip())}</font>'
            head = [Paragraph(title, s["title"]), org_date_row(e.org, e.date)]
            bullets = [Paragraph(inline(b), s["bullet"], bulletText="•") for b in e.bullets]
            # Mantém cargo, empresa e o primeiro bullet na mesma página.
            story += [KeepTogether([*head, Spacer(1, 3), *bullets[:1]]), *bullets[1:], Spacer(1, 6)]
        for item in sec.lines:
            story += [Paragraph(inline(item), s["body"]), Spacer(1, 3)]

    doc.build(story)


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    src = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".pdf")
    build(parse(src.read_text(encoding="utf-8")), out)
    print(f"PDF gerado: {out}")


if __name__ == "__main__":
    main()

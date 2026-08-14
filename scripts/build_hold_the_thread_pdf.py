#!/usr/bin/env python3
"""Build the one-page Hold the Thread curriculum PDF."""

from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf" / "hold-the-thread-agency-centered-family-care-coordination.pdf"

NAVY = HexColor("#17324D")
TEAL = HexColor("#168C8C")
PALE_TEAL = HexColor("#EAF6F4")
PALE_BLUE = HexColor("#EEF3F8")
INK = HexColor("#243342")
MUTED = HexColor("#5D6D7B")
LINE = HexColor("#CFDAE3")


def styles():
    return {
        "body": ParagraphStyle(
            "body", fontName="Helvetica", fontSize=7.65, leading=9.55,
            textColor=INK, alignment=TA_LEFT, spaceAfter=0,
        ),
        "body_small": ParagraphStyle(
            "body_small", fontName="Helvetica", fontSize=7.25, leading=9.0,
            textColor=INK, alignment=TA_LEFT,
        ),
        "habit": ParagraphStyle(
            "habit", fontName="Helvetica", fontSize=7.45, leading=9.25,
            textColor=INK, alignment=TA_LEFT,
        ),
        "section": ParagraphStyle(
            "section", fontName="Helvetica-Bold", fontSize=9.2, leading=11,
            textColor=NAVY, alignment=TA_LEFT,
        ),
        "quote": ParagraphStyle(
            "quote", fontName="Helvetica-Bold", fontSize=8.0, leading=10.1,
            textColor=NAVY, alignment=TA_LEFT,
        ),
        "footer": ParagraphStyle(
            "footer", fontName="Helvetica", fontSize=6.2, leading=7.4,
            textColor=MUTED, alignment=TA_LEFT,
        ),
    }


def paragraph(c, html, style, x, y_top, width):
    p = Paragraph(html, style)
    _, height = p.wrap(width, 1000)
    p.drawOn(c, x, y_top - height)
    return y_top - height


def section_heading(c, label, x, y_top, width, s):
    y = paragraph(c, label.upper(), s["section"], x, y_top, width)
    c.setStrokeColor(TEAL)
    c.setLineWidth(1.4)
    c.line(x, y - 2.5, x + width, y - 2.5)
    return y - 8


def habit(c, number, title, text, x, y_top, width, s):
    c.setFillColor(TEAL)
    c.circle(x + 8, y_top - 8, 8, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(x + 8, y_top - 10.7, str(number))
    html = f"<b>{title}</b><br/>{text}"
    y = paragraph(c, html, s["habit"], x + 21, y_top, width - 21)
    return y - 7


def panel(c, x, y_top, width, height, fill):
    c.setFillColor(fill)
    c.setStrokeColor(LINE)
    c.setLineWidth(0.6)
    c.roundRect(x, y_top - height, width, height, 7, fill=1, stroke=1)


def build():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUT), pagesize=letter)
    c.setTitle("Hold the Thread: Agency-Centered Family Care Coordination")
    c.setAuthor("Hugo Campos")
    c.setSubject("A one-page care coordination curriculum grounded in Critical AI Health Literacy")
    width, height = letter
    s = styles()

    # Header
    c.setFillColor(NAVY)
    c.rect(0, height - 110, width, 110, fill=1, stroke=0)
    c.setFillColor(TEAL)
    c.rect(0, height - 116, width, 6, fill=1, stroke=0)
    c.setFillColor(PALE_TEAL)
    c.roundRect(34, height - 32, 172, 17, 8, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 7.3)
    c.drawString(43, height - 26.3, "ONE-PAGE CARE COORDINATION GUIDE")
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 28)
    c.drawString(34, height - 65, "Hold the Thread")
    c.setFont("Helvetica-Bold", 10)
    c.drawString(35, height - 84, "Agency-Centered Family Care Coordination")
    c.setFont("Helvetica-Oblique", 8.5)
    c.drawString(35, height - 99, "Keep care connected without trying to become the clinician.")

    margin = 34
    gap = 18
    left_w = 326
    right_x = margin + left_w + gap
    right_w = width - right_x - margin
    y0 = height - 133

    # Left column
    y = section_heading(c, "The aim", margin, y0, left_w, s)
    y = paragraph(
        c,
        "Healthcare is divided across clinics, portals, medication lists, home-health services, and family conversations. The goal is not perfect documentation. It is to keep the person's preferences and lived experience central while making the next safe step clear.",
        s["body"], margin, y, left_w,
    ) - 10
    y = section_heading(c, "Six habits", margin, y, left_w, s)
    habits = [
        ("Begin with the person, not the record", "Ask what matters now, what the patient is experiencing, and what they want help deciding. A caregiver adds continuity; they do not speak over the person receiving care."),
        ("Keep one living summary", "Track actual medication use, meaningful symptoms or function changes, upcoming appointments, two or three open questions, and next steps with owners. Start small."),
        ("Label the source", "Distinguish patient report, caregiver observation, clinician instruction, electronic record, home measurement, and AI synthesis. Keep conflicts visible."),
        ("Compare the record with real life", "Turn discrepancies into questions: <i>Dad takes 10 mg, but the portal lists 20 mg. Which is correct, and who will update the record?</i> Do not resolve consequential conflicts alone."),
        ("Turn uncertainty into ownership", "Record the question, why it matters, the responsible person, the next action, and expected follow-up. Ask: <b>Who owns the next step?</b>"),
        ("Close the loop without carrying every loop", "Follow safety-critical items; let lower-priority questions wait; return responsibilities to clinics, agencies, and vendors. Advocacy should not require heroic unpaid labor."),
    ]
    for i, (title, text) in enumerate(habits, 1):
        y = habit(c, i, title, text, margin, y, left_w, s)

    # Right column: visit practice
    y = section_heading(c, "A simple visit practice", right_x, y0, right_w, s)
    for label, text in [
        ("BEFORE", "Choose two or three decisions or questions. Bring a short summary; keep detail available only if needed."),
        ("DURING", "Lead with a shared goal. Describe your understanding, invite correction, and separate observation from conclusion."),
        ("AFTER", "Record decisions, uncertainty, owners, and timing. Confirm important changes reached the official record."),
    ]:
        c.setFillColor(TEAL)
        c.setFont("Helvetica-Bold", 6.4)
        c.drawString(right_x, y - 7, label)
        y = paragraph(c, text, s["body_small"], right_x + 42, y, right_w - 42) - 7

    # AI panel
    ai_top = y - 3
    ai_h = 202
    panel(c, right_x, ai_top, right_w, ai_h, PALE_TEAL)
    px = right_x + 11
    pw = right_w - 22
    py = ai_top - 12
    py = paragraph(c, "AI + CRITICAL AI HEALTH LITERACY", s["section"], px, py, pw) - 5
    py = paragraph(
        c,
        "AI can organize notes, compare records, flag possible contradictions, and prepare questions. Treat its output as <b>synthesis to verify</b>, not medical fact or instruction.",
        s["body_small"], px, py, pw,
    ) - 7
    questions = [
        "Who does this tool serve?",
        "Does it expand understanding and choices - or narrow them?",
        "What might it omit or invent?",
        "What sensitive information am I sharing?",
        "Could its framing overshadow the patient's own words?",
    ]
    for q in questions:
        c.setFillColor(TEAL)
        c.circle(px + 2.5, py - 4.5, 1.7, fill=1, stroke=0)
        py = paragraph(c, q, s["body_small"], px + 9, py, pw - 9) - 3
    py -= 2
    paragraph(c, "<b>Bring AI material as questions:</b><br/><i>“This is our current understanding. What are we missing?”</i>", s["quote"], px, py, pw)

    # Limits panel
    y = ai_top - ai_h - 12
    y = section_heading(c, "Limits", right_x, y, right_w, s)
    y = paragraph(
        c,
        "This practice cannot repair every fragmented system. Risks include caregiver burden, privacy exposure, bias, unequal access, and shifting system failures onto one family member. Urgent safety concerns require appropriate clinical or emergency help - not reliance on a record or AI.",
        s["body_small"], right_x, y, right_w,
    ) - 12

    # Closing callout
    quote_h = 82
    panel(c, right_x, y, right_w, quote_h, PALE_BLUE)
    paragraph(
        c,
        "You are not training to become a medical expert. You are learning to <b>hold the thread</b>: preserve the patient's voice, keep sources clear, bring the right questions forward, and help responsible people close the next loop.",
        s["quote"], right_x + 11, y - 12, right_w - 22,
    )

    # Footer
    c.setStrokeColor(LINE)
    c.setLineWidth(0.5)
    c.line(margin, 25, width - margin, 25)
    paragraph(c, "A practical teaching aid based on the Critical AI Health Literacy framework. It does not replace clinical judgment or emergency care.", s["footer"], margin, 20, width - 2 * margin)

    c.showPage()
    c.save()
    print(OUT)


if __name__ == "__main__":
    build()

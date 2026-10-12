from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

WIDTH, HEIGHT = A4

NAVY = HexColor("#0a1628")
COPPER = HexColor("#c47a4a")
WHITE = HexColor("#ffffff")
WARM_BG = HexColor("#f5f1ec")

margin_left = 28*mm
margin_right = 22*mm
content_width = WIDTH - margin_left - margin_right

def draw_text(c, text, x, y, font, size, color, max_width, leading=None):
    if leading is None:
        leading = size * 1.45
    style = ParagraphStyle('s', fontName=font, fontSize=size, leading=leading, textColor=color, alignment=TA_LEFT)
    p = Paragraph(text, style)
    w, h = p.wrap(max_width, 500)
    p.drawOn(c, x, y - h)
    return h

c = canvas.Canvas("/home/claude/av-diagnostics/AV_Diagnostics_Women_Friendly_Carousel_Copy.pdf", pagesize=A4)

# Header bar
c.setFillColor(NAVY)
c.rect(0, HEIGHT - 18*mm, WIDTH, 18*mm, fill=1, stroke=0)
c.setFillColor(COPPER)
c.rect(0, HEIGHT - 21*mm, WIDTH, 3*mm, fill=1, stroke=0)

c.setFont("Helvetica-Bold", 13)
c.setFillColor(WHITE)
c.drawString(margin_left, HEIGHT - 13*mm, "Women-Friendly Environment · Carousel Copy")

y = HEIGHT - 38*mm

# POST 1
c.setFillColor(COPPER)
c.setFont("Helvetica-Bold", 10)
c.drawString(margin_left, y, "POST 1")
y -= 8*mm

c.setFillColor(WARM_BG)
c.roundRect(margin_left - 4*mm, y - 28*mm, content_width + 8*mm, 28*mm, 2*mm, fill=1, stroke=0)
draw_text(c, "<b>Slide 1:</b> More women cancel a breast scan over discomfort than over fear of the diagnosis.", margin_left, y - 5*mm, "Helvetica", 11, NAVY, content_width, leading=16)
y -= 35*mm

c.setFillColor(WARM_BG)
c.roundRect(margin_left - 4*mm, y - 42*mm, content_width + 8*mm, 42*mm, 2*mm, fill=1, stroke=0)
draw_text(c, "<b>Slide 2:</b> Nobody tells us this. They do not have to. Years of doing this work have taught us what comfort looks like before a patient says a word. That is why women handle every step of your breast scan here. Not as a policy. As a habit we started and never stopped.", margin_left, y - 5*mm, "Helvetica", 11, NAVY, content_width, leading=16)
y -= 55*mm

# Divider
c.setStrokeColor(HexColor("#dddddd"))
c.setLineWidth(0.5)
c.line(margin_left, y, WIDTH - margin_right, y)
y -= 12*mm

# POST 2
c.setFillColor(COPPER)
c.setFont("Helvetica-Bold", 10)
c.drawString(margin_left, y, "POST 2")
y -= 8*mm

c.setFillColor(WARM_BG)
c.roundRect(margin_left - 4*mm, y - 28*mm, content_width + 8*mm, 28*mm, 2*mm, fill=1, stroke=0)
draw_text(c, "<b>Slide 1:</b> A breast scan is one of the simplest scans in radiology. It is also the most postponed.", margin_left, y - 5*mm, "Helvetica", 11, NAVY, content_width, leading=16)
y -= 35*mm

c.setFillColor(WARM_BG)
c.roundRect(margin_left - 4*mm, y - 42*mm, content_width + 8*mm, 42*mm, 2*mm, fill=1, stroke=0)
draw_text(c, "<b>Slide 2:</b> Not because it is painful. Not because it takes long. Because most women are not sure who will be in the room. We have watched this long enough to know. That is why women handle every step of your scan here. It was never a policy. It was the first thing we built.", margin_left, y - 5*mm, "Helvetica", 11, NAVY, content_width, leading=16)

c.save()
print("Done.")

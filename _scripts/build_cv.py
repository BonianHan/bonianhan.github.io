"""Regenerate files/CV.pdf with Python and ReportLab."""
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
# Embed the font family so bold and italic render consistently in PDF viewers.
FONT_DIR = Path('/System/Library/Fonts/Supplemental')
for font, filename in [('Times-Roman', 'Times New Roman.ttf'), ('Times-Bold', 'Times New Roman Bold.ttf'), ('Times-Italic', 'Times New Roman Italic.ttf'), ('Times-BoldItalic', 'Times New Roman Bold Italic.ttf')]:
    pdfmetrics.registerFont(TTFont(font, str(FONT_DIR / filename)))
pdfmetrics.registerFontFamily('Times-Roman', normal='Times-Roman', bold='Times-Bold', italic='Times-Italic', boldItalic='Times-BoldItalic')
INK = colors.HexColor('#192632')
BLUE = colors.HexColor('#234e70')
body = ParagraphStyle('Body', fontName='Times-Roman', fontSize=11, leading=14, textColor=INK, spaceAfter=7)
small = ParagraphStyle('Small', parent=body, fontSize=10, leading=13)
heading = ParagraphStyle('Heading', fontName='Times-Bold', fontSize=13, leading=16, textColor=BLUE, spaceBefore=13, spaceAfter=7)
name = ParagraphStyle('Name', fontName='Times-Bold', fontSize=26, leading=30, textColor=INK, alignment=TA_CENTER, spaceAfter=7)
contact = ParagraphStyle('Contact', parent=small, alignment=TA_CENTER, spaceAfter=5)
story = []
def p(text, style=body):
    return Paragraph(text, style)
def add(text, style=body):
    story.append(p(text, style))
def section(text):
    story.append(p(text, heading))
def entry(title, date, text):
    row = Table([[p(title), p(date, ParagraphStyle('Date', parent=small, alignment=2))]], colWidths=[390,114])
    row.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)]))
    story.append(KeepTogether([row, p(text)]))
def pub(number, text):
    style=ParagraphStyle('Publication',parent=body,leftIndent=17,firstLineIndent=-17,spaceAfter=11)
    add(f'{number}. {text}',style)

def footer(canvas, doc):
    canvas.setStrokeColor(colors.HexColor('#c7cdd2'))
    canvas.line(54,43,558,43)
    canvas.setFont('Times-Roman',9)
    canvas.setFillColor(colors.HexColor('#64717b'))
    canvas.drawString(54,29,'Bonian Han | Curriculum Vitae')
    canvas.drawRightString(558,29,f'{doc.page}')

add('Bonian Han',name)
add('<link href="mailto:bonianhan@u.boisestate.edu" color="#234e70">bonianhan@u.boisestate.edu</link>  |  <link href="https://bonianhan.github.io/" color="#234e70">bonianhan.github.io</link>',contact)
section('Education')
entry('<b>Boise State University</b><br/>Ph.D. in Computing (expected start: Fall 2026)', 'Fall 2026', 'Advisor: Prof. Yu Zhang')
entry('<b>New Jersey Institute of Technology</b><br/>Ph.D. studies in Computer Science', '2025 - 2026', 'Advisor: Prof. Zhi Wei | GPA: 4.0')
entry('<b>Hangzhou Dianzi University</b><br/>B.S. in Statistics', 'Sept 2021 - July 2025', 'GPA: 3.48 (84.8/95)')
section('Research Interests')
add('Computer vision; continual learning; embodied AI; trustworthy machine learning, including model calibration and uncertainty quantification; neural representation methods for spatial transcriptomics.')
section('Publications')
pub(1,'J. Zhang, <b>B. Han</b>, G. Liang, and Y. Zhang. "Rethinking Learned Occupancy in Autonomous Active Mapping with Observation-Gated Filtering." <i>IEEE/RSJ IROS 2026 Workshop on Space Exploration and Sustained Operations Beyond Earth</i>, 2026.<br/><b>Oral; Best Paper Runner-Up Award.</b>')
pub(2,'<b>B. Han</b>, C. Qi, P. Musialski, and Z. Wei. "INST-Align: Implicit Neural Alignment for Spatial Transcriptomics via Canonical Expression Fields." <i>Medical Image Computing and Computer Assisted Intervention (MICCAI)</i>, 2026. Accepted. <link href="https://bonianhan.github.io/files/MICCAI26.pdf" color="#234e70">Paper</link>.')
pub(3,'<b>B. Han</b>, Y. P. Masupalli, X. Xing, and G. Liang. "Improving Medical Imaging Model Calibration through Probabilistic Embedding." <i>IEEE International Conference on Big Data</i>, 2024. <link href="https://doi.org/10.1109/BigData62323.2024.10825661" color="#234e70">doi:10.1109/BigData62323.2024.10825661</link>.')
pub(4,'<b>B. Han</b>, C. Moran, J. Yang, Y. Lee, Z. Cao, and G. Liang. "Multi-Scale Self-Supervised Consistency Training for Trustworthy Medical Imaging Classification." <i>46th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)</i>, 2024. Podium (acceptance rate approx. 28%); H5-Index: 48. <link href="https://doi.org/10.1109/EMBC53108.2024.10782322" color="#234e70">doi:10.1109/EMBC53108.2024.10782322</link>.')
pub(5,'J. Zulu, <b>B. Han</b>, I. Alsmadi, and G. Liang. "Contextualized Embedding-Based Approach for Enhanced SQL Injection Detection." <i>62nd ACM SouthEast Annual Conference</i>, 2024. <link href="https://doi.org/10.1145/3603287.3651187" color="#234e70">doi:10.1145/3603287.3651187</link>.')
story.append(PageBreak())
section('Research Experience')
entry('<b>New Jersey Institute of Technology</b><br/>Research with Prof. Zhi Wei', 'Sept 2025 - 2026', 'Conducted research on spatial transcriptomics and neural representation methods. Worked on INST-Align, coupling spatial alignment with a canonical expression field; accepted to MICCAI 2026.')
entry('<b>Texas A&amp;M University-San Antonio</b><br/>Research with Dr. Gongbo Liang', 'Nov 2023 - Nov 2024', 'Conducted computer vision research on medical image analysis, model calibration, and feature extraction to reduce model bias. Work resulted in publications at IEEE EMBC, ACMSE, and IEEE Big Data.')
section('Skills &amp; Languages')
add('<b>Technical skills:</b> Python, C/C++, PyTorch, SQL, R, Linux, Bash, Git, Docker')
add('<b>Languages / tests:</b> TOEFL: 91; GRE: 326 (Verbal: 156, 69th percentile; Quantitative: 170, 92nd percentile)')
section('Additional Experience')
entry('<b>Ballkids Coach &amp; Manager</b><br/>Hangzhou Open ATP 250 and ATP Challenger', 'Sept 2024', 'Trained and managed professional ballkids (ages 9-14), coordinated on-court schedules across departments, and ensured smooth match operations, court etiquette, and safety protocols.')
entry('<b>Tennis Ballkids &amp; Ceremony Assistant</b><br/>19th Asian Games and Asian Para Games', 'Sept - Oct 2023', 'Managed on-court operations and assisted players and umpires. Featured by China Central Television (CCTV); honored as an Outstanding and Excellent Volunteer.')
section('Awards &amp; Honors')
entry('<b>Best Paper Runner-Up Award</b>', '2026', 'IEEE/RSJ IROS Workshop on Space Exploration and Sustained Operations Beyond Earth; "Rethinking Learned Occupancy in Autonomous Active Mapping with Observation-Gated Filtering." Oral presentation.')
add('<b>Outstanding &amp; Excellent Volunteer</b>, National, 2023')
add('<b>Second Prize</b>, Statistics Research Competition, Provincial (State), 2023')
add('<b>Third Prize</b>, National College Students Mathematics Competition (Online Challenge), 2022')
add('<b>Fifth Place</b>, University Basketball Annual Competition, May 2022')

SimpleDocTemplate(str(ROOT/'files/CV.pdf'), pagesize=letter, rightMargin=54, leftMargin=54, topMargin=42, bottomMargin=55, title='Bonian Han - Curriculum Vitae', author='Bonian Han').build(story,onFirstPage=footer,onLaterPages=footer)

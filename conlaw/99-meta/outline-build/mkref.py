from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_BREAK
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
d=Document('ref.docx')
for s in d.sections:
    s.page_width=Inches(8.5); s.page_height=Inches(11)
    s.left_margin=s.right_margin=Inches(0.55); s.top_margin=s.bottom_margin=Inches(0.6)
def font(st,size,bold=None,color=None,before=None,after=None,italic=None):
    st.font.name='Calibri'; st.font.size=Pt(size)
    rpr=st.element.get_or_add_rPr(); rf=rpr.find(qn('w:rFonts'))
    if rf is None: rf=OxmlElement('w:rFonts'); rpr.append(rf)
    for a in ('w:ascii','w:hAnsi','w:cs','w:eastAsia'): rf.set(qn(a),'Calibri')
    for a in ('w:asciiTheme','w:hAnsiTheme','w:cstheme','w:eastAsiaTheme'):
        if rf.get(qn(a)) is not None: del rf.attrib[qn(a)]
    if bold is not None: st.font.bold=bold
    if italic is not None: st.font.italic=italic
    if color: st.font.color.rgb=RGBColor.from_string(color)
    pf=st.paragraph_format
    if before is not None: pf.space_before=Pt(before)
    if after is not None: pf.space_after=Pt(after)
S={st.name:st for st in d.styles}
for n in ['Normal','Body Text','First Paragraph','Compact','Block Text']:
    try:
        font(S[n],9.5,before=0,after=1.5); S[n].paragraph_format.line_spacing=1.0
    except KeyError: pass
font(S['Title'],20,bold=True,color='1F3864',after=4)
font(S['Heading 1'],16,bold=True,color='1F3864',before=0,after=6)
S['Heading 1'].paragraph_format.page_break_before=True
font(S['Heading 2'],13,bold=True,color='2E5597',before=10,after=3)
font(S['Heading 3'],10.5,bold=True,color='404040',before=5,after=1)
for n in ['Heading 4','Heading 5']:
    font(S[n],10,bold=True,color='404040',before=4,after=1)
font(S['Block Text'],10,italic=False,before=2,after=2)
for h in ['Heading 1','Heading 2','Heading 3']: S[h].paragraph_format.keep_with_next=True
d.save('ref2.docx')

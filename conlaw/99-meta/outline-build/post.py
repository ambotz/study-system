from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import Pt
d=Document('outline.docx')
for t in d.tables:
    tblPr=t._tbl.tblPr
    b=OxmlElement('w:tblBorders')
    for e in ('top','left','bottom','right','insideH','insideV'):
        el=OxmlElement(f'w:{e}'); el.set(qn('w:val'),'single'); el.set(qn('w:sz'),'4'); el.set(qn('w:color'),'A6A6A6'); b.append(el)
    for old in tblPr.findall(qn('w:tblBorders')): tblPr.remove(old)
    tblPr.append(b)
    for i,row in enumerate(t.rows):
        for c in row.cells:
            for p in c.paragraphs:
                p.paragraph_format.space_after=Pt(0)
                for r in p.runs:
                    r.font.size=Pt(8.5)
                    if i==0: r.font.bold=True
            if i==0:
                tcPr=c._tc.get_or_add_tcPr(); sh=OxmlElement('w:shd'); sh.set(qn('w:val'),'clear'); sh.set(qn('w:fill'),'DCE6F2'); tcPr.append(sh)
# footer page numbers
for s in d.sections:
    p=s.footer.paragraphs[0] if s.footer.paragraphs else s.footer.add_paragraph()
    p.alignment=1
    r=p.add_run('Con Law I · Baude · Master Outline · p. '); r.font.size=Pt(8)
    for typ,txt in (('begin',None),(None,'PAGE'),('end',None)):
        if typ:
            f=OxmlElement('w:fldChar'); f.set(qn('w:fldCharType'),typ); r2=p.add_run(); r2._r.append(f)
        else:
            it=OxmlElement('w:instrText'); it.set(qn('xml:space'),'preserve'); it.text=txt; r2=p.add_run(); r2._r.append(it)
d.save('outline.docx')

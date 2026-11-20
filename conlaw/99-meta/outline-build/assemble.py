import re, json, datetime, pathlib, sys
S=pathlib.Path(__file__).parent/'sections'
order=['00-part-0.md','10-part-I.md','20-part-II.md','30-part-III.md','40-part-IV.md','50-part-V.md','60-part-VI.md','70-part-VII.md','80-part-VIII.md','90-part-IX.md','95-part-X.md']
parts=[(S/f).read_text().strip() for f in order]
# frontmatter: written by script from a validated dict, never freehand
fm={'kind':'master_outline','class':'conlaw','generated':True,'source':'30-doctrine','modules_covered':31,'built':datetime.date.today().isoformat()}
allowed={'kind','class','generated','source','modules_covered','built'}
assert set(fm)==allowed and all('-' not in k for k in fm)
def y(v):
    return 'true' if v is True else str(v)
front='---\n'+''.join(f'{k}: {y(v)}\n' for k,v in fm.items())+'---\n'
# contents
toc=[]
for p in parts:
    for line in p.splitlines():
        if line.startswith('# '): toc.append('- **'+line[2:].strip()+'**')
        elif line.startswith('## '): toc.append('  - '+line[3:].strip())
title='# Constitutional Law I — Master Outline\n\nProfessor William Baude · University of Chicago Law School · Autumn 2026 · Exam: December 9, 2026\n\n## Contents\n\n'+'\n'.join(toc)
body=front+'\n'+title+'\n\n'+'\n\n'.join(parts)+'\n'
out=pathlib.Path(sys.argv[1]); out.write_text(body)
print(len(body.split()), 'words')

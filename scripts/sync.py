from pathlib import Path
import argparse, shutil
parser=argparse.ArgumentParser(description="Refresh the public site from the recruiting repository's reviewed outputs.")
parser.add_argument('--source',type=Path,default=Path(__file__).resolve().parents[2]/'VT-ISE-Grad-Recruiting-Committee')
a=parser.parse_args()
repo=Path(__file__).resolve().parents[1]
docs=repo/'docs';docs.mkdir(exist_ok=True)
html=(a.source/'outputs/faculty-finder/Faculty-Finder.html').read_text()
html=html.replace('../faculty-brochure-20261112/ISE-Faculty-and-Research-Brochure.html','brochure.html')
html=html.replace('Read the full faculty brochure ↗</a></p>', 'Read the full faculty brochure ↗</a> · <a href="faculty-brochure.pdf">Download brochure PDF ↗</a></p>')
(docs/'index.html').write_text(html)
shutil.copy2(a.source/'outputs/faculty-brochure-20261112/ISE-Faculty-and-Research-Brochure.html',docs/'brochure.html')
shutil.copy2(a.source/'output/pdf/ISE-Faculty-and-Research-Brochure.pdf',docs/'faculty-brochure.pdf')
(docs/'.nojekyll').touch()
print('Prepared faculty finder and linked HTML/PDF brochure in docs/')

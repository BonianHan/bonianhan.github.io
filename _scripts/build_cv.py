"""Rebuild files/CV.pdf in its original LaTeX style (requires TeX Live)."""
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
compiler = shutil.which('pdflatex')
if not compiler:
    raise SystemExit('pdflatex is required to rebuild the CV. Install TeX Live first.')
with tempfile.TemporaryDirectory(prefix='bonian-cv-') as temporary:
    command = [compiler, '-interaction=nonstopmode', '-halt-on-error',
               '-output-directory', temporary, str(ROOT / '_scripts/cv.tex')]
    for _ in range(2):
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        if result.returncode:
            raise SystemExit(result.stdout + result.stderr)
    for line in result.stdout.splitlines():
        if 'Overfull' in line or 'Output written' in line:
            print(line)
    shutil.copyfile(Path(temporary) / 'cv.pdf', ROOT / 'files/CV.pdf')

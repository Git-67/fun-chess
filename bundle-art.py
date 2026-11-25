from pathlib import Path
import base64,json,re
p=Path(__file__).resolve().parents[1]/'docs';art={}
for f in (p/'assets').glob('*.svg'):
 s=f.read_text();s=re.sub(r'<path d="M0 0h512v512H0z"\s*/>','',s)
 if f.stem in ['undo','reset','bolt','close','next','book','sound','muted','swords','help','settings']:s=s.replace('currentColor','#f0f4e8')
 if f.stem=='pacman':
  dark=s.replace('currentColor','#352900');art['pacman-board']='data:image/svg+xml;base64,'+base64.b64encode(dark.encode()).decode();s=s.replace('currentColor','#f5eaba')
 art[f.stem]='data:image/svg+xml;base64,'+base64.b64encode(s.encode()).decode()
art['dino-sprite']='data:image/png;base64,'+base64.b64encode((p/'assets/dino-sprite.png').read_bytes()).decode()
(p/'artwork.js').write_text('window.ART='+json.dumps(art,separators=(',',':'))+';')
print('Bundled',len(art),'sourced images')

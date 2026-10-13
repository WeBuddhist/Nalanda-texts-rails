"""Chapter nodes 2-20 of Ka_3CDZ from the commentary's own closers (… X བརྟག་པ་སྟེ་ N པའོ།)."""
import re
from pathlib import Path
U = Path("0-INBOX/temp/PIPE-Ka_3CDZ/Ka_3CDZ.units.md").read_text(encoding="utf-8").split("\n")
CLOSERS = [1622, 2178, 2273, 2434, 2719, 2841, 3271, 3748, 3922, 4063, 4129, 4310, 5230, 5709, 6364,
           6926, 7054, 7722, 7758, 7930]  # 1-based lines, chapters 1..20
out = []
for k in range(2, 21):
    closer = re.sub(r"\[\^\d+\]", "", U[CLOSERS[k - 1] - 1]).replace("༌", "་")
    m = re.search(r"(?:ལས་)?([^།]*?བརྟགས?་པ་སྟེ་[^།]*?)འོ", closer)
    title = m.group(1)
    title = re.sub(r"^.*?དཀའ་འགྲེལ་ལས་", "", title).strip("་ ")
    i = CLOSERS[k - 2]  # line after previous closer
    while not U[i].strip():
        i += 1
    anc = U[i][:70]
    out.append(f"* {k}. {title} [[{anc}]]")
    print(k, i + 1, title)
Path("0-INBOX/temp/TOC-Ka_3CDZ/chapters-2-20.md").write_text("\n".join(out) + "\n", encoding="utf-8")

=== SYSTEM PROMPT ===
You are an expert in classical Tibetan Buddhist commentary (འགྲེལ་པ་) structure.

You are given a numbered list of blocks from a Tibetan verse commentary. A
rule-based segmenter has already cut them; most cuts are right. Your job is to
output the few merge/split operations that bring the blocks to the layout the
human editors of this vault use.

━━━ TARGET LAYOUT — one block per FUNCTIONAL UNIT ━━━

OPENER       A node's division announcement together with the first-child opener
             that follows it is ONE block:
               "<topic> ལ་གསུམ། A། B། C་འོ། །དང་པོ་ནི།"
             A sibling opener "གཉིས་པ་ <title> ནི།" is its own block.
ROOT QUOTE   A quoted root stanza is its own block. These blocks are tagged
             [VERSE]; they are protected — never include them in any operation.
EXPLANATION  The gloss that follows a quote ("ཞེས་པ་སྟེ། …", "ཞེས་པ་ནི། …", or a
             running explanation) is ONE block up to the next opener, quote or
             heading — even when it is long (100–250 syllables) and contains several
             sentence ends, a question and answer ("…ལོ། །གང་ལ་ན། …"), a side remark
             on a variant reading ("…ཞེས་འགྱུར་བཅོས་…"), a cross-reference
             ("འདི་དང་འོག་གི་ས་བཅད་…"), or a mantra cited in passing.
SECOND LEVEL A passage that re-reads the same stanza on another level — opening
             "སྦས་དོན་ནི།", "ངེས་དོན་ནི།", "ངེས་པའི་དོན་དུ།", "ཟབ་དོན་ནི།",
             "དེའི་ནང་གི་དོན་ལ།", "མཐར་ཐུག་གི་དོན་ནི།" or the like after the literal
             gloss — is its OWN block, never merged into the literal gloss before it
             (the editors keep the two readings apart). Within that passage, M1 applies.
FRAME        The namo line alone; each of the author's own verses one block;
             "སྨྲས་པ།" alone; the colophon ("ཅེས་ … སྦྱར་བའོ། །" + closing wishes) one block.

━━━ MERGE — adjacent blocks that are one unit ━━━

M1  CONTINUED EXPLANATION
    A block that goes on explaining the same quote/topic as the block before it —
    no new opener, no new quote, no new verse being treated — belongs to that block.
    This is the most common fix. Do NOT keep a cut just because a sentence ends.
    Exception: a SECOND LEVEL opener (see above) always starts a new block.
M2  INCOMPLETE SENTENCE
    A block ending in a connector (དང་། / ཞིང་། / ཅིང་། / ནས། / སྟེ། / ཏེ།) that
    the next block completes.
M3  OPENER CHAIN
    An enumeration block followed by "དང་པོ་ནི།" / "དང་པོ་ལ་ N།" (and further
    nested first-child enumerations) — merge them into one opener block.
M4  COLOPHON
    The parts of the closing colophon and its final wishes form one block.

━━━ SPLIT — one block that holds two units ━━━

S1  A new node opener (ordinal + title + "ནི།" or "ལ་ N།") buried mid-block:
    split before it.
S2  The treatment of a new verse/topic starts mid-block (e.g. "ཡང་ཕྱག་གང་ལ་འཚལ་ན"
    starting the next homage): split before it.
S3  An introductory opener "… ནི།" fused to the explanation of the PREVIOUS
    quote: split so the opener starts the next unit.

Never split a block only because it is long.

━━━ TOPIC SHIFT vs CONTINUATION (from the editors' corrections) ━━━

The editors' blocks are large (median ≈ 55 syllables; whole explanations of
100–250 syllables are normal). A sentence end is NOT a boundary. Inside one
explanation they cut only where the commentary turns to something new:
  START a new block at   "ཡང་ན་ …" (an alternative explanation)
                         "ཁ་ཅིག་ …", "གཞན་དག་ …" (another party's view)
                         "འོ་ན་ …" (the reply to an objection)
                         "དེ་སྐད་དུ་ …", "ཇི་སྐད་དུ་ …" (introducing a supporting quotation)
                         "དེ་ནས་ …" when it opens the next step of a procedure
                         "དཔེ་ …" / "དཔེར་ན་ …" when an example section begins
KEEP WITH the block before (merge into it):
                         "ད་ནི་ …" — a transitional "now …" line is not a new unit
                         (no heading or verse between them)
                         "ལེའུ་ … པའོ། །" — a chapter-closing line stays with the
                         explanation it closes
                         "ཞེས་ / ཅེས་ …" — the quotative closing the words just before it

━━━ HEADING / VERSE BLOCKS — always KEEP ━━━

Blocks tagged [HEADING] or [VERSE] are NEVER part of any operation.

━━━ OUTPUT FORMAT ━━━

A JSON array of operations. Blocks not mentioned are kept as-is.

[
  {"op": "merge", "blocks": [N, M]},
  {"op": "merge", "blocks": [N, M, P]},
  {"op": "split", "block": N, "after": "<verbatim unique substring ending at split point>"},
  {"op": "split", "block": N, "after": ["<sub1>", "<sub2>", "<sub3>"]}
]

Rules for the output:
- Block numbers are CONTINUOUS and INCLUDE heading and verse blocks. You may only
  merge blocks with consecutive numbers (N and N+1). Never merge across a heading
  or a verse block, and never propose a merge whose numbers skip over one.
- Each block number appears in AT MOST ONE operation.
- For each "after" substring: copy a verbatim slice from the block that ends exactly
  at the split point and is UNIQUE within that block (10–20 characters is usually enough).
- If nothing needs to change in this window, output: []
- Output ONLY the JSON array. No explanation, no commentary, no code fences.

=== USER PROMPT ===
Review the following blocks from a Tibetan commentary and output the merge/split operations needed to make each block a single citable thought unit. Block numbers are global (file-level).

--- BEGIN BLOCKS ---
[Block 1821]
བཅོམ་ལྡན་འདས་གལ་ཏེ་གཟུགས་ཡིད་ལ་མི༌[^1254]བགྱི་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་གཉིས་པའོ། །

[Block 1822]
བཅོམ་ལྡན་འདས་ཅིའི་སླད་དུ་འདི་ལྟར་གཟུགས་ཡིད་ལ་མི༌[^1255]བགྱི་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་གསུམ་པའོ། །

[Block 1823]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་དེ་ལྟར་སྤྱོད་པ་གང་ལ་གནས་པར་མི་འགྱུར་བ་ལགས་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་བཞི་པའོ། །

[Block 1824]
བཅོམ་ལྡན་འདས་ཅིའི་སླད་དུ་བྱང་ཆུབ་སེམས་དཔའ་གཟུགས་ལ་གནས་པར་མི་འགྱུར་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་ལྔ་པའོ། །

[Block 1825]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ན་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པའི་སྐྱོན་འདི་དག་མ་མཆིས་པར་འགྱུར་བ་ལགས་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་དྲུག་པའོ། །

[Block 1826]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་མ་བྲལ་བ་ལགས་སམ་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་བདུན་པའོ། །

[Block 1827]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་རྣམས་ཀྱི་ལམ་ནི་གང་ལགས་ལམ་མ་ལགས་པ་ནི་གང་ལགས་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་བརྒྱད་པའོ། །

[Block 1828]
བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པས་ཇི་ལྟར་སྦྱིན་པ་སྦྱིན་པར་བགྱི་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་དགུ་པའོ། །

[Block 1829]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་ཇི་ལྟར་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ལ་བརྩོན་པར་བགྱི་ཞེས་བྱ་བ་ནི་བརྒྱད་ཅུ་པའོ། །

[Block 1830]
བཅོམ་ལྡན་འདས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་བསླབ་པར་བྱའོ་ཞེས་གསུངས་པ་ལགས་སམ༌[^1256]ཞེས་བྱ་བ་ནི་བརྒྱད་ཅུ་གཅིག་པའོ། །

[Block 1831]
བཅོམ་ལྡན་འདས་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཇི་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པ་ལ་དགོངས་པ་མཛད་ཅེས་བྱ་བ་ནི་བརྒྱད་ཅུ་གཉིས་པའོ། །

[Block 1832]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ན་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཐམས་ཅད་ཀྱི་མདོ་དང་རྒྱས་པ༌[^1257]འཚལ་བར་འགྱུར་བ་ལགས་ཞེས་བྱ་བ་ནི་བརྒྱད་ཅུ་གསུམ་པའོ། །

[Block 1833]
བཅོམ་ལྡན་འདས་གཟུགས་ཀྱི་དེ་བཞིན་ཉིད་ཇི་ལྟ་བུ་ལགས་ཞེས་བྱ་བ་ནི་བརྒྱད་ཅུ་བཞི་པའོ། །

[Block 1834]
བཅོམ་ལྡན་འདས་ཡང་དག་པའི་མཐའ་དེ༌[^1258]གང་ལགས་ཞེས་བགྱི་བ༌[^1259]ནི་བརྒྱད་ཅུ་ལྔ་པའོ། །

[Block 1835]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ཆོས་ཐམས་ཅད་ཀྱི་མདོ་དང་རྒྱས་པ་འཚལ་བར་བགྱི་ཞེས་བྱ་བ་ནི་བརྒྱད་ཅུ་དྲུག་པའོ། །

[Block 1836]
བཅོམ་ལྡན་འདས་ཆོས་གང་དག༌[^1260]ལྡན་པ་ཡང་མ་ལགས་མི་ལྡན་པ་ཡང་མ་ལགས་པའི་ཆོས་དེ་དག་ཀྱང་གང་ལགས་ཞེས་བྱ་བ་ནི་བརྒྱད་ཅུ་བདུན་པའོ། །

[Block 1837]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱད་པར་བགྱི་ཞེས་བྱ་བ་ནི་བརྒྱད་ཅུ་བརྒྱད་པའོ། །

[Block 1838]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་ཡུན་རིང་པོ་ཇི་སྲིད་ཅིག་ཏུ་སྤྱད་ན་ཞེས་བྱ་བ་ནི་བརྒྱད་ཅུ་དགུ་པའོ། །

[Block 1839]
བཅོམ་ལྡན་འདས་ཅི་ལགས་སེམས་ཀྱི་རྒྱུན་མ་ཆད་པ་དང་མ་བྲལ་བར་རྗེས་སུ་འབྲེལ་བས༌[^1261]སྤྱད་པར་བགྱི་འམ་ཞེས་བྱ་བ་ནི་དགུ་བཅུ་པའོ། །

[Block 1840]
བཅོམ་ལྡན་འདས་ཅི་ལགས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱད་པ་དང་ཞེས་བྱ་བ་ནི་དགུ་བཅུ་གཅིག་པའོ། །

[Block 1841]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ན་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བྱ་བའི་སྐབས་འདིར་བར༌[^1262]སྐབས་སུ་ཞུས་པའི༌[^1263]རྣམ་པ་བཞིའོ། །

[Block 1842]
བཅོམ་ལྡན་འདས་ཅི་ལགས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གདགས༌[^1264]སུ་མ་མཆིས་པ་ལགས་སམ་ཞེས་བྱ་བ་ནི་དགུ་བཅུ་གཉིས་པའོ། །

[Block 1843]
བཅོམ་ལྡན་འདས་ཅིའི་སླད་དུ་སེམས་ཅན་དམྱལ་བ་གདགས་སུ་མ༌[^1265]མཆིས་པར་གྱུར་ཅེས་བྱ་བ་ནི་དགུ་བཅུ་གསུམ་པའོ། །

[Block 1844]
བཅོམ་ལྡན་འདས་འོ་ན་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པས་ཞེས་བྱ་བ་ནི་དགུ་བཅུ་བཞི་པའོ། །

[Block 1845]
བཅོམ་ལྡན་འདས་སྐྱེ་བ་མ་མཆིས་པ་དང་། འགག་པ་མ་མཆིས་པ་ལ་ཇི་ལྟར་བསླབ་པར་བགྱི་ཞེས་བྱ་བ་ནི་དགུ་བཅུ་ལྔ་པའོ། །

[Block 1846]
བཅོམ་ལྡན་འདས་ཆོས་ཐམས་ཅད་རང་གི་མཚན་ཉིད་ཀྱིས་སྟོང་པར་ཇི་ལྟར་བསླབ་པར་བགྱི་ཞེས་བྱ་བ་ནི་དགུ་བཅུ་དྲུག་པའོ། །

[Block 1847]
བཅོམ་ལྡན་འདས་གལ་ཏེ་གཟུགས་ནི་གཟུགས་ཀྱིས་སྟོང་ཞེས་བྱ་བ་ནི་དགུ་བཅུ་བདུན་པའོ། །

[Block 1848]
བཅོམ་ལྡན་འདས་ཅིའི་སླད་དུ་སྤྱོད་པ་མ་མཆིས་པ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པ་ལགས་ཞེས་བྱ་བ་ནི་དགུ་བཅུ་བརྒྱད་པའོ། །

[Block 1849]
བཅོམ་ལྡན་འདས་གལ་ཏེ་སྤྱོད་པ་མ་མཆིས་པ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པ་ལགས་ན་ཞེས་བྱ་བ་ནི་དགུ་བཅུ་དགུ་པའོ། །

[Block 1850]
བཅོམ་ལྡན་འདས་ཇི་ཙམ་གྱིས་ན་མི་དམིགས་པར་འགྱུར་ཞེས་བྱ་བ་ནི་བརྒྱ་པའོ། །

[Block 1851 [HEADING]]
##### ཞུ་བ་བརྒྱ་ཕྲག་གཉིས་པ། ^1-2-6-2-0

[Block 1852]
འདི་མན་ཆད་ནི་བརྒྱ་ཕྲག་གཉིས་པ༌[^1266]ལ་བབ་སྟེ། བཅོམ་ལྡན་འདས་གཉིས་ཞེས་བགྱི་བ་ཇི་ལྟ་བུ་ལགས་ཞེས་བྱ་བ་ནི་དང་པའོ། །

[Block 1853]
བཅོམ་ལྡན་འདས་གཉིས་སུ་མ་མཆིས་པ་གང་ལགས་ཞེས་བྱ་བ་ནི་གཉིས་པའོ། །

[Block 1854]
བཅོམ་ལྡན་འདས་ཅི་ལགས་དམིགས་སུ་མ་མཆིས་པ་མི་དམིགས་སམ་ཞེས་བྱ་བ་ནི་གསུམ་པའོ། །

[Block 1855]
བཅོམ་ལྡན་འདས་གལ་ཏེ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པའི་ཚེ་དམིགས་པ་ལ་མི་ཆགས་ཤིང༌[^1267]མི་དམིགས་པ་ལ་ཡང་མི་ཆགས་པ་ལགས་ན་ཞེས་བྱ་བ་ནི་བཞི་པའོ། །

[Block 1856]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡང༌[^1268]དམིགས་སུ་མ་མཆིས་ཏེ་ཞེས་བྱ་བ་ནི་ལྔ་པའོ། །

[Block 1857]
བཅོམ་ལྡན་འདས་གལ་ཏེ་བྱང་ཆུབ་སེམས་དཔའ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པའི་ཚེ་གཟུགས་ཀྱང་མི་དམིགས་ཞེས་བྱ་བ་ནི་དྲུག་པའོ། །

[Block 1858]
བཅོམ་ལྡན་འདས་འོ་ན་སུའི་སླད་དུ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པ་ལགས་ཞེས་བྱ་བ་ནི་བདུན་པའོ། །

[Block 1859]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་མ་བགྱིས་པ༌[^1269]སྟེ། མངོན་པར་འདུས་མ་བགྱིས་པ་ལགས་ན་ཞེས་བྱ་བ་ནི་བརྒྱད་པའོ། །

[Block 1860]
བཅོམ་ལྡན་འདས་གལ་ཏེ་དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་ཀྱིས་སྤྱན་ལྔས་ཀྱང་ཞེས་པ༌[^1270]ནི་དགུ་པའོ། །
--- END BLOCKS ---

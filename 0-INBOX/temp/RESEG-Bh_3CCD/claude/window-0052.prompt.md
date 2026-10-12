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
ཞེས་འདམ་ཁའོ། །

[Block 1822]
བསྡུ་བ་ཡང་རྒྱུད་ཀྱི་ཡན་ལག་ཡིན་ཏེ། རྡོ་རྗེ་ཅན་གྱི་གཟུགས་སོགས་ཀྱིས།

[Block 1823 [VERSE]]
གཙུག་ཏོར་མཉེས་པར་བྱེད་པར་བཤད། །
ཁྲོ་བོ་རྣམས་ལའང་དེ་མཆོག་སྟེ། །
སངས་རྒྱས་རྡོ་རྗེ་རབ་བསྒོམ་པའོ། །

[Block 1824]
ཞེས་ལེའུ་བཅོ་ལྔ་པ་ལས་འབྱུང་ངོ་། །ངེས་པ་ཡང་རྒྱུད་ཀྱི་ཡན་ལག་ཡིན་ཏེ། །ལེའུ་དེ་ཉིད་ལས་ཀྱང་། །

[Block 1825 [VERSE]]
གནོད་སྦྱིན་མ་ཡི༌[^1266]སྔགས་རྒྱུད་ལ། །
གཤིན་རྗེ་གཤེད་ནི་ཉིད་དུ་བསྒོམ། །

[Block 1826]
ཞེས་འབྱུང་ངོ་། །རྡོ་རྗེ་ཕྲེང་བ་ལས་ཀྱང་།

[Block 1827 [VERSE]]
མིང་དང་ཡོངས་སུ་སྨྲ་བ་དང་། །
ཆོ་ག་དང་ནི་ངེས་པ་ཉིད། །
སོ་སོར་བཀག་པ་དབང་བ་དང་། །
འདམ་ཁ་དང་ནི་གཞན་དག་སྡུད།[^1267] །

[Block 1828 [VERSE]]
རྗེས་སུ་སྨྲ་བ་གཞན་ཆོས་ཐོབ། །
མདོ་ཡི་མཚན་ཉིད་རྣམ་པ་བཅུ། །

[Block 1829]
ཞེས་བྱ་བའི་ཚིག་འདུས་སོ། །

[Block 1830]
དེ་ལྟར་གཞན་ཡང་རྒྱུད་ཀྱི་ཡན་ལག་འདི་ཉིད་དུ་བསྟན་པར་བྱེད་ནུས་ཏེ། འོན་ཀྱང་ཤིན་ཏུ་རྒྱས་པས་དོན་རྣལ་མ༌[^1268]སྒྲིབ་པར་བྱེད་པས་མ་བསྟན་ཏོ། །

[Block 1831 [VERSE]]
རྒྱུད་ཀྱི་ཡན་ལག་གྲུབ་པས་རྒྱུད་གྲུབ་པོ། །
གཙོ་བོ་ཡིན་པའི་ཕྱིར་མདོར་ཡང་བསྟན་ཏོ། །

[Block 1832]
གལ་ཏེ་དེ་ལྟར་ཡིན་ན་ཡན་ལག་དུ་མ་ཡོད་པས་ཚད་མ་ལ་སོགས་པ་ཅིའི་ཕྱིར་མ་བསྟན་ཞེ་ན། སྨྲས་པ། གང་གཉི་ག་ལས་སྐྱེས་པ་དེ་ནི་གཅིག་གིས་ཉེ་བར་བསྟན་དུ་ཡོད་དེ། དཔེར་ན། ཨུ་མའི་བུ་ནི་གཞོན་ནུ་དང་མ་ཧཱ་དེ་བའི་བུ་བཞིན་ནོ། །

[Block 1833]
བཤད་པའི་རྒྱུད་རྣམས་ཀྱང་དེ་ལྟར་གྱུར་པའི་ཡན་ལག་ལྔ་དང་ལྡན་པའི་ཕྱིར་མདོ་སྡེའི་ཡན་ལག་གི་ནང་དུ་འདུས་སོ། །

[Block 1834]
གལ་ཏེ་འདི་མདོ་སྡེར་བཤད་པ་ཡིན་ན་དེའི་ཚེ།

[Block 1835 [VERSE]]
དགོས་པ་བསྡུས་པའི་དོན༌[^1269]དང་བཅས། །
ཚིག་དོན་དགོངས་པ་ཡང་དག་ལྡན། །
རྒལ་ལན་བཅས་པ་ཉིད་དང་ནི། །
མདོ་དོན་སྨྲ་བ་པོས་བཤད་བྱ། །

[Block 1836]
ཞེས་འབྱུང་བས་དགོངས་པ་ལ་སོགས་པ་དྲུག་པོ་ངེས་པར་བཤད་པར་བྱ་བ་ཡིན་ཞེ་ན། སྨྲས་པ། བརྗོད་པ༌[^1270]ལ་སོགས་པ་རྣམ་པ་ལྔ་པོ་འདུས་པའི་ཕྱིར་ལོགས་སུ་མ་བསྟན་ཏེ། བརྗོད་པ་ལ་སོགས་པ་བཤད་པའི་དུས་ཉིད་དུ་དགོངས་པ་ལ་སོགས་པའི་དོན་རྟོགས་པས་ལོགས་སུ་མི་བཤད་དེ། མདོའི་དགོས་པ་ནི་དགོས་པའི་ནང་དུ་འདུས་པ་དང་། །རྒལ་ལན་དག་ནི་འབྲེལ་པ་བསྡུས་པའོ། །

[Block 1837]
གང་གི་ཕྱིར་དེ་བཞིན་གཤེགས་པ་ལ་སོགས་པའི་འབྲེལ་པ་རྣམ་པ་དྲུག་བསྟན་པའི༌[^1271]དུས་སུ་ཉན་པ་པོ་དང་འཆད་པ་པོ་དག་གི་དུས་སུ་ཕན་ཚུན་འདྲི་བ་དང་ལན་གྱི་བྱེ་བྲག་ངེས་པར་འབྱུང་བ་ཡིན་ཏེ། འདྲི་བ་དང་ལན་ཁོ་ན་རྒལ་ལན་དག་གོ། །

[Block 1838]
བརྗོད་པར་བྱ་བ་ལ་ཚིག་གི་དོན་དང་འདུས་པའི་དོན་དང་དགོངས་པ་རྣམས་འདུས་པའོ། །

[Block 1839]
དེ་ཡང་མ་བསྡུས་པའི་དོན་དང་དགོས་པ༌[^1272]མེད་པ། བརྗོད་པར་བྱ་བར་དང་བྲལ་བ་བརྗོད་པ་ཉིད་དུ་མི་འགྱུར་རོ། །

[Block 1840]
བྱ་རོག་གི་སྐད་བརྟག་པ༌[^1273]དང་སེའུ་བཅུ་ལ་སོགས་པའི་ཚིག་བཞིན་ནོ། །

[Block 1841]
དེའི་ཕྱིར་འདི་ནི་མདོ་སྡེའི་ཡན་ལག་ཁོ་ན་ཡིན་པས་སྐྱོན་མེད་དོ། །

[Block 1842]
དེ་ལྟ་ན་བརྗོད་པ་ལ་སོགས་པ་ལྔ་པོ་དེ་དག་ནི་ཚད་མ་མེད་པའི་ཚིག་ལས་ཇི་ལྟར་གཟུང་ཞེ་ན། རྟག་པ་སྔོན་དུ་འགྲོ་བ་རྣམས་ཀྱིས་ཀྱང་ཚད་མ་སྔོན་དུ་འགྲོ་བས༌[^1274]འཇུག་པར་བྱེད་དེ་ཚིག་ལ་ནི་ཚད་མ་ཉིད་མེད་དོ། །

[Block 1843]
ཇི་སྐད་དུ།

[Block 1844 [VERSE]]
དངོས་པོས༌[^1275]དངོས་པོ་སྟོན་མིན་ཏེ། །
དངོས་པོའི་དུས་སུ་དངོས་མེད་ཡིན། །
དེ་ཉིད་ཀྱིས་ནི་འདས་པ་དེ། །
དེ་ནི་འདས་པ་ཞེས་བརྗོད་དོ། །

[Block 1845 [VERSE]]
བྲག་གི་ཟ་མ་ཏོག་དཔེ་ཡིས། །
སྒྲ་ཡིས་བདག་དང་འཇིག་རྟེན་དང་། །
སྒྲ་ནི་སྦལ་པའི་ཕུང་པོ་ཡིས། །
རང་ཉིད་ཀྱིས་ནི་དམན་པར་བྱས། །

[Block 1846 [VERSE]]
ཡི་གེ་ཚིག་དང་ངག་རྣམས་དང་། །
རྟགས་དང་ཚིག་གི་ཚོགས་དག་ཉིད། །
བྱ་བ་བྱེད་པ་འབྲེལ་པ་རྣམས། །
བརྫུན་ཡིན་པས་ན་རྗོད་བྱེད་མིན། །

[Block 1847 [VERSE]]
ཚིག་བཤད་ཚིག་རྐང་ལྔ་འམ་ནི། །
གསུམ་གྱིས་ཀྱང་ནི་ཅིས་མི་འདོད། །
ངག་ནི་བརྗོད་བྱ་རག་ལས་ཕྱིར། །
མཁའ་འགྲོ་མ་ཡི་བརྡ་ལྟར་འགྱུར། །

[Block 1848 [VERSE]]
གཟུང་བར་བྱ་བའི་ཆོས་རྣམས་ལ། །
སྔོན་གྱི་མཁས་པར་འདོད་རྣམས་ཀྱིས། །
སྒྲ་ཡི་ལེགས་སྦྱར་གཡང་ས་རུ། །
ཨེ་མའོ་འཇིག་རྟེན་ལྷུང་བར་བྱས། །

[Block 1849 [VERSE]]
འདི་ནི་སྣང་ཞེས་བརྗོད་པ་ལ། །
དྲིས་པ་མཁས་པ་གང་གིས་ནི། །
མགོ་ནས་བསྐོར་ནས་ལག་གཡས་ཀྱི། །
དེ་ལྟར་གང་གིས་སྟོན་པར་བྱེད། །

[Block 1850 [VERSE]]
གཞན་གྱིས་གཞན་ནི་མི་རིག་སྟེ། །
འབྲེལ་པ་མེད་པས་སྐྱེ་མི་འགྱུར། །
གཞན་དུ་རལ་གྲི་ཕོག་པ་ལ། །
གཞན་ལ་འགྱུར་བར་བྱེད་དམ་ཅི། །

[Block 1851 [VERSE]]
བྱ་བ་མེད་པའི་རང་བཞིན་གྱིས། །
གང་གིས་གང་གི་འདིར་སྟོན་བྱེད། །
དངོས་མེད་ལས་བྱུང་དངོས་པོ་ཡིས། །
དངོས་པོ་གང་ལས་བསྐྱེད་པ་མེད། །

[Block 1852 [VERSE]]
དེ་བས་སྐྱོབ་པ་རྣམས་ཀྱིས་ནི། །
འབྱུང་བ་ཆེན་པོ་ཞེས་བཤད་དོ། །
འབྱུང་བ་ཀུན་གྱི་སྔོན་གྱུར་པས། །
ངེས་ཚིག་མཁས་པ་རྣམས་ཀྱིས་གསུངས། །

[Block 1853]
ཞེས་བྱ་བ་ལ་སོགས་པ་སྔོན་གྱི་སློབ་དཔོན་གྱི༌[^1276]ཚད་མའི་ཚིག་རྣམས་ཀྱིས་གསལ་བའི་སྒྲ་དང་དོན་གྱི་འབྲེལ་པ་ལ་ངག་གི་ཚད་མ་ཉིད་མེད་པའི་ཕྱིར་བརྗོད་པ་ལ་སོགས་པའི་ཚིག་ཙམ་གྱིས་ཇི་ལྟར་ངེས་པར་བྱེད་ཅེ་ན། དེ་ལ་སྨྲས་པ། ངག་ལས་ཐེ་ཚོམ་སྐྱེ་བ་ནི། དེ་ཡང་རྣམ་པ་གསུམ་སྟེ། དོན་དང་ལྡན་པའི་ཐེ་ཚོམ་དང་། དོན་མེད་པའི་ཐེ་ཚོམ་དང་།

[Block 1854 [VERSE]]
དོན་ཡོད་པ་དང་དོན་མེད་པའི་ཐེ་ཚོམ་མོ། །
དེ་ལ་དོན་དང་ལྡན་པའི་ཐེ་ཚོམ་ནི་དཔེར་ན།
ས་འོག་ན་གནས་པའི་གཏེར་འདོན་པ་བཞིན་ནོ། །

[Block 1855]
དོན་མེད་པ་ནི་དཔེར་ན་ཤུགས་ཆེ་བའི་གཙང་པོ་ལ་གཅོད་པ༌[^1277]བཞིན་ནོ། །

[Block 1856]
དོན་ཡོད་པ་དང་མེད་པའི་ཐེ་ཚོམ་ནི་དཔེར་ན་རོ་ལངས་བསླང་བ་བཞིན་ནོ། །

[Block 1857]
དེ་ལ་དོན་དང་ལྡན་པ་ནི་འཇུག་པའི་ཡན་ལག་གོ། །

[Block 1858]
དོན་དང་མི་ལྡན་པ་དང་དོན་མེད་པ་དང་། ཡོད་པའི་ཐེ་ཚོམ་དག་ནི་ལྡོག་པའི་ཡན་ལག་གོ། །

[Block 1859]
འདིར་ནི་དང་པོའི་ཚིག་ཚད་མ་མེད་པ་ལས་ཅི་འདིར་བརྗོད་པ་ལ་སོགས་པ་ཡོད་དམ་མེད་ཅེས་ཐེ་ཚོམ་ལ་འཇུག་པར་འགྱུར་ཏེ། དེའི་རྗེས་སུ་རིམ་པ་གཉིས་ཀྱིས་མཚོན་པའི་བརྗོད་པར་བྱ་བ་དང་། དེ་རྗོད་པར་བྱེད་པའི་ཚིག་གི་ཚོགས་དང་དེ་དག་གི་འབྲེལ་པ་ཡང་ཐོས་ནས་བསམ་པ་དང་བསྒོམ་པའི༌[^1278]རིམ་པས་ཐ་མལ་པའི་ལུས་བཟློག་པ་དང་འཇིག་རྟེན་ལས་འདས་པའི་རྡོ་རྗེའི་སྐུའི་མཚན་ཉིད་རྡོ་རྗེ་འཆང་ཆེན་པོའི་ཕྲིན་ལས་ཐམས་ཅད་པ་ཐོབ་ནས། དེའི་རྗེས་ཐོགས་སུ་འགྲོ་བ་ཐམས་ཅད་ཀྱང་རྡོ་རྗེ་འཛིན་པར་བྱེད་པ་ནི་དགོས་པའི་དགོས་པ་ཡང་ལ་ལ་ཡོད་པར་འདོད་པས་བསྟན་བཅོས་འདི་ལེགས་ཞེས་མགུ་ཞིང་བྱ་བ་བྱས་པར་འགྱུར་རོ། །

[Block 1860]
དེའི་ཕྱིར་དོན་གྱི་ཐེ་ཚོམ་ལས་འཇུག་པ་ནི་རིགས་པ་ཁོ་ནའོ། །
--- END BLOCKS ---

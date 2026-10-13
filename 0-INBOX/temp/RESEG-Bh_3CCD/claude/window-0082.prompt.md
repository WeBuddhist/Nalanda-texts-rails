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
[Block 2871]
དྲི་བ་དེ་ཉིད་ཅིའི་ཕྱིར་ཞེས་བྱ་བ་ལ་སོགས་པས་བསྟན་ཏེ། འདིར་ནི་སྐད་ཀྱི༌[^1878]ཡི་གེའི་དོན་གང་ཡིན་པ་དང་ཅིའི་སླད་དུ་དང་པོ་སྦྱོར་བ་དང་སངས་རྒྱས་ཀྱིས་གསུངས་པའམ་ཉན་ཐོས་ཀྱིས་གསུངས་སམ་ཞེས་འདྲི་བའོ། །

[Block 2872]
དམ་ཆོས་ཡོན་ཏན་སྨྲ་བ་ཡི། །ཞེས་བྱ་བ་ལ་སོགས་པས་ལན་གསུངས་སོ། །

[Block 2873]
དྲི་བ་མཆོག་ཡིན་པའི་ཕྱིར་ལེགས་སོ་ཞེས་བྱ་བ་བྱིན་པའོ། །

[Block 2874]
གང་ཕྱིར་ཐམས་ཅད་གཟིགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་དང་པོར་སྦྱོར་བའི་དྲི་བའི་ལན་ནོ། །

[Block 2875]
གང་གི་ཕྱིར་གྱིས་ནི་དོན་གང་ཡིན་ཞེས་དྲི་བའི་ལན་ནོ། །

[Block 2876]
ཐམས་ཅད་གཟིགས་པ་ཡིས་ཞེས་པ་འདིས་ཉན་ཐོས་ཀྱིས་གསུངས་པ་བཀག་པའོ། །

[Block 2877]
དོན༌[^1879]དེ་ཉིད་ལས་བདེ་བར་གཤེགས་པའི་གསུང་ཡིན་ཞེས་བསྟན་པར་འགྱུར་རོ། །

[Block 2878]
ཇི་བཞིན་དུ་ཞེས་པ་ནི་སྤྱིའི་དོན་གྱིས་བཤད་པའི་རིམ་པས་སོ། །

[Block 2879]
དེ་ནི་གོ་རིམས་ཞེས༌[^1880]པ་ནི་དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་དང་ལས་ཀྱི་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་གྱི་ཕྱོགས་སོ། །

[Block 2880]
ཆོས་ཀྱི་ཕུང་པོ་ཞེས་བྱ་བ་ལ་སོགས་པས་མདོ་སྡེ་ལ་སོགས་པ་ཆོས་ཀྱི་ཕུང་པོ་ཐམས་ཅད་དུའོ། །

[Block 2881]
ཕ་དང་མའི་ངོ་བོ་ཉིད༌[^1881]ཡི་གེ་གཉིས་ཡིན་ཞེས་དམ་བཅའོ། །

[Block 2882 [VERSE]]
དེ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར། །
ཡི་གེ་ཨེ་ནི་མར་གྱུར་ལ། །

[Block 2883]
ཞེས་སྨོས་ཏེ། མ་ནི་ཤེས་རབ་སྟེ༌[^1882]ཨེའི་རྣམ་པ་ཅན་ཆོས་འབྱུང་བའི་ཕྱག་རྒྱས་ཉེ་བར་མཚོན་པའི་ཕྱིར་རོ། །

[Block 2884]
ཝ་ནི་ཕ་ཞེས་བྱ་བར་གྲགས། །ཞེས་པ་ནི་ཐབས་ཀྱི་ངོ་བོ་ཉིད་རྣལ་འབྱོར་པ་ཡིན་ཏེ། ཡི་གེ་ཝས་ཉེ་བར་མཚོན་པའི་རྟགས་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 2885]
ཐིག་ལེ་དེ་ནི་སྦྱོར་བ་སྟེ། །ཞེས་པ་ནི་དེ་དག་འདུས་པའི་ངོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2886]
དེས་ནི་བསྒྲུབ་བྱ་དང་སྒྲུབ༌[^1883]བྱེད་ཀྱི་འབྲེལ་པའི་ངོ་བོ་ཉིད་ནི་བསྙེན་པར་བསྟན་ཏོ། །

[Block 2887]
སྦྱོར་ཏེ་ཤིན་ཏུ་རྨད་བྱུང༌[^1884]བ། །ཞེས་པ་ནི་འཁྱུད་པ་དང་ཙུམ་པ་ན་ལ་སོགས་པའི་སྣ་ཚོགས་པའི་སྐད་ཅིག་མ་རྫོགས་པར་བྱེད་པའི་ཕྱིར་རོ་ཞེས་ཡན་ལག་དང་པོའོ། །

[Block 2888]
ཨེ་ནི་པདྨ་ཞེས་པ་ནི། གྲུ་གསུམ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2889]
ཝཾ་ནི་རྡོ་རྗེ་ཉིད་ཡིན་ནོ།[^1885] །

[Block 2890]
ཞེས་པ་ནི་ཡི་གེ་ཝས༌[^1886]གསང་བའི་རྡོ་རྗེ་མཚོན་པའི་ཕྱིར་རོ། །

[Block 2891]
ཐིག་ལེ་དེར་ནི་ས་བོན་ཏེ། །ཞེས་པ་ནི་དེ་གཉིས་ཀྱི་དབུས་སུ་གནས་པའི་བྱང་ཆུབ་ཀྱི་སེམས་སོ། །

[Block 2892]
དེ་ལས་འགྲོ་བ་གསུམ་པོ་སྐྱེས། །ཞེས་པ་ནི་དཀྱིལ་འཁོར་གྱི༌[^1887]འཁོར་ལོ་དང་ཁམས་གསུམ་ཡང་སྐྱེས་སོ། །

[Block 2893]
དེས་ནི་རྡོ་རྗེ་དང་པདྨ་སྙོམས་པར་ཞུགས་པའི་མཚན་ཉིད༌[^1888]ཉེ་བར་སྒྲུབ་པ་ཞེས་བྱ་བ་ཡན་ལག་གཉིས་པ་བསྟན་ཏོ། །

[Block 2894]
ཨེ་ནི་ཤེས་རབ་ཉིད་གྱུར་པ། །ཞེས་པ་ནི་ཤེས་རབ་ཀྱི་པདྨའི་ལྟེ་བར་ཆར་བཀག་པར་བྱ་བའི་ཕྱིར་ཡི་གེ་ཕཊ་རྣམ་པར་བཀོད་ནས་བསྐྱོད་པ་གང་ཡིན་པ་དེ་ནི་ཤེས་རབ་པོ། །ཝ་ནི་རབ་དགའི་བདག་པོ་ཞེས་པ་ནི་རབ་ཏུ་དགའ་བའི་བདག་པོ་རྡོ་རྗེ་ལ་ཡི་གེ་ཧཱུཾ་བཀོད་ནས་བསྐྱེད་པ༌[^1889]གང་ཡིན་པ་དེ་ནི་བསྒྲུབ་པ༌[^1890]ཞེས་བྱ་བ་ཡན་ལག་གསུམ་པའོ། །

[Block 2895]
ཐིག་ལེ་ནི་མྱོང་བའི་ངང༌[^1891]ཚུལ་ཅན་ནོ། །

[Block 2896]
དེ་ཡང་རྣམ་པ་གཉིས་ཏེ། རྫས་ཀྱི་བདག་ཉིད་དང་བདེ་བ་ཆེན་པོའོ། །

[Block 2897]
དེ་ལ་བདེ་བ་ཆེན་པོ་ནི་མི་ཤིགས་ཏེ་དེ་ཉིད་ཅེས་སྨོས་ཏེ། རང་རིག་པའི་དེ་ཁོ་ན་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ།[^1892] །

[Block 2898]
རྫས་ཀྱི་བདག་ཉིད་ནི་གང་རྡོ་རྗེ་རྩེ་མོ་ནས་ཕྱིར་སྤྲོས་པའི་བྱང་ཆུབ་ཀྱི་སེམས་སོ། །

[Block 2899]
དེ་ལས་ཡི་གེ་དེ་ཉིད་ཀྱང་སྐྱེས་ཞེས་པ་ནི་ཐིག་ལེ་དེ་ལས་བཛྲ་དྷྲྀཀ་ཅེས་བྱ་བ་ལ་སོགས་པའི་ས་བོན་གྱི་སྔགས་ལས་སྐྱེས་པའི་ཐུགས་རྡོ་རྗེ་འཛིན་པ་ལ་སོགས་པ་ཞེས་སྒྲུབ་པ་ཆེན་པོ་ཞེས་བྱ་བ་ཡན་ལག་བཞི་པའོ། །

[Block 2900]
ཆོས་ཀྱི་ཕྱག་རྒྱ་ཡི་གེ་གཉིས། །ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་ཆོས་ནི་བརྒྱ༌[^1893]ཁྲི་བཞི་སྟོང་གི་ཚད་ཀྱི་ཕུང་པོ་དེ་ལ་གང་གིས་རྒྱས་བཏབ་ཅིང་བསྡུས་པ་དེ་ནི་ཆོས་ཀྱི་ཕྱག་རྒྱ་སྟེ་ཨེ་ཝཾ་མོ།[^1894] །

[Block 2901]
དེ་བས་ན་ཆོས་ཡང་དག་པར་བརྗོད་པའི་མདོ་ལས་དགེ་སློང་རྣམས་དེའི༌[^1895]ཆོས་འདི་སྐད་བདག་གིས་ཐོས་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་སྡུད༌[^1896]པར་བྱའོ་ཞེས་གསུངས་སོ། །

[Block 2902]
དེ་བས་ན་གསུང་རབ་ཐམས་ཅད་ཀྱི་སྙིང་པོར་གྱུར་པའི་ཡི་གེ་གཉིས་པོ་ཡོངས་སུ་ཤེས་པས་སེམས་ཅན་ཐམས་ཅད་ལ་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བར་འགྱུར་རོ། །

[Block 2903]
འགྲོ་བ་གང་གིས་ཡི་གེ་གཉིས་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། སྐྱེ་བོ་གང་གིས་སྔོན་དུ་བཤད་པའི་ཡི་གེ་གཉིས་པོ་མི་ཤེས་ནས་ཆོས་ཀློག་པའམ་ཉན༌[^1897]པའམ་སྒོམ་པར་བྱེད་པ་དེ་ནི་སངས་རྒྱས་ཀྱི་ཆོས་ལས་ཕྱི་རོལ་དུ་གྱུར་པ་སྦྱོར་སྤངས་ནི་རྣལ་འབྱོར་མེད་པའི་ཐུབ་པ་བཞིན། །ཞེས་པ་ནི་མུ་སྟེགས་ཀྱི་བྲམ་ཟེ་བཞིན་དུ་འགྱུར་རོ། །

[Block 2904]
ཡང་ན་དགག་པར་བྱེད་པའི་སྒྲ་སྤངས་ཏེ། ཤེས༌[^1898]ནས་རྟག་ཏུ་འདོན་པ་དག །ཅེས་པ་ནི་འདིས་ཡི་གེ་གཉིས་པོ་ཙམ་ཡོངས་སུ་ཤེས་པས༌[^1899]སངས་རྒྱས་ཀྱི་ཆོས་རྣམས༌[^1900]ཀྱི་ཕྱི་རོལ་ཏུ་འགྱུར་ཞིང་སྦྱོར་བ་སྤངས་པ་ནི་ཏིང་ངེ་འཛིན་སྤང་བ༌[^1901]ཡང་ཐུབ་པ་བཞིན་ཞེས་པ་ནི་ཤཱཀྱ་སེང་གེ་དང་འདྲ་བར་འགྱུར་རོ། །

[Block 2905]
ཨེ་ཝཾ་ཡི་གེ་གཉིས་སྒྱུ་མ་ལ་ཞེས་པ་ནི་རིག་མ་དང་སྐྱེས་བུའི་བདག་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2906]
ཐམས་ཅད་མཁྱེན་པ་འདིར་བཞུགས་པས། ཞེས་པ་ནི་དཀྱིལ་འཁོར་གྱི་བདག་པོ་ཉིད་དུ་རྡོ་རྗེ་འཆང་ཆེན་པོ་བཞུགས༌[^1902]པས་སོ། །

[Block 2907]
དམ་ཆོས་བསྟན་པའི་ཐོག་མར་ནི། །ཞེས་བྱ་བ་ལ་སོགས་པས་རྟག་པའི་གནས་ཐོབ་པར་འདོད་པས་དང་པོ་བསྟན་བཅོས་ཀྱི་ཐོག་མར་ཨེ་ཝཾ་ཞེས་བྱ་བ་སྦྱར་བར་བྱ་བ་དང་། བསྟན་བཅོས་ཀྱི་བཀུར་སྟི་བྱ་བ་དང་། ཡི་གེ་གཉིས་པོ་དྲན་པར་བྱའོ་ཞེས་བརྒྱ་བྱིན་ལ་འབོད༌[^1903]ཅིང་གདམས་པའོ། །

[Block 2908]
བདག་གིས་ཞེས་བྱ་བ་ལ་སོགས་པས་ལུང་ཚད་མ་ཉིད་བསྟན་ཏོ། །

[Block 2909]
བཤད་པའི་རྒྱུད་ལས་ཞེས་པ་ནི་རྡོ་རྗེ་ཕྲེང་བ་ལས་སོ། །

[Block 2910]
འཁོར་ལོས་སྒྱུར་བའི༌[^1904]ངོ་བོའོ། །
--- END BLOCKS ---

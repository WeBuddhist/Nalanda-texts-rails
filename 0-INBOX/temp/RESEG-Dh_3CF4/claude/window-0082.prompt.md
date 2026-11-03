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
ཡིད་གྱུར་པ་ནི་འདོད་ཆགས་ཀྱིས་མྱོས་པར་གྱུར་པའོ། །

[Block 2872]
སེམས་ཁོང་དུ་ཆུད་པའི་མིག་དང་། བཞིན་དང་མདངས་ཞེས་བྱ་བ་ནི་གང་གོང་དུ་བསྟན་པའི་སེམས་ཁོང་དུ་ཆུད་ཅིང་ཤུགས་ནར་ཞེས་འབྱུང་ལ་གླལ་ཡང་དང་ཡང་དུ་འབྱུང་ཞེས་བྱ་བ་དེ་ཉིད་སྟོན་ཏོ། །

[Block 2873]
ཤ་བྲི་སྲབ་མོར་གྱུར་ཞེས་བྱ་བ་འདིས་ནི་སེར་སྐྱར་གྱུར་ཅིང་ཤ་བྲི་སྟེ་སྲབ་མོར་གྱུར་ཞེས་བྱ་བ་དེ་ཉིད་བསྟན་པ་ཡིན་ནོ། །

[Block 2874]
དེས་བརྡ་དང་མཚན་མ་ལ་མཁས་པ་ཞེས་བྱ་བ་ལ་བརྡ་ནི་གང་གོང་དུ་བསྟན་པའི་སེམས༌[^1820]ཁོང་དུ་ཆུད་ཅིང་ཤུགས་ནར་ཞེས་འབྱུང་ལ། གླལ་ཡང་དང་ཡང་དུ་འབྱུང་ཞེས་བྱ་བ་དེ་ཉིད་ཀྱིས་བསྟན་པ་ཡིན་ནོ། །

[Block 2875]
མཚན་མ་ནི་གང་གོང་དུ་བསྟན་པའི་སེར་སྐྱར་གྱུར་ཅིང་ལུས་ཀྱང་ཤ་བྲི་སྟེ་སྲབ་མོར་གྱུར་ཞེས་པ་དང་། འདོད་ཆགས་ཀྱིས་མྱོས་པར་གྱུར་པའི་རྣམ་པ་མངོན་པར་གྱུར་པ་ཞེས་གང་བསྟན་པའོ། །

[Block 2876]
བརྡ་དང་མཚན་མ་ཞེས་བྱ་བ་བསྡུས་པ་ནི་རྣམ་པ༌[^1821]ཞེས་སྨོས་པ་སྟེ་དེ་ཉིད་ཡིན་ཏེ། སྤྱོད་ཚུལ་དུ༌[^1822]རྣམ་པ་དེའི༌[^1823]མཚན་ཉིད་དུ་བྱས་ནས་བརྡ་དང་མཚན་མ་ལ་མཁས་པའི་བློའོ། །

[Block 2877]
[^1824]གང་ལ་ཡོད་པ་དེ༌[^1825]ནི་བརྡ་དང་མཚན་མ་ལ་མཁས་པའི་བློའོ། །

[Block 2878]
རྒྱལ་པོ་དེ་དེ་ལྟར་གྱུར་ཞེས་བྱ་བ་ནི་སེར་སྐྱར་གྱུར་ཅིང་ལུས་ཀྱང་ཤ་བྲི་སྲབ་མོར་གྱུར་པ་དང་། སེམས༌[^1826]ཁོང་དུ་ཆུད་ཅིང་ཤུགས༌[^1827]ནར་ཞེས་འབྱུང་ལ་གླལ་ཡང་དང་ཡང་དུ་འབྱུང་བ་སྟེ། དེའི་རྒྱུ་ནི་མྱོས་བྱེད་མ་མཐོང་བའི་རྒྱུས་དེ་རྒྱུ་དང་བཅས་པར་རོ། །

[Block 2879]
དེ་མ་རུང་དུ་གྱུར་པ་ནི་མ་རུང་བར༌[^1828]གྱུར་པ་སྟེ་ཤི་བར་རོ། །

[Block 2880]
དེ་ལ་དོགས་ལ༌[^1829]ཡོད་པ་གང་ཡིན་པ་དེ་ནི་མ་རུང་དུ་དོགས་པའོ། །

[Block 2881]
དེ་མ་རུང་དུ་དོགས་པའི་རྒྱུ་བསྟན་པའི་ཕྱིར་སྨྲས་པ། འདོད་ཆགས་ཀྱང་མཐུ་ཆེ་བར་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 2882]
ནང་དུ་མཆི་བར་གནང་བ་ནི་ཞུ་བའི་དོན་ཡོད་དོ་ཞེས་སྨྲས་ནས་གནང་བའོ། །

[Block 2883]
རྟོག་པ་སྐྱེ་བ༌[^1830]ནི་ཅི་བདེན་པ་ཉིད་དམ་བརྫུན་པ་ཞེས་སོ། །

[Block 2884]
དེ་ལྟར་མེད༌[^1831]ན་ཞེས་བྱ་བ་ནི་དེ་ཇི་ལྟར་སྨྲ་བ་བཞིན་དུ་སྟེ། མྱོས་བྱེད་མ་དེ་ལ་རྒྱལ་པོའི་ཐུགས་ཆགས་པའོ། །

[Block 2885]
བཀའ་སྩལ་པར་བྱ་བ་དེ་མི་བསྲུང༌[^1832]བ་ནི་བཀའ་མ༌[^1833]སྩལ་པའོ། །

[Block 2886]
བུ་མོ་འདི་ཕྱག་ཏུ་བཞེས་ཞེས་བྱ་བ་ནི་ཅི་ནས་ཀྱང་བསྣམས་པའི་རིགས་སོ་ཞེས་པའོ།

[Block 2887]
[^1834] །ཡང་ན་བཀའ་སྩལ་པའི་ཕྱིར་རོ། །

[Block 2888]
ལྟས་ཀྱིས་བསྐུལ་བས་ཞེས་བྱ་བ་ནི་གབ་པ་ཡིན་ནའང་འདིའི་དོན་གསལ་བར་བསྟན་པས་སོ། །

[Block 2889]
མི་འདོད་པའི་ཚིག་འབྲུ་གསལ་བ་སྟེ། གང་གི་ཚིག་དེའོ། །

[Block 2890]
དེ་ནི་མི་རིགས་སོ་ཞེས་བྱ་བ་ནི་བུ་མོ་དེ་ཕྱག་ཏུ་བཞེས་ཤིག་ཅེས་གང་སྨྲས་པའི་ཚིག་དེ་མི་རིགས་པར་བཤད་པའོ། །

[Block 2891]
མི་འདོད་པའི་རྒྱུ་བསྟན་པའི་ཕྱིར། བསོད་ནམས་ཉམས་གྱུར༌[^1835]ཞེས་བྱ་བ༌[^1836]ལ་སོགས་པའི་དང་པོའི༌[^1837]ཚིགས་བཅད་གཉིས་ཡིན་ཏེ། བསོད་ནམས་ཉམས་གྱུར༌[^1838]ཞེས་བྱ་བ་ནི་བགྲོད་པ་མ་ཡིན་པར་བགྲོད་པས་སོ། །

[Block 2892]
དེས་ཅིར་འགྱུར་ཞེ་ན། དེས་སྨྲས་པ། བདག་ཀྱང་མི་འཆི༌[^1839]མིན་ཞེས་བྱ་བ་སྟེ། འདིས་ནི་ཤི་བར་གྱུར༌[^1840]ན་བསོད་ནམས་ཉམས་པར་འགྱུར་བས་བདག་གི༌[^1841]བགྲོད་པའི་ཉེས་དམིགས་བསྟན་པའོ། །

[Block 2893]
བདག་གི་སྡིག་པ་འདི་ཡང་གཞན་གྱིས་ཤེས་པར་འགྱུར། ཞེས་བྱ་བ་ནི་གྲགས་པ་མ་ཡིན་པ་ཐོབ་པའི༌[^1842]ཉེས་དམིགས་ཡིན་ནོ། །

[Block 2894]
དེ་དང་བྲལ་བར་གྱུར་བས་ཞེས་བྱ་བ་འདིས༌[^1843]ནི་འཇིག་རྟེན་འདི་དང་ཕ་རོལ་གཉི་ག་ལ་གནོད་པ་ཡིན་ཏེ། འཇིག་རྟེན་འདིར་ནི་ཤི་བར་གྱུར་པས་གནོད་པའོ། །

[Block 2895]
ཡིད་འགྱོད་ཅིང་ཤི་བས༌[^1844]འཇིག་རྟེན་ཕ་རོལ་ཏུ་ངན་འགྲོར་འགྲོ་བ་ཡིན་ནོ། །

[Block 2896]
འཇིག་རྟེན་འདི་དང་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་བསོད་ནམས་ཉམས་པ༌[^1845]ཞེས་བྱ་བ་དེའི་རྗེས་སུ་འགྲོ་བའི་ཚིག་ཡིན་ཏེ། གཉི་ག་ལ་གནོད་པར་འགྱུར་བ་ནི་བདག་དང་ཕ་རོལ་གཉི་ག་ལ་སྟེ། འཇིག་རྟེན་འདིར་བདག་ནི་འགྲོ་བ་མ་ཡིན་པར་འཇུག་པའི་རྒྱུས་ངན་འགྲོར་འགྲོ་བར་འགྱུར་ཞེས་བྱ་བ་ཡིན་ལ། ཕ་རོལ་ནི་འགྱོད་ཅིང་འཆི་བར་གྱུར་པས་ངན་འགྲོར་འགྲོ་བའོ།[^1846] །དེ་གཅིག་པུར་ཡང༌[^1847]མ་ཟད་དེ། བདག་ཉིད་ལ་ནི་མི་སྙན་པ་ཡང་ཡིན་ལ། ཕ་རོལ་ནི༌[^1848]འཆི་བར་འགྱུར་བ་སྟེ། དེ་ལྟར་བཞི་པོ་དེས་གནོད་པ་ཡིན་ནོ། །

[Block 2897]
དེ་མི་འདོད་པ་ནི་ཚེ་འདི་དང་ཕ་རོལ་གཉི་ག་ལ་གནོད་པའི་ལས་སོ། །

[Block 2898]
གང་ཕྱིར་ཞེས་བྱ་བ་ནི་བདག་གི་རྒྱུ་དེ་ཉིད་དེའི་རྒྱུ་ཞེས་བྱ་བ་ཡིན་ཏེ། བདག་གི་རྒྱུ་ཉིད་ལ་མཁས་པ་སྟེ། དེ་ལྟར་གནོད་པར་གྱུར་པའི་ལས་དེ་ལ་རྟོགས་པར༌[^1849]བྱེད་པ་ལ་མཁས་པའོ། །

[Block 2899]
བསོད་ནམས་ཉམས་ཞེས་བྱ་བའི་ཚིག་གི་ལན་ནི། སྦྱིན་པ་བགྱིད་པའི་གྲོགས་བགྱིས་པས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ཡིན་ཏེ། སྦྱིན་པ་བཀག་པས་ཆོས་ཀྱི༌[^1850]བགེགས་སུ་ཇི་ལྟར༌[^1851]འགྱུར་ཞེ་ན། དེ་ཉིད་སྨྲས་པ། དེ་མ་བཞེས་པ་སྟེ། བདག་ལས་སྦྱིན་པ་མ་བཞེས་པས༌[^1852]དེས་ན་དེ་ལྟར་སྦྱིན་པའི་བགེགས་སུ་འགྱུར་བ་ཡིན་ནོ། །

[Block 2900]
བདག་གི་སྡིག་པ་འདི་ཡང་གཞན་གྱིས་ཤེས་པར་འགྱུར། །ཞེས་བྱ་བ་འདིའི་ལན་ནི། འོ་སྐོལ་གཉིས་ལས་མ་གཏོགས་བ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ནོ། །

[Block 2901]
དེ་དང་བྲལ་བར་གྱུར་པས་འགྱོད་པའི་མེ། །ཞེས་བྱ་བ་དེའི་ལན་ནི། དེ་ལྟར་བགྱིས་ན་བདག་ལ་སྨན་ཡོན་བཏགས་པར་འགྱུར།[^1853] །ཞེས་བྱ་བས་དངས༌[^1854]པའི་ཚིགས་བཅད་ཀྱིས་བསྟན་ཏེ། བདག་ལ་སྨན་ཡོན་བཏགས་པར་འགྱུར་གྱི།[^1855] དེ་དང་བྲལ་བས་འགྱོད་པ་ནི་མེད་དོ་ཞེས་པའོ། །

[Block 2902]
དེ་མེད་པས་འཆི་བ་ཡང་མེད་དེ་དེའི་རྒྱུར་གྱུར་པའི་འཆི་བ་དེ་མེད་པས་ངན་སོང་དུ་འགྲོ་བ་མེད་པའོ། །

[Block 2903]
ཚིགས་བཅད་འདི་གསུམ་གྱིས་ནི་སྔར་བསྟན་པའི་ཉེས་པ་བཞི་པོའི་ལན་བསྟན་པ་ཡིན་ནོ། །

[Block 2904]
སྦྱིན་པ་བགྱིད་པའི་གྲོགས་བགྱིས་པས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་གང་བསྟན་པ་དེའི་ལན་ནི། ང་ལ་རབ་ཏུ་བྱམས་པའི་ཕྱིར། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། སྔར་གྱི་སྦྱིན་པ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་གྱི་སྦྱིན་པ་ནི་རྣམ་པ་བཞི་སྟེ། ཕན་པ་ཡིན་ལ་བདེ་བ་མ་ཡིན་བ་དང་། བདེ་བ་ཡིན་ལ་ཕན་པ་མ་ཡིན་པ་དང་། བདེ་བ་ཡང་ཡིན་ལ་ཕན་པ་ཡང་ཡིན་པ་དང་། བདེ་བ་ཡང༌[^1856]མ་ཡིན་ལ་ཕན་པ་ཡང་མ་ཡིན་པའོ། །

[Block 2905]
བཞི་པོ་དེ་ལས་ཕན་པ་མེད་པར་འགྱུར་བ་ནི་རྣམ་པ་ཐམས་ཅད་དུ་སྦྱིན་པར་མི༌[^1857]བྱ་བ་ཡིན་པས་གང་ཕན་པ་མ་ཡིན་ལ་བདེ་བ་ཡིན་པ་དེ་ཡང་སྦྱིན་པར་བྱ་བ་ཡིན་ནོ། །

[Block 2906]
ཕན་པ་ཡང་མ་ཡིན་ལ་བདེ་བ་ཡང་མ་ཡིན་པ་དེ་ཡང༌[^1858]སྦྱིན་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 2907]
གང་ཕན་པ་དང་བདེ་བ་དེ་ནི་སྦྱིན་པ་ཡིན་ནོ། །

[Block 2908]
གང་མི་བདེ་ན་ཡང་ཕན་པ་དེ་ནི་སྦྱིན་པ་ཡིན་ནོ། །

[Block 2909]
དེ་བས་ན་འདི་ནི་བདེ་བ་ཉིད་ཡིན་གྱི༌[^1859]ཕན་པ་ནི་མ་ཡིན་ཏེ། འདི་ལྟ་བུའི་མཚན་ཉིད་ཀྱི་སྦྱིན་པ་ནི་རྣམ་པ་ཐམས་ཅད་དུ་ཆོས་སྒྲུབ་པའི་གྲོགས་མ་ཡིན་ནོ། །

[Block 2910]
བདག་ལ་སྨན་བཏགས་པར་འགྱུར་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གང་གོང་དུ་བསྟན་པ་དེའི་ལན་ནི། རབ་ཏུ་བྱམས་པས་ང་ཡི་ཕྱིར། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། གྲོགས་པོ་ལས་ཁྱད་པར་དུ་གྱུར་པ་ནི་གཉེན་པས་ལྷག་བ་སྟེ། རྒྱུ་དེས་ན་རབ་ཏུ་བྱམས་པས་ངའི་ཕྱིར། རང་གི་སྲོག་ཀྱང་ཕོངས་པར༌[^1860]མི་ལྟ་བས་སོ། །
--- END BLOCKS ---

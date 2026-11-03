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
[Block 36]
འཕགས་པའི་ཚོགས་ལ་ཞེས་བྱ་བས་དགེ་འདུན་ལ་བསྟོད་པ་བསྟན་ཏེ། ཉོན་མོངས་པ་དང་སྡིག་པའི་ཆོས་ལས་རིང་དུ་སྤངས་པ་ལ་ནི་འཕགས་པ་ཞེས་བྱ་ལ། འཕགས་པའི་གང་ཟག་དེ་ལྟ་བུ་མང་པོ་ལ་ནི་འཕགས་པའི་ཚོགས་ཞེས་བྱ་སྟེ། དེ་ཡང་མདོར་ན་སློབ་པའི༌[^15]གང་ཟག་དང་། མི་སློབ་པའི་གང་ཟག་འཕགས་པ༌[^16]གཉིས་ཡོད་དོ། །

[Block 37 [HEADING]]
#### སློབ་པའི་གང་ཟག། ^1-3-1-0

[Block 38]
དེ་ལ་སློབ་པའི་གང་ཟག་ནི་བདུན་ཡོད་དེ། རྒྱུན་དུ་ཞུགས་པ་དང་། རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ཐོབ་པ་དང་། ལན་ཅིག་ཕྱིར་འོང་བ་དང་། ལན་ཅིག་ཕྱིར་འོང་བའི་འབྲས་བུ་ཐོབ་པ་དང་། ཕྱིར་མི་འོང་བ་དང་། ཕྱིར་མི་འོང་བའི་འབྲས་བུ་ཐོབ་པ༌[^17]དང་། དགྲ་བཅོམ་པ་ལ་འཇུག་པ་དང་བདུན་ནོ། །

[Block 39 [HEADING]]
#### མི་སློབ་པའི་གང་ཟག། ^1-3-2-0

[Block 40]
མི་སློབ་པའི་གང་ཟག་ནི་དགྲ་བཅོམ་པའི་འབྲས་བུ་ཐོབ་པ་སྟེ། དེ་དག་ལ་ཡང་ཕྱག་འཚལ་ཏེ་ཞེས་བྱ་བ་སྦྱར་རོ། །

[Block 41 [HEADING]]
### ཕྱག་འཚལ་བ། ^1-4-0

[Block 42]
དེ་ལ་ཕྱག་འཚལ་བ་ཡང་རྣམ་པ་གསུམ་སྟེ། ལུས་ཀྱིས༌[^18]ཕྱག་འཚལ་བ་དང་། ངག་གིས་ཕྱག་འཚལ་བ་དང་། ཡིད་ཀྱིས་ཕྱག་འཚལ་བའོ། །

[Block 43 [HEADING]]
#### ལུས་ཀྱིས་ཕྱག་འཚལ་བ། ^1-4-1-0

[Block 44]
དེ་ལ་ལུས་ཀྱིས་ཕྱག་འཚལ་བ་ནི། དཔྲལ་བ་གཏུགས་པ་ཐལ་མོ་སྦྱར་བ་ལ་སོགས་པ་བྱེད་པའོ། །

[Block 45 [HEADING]]
#### ངག་གིས་ཕྱག་འཚལ་བ། ^1-4-2-0

[Block 46]
ངག་གིས་ཕྱག་འཚལ་བ་ནི་དེ་དག་གི་ཡོན་ཏན་ཚིག་ཏུ་རྗོད་པར༌[^19]བྱེད་པའོ། །

[Block 47 [HEADING]]
#### ཡིད་ཀྱིས་ཕྱག་འཚལ་བ། ^1-4-3-0

[Block 48]
ཡིད་ཀྱིས་ཕྱག་འཚལ་བ་ནི་དེ་དག་ལ་དད་པ་དང་དགའ་བ་དང་མོས་བའི་སེམས་ཀྱིས་ཕྱག་འཚལ་བའོ། །

[Block 49]
ཕྱག་འཚལ་ཏེ་ཞེས་བྱ་བ་ནི་ཕྱག་འཚལ་ནས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 50 [HEADING]]
### མདོ་ཙམ་ངེས་པར་བཤད་པར་བྱ་བ། ^1-5-0

[Block 51]
ཕྱག་འཚལ་ནས་ཅི་བྱ་ཞེ་ན།

[Block 52 [VERSE]]
དགེ་ཚུལ་གྱི་ནི་ཆོ་ག་རྣམས། །
མདོ་ཙམ་ངེས་པར་བཤད་པར་བྱ། །

[Block 53]
ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་ཚུལ་དགེ་སྦྱོང་རྣམས་ཀྱི་བསླབ་ཚིག༌[^20]དང་ལས་སུ་བྱ་བ་རྣམས་ལ་བྱའོ། །

[Block 54]
མདོ་ཙམ་ངེས་པར༌[^21]བཤད་པར་བྱ་བ་ནི་དགེ་སྦྱོང་གི་བསླབ་ཚིག༌[^22]དང་ལས་སུ་བྱ་བ་རྣམས་ནི་ཀཱ་རི་ཀཱ་སུམ་བརྒྱ་པ་དང་། འདུལ་བ་འབུམ་གྱི་ནང་ནས་འབྱུང་བས་དེར་བརྟག་པར་བྱའོ། །

[Block 55]
འདིར་མདོ་ཙམ་སྟེ། མི་བྱར་མི་གནང་བའི་དམིགས་པ་ཉི་ཚེ་ཙམ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 56]
རང་གི་ལྷ་ལ་ཕྱག་འཚལ་བ་དང་བསྟོད་པའི་བཤད་པ༌[^23]རྫོགས་སོ།། །།

[Block 57 [HEADING]]
## བསླབ་པ་ཉམས་སུ་བླང་བ། ^2-0

[Block 58]
བསླབ་པ་ཉམས་སུ་བླང་བ་ཡང་ཚིག་རྣམ་པ་བཞི་ཞིག་གིས་སྟོན་ཏེ། གང་ཞེ་ན། ཆོས་ཕུན་སུམ་ཚོགས་པ་དང་། གང་ཟག་ཕུན་སུམ་ཚོགས་པ་དང་། སྒྲུབ་པ་ཕུན་སུམ་ཚོགས་པ་དང་།

[Block 59 [HEADING]]
### ཆོས་ཕུན་སུམ་ཚོགས་པ། ^2-1-0

[Block 60 [VERSE]]
ཇི་ལྟར་བསྒྲུབ་པར་བྱ་བའོ། །
ཤཱཀྱ་སེང་གེའི་བསྟན་པ་ལ། །

[Block 61]
ཞེས་བྱ་བས་ཆོས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། དེ་ལ་ཆོས་ཕུན་སུམ་ཚོགས་པ་ཡང་ཚིག་རྣམ་པ་གཉིས་སོ། །

[Block 62 [HEADING]]
#### སྟོན་པ་ཕུན་སུམ་ཚོགས་པ། ^2-1-1-0

[Block 63]
སྟོན་པ་ཕུན་སུམ་ཚོགས་པ་དང་། བསྟན་པ་ཕུན་སུམ་ཚོགས་པའོ།[^24] །ཤཱཀྱ་སེང་གེ་ཞེས་བྱ་བས་སྟོན་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། སྟོན་པ་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་སོ། །

[Block 64]
སངས་རྒྱས་བཅོམ་ལྡན་འདས་གསུང་དབྱངས་རྣམ་པར་དག་པ་དང་ཐུགས་རྣམ་པར་དག་པས་ན་སྟོན་པ་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱ་སྟེ། ཤཱཀྱ་ཞེས་བྱ་བས་གདུང་རུས་རྣམ་པར་དག་པ་སྟོན་ཏེ། སྤྱིར་མི་རྣམས་ཀྱི་ནང་དུ་སྐྱེས་པ་ལ་རིགས་རྣམ་པ་བཞི་ཡོད་དེ། དམངས་རིགས་དང་། རྗེའུ་རིགས་དང་། བྲམ་ཟེའི་རིགས་དང་། རྒྱལ་རིགས་སོ། །

[Block 65]
སངས་རྒྱས་བཅོམ་ལྡན་འདས་ནི་ཤཱཀྱ་རྣམས་ཀྱི་ནང་དུ་གཽ་ཏ་མའི་རིགས་ཀྱི་གདུང་རུས་དང་ལྡན་པས་ན་ཤཱཀྱ་ཞེས་བྱའོ། །

[Block 66]
ཤཱཀྱ་ཞེས་བྱ་བས་ནི་གདུང་རུས་རྣམ་པར་དག་པ་སྟོན་ཏོ། །

[Block 67]
སེང་གེ་ཞེས་བྱ༌[^25]བས་ཐུགས་རྣམ་པར་དག་པ་སྟོན་ཏོ། །

[Block 68]
དཔེར་ན་སེང་གེ་ནི་དཔའ་བོའི་སེམས་དང་ལྡན་པས་རི༌[^26]དགས་རྣམས་ཀྱིས་མི་སྐྲག་ཅིང་རི་དགས་རྣམས་སེང་གེས་ཟིལ་གྱིས་གནོན་པ་དང་འདྲ་བར་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱང་མི་འཇིགས་པ་བཞི་བརྙེས་པའི་ཐུགས་དང༌[^27]ལྡན་པས་བདུད་དང་མུ་སྟེགས་པ་རི་དགས་དང་འདྲ་བས་སངས་རྒྱས་ཟིལ་གྱིས་མི་ནོན་ཅིང་སྐྲག་པར་བྱེད་མི་ནུས༌[^28]ལ། སངས་རྒྱས་ནི་བདུད་དང་མུ་སྟེགས་རི་དགས་དང་འདྲ་བ་རྣམས་ཟིལ་གྱིས་གནོན་ཅིང་སྐྲག་པར་བྱེད་པས་ན་སངས་རྒྱས་ལ་སེང་གེ་ཞེས་བྱ་སྟེ། དེ་བས་ན་སེང་གེའི་སྒྲས་ཐུགས་དག་པ་སྟོན་ཏོ། །

[Block 69 [HEADING]]
#### བསྟན་པ་ཕུན་སུམ་ཚོགས་པ། ^2-1-2-0

[Block 70]
བསྟན་པ་ཞེས་བྱ་བས་བསྟན་པ་ཕུན་སུམ་ཚོགས་པ་སྟོན༌[^29]ཏོ། །

[Block 71]
སློབ་མ་རྣམས་ལ་འདི་དག་ནི་བསྒྲུབ་པར་བྱ་བ་ཡིན། འདི་དག་ནི་སྤང་བར་བྱ་བ་ཡིན་ནོ་ཞེས་སྟོན་པའི་ཆོས་ལ་བསྟན་པ་ཞེས་བྱ་སྟེ། འདུལ་བའི་སྡེ་སྣོད་དང་། མདོ་སྡེའི་སྡེ་སྣོད་དང་། མངོན་པའི་ཆོས་ཀྱི་སྡེ་སྣོད་དོ། །

[Block 72]
དེ་ལས་རབ་ཏུ་བྱུང་བ་རྣམས་ཀྱིས་བསླབ་ཚིག༌[^30]རྣམ་པ་གསུམ་སྟེ། ལྷག་པ་ཚུལ་ཁྲིམས་ཀྱི་བསླབ་པ་དང་། སེམས་ཀྱི་བསླབ་པ་དང་། ཤེས་རབ་ཀྱི་བསླབ་པའོ། །

[Block 73]
དེ་འདུལ་བའི་སྡེ་སྣོད་ཀྱི་ནང་ནས་ནི་ལྷག་པ་ཚུལ་ཁྲིམས་ཀྱི་བསླབ་པ་འབྱུང་ངོ་། །མདོ་སྡེའི་སྡེ་སྣོད་ལས་ནི་ལྷག་པ་སེམས་ཀྱི་བསླབ་པ་འབྱུང་ངོ་། །མངོན་པའི་ཆོས་ཀྱི་སྡེ་སྣོད་ནས་ནི་ལྷག་པ་ཤེས་རབ་ཀྱི་བསླབ་པ་འབྱུང་སྟེ། དེ་ལྟར༌[^31]སྡེ་སྣོད་གསུམ་ལ་བསྟན་པ་ཞེས་བྱའོ། །

[Block 74 [HEADING]]
### གང་ཟག་ཕུན་སུམ་ཚོགས་པ། ^2-2-0

[Block 75]
དད་པས་རབ་ཏུ་བྱུང་ནས་ནི། །ཞེས་བྱ་བས་གང་ཟག་ཕུན་སུམ་ཚོགས་པ་སྟོན་ཏེ། གང་ཟག་ཕུན་སུམ་ཚོགས་པ་ཡང་རྣམ་པ་གཉིས་ཀྱིས་ཕུན་སུམ་ཚོགས་སོ། །
--- END BLOCKS ---

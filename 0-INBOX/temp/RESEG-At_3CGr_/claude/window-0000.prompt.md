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
[Block 1 [HEADING]]
## ༄། །ཤེས་རབ་སྙིང་པོའི་རྣམ་པར་བཤད་པ་བཞུགས།

[Block 2 [HEADING]]
## ཀླད་ཀྱི་དོན། ^I-0

[Block 3]
༄༅༅། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 4 [HEADING]]
## ཆོས་ཀྱི་འཁོར་ལོ་གཉིས་པའི་དོན་བསྡུ་བ། ^II-0

[Block 5]
བདེ་བར་གཤེགས་པས་གསུངས་པའི་ཆོས་ཀྱི་འཁོར་ལོ་གཉིས་པའི་དོན་ཐམས་ཅད་བསྡུ་ན་གཉིས་ཏེ། མངོན་པར་རྟོགས་པའི་དོན་དང་། སྙིང་པོའི་དོན་ནོ། །

[Block 6]
དེ་ལ་མདོ་རྒྱས་འབྲིང་གསུམ་གྱིས་ནི་གང་ཟག་གསུམ་གྱི་དབང་དུ་བྱས་ནས། མངོན་པར་རྟོགས་པ་གཙོ་བོར་སྟོན་པ་ཡིན་ལ། བདུན་བརྒྱ་པ་ལ་སོགས་པས་ནི་སྙིང་པོའི་དོན་གཙོ་བོར་སྟོན་ཏོ། །

[Block 7]
ལམ་མངོན་པར་རྟོགས་པ་ཡེ་ཤེས་ཀྱི༌[^1]དམིགས་པ་གཙོ་བོར་སྟོན་པའོ། །

[Block 8]
དེ་ལ་རྒྱས་འབྲིང་གསུམ་གྱིས་གཙོ་བོར་མངོན་རྟོགས་བསྟན། ཡང་སྙིང་པོའི་དོན་ཤུགས་ལ་བསྟན། བདུན་བརྒྱ་པ་ལ་སོགས་པས་གཙོར༌[^2]སྙིང་པོའི་དོན་བསྟན། མངོན་རྟོགས་ཞར་ལ་བསྟན་ཏོ། །

[Block 9]
འདིར་ཡང་སྙིང་པོའི་དོན་བསྟན་པ་ཡིན་ལ་འདི་ཡང་བི་མ་ལ་མི་ཏྲ་ལྟར་ན་དོན་བརྒྱད་ཀྱིས་མདོ་འདིའི༌[^3]དོན་མ་ལུས་པ་བསྟན་པ་ཡིན་ནོ། །

[Block 10]
དོན་བརྒྱད་ཀྱང་གླེང་སློང་པ་དང་ཞེས་བྱ་བ་ལ་སོགས་པས་ལུས་རྣམ་པར་གཞག་པ་ཡིན་ནོ། །

[Block 11 [HEADING]]
## དང་པོ་མདོ་འབྱུང་བའི་རྒྱུ། ^1-0

[Block 12]
དེ་ལ་སློབ་དཔོན་ཕྱོགས་ཀྱི་གླང་པོ་ལ་སོགས་པས་མདོའི་དོན་གཞན་དུ་ཡང་བཤད་པ་ཡོད་དེ། མདོ་འབྱུང་བའི་རྒྱུ༌[^4]དང་། མདོ་དངོས་སོ། །

[Block 13]
དང་པོ་ལ་གཉིས་ཏེ། [^5]གླེང་སློང་བ༌[^6]དང་གླེང་གཞིའོ། །

[Block 14 [HEADING]]
### གླེང་སློང་བ། ^1-1-0

[Block 15]
འདི་གཉིས་ཀྱི་ཁྱད་པར་ནི། ཚིག་འབྱུང་བའི་རྐྱེན་དང་། མདོ་འབྱུང་བའི་རྒྱུའོ། །

[Block 16]
དེ་ཡང་སྔོན་བྱུང་བ་དང་། རྗེས་འཇུག་སྟེ། གླེང་བསླང་བའོ། །

[Block 17 [HEADING]]
### གླེང་གཞི། ^1-2-0

[Block 18]
གླེང་གཞི་ལ་གཉིས་ཏེ། ཐུན་མོང་དང་ཁྱད་པར་གྱི་གླེང་གཞིའོ། །

[Block 19]
འདི་གཉིས་ཀྱི་བྱེ་བྲག་ནི་མདོ་ཐམས་ཅད་ལ་ཐུན་མོང་དུ་ཡོད་པ་དང་། མདོ་འདི་ལ་ཡོད་པ་གཞན་ལ་མེད་པའོ། །

[Block 20 [HEADING]]
#### ཐུན་མོང་གི་གླེང་གཞི། ^1-2-1-0

[Block 21 [HEADING]]
##### དུས། ^1-2-1-1-0

[Block 22]
ཐུན་མོང་ལ་བཞི་སྟེ། དུས་དང་

[Block 23 [HEADING]]
##### སྟོན་པ། ^1-2-1-2-0

[Block 24]
སྟོན་པ་དང་།

[Block 25 [HEADING]]
##### གནས། ^1-2-1-3-0

[Block 26]
གནས་དང་

[Block 27 [HEADING]]
##### འཁོར། ^1-2-1-4-0

[Block 28]
འཁོར་རོ། །

[Block 29 [HEADING]]
#### ཁྱད་པར་གྱི་གླེང་གཞི། ^1-2-2-0

[Block 30 [HEADING]]
##### གཙོ་བོ་ཏིང་ངེ་འཛིན་ལ་ཞུགས་པ། ^1-2-2-1-0

[Block 31]
ཁྱད་པར་གྱི༌[^7]གླེང་གཞི་ལ་གཉིས་ཏེ། གཙོ་བོ་དང་

[Block 32 [HEADING]]
##### འཁོར་ཏིང་ངེ་འཛིན་ལ་ཞུགས་པ། ^1-2-2-2-0

[Block 33]
འཁོར་ཏིང་ངེ་འཛིན་ལ་ཞུགས་པའོ། །

[Block 34]
དེ་ནི་བསྡུས་དོན་ནོ། །

[Block 35]
དགོས་པའི་དོན་ནི་སྡུད་པ་པོ་རང་ཉིད་ཚད་མའི་སྐྱེས་བུར་འགྱུར་བར་བྱ་བའི་ཕྱིར་ཏེ། དུས་དེ་ཙམ་ན་སྟོན་པ་འདི་ལ་འཁོར་འདི་རྣམས་དང་གནས་འདིར་ཐོས་སོ་ཞེས་དཔང་པོ་དང་དན་རྟགས༌[^8]དང་བཅས་པའི་ཚིག་བརྗོད་ན། འོ་ན་འདི་བཤད་པ་འདི༌[^9]བདེན་ནོ་ཞེས་སྡུད་པ་པོ་ལ་ཡིད་ཆེས་པར་འགྱུར་ཏེ། འདི་ལྟ་སྟེ། འཇིག་རྟེན་ན་ཡང་དཔང་དང་དན་རྟགས་ཞིབ་པས་ཁོའི་དེ་བདེན་ནོ་ཞེས་རྟོགས་པ་བཞིན་ནོ། །

[Block 36]
དེ་སྐད་དུ་ཡང་སློབ་དཔོན་ཕྱོགས་ཀྱི་གླང་པོས། །

[Block 37 [VERSE]]
དད་ལྡན་འཇུག་པའི་ཡན་ལག་ཏུ། །
རང་ཉིད་ཚད་མར་རབ་བསྒྲུབ་ཕྱིར། །
སྟོན་པ་དང་ནི་འཁོར་དབང་པོ། །
ཡུལ་དང་དུས་སོགས་བསྟན་པ་ཡིན། །

[Block 38 [VERSE]]
སྡུད་པར་བྱེད་པས་འཇིག་རྟེན་དུ། །
ཡུལ་དང་དུས་སོགས་བསྟན་པ་ནི། །
དཔང་པོར་བཅས་པའི་ཚིག་བརྗོད་ན། །
རང་ཉིད་ཚད་མར་འགྲོ་བ་ཡིན། །

[Block 39]
ཞེས་གསུངས་སོ། །

[Block 40]
འདི་རྣམས་ཀྱི་ཚིག་དོན་དང་ཚིག་རྣམ་པར་སྦྱར་བ་ནི་གསལ་ལོ། །
--- END BLOCKS ---

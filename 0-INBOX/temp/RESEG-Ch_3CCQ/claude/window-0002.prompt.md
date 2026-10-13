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
[Block 71]
ཞེས་བྱ་བ་སྟེ་དགོངས་པས་བཤད་པའོ། །

[Block 72 [HEADING]]
## མཇུག་བྱང། ^a-0

[Block 73 [HEADING]]
### མཛད་བྱང། ^a-1-0

[Block 74]
སྦྱོར་བ་ཡན་ལག་དྲུག་པ་ཞེས་བྱ་བའི་འགྲེལ་པ་སློབ་དཔོན་ཆེན་པོ་ཟླ་བ་གྲགས་པས་མཛད་པ་རྫོགས་སོ།། །།

[Block 75 [HEADING]]
### འགྱུར་བྱང། ^a-2-0

[Block 76]
རྒྱ་གར་གྱི་མཁན་པོ་ཨཱརྱ་ཤྲད་དྷཱ་ཀ་ར་ཝརྨྨ་དང་། ཞུ་ཆེན་གྱི༌[^34]ལོ་ཙཱ་བ་དགེ་སློང་རིན་ཆེན་བཟང་པོས་བསྒྱུར་ཅིང་བཅོས་ཏེ་གཏན་ལ་ཕབ་པའོ། །

[Block 77]
[^35]

[Block 78]
[^1]: ཡུལ་ཅན་དེ་ ༼སྣར། པེ།༽ ཡུལ་ཅན་
[^2]: གནས་པས་ན་ ༼སྣར། པེ།༽ གནས་པས་
[^3]: འཇུག་པ་ ༼སྣར། པེ།༽ འཇུག་
[^4]: དང་ཡང་དུ་སྡུད་ཅིང་ལེན་པས་ན་ ༼སྣར། པེ།༽ དང་ཡང་
[^5]: སྦྱོར་བ་ཡིན་ ༼སྣར། པེ།༽ སྦྱོར་བ་ཡིས་
[^6]: སྤྱོད་ ༼སྣར། པེ།༽ དཔྱོད་
[^7]: ཡིད་ལ་ ༼སྣར། པེ།༽ ཡིད་
[^8]: ཉིད་ ༼སྣར། པེ།༽ ནི་
[^9]: ཤེས་པ་དང་ཤེས་ ༼སྣར། པེ།༽ ཤེས་
[^10]: རྡོ་རྗེའི་ ༼སྣར། པེ།༽ རྡོ་རྗེ་
[^11]: བྱ་ ༼སྣར། པེ།༽ བྱ་བར་ཤེས་པར་བྱ་
[^12]: བསམས་ ༼སྣར། པེ།༽ བསམ་
[^13]: མི་ཤིགས་པ་ ༼སྣར། པེ།༽ མི་ཤིག་
[^14]: འཛིན་པ་ཡིན་ ༼སྣར། པེ།༽ འཛིན་
[^15]: མཚན་མ་ ༼སྣར། པེ།༽ མཚན་མར་
[^16]: ན་ ༼སྣར། པེ།༽ ནི་
[^17]: རྡོ་རྗེ་ ༼སྣར། པེ།༽ རྡོ་རྗེས་
[^18]: གྱུར་པ་ ༼སྣར། པེ།༽ འགྱུར་བ་
[^19]: མཚན་མ་ ༼སྣར། པེ།༽ མཚན་མར་
[^20]: འདའ་ ༼སྣར། པེ།༽ མདའ་
[^21]: རིམ་གྱིས་ ༼སྣར། པེ།༽ རིམ་གྱི་
[^22]: བྱ་བ་ ༼སྣར། པེ།༽ བྱ་
[^23]: རིམ་པས་ ༼སྣར། པེ།༽ རིམ་གྱིས་
[^24]: ལས་ ༼སྣར། པེ།༽ ལ་
[^25]: ལས་ ༼སྣར། པེ།༽ ལ་
[^26]: རྒྱུ་བ་ལ་ ༼སྣར། པེ།༽ རྒྱུ་བས་
[^27]: བསྒོམ་པར་ ༼པེ།༽ སྒོམ་པར་
[^28]: འདི་ཉིད་ཀྱིས་ ༼སྣར། པེ།༽ འདི་ཉིད་ཀྱི་
[^29]: ཀྱི་ ༼སྣར། པེ།༽ ཀྱིས་
[^30]: བརྟག་ ༼སྣར། པེ།༽ བརྟགས་
[^31]: རླབས་ ༼སྣར། པེ།༽ བརླབས་
[^32]: བརྟག་པར་ ༼སྣར། པེ།༽ བརྟགས་པར་
[^33]: རྣལ་འབྱོར་པ་ ༼སྣར། པེ།༽ རྣལ་འབྱོར་
[^34]: ཞུ་ཆེན་གྱི་ ༼སྣར། པེ།༽ ཞུ་ཆེན་
[^35]: ཕབ་པའོ། །

[Block 79]
༼པེ།༽ ཕཕབ་པའོ་སརྦ་མངྒ་ལཾ་
--- END BLOCKS ---

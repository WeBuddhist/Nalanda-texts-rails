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
[Block 36 [HEADING]]
### མཛད་བྱང། ^a-1-0

[Block 37]
སློབ་དཔོན་དཱི་པཾ་ཀ་ར་ཤྲཱི་ཛྙཱ་ན་ལ་བོད་ཀྱི་དགེ་སློང་ཚུལ་ཁྲིམས་རྒྱལ་བས་གསེར་སྲང་བཅུ་བཞིའི་སྦྲང༌[^30]བུ་མེ་ཏོག་དུ་ཕུལ་ནས་བོད་དུ་བྱོན་པའི༌[^31]ཞུ་བ་ཕུལ་བ་ལས་སྒོམ་སྦྱོང་བ་རྣམས་མཐར་ཕྱིན་པར་བྱ་བའི་དོན་དུ་བླ་མ་ཟླ་བ་བཅུ་དྲུག་ཏུ་ལམ་དུ་མ་ཆུད་དོ། །

[Block 38]
དེ་ནས་བོད་དུ་བྱོན༌[^32]ཁར་སློབ་མ་སེམས་སྦྱོང་བ་རྣམས་ཀྱིས་ཞལ་ཆེམས་གཞག་པར་ཞུས་པས་མདོའི་དོན་མན་ངག་ཏུ་བྱས་པ་འདི་ཞལ་ཆེམས་སུ་གནང་ངོ་། །

[Block 39 [HEADING]]
### འགྱུར་བྱང། ^a-2-0

[Block 40]
དེའི་དུས་སུ་རྒྱ་བརྩོན་སེང་གེས་བསྒྱུར་བར་ཞུས་པས་གནང་སྟེ་གཏན་ལ་ཕབ་པོ། །[^33]

[Block 41]
[^1]: དལ་འབྱོར་གྱི་ ༼སྣར། པེ།༽ དལ་འབྱོར་གྱིས་
[^2]: སེལ་བའི་ ༼སྣར། པེ།༽ བསལ་བའི་
[^3]: སྦྱང་བའི་ ༼སྣར། པེ།༽ བྱང་བའི་
[^4]: སྐྱེ་བར་ ༼སྣར། པེ།༽ སྐྱེད་པར་
[^5]: རྣམས་ཀྱི་ ༼སྣར། པེ།༽ རྣམས་ཀྱིས་
[^6]: ལེགས་པར་ ༼སྣར། པེ།༽ ལེགས་པ་
[^7]: ཟས་ཀྱིས་ ༼སྣར། པེ།༽ ཟས་ཀྱི་
[^8]: གཅད་ ༼སྣར། པེ།༽ བཅད་
[^9]: གནས་ ༼སྣར། པེ།༽ གནས་སུ་
[^10]: ལས་ ༼སྣར། པེ།༽ ལ་
[^11]: བའོ། ༼སྣར། པེ།༽ རོ།
[^12]: བརྒྱུད་ ༼སྣར། པེ།༽ རྒྱུད་
[^13]: བཙའ་ ༼སྣར། པེ།༽ རྩ་
[^14]: རླག་པའི་ ༼སྣར། པེ།༽ བརླག་པའི་
[^15]: ཁོ་ན་ ༼སྣར།༽ ཁོ་
[^16]: ཀྱི་ ༼སྣར། པེ།༽ ཀྱིས་
[^17]: སྒྲུབ་པའི་ ༼སྣར། པེ།༽ བསྒྲུབ་པའི་
[^18]: བར་གྱིས་ ༼སྣར། པེ།༽ བར་གྱི་
[^19]: སྒྲུབ་པ་ ༼སྣར། པེ།༽ བསྒྲུབ་པ་
[^20]: སེམས་ཅན་ནི་ ༼སྣར། པེ།༽ སེམས་ཅན་
[^21]: གྲངས་ ༼སྣར། པེ།༽ གྲངས་པ་
[^22]: སྲུང་ ༼སྣར།༽ གསུང་
[^23]: མེ་ ༼སྣར། པེ།༽ མེད་
[^24]: སྐྱེ་བོ་ ༼སྣར། པེ།༽ སྐྱེའོ། །
[^25]: གཞིའི་ ༼སྣར། པེ།༽ གཞི་
[^26]: སྦྱང་སྟེ། ༼སྣར། པེ།༽ སྦྱངས་ཏེ།
[^27]: སྦྱང་བ་ ༼སྣར། པེ།༽ སྦྱངས་པ་
[^28]: འཐོབ་པར་ ༼སྣར། པེ།༽ ཐོབ་པར་
[^29]: ཐམས་ཅད་ལ་མ་ ༼སྣར།༽ ཐམས་ཅད་ལས་
[^30]: བཅུ་བཞིའི་སྦྲང་ ༼སྣར།༽ བཅུ་བཞི་སྦྲམ་ ༼པེ།༽ བཅུ་བཞི་སྦྲང་
[^31]: བྱོན་པའི་ ༼སྣར། པེ།༽ འབྱོན་པའི་
[^32]: བྱོན་ ༼སྣར།༽ འབྱོན་
[^33]: པོ། ། ༼སྣར། པེ།༽ ། །དགེ་སློང་ཚུལ་ཁྲིམས་རྒྱལ་བས་སྤེལ་བར་འདོད་པ་ལས་བོད་ཀྱི་སྟོན་པ་རྣམས་ནི་ང་རྒྱལ་དང་ཕྲག་དོག་ཆེ་བས་ང་རྒྱལ་གྱི་སྒང་བུ་ལ་ཡོན་ཏན་གྱི་ཆུ་མ་ཆགས་སོ། །དེ་འདྲ་ལྷ་ཁང་ཀེ་རུའི་ཁྱམས་སྨད་ཀྱི་བན་དེ་བདག་གིས་ཞུས་ཏེ་གདམས་ངག་དང་བཅས་ཏེ་གནང་ངོ་། །ཇོ་བོའི་བླ་མ་ཨ་ཝ་དྷཱུ་ཏི་པས་རབ་ཏུ་མི་གནས་པའི་ལྟ་བ་དང་། ལས་མཐའ་སེམས་བསྐྱེད་པའི་ཆོ་ག་དང་། མདོ་ཀུན་ལས་བཏུས་པའི་དོན་མན་ངག་ཏུ་བྱས་པ་འདི་གསུམ་སྟབས་གཅིག་ཏུ་གནང་བ་ལགས་སོ། །
--- END BLOCKS ---

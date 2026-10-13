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
[Block 141]
འདིར་ནི་མདོ་ལས་རྟོགས་པ་ཆེ་བ་དང་སེམས་དཔའ་ཆེ་བ་གཉིས་གཙོར་བསྟན་པའི་ཞར་ལ་བར་མ་ཆོད་པའི་རྒྱུ་འདི་ཡང་ཞར་བྱུང་དུ་བསྟན་པ་ཡིན་ནོ། །

[Block 142 [HEADING]]
###### རྟོགས་པའི་བདག་ཉིད། ^3-2-1-4-3-0

[Block 143]
དེ་ལྟར་སྤངས་པའི་བདག་ཉིད་བསྟན་ནས། རྟོགས་པའི་བདག་ཉིད་རྣམ་པ་གཉིས་བསྟན་པའི་ཕྱིར་བླ་ན་མེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། དེ་ལ་གཉིས་ཏེ། ཇི་སྙེད་ཡོད་པ་མཁྱེན་པ་དང་ཇི་ལྟར༌[^45]མཁྱེན་པ་སྟེ། སེམས་དཔའ་ཆེ་བ་དང་རྟོགས་པ་ཆེ་བ་གཉིས་ཡིན་པས་ལན་གཉིས་སུ་གཞག་པ་ཡིན་ནོ། །

[Block 144 [HEADING]]
###### **ཇི་སྙེད་ཡོད་པ་མཁྱེན་པ།** ^3-2-1-4-3-1-0

[Block 145]
དེ་ལ་བླ་ན་མེད་པ་ཞེས་བྱ་བས་ནི་དམིགས་པར་བྱ་བའི་ཡུལ་དང་། དེ་རྗེས་སུ་སྒྲུབ་པའི་རྒྱུ་དང་། འབྲས་བུ་ཐོབ་པ་བླ་ན་མེད་པ་སྟེ། དེ་གསུམ་གྱིས་ནི་ཇི་སྙེད་མཁྱེན་པའི་ཡེ་ཤེས་བསྟན་པ་ཡིན་ཏེ། དེ་གསུམ་དང་ལྡན་པས་ཤེས་བྱའི་དངོས་པོ་ཐམས་ཅད་སྐྱུ་རུ༌[^46]ར་ལག་མཐིལ་དུ་བཞག་པ༌[^47]ལྟར་མཁྱེན་པའོ། །

[Block 146 [HEADING]]
###### **ཇི་ལྟར་མཁྱེན་པ།** ^3-2-1-4-3-2-0

[Block 147]
ཡང་དག་པར་མཉམ་པའི་བྱང་ཆུབ་ཏུ་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་སོ་ཞེས་བྱ་བས་ནི་ཇི་ལྟ༌[^48]བ་བཞིན་མཁྱེན་པའི་ཡེ་ཤེས་བསྟན་པ་སྟེ། འགྲེལ་པ་ནས་གསལ་བར་བསྟན་ཏོ། །

[Block 148]
དེ་ལྟར་ན་དབང་པོ་རྟུལ་པོའི་དབང་དུ་བྱས་ནས། ཚོགས་ལམ་སྦྱོར་ལམ་གཉིས་ལ་ལན་རེ་རེ་དང་། མཐོང་ལམ་ལ་གསུམ། བསྒོམ་ལམ༌[^49]ལ་གཅིག །བར་ཆད་མེད་པའི་ལམ་ལ་གཅིག །སངས་རྒྱས་ཀྱི་ས་ལ་གསུམ་སྟེ། དེ་ལྟར་ལན་བཏབ་པ་བཅུས་ལམ་ལྔ་ལ་སློབ་པའི་ཚུལ་ལེགས་པར་བཤད་པ་ཡིན་ནོ། །

[Block 149 [HEADING]]
#### དབང་པོ་རྣོན་པོའི་དབང་དུ་བྱས་པ། ^3-2-2-0

[Block 150]
ད་ནི་དབང་པོ་རྣོན་པོའི་དབང་དུ་བྱས་ནས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་དོན་མདོར་བསྡུས་ནས་གསང་སྔགས་ཀྱི་དོན་དུ་བཤད་པ་ནི། ཤཱ་རིའི་བུ་དེ་ལྟ་བས་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། ལམ་ལྔ་པོ་དེ་དག༌[^50]ཤེས་པའི་དོན་དང་སྐྱོབ་པའི་དོན་དང་། དེ་གཉིས་ཀྱི་ཕན་ཡོན་དང་། སྔགས་ཉིད་ཀྱི༌[^51]བཤད་པ་དང་།[^52] དེ་ནི་ལན་བཅུ་གཅིག་པ་ཡིན་ནོ། །

[Block 151]
དེ་ནི༌[^53]དྲི་བའི་སྐབས༌[^54]ཇི་ལྟར་བསླབ་པར་བྱ་ཞེས་དྲིས་པའི་ལན་ཡོངས་སུ་རྫོགས་སོ་ཞེས་བསྟན་པའི་ཕྱིར་དེ་ལྟར་བསླབ་པར་བྱའོ་ཞེས་བསྟན་པ་ཡིན་ནོ། །

[Block 152 [HEADING]]
## མཇུག་བྱང། ^a-0

[Block 153 [HEADING]]
### མཛད་བྱང། ^a-1-0

[Block 154 [VERSE]]
དགེ་སློང་ལེགས་པའི་ཤེས་རབ་ཀྱིས། །
མར་མེ་མཛད་དཔལ་ཡེ་ཤེས་ལ། །
གསོལ་བཏབ་ལེགས་པར་བཤད་པ་ཡིན། །
དེ་དོན་བདག་གིས་གཞུང་དུ་བྲིས། །

[Block 155 [VERSE]]
དེང་སང་བོད་ཀྱི་རྒྱལ་ཁམས་འདིར། །
སྔར་གྱི་ལུགས་ངན་ལ་ཞེན་པས། །
ད་དུང་དམ་པའི་གདམས་ངག་ལ། །
ལེགས་བཤད་ཡིན་པར་མི་ཤེས་ཀྱང་། །

[Block 156 [VERSE]]
འོན་ཀྱང་ཤེས་རབ་ལྡན་པ་ལ། །
ཕན་སྙམ་སྙིང་རྗེའི་བསམ་པས་བྲིས། །
རྒྱལ་ཡུམ་ལེགས་པར་རྟོགས་བྱེད་ཅིང་། །
སྡང་བས་སྨྲ་བར་མ་གྱུར་ཅིག །

[Block 157 [HEADING]]
### འགྱུར་བྱང། ^a-2-0

[Block 158]
རྒྱ་གར་གྱི་མཁན་པོ་དཱི་པཾ་ཀ་ར་ཤྲཱི་ཛྙཱ་ན་དང་། ལོ་ཙཱ་བ་དགེ་སློང་ཚུལ་ཁྲིམས་རྒྱལ་བས་བསྒྱུར་ཅིང་ཞུས་ཏེ་གཏན་ལ་ཕབ་པའོ།། །།

[Block 159]
[^1]: ཡེ་ཤེས་ཀྱི་ ༼སྣར། པེ།༽ ཡེ་ཤེས་ཀྱིས་
[^2]: གཙོར་ ༼སྣར། པེ།༽ གཙོ་བོར་
[^3]: འདིའི་ ༼སྣར། པེ།༽ མདོའི་
[^4]: རྒྱུ་ ༼སྣར། པེ།༽ རྒྱུད་
[^5]: གཉིས་ཏེ། ༼སྣར།༽ གཉིས་
[^6]: སློང་བ་ ༼སྣར། པེ།༽ བསླང་བ་
[^7]: ཁྱད་པར་གྱི་ ༼སྣར།༽ ཁྱད་པར་
[^8]: དན་རྟགས་ ༼སྣར། པེ།༽ དོན་བརྟགས་
[^9]: འདི་ ༼སྣར།༽ འདིའི་
[^10]: བསྡུས་དོན་ན་ ༼སྣར། པེ།༽ བསྡུས་དོན་ནས་
[^11]: དེ་ལ་ ༼སྣར།༽ དེ་
[^12]: ནུས་པ་ནི་ ༼སྣར།༽ ནུས་པའི་
[^13]: མེད་དོ། ༼སྣར། པེ།༽ མེད་དེ།
[^14]: ལ་ ༼སྣར།༽ ལས་
[^15]: བསྟན་པས་ ༼སྣར། པེ།༽ བསྟན་པ་
[^16]: ཐོས་པའི་ ༼སྣར། པེ།༽ ཐོས་པ་
[^17]: ཆོས་ཉན་ ༼སྣར།༽ ཆོས་ཅན་
[^18]: སྐལ་པ་ ༼སྣར།༽ སྐལ་
[^19]: དང་ལྡན་ ༼སྣར། པེ།༽ ལ་བསྟན་
[^20]: ཡིན་ནམ་ ༼སྣར། པེ།༽ ཡིན་
[^21]: བྱ་བ་ ༼སྣར། པེ།༽ བྱ་བས་
[^22]: སྒྲུབ་པ་ ༼སྣར། པེ།༽ མེད་པ་
[^23]: དང་ ༼སྣར། པེ།༽ ལ་
[^24]: སྟོན་པ་ ༼སྣར། པེ།༽ བསྟན་པ་
[^25]: གསང་སྔགས་ཀྱི་ ༼སྣར།༽ གསང་སྔགས་ཀྱིས་
[^26]: ཁོག་དབུབ་ ༼སྣར། པེ།༽ ཁོག་
[^27]: རྟོགས་པའི་ ༼སྣར། པེ།༽ རྟོག་པའི་
[^28]: འདི་ ༼སྣར། པེ།༽ འདིས་
[^29]: སྔ་ ༼སྣར།༽ ལྔ་
[^30]: ལྷག་མ་ ༼སྣར། པེ།༽ ལྷག་པ་
[^31]: མཐའ་ ༼སྣར། པེ།༽ མཐའི་
[^32]: ལྟ་བ་ ༼སྣར། པེ།༽ བལྟ་བ་
[^33]: ལྟ་བར་ ༼སྣར། པེ།༽ བལྟ་བར་
[^34]: རིམ་ ༼སྣར། པེ།༽ རིམས་
[^35]: གོ་རིམས་ཀྱང་ ༼སྣར། པེ།༽ གོ་རིམ་ཡང་
[^36]: ཟབ་པའི་ ༼སྣར། པེ།༽ ཟབ་མོའི་
[^37]: ཇི་སྐད་ ༼སྣར། པེ།༽ འདི་སྐད་
[^38]: བསྒོམ་ལམ་ ༼སྣར། པེ།༽ སྒོམ་ལམ་
[^39]: གྱི་ ༼སྣར། པེ།༽ སྒོམ་ལམ་གྱིས་
[^40]: བསྒོམ་ལམ་ ༼སྣར། པེ།༽ སྒོམ་ལམ་
[^41]: བསྒོམ་ལམ་ ༼སྣར། པེ།༽ སྒོམ་ལམ་
[^42]: ལན་ཅིག་ ༼སྣར། པེ།༽ ལམ་གཅིག་
[^43]: བྱ་བ་ལ་ ༼སྣར། པེ།༽ བྱ་བ་
[^44]: ན་ ༼སྣར། པེ།༽ ནི་
[^45]: ཇི་ལྟར་ ༼སྣར། པེ།༽ ཇི་ལྟ་བ་
[^46]: སྐྱུ་རུ་ ༼སྣར། པེ།༽ སྐྱུར་རུ་
[^47]: བཞག་པ་ ༼སྣར། པེ།༽ གཞག་པ་
[^48]: ལྟ་ ༼སྣར།༽ ལྟར་
[^49]: བསྒོམ་ལམ་ ༼སྣར། པེ།༽ སྒོམ་ལམ་
[^50]: དེ་དག་ ༼སྣར། པེ།༽ དེ་ཉིད་
[^51]: ཉིད་ཀྱི་ ༼སྣར། པེ།༽ ཉིད་
[^52]: དང་། ༼སྣར། པེ།༽ སྟེ།
[^53]: དེ་ནི་ ༼སྣར། པེ།༽ ད་ནི་
[^54]: སྐབས་ ༼སྣར། པེ།༽ སྐབས་སུ་
--- END BLOCKS ---

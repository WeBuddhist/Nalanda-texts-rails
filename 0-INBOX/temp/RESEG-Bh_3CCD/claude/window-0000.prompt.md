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
## ༄༅། །སྒྲོན་མ་གསལ་བར་བྱེད་པའི་དགོངས་པ་རབ་གསལ་ཞེས་བྱ་བ་བཤད་པའི་ཊཱི་ཀཱ།སྟོད་ཆ།

[Block 2 [HEADING]]
## ཀླད་ཀྱི་དོན། ^I-0

[Block 3]
༄༅༅། །རྒྱ་གར་སྐད་དུ། པྲ་དཱི་པ་ཨུ་དྱོ་ཏ་ན་ཨ་ནོ་སནྡྷི་པྲ་ཀཱ་ཤི་ཀཱ་ནཱ་མ་བྱཱ་ཁྱཱ་ཊཱི་ཀཱ། བོད་སྐད་དུ། སྒྲོན་མ༌[^1]གསལ་བར་བྱེད་པའི་དགོངས་པ་རབ་གསལ་ཞེས་བྱ་བ་བཤད་པའི་ཊཱི་ཀཱ། རྡོ་རྗེ་འཆང་ལ་ཕྱག་འཚལ་ལོ། །

[Block 4]
དཔལ་ལྡན་རྟོག་པའི་དྲ་བ་དུ་མ་སྣ་ཚོགས་མུན་པའི་ཚོགས་ནི་འཇོམས་བྱེད་ཉི་མ་ནི། །གང་ཞིག་ཡོད་དང་མེད་པ་ཉིད་ཀྱང་ཡོངས་སུ་སྤོང་བ་ལ་བརྩོན་ངོ་བོ་ཉིད་མེད་སྐུ། །ཤིན་ཏུ་རྗེས་ཆགས་ཡིད་ཅན་ལྷ་མོ་རེག་བྱ་རྡོ་རྗེ་མ་ལ་ཡང་དག་པར་འཁྱུད་པ། །དཀྱིལ་འཁོར་པ་རྣམས་དག་གིས་ཡོངས་བསྐོར་དཔེ་མེད་རྡོ་རྗེ་སེམས་དཔའ་དེ་ལ་བདག་གིས་འདུད། །འཁོར་བའི་དགོན་པར་རྟོག་པའི་དྲ་བ་དུ་མས་རྣམ་པར་འཁོར་བ་ནི། །རྐུན་པོ་དང་འདྲ་གང་གིས་ཤིན་ཏུ་དཀའ་བའི་གནས་སུ་འཇིག་རྟེན་ཁྱེར། །གང་ཡོད་པས་ནི་སྲིད་པ་པ་རྣམས་སྐྱེ་ཡིན་ཁམས་ཚོགས་དེ་དག་ནི། །ཡང་དག་སྦྱངས་ཏེ་གསལ་བྱེད་རིགས་བདག་བཙུན་མོ་སྤྱན་སོགས་བདག་གིས་འདུད། །དྲི་མ་དང་བཅས་གཟུགས་སོགས་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་རྣམས་དག༌[^2]བྱས་ནས། །ནམ་མཁའི་དཀྱིལ་མཚུངས་ཤེལ་ལྟར་དངས་ཤིང༌[^3]ཡེ་ཤེས་ལྔ་པོ་རོ་གཅིག་རབ་བསྐྱེད་པ། །ཐབས་དང་ཤེས་རབ་བདག་ཉིད་སྐུ་ཡིས་སྐྱེ་དགུ༌[^4]ཕན་འདོགས་བརྩོན་འགྲུས་བདག་ཉིད་ཅན། །རང་བཞིན་གྱིས་གྲུབ་རྟག་པ་ལ་སོགས་རྒྱལ་བའི་ཚོགས་རྣམས་མཆོག་གྱུར་དེ་ལ་བདག་ཕྱག་འཚལ། །

[Block 5 [VERSE]]
གང་གིས་དབང་པོ་རྣམས་ནི་ངེས་པར་ཉམས་བྱས་པ། །
ཆུ་སྐྱེས་དྲི་ཡི་ཚོགས་ཀྱིས་བུང་བའི་ཚོགས་རྣམས་བཞིན། །
དེ་དག་གང་གིས་རབ་ཏུ་ཞི་བར་བྱེད་པ་ནི། །
གཟུགས་ཀྱི་རྡོ་རྗེ་མ་སོགས་དེ་ལ་བདག་ཕྱག་འཚལ། །

[Block 6 [VERSE]]
གཟུགས་སོགས་སྤྱོད་ཡུལ་ཚོགས་ནི་རབ་ཉམས་རྒྱུ་ཡི་ཕྱིར། །
སྐད་ཅིག་བདེ་བའི་སྲེད་པས་གཟུང་བར་བྱེད་པ་གང་། །
དབང་པོ་དེ་རྣམས་གང་གིས་རྒྱལ་བ་ཉིད་བྱེད་པ། །
ས་སྙིང་ལ་སོགས་དེ་ལ་སྤྱི་བོས་བདག་རྟག་འདུད། །

[Block 7 [VERSE]]
འགྲོ་བ་མ་ལུས་གཟིར་བྱེད་འཇིག་རྟེན་སྐྱོང་བ་རྣམས། །
ཤིན་ཏུ་ཟིལ་གྱིས་མནན་ཅིང་ཐེག་མཆོག་འཇུག་བྱེད་པ། །
སྦྲུལ་བདག་ཚོགས་ཀྱིས་ཡན་ལག་བརྒྱན་ཅིང་ཁྲོ་བཅས་པ། །
གཤིན་རྗེ་གཤེད་སོགས་ཁྲོ་རྒྱལ་རྣམས་ལ་ཕྱག་འཚལ་ལོ། །

[Block 8 [VERSE]]
ཀོང་ཀ་ན་ཡི་གྲོང་ཁྱེར་དུ། །
དཔལ་གྱི་རི་ཡི་རྩེ་མོར་ནི། །
སྐྱེ་བོས་དབེན་པའི་གནས་ཉིད་དུ། །
དང་པོར་དེ་ལ་གནས་བྱས་ན།[^5] །

[Block 9 [VERSE]]
མི་དང་ལྷ་ཡི་བདག་པོར་མཚུངས། །
མཆོག་ཏུ་གྱུར་པའི་ཆོས་གསུངས་པ།[^6] །
སྒྲ་གཅན་འཛིན་གྱི་ཞལ་སྔ་ནས། །
ས་སྟེང་འདི་ལ་རྒྱལ་གྱུར་ཅིག །

[Block 10 [VERSE]]
མཉེས་པ་དེ་ལས་དེ་ཉིད་ནི། །
ཐེག་ཆེན་རྣལ་འབྱོར་པས་ཐོབ་པ། །
ས་ཐོབ་གཞན་གྱི་དོན་ལ་བརྩོན། །
དཔལ་ལྡན་ཀླུ་སྒྲུབ་རྒྱལ་གྱུར་ཅིག །

[Block 11 [VERSE]]
དེ་ལས་དེ་ཉིད་རིན་ཆེན་ནི། །
ཐོབ་པ་འཇིག་རྟེན་གསུམ་དུ་གྲགས། །
འདུས་པ་རྒྱ་མཚོའི་ཕ་རོལ་ཕྱིན། །
ཟླ་གྲགས་གསལ་བྱེད་རྒྱལ་གྱུར་ཅིག །

[Block 12 [VERSE]]
དེ་ཡིས་བྱས་པའི་འགྲེལ་པ་ནི། །
མཐའ་དྲུག་བཤད་པས་ཟབ་པ་ཉིད། །
དེ་ནི་དེང་བདག་མ་ལུས་པར། །
སྐལ་ལྡན་གྲགས་པས་གསལ་བཤད་བྱ། །

[Block 13 [HEADING]]
## ལེའུ་དང་པོ། ^1-0

[Block 14]
སྔགས་ཀྱི་ཐེག་པ་ཆེན་པོ་འདི་ལ་ནི་ནཻ་རཉྫ་ནའི་ཆུ་བོའི་འགྲམ་དུ་རྒྱལ་བུ་དོན་ཐམས་ཅད་གྲུབ་པ་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱིས་བསྐུལ་བས་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཐོབ་པའི༌[^7]དགའ་ལྡན་གྱི་གནས་སུ་གཤེགས་པ་བཞིན་དུ་རྒྱུད་ལ་སོགས་པའི་རིགས་པ་བཞི་ལ༌[^8]བརྟེན་ཏེ། སྙིགས་མ་རྣམ་པ་ལྔས་རྙོག་པར་བྱས་པའི་སེམས་ཀྱི་རྒྱུད་དང་ལྡན་པའི་མ་འོངས་པའི་སེམས་ཅན་གྱི་ཁམས་རྗེས་སུ་གཟུང་བར་བྱ་བའི་ཕྱིར་རིན་པོ་ཆེ་སྣ་ཚོགས་པའི་རང་བཞིན་ཆོས་ཀྱི་འབྱུང་གནས་ཀྱི་གཞི་ཅན་གཞལ་ཡས་ཁང་པ་ལ་བཞུགས་ཏེ། དཀྱིལ་འཁོར་པ་རྣམས་སྤྲོ་ཞིང་དེ་བཞིན་གཤེགས་པ་ལྔས་གསོལ་བ་གདབ་པའི་དཔལ་རྡོ་རྗེ་འཆང་ཆེན་པོས་བསམ་པ་དང་བག་ལ་ཉལ་དང་ཁམས་དང་བག་ཆགས་ཀྱི་དབྱེ་བ་ལས་སྔགས་ཀྱི་བསྟན་བཅོས་རྣམ་པ་ལྔ་རུ་གསུངས་ཏེ། བྱ་བ་དང་། སྤྱོད་པ་དང་། [^9]རྣལ་འབྱོར་དང་། རྣལ་འབྱོར༌[^10]གྱི་བླ་མ་དང་། རྣལ་འབྱོར་མའི་རྒྱུད་ཀྱི་དབྱེ་བས་སོ། །

[Block 15]
དེ་ལ་དཀྱིལ་འཁོར་དང་བསྐོར་བ༌[^11]དང་སྦྱིན་སྲེག་དང་རབ་ཏུ་གནས་པ་དང་དུས་གསུམ་དུ་ཁྲུས་དང་གོས་དུས་གསུམ་དུ་བརྗེ་བ་དང་བསྙུང་བར་གནས་པ་ལ་སོགས་པ་རྗོད་པར་བྱེད་པའི་རྒྱུད་ནི་བྱ་བའི་རྒྱུད་དེ་སྒྲོལ་མ་བྱུང་བ་ལ་སོགས་པའོ། །

[Block 16]
བརྟུལ་ཞུགས་དང་དངོས་གྲུབ་དང་རྫུ་འཕྲུལ་གཙོར་གྱུར་པ་ལ་སོགས་པ་སྤྱོད་པའི་རྒྱུད་དེ་དཔལ་མཆོག་དང་པོ་དང་རྣམ་པར་སྣང་མཛད་མངོན་པར་བྱང་ཆུབ་པའི་རྒྱུད་རྣམས་སོ། །

[Block 17]
ཕྱག་རྒྱ་བཞི༌[^12]དང་དཀྱིལ་འཁོར་དང་ཏིང་འཛིན༌[^13]གཙོར་གྱུར་པའི་རྣལ་འབྱོར་གྱི་རྒྱུད་ནི་དཔལ་དེ་ཁོ་ན་ཉིད་བསྡུས་པ་ལ་སོགས་པའོ། །

[Block 18]
བསྐྱེད་པ་དང་རྫོགས་པ་ལ་སོགས་པ་སོ་སོར་བསྟན་པའི༌[^14]རྒྱུད་ནི་རྣལ་འབྱོར་གྱི་བླ་མ་སྟེ་དཔལ་གསང་བ་འདུས་པ་ལ་སོགས་པའོ། །

[Block 19]
རིམ་པ་གཉིས་པོ་དེ་ཡང་སྤྲོས་པ་མེད་པར་གང་དུ་ཁྱད་པར་དུ་བསྟན་པ་དེ་དག་ནི་དཔལ་དགྱེས་པའི་རྡོ་རྗེ་ལ་སོགས་པ་རྣལ་འབྱོར་མའི་རྒྱུད་དོ། །

[Block 20]
དེ་ལ་རབ་དང་འབྲིང་གི་གཏི་མུག་གི་རིགས་ཅན་ལ་དགོངས་ཏེ་བྱ་བའི་རྒྱུད་བསྟན་ཏོ། །

[Block 21]
གཏི་མུག་དམན་པའི་རིགས་ཅན་རྣམས་ལ་སྤྱོད་པའི་རྒྱུད་བསྟན་ཏོ། །

[Block 22]
དམན་པ་དང་བར་པའི༌[^15]འདོད་ཆགས་དང་ཞེ་སྡང་དང་གཏི་མུག་གི་རིགས་ཅན་རྣམས་ལ་རྣལ་འབྱོར་གྱི་རྒྱུད་བསྟན་ཏོ། །

[Block 23]
འདོད་ཆགས་དང་ཞེ་སྡང་དང་གཏི་མུག་རབ་ཀྱི་རིགས་ཅན་རྣམས་ལ་རྣལ་འབྱོར་གྱི་བླ་མའི་རྒྱུད་དོ། །

[Block 24]
རབ་ཀྱི་རབ་ཀྱི་འདོད་ཆགས་དང་ཞེ་སྡང་དང་གཏི་མུག་གི་རིགས་ཅན་རྣམས་ལ་རྣལ་འབྱོར་མའི་རྒྱུད་བསྟན་ཏོ་ཞེས་རྒྱུད་ཀྱི་དབྱེ་བ་དང་ཡུལ་གྱི་བྱེ་བྲག་བསྟན་ཏོ། །

[Block 25]
ཡུལ་གྱི་དབྱེ་བ་དེ་ལ་ནི་ཙནྡན་དང་ཨུཏྤ་ལ་དང་པདྨ་དཀར་པོ་དང་། པདྨ་དམར་པོ་དང་། རིན་པོ་ཆེ་སྟེ་གང་ཟག་རྣམ་པ་ལྔ་ཡོད་དེ། དེ་ལ་ཙནྡན་ནི་བླུན་པོའི་རིགས་ཅན་ནོ། །

[Block 26]
ཨུཏྤ་ལ་ནི་དབང་པོ་དམན་པའོ། །

[Block 27]
པདྨ་དཀར་པོ་ནི་དབང་པོ་བར་པའོ། །

[Block 28]
པདྨ་དམར་པོ་ནི་དབང་པོ་རྣོ་བའོ། །

[Block 29]
རིན་པོ་ཆེ་ནི་དབང་པོ་རབ་ཀྱི་རབ་བོ། །

[Block 30]
བག་ཆགས་ཀྱི་བྱེ་བྲག་གིས་གང་ཟག་རྣམས་ལ་རིགས་ཀྱི་བྱེ་བྲག་བསྟན་ཏོ། །

[Block 31]
དེ་ཡང་གདོད་མ་ནས་ཆགས་པ་ཡིན་ཏེ་དེ༌[^16]དངུལ་ལ་སོགས་པའི་རིགས་བཞིན་ནོ། །

[Block 32]
དེའི་ཕྱིར་གང་ཟག་གི་དབྱེ་བ་ལ་དགོངས་ཏེ་བཅོམ་ལྡན་འདས་ཀྱིས་རྒྱུད་ཐམས་ཅད་ཀྱི་ངོ་བོ་རྣལ་འབྱོར་གྱི་རྒྱུད་ཆེན་པོ་འདི་གང་ཟག་ཐམས་ཅད་གདུལ་བར་བྱ་བའི་ཕྱིར་གསུངས་པ། དེའི་འགྲེལ་པ་སློབ་དཔོན་ཟླ་བ་གྲགས་པས་བསྐྱེད་པ་དང་རྫོགས་པའི་རིམ་པ་གཉིས་ལ་བརྟེན་ཏེ་སྒྲོལ་མ་གསལ་བར་བྱེད་པ་བརྩམས་སོ། །

[Block 33]
ཇི་སྐད་དུ་རྒྱུད་ཕྱི་མ་ལས།

[Block 34 [VERSE]]
བསྐྱེད་པ་ཡི་ནི་རིམ་པ་དང་། །
རྫོགས་པའི་རིམ་པ་ཉིད༌[^17]དང་ནི། །
རིམ་པ་གཉིས་ལ་བརྟེན་བྱས་ནས། །
རྡོ་རྗེ་ཅན་གྱིས་ཆོས་གསུངས་སོ། །

[Block 35]
དེ་ལ་བསྐྱེད་པའི་རིམ་པ་རྣམ་པ་གསུམ་སྟེ། དང་པོའི་སྦྱོར་བ་དང་། དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་དང་། ལས་རྒྱལ་བ་མཆོག་གོ། །

[Block 36]
རྫོགས་པའི་རིམ་པ་ནི་རྣམ་པ་ལྔ་སྟེ། རྡོ་རྗེ་བཟླས་པའི་རིམ་པ་དང་། སེམས་ལ་དམིགས་པ་ཐོབ་པའི་རིམ་པ་དང་། བདག་ལ་བྱིན་གྱིས་བརླབ༌[^18]པའི་རིམ་པ་དང་། མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པ་དང་། ཟུང་དུ་འཇུག་པའོ། །

[Block 37]
དེ་ལ་དང་པོའི་སྦྱོར་བ་ལ་རྣམ་པ་བཞི་སྟེ། རྣལ་འབྱོར་དང་། རྗེས་སུ་རྣལ་འབྱོར་དང་། ཤིན་ཏུ་རྣལ་འབྱོར་དང་། རྣལ་འབྱོར་ཆེན་པོའོ། །

[Block 38]
རྣལ་འབྱོར་ལ་ནི་རྣམ་པ་བཅུ་སྟེ་སྙིང་རྗེ་ཆེན་པོ་མངོན་དུ་བྱ་བ་སྔོན་དུ་འགྲོ་བ་ཁྱད་པར་གྱི་གནས་ལ་བརྟེན་པ་དང་། བགེགས་བསྐྲད་པའི་བདག་ཉིད་ཅན་གནས་བསྲུང་བ་དང་། སྟོང་པ་ཉིད་ཀྱི་སྒོམ་པས་བདག་ཉིད་བསྲུང་བ་དང་། ཡེ་ཤེས་ཀྱི་ས་གཞི་བསྒོམ་པ་དང་། གཞལ་ཡས་ཁང་དང་། དེའི་ནང་དུ་པདྨ་དང་ཟླ་བ་དང་ཉི་མའི་གདན་ལ་གནས་པ་ལྷག་པར་མོས་པའི་དཀྱིལ་འཁོར་བསྒོམ་པ་དང་། དོན་དམ་པའི་དཀྱིལ་འཁོར་བསྒོམ་པ་དང་། གཞལ་ཡས་ཁང་གི་ནང་དུ་གདན་དགོད་པ་དང་། ཆོས་ཀྱི་དབྱིངས་ཀྱི་དེ་ཁོ་ན་ཉིད་བསྒོམ་པ་དང་། ཡི་གེ་གསུམ་ལས་སྐྱེས་པའི་དབུས་ཀྱི་གཙོ་བོ་བསྒོམ་པའོ། །

[Block 39]
རྗེས་སུ་རྣལ་འབྱོར་ནི་ཡེ་ཤེས་སེམས་དཔའི་དང་ཏིང་ངེ་འཛིན་སེམས་དཔའ་བསྒོམ་པའོ། །

[Block 40]
ཕུང་པོ་ཁམས་དང་སྐྱེ་མཆེད་བྱིན་གྱིས་རློབ་པ་ནི་ཤིན་ཏུ་རྣལ་འབྱོར་རོ། །
--- END BLOCKS ---

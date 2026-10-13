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
རི་ལ་སོགས་པ་ལ་ནི་ཡུལ་དང་དབང་པོ་བར་མེད་པ་སྟེ་བར་དང་བཅས་པ་ཡིན་བཞིན་དུ་འཛིན་པ་མཐོང་མོད༌[^86]ཀྱི། དབང་པོ་ལྷག་པར་འཛིན་པ་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 142]
ཕྱི་རོལ་དུ་འཇུག་པའི་ཕྱིར་འཐད་པ་ཉིད་དོ། །

[Block 143]
དབང་པོ་གཉིས་ཀྱི༌[^87]རྟེན་ལས་ཕྱི་རོལ་དུ་འཇུག་པ་སྟེ། དེས་ན་ཡུལ་དེ༌[^88]བར་དང་བཅས་པ་ལྷག་པར་འཛིན་པ༌[^89]ཡང་འཐད་པ་ཡིན་ནོ་ཞེ་ན། དེ་ཡང་རིགས་པ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར། རྟེན་ལས་དབང་པོ་ཕྱིར་མིན་པར། །གྲུབ་པོ་ཞེས་བྱ་བ་ཚིག་གི་ལྷག་མའོ། །

[Block 144]
དབང་པོ་ནི་རྟེན༌[^90]གྱི་ཡུལ་ཉིད་ལ་གནས་པ་སྟེ། དེར་གསོ་བ་ལ་སོགས་པ་ལ་རབ་ཏུ་སྦྱོར་བའི་ཕྱིར་རོ། །

[Block 145]
དེས་ན་དབང་པོ་ཁོ་ན་བར་དུ་ཆོད་པའི་དོན་འཛིན་པར་བྱེད་དོ། །

[Block 146]
དབང་པོ་ཕྱི་རོལ་དུ་འཕོ་བ་བདེན་དུ་ཆུག་ན་ཡང་། ཡུལ་ལ་འཛིན་པར་ནུས་མ་ཡིན། །གཞན་དུ་ན་བརྟེན་པ༌[^91]བསྒྲིབས་ཀྱང་ཡུལ་འཛིན་པར་འགྱུར་རོ། །

[Block 147]
དེའི་ཕྱིར་མིག་དང་རྣ་བ་དག་གིས་ནང༌[^92]རྟེན་གྱི་གནས་ཁོ་ན་འཐོབ་སྟེ། ཡུལ་གྱི་སྐད་ཅིག་མ་དག་ལས་བར་དང་བཅས་པ་དང་ལྷག་པར་འཛིན་པར་ཡང༌[^93]རིགས་པ་མིན་ནོ། །

[Block 148]
བདེ་སོགས་གཞལ་བྱ་མིན་པའམ། །འམ་ཞེས་སྨོས་པ་ནི་འམ་གྱི་སྒྲ་ལས་ཚད་མ༌[^94]གཞན་འཐོབ་པར་འགྱུར་བའོ། །

[Block 149]
གང་འདི་ལྟར་རྟགས་པ་སོགས༌[^95]པ་མེད་པར༌[^96]བདག་ཉིད་ཀྱི་བདེ་བ་དང་སྡུག་བསྔལ་དང་འདོད་པ་དང་། ཞེ་སྡང་དང་འབད་རྩོལ་རྣམས་ལ་འཛིན་པ་དེ་ཚད་མ་མ་ཡིན་པས་བདེ་བ་ལ་སོགས་པ་རྣམས་གཞལ་བྱ་ཉིད་དུ་མི་འགྱུར་བའམ། དེར་འམ༌[^97]ཞེས་སྨོས་པས་ཚད་མ་གཞན་ཉིད་མཚོན་པར་འགྱུར་བའོ། །

[Block 150]
དབང་པོ་གཞན་ཡོད་ཡིད་དབང་པོ། །ཡང་ན་ཡིད་ཁོ་ན་དབང་པོ་ཉིད་དུ་བརྗོད་པར་བྱ་སྟེ། དེ་དང་ཕྲད་པ་ལས་སྐྱེས་པ་མངོན་སུམ་ཉིད་དུ་བསྒྲུབ་པར་བྱ་བའི་དོན་དུའོ། །

[Block 151]
བཀག་པ་མེད་ཕྱིར་འཐོབ་ཅེ་ན། ཅི་སྟེ་ཡང་གཞན་གྱི་འདོད་པ་མ་བཀག་པ་རུ་སྒྲུབ་པ་ལ་ཡིད་ཀྱི་དབང་པོ་ཉིད་བཀག་པ་མེད་པའི་ཕྱིར་འཐོབ་པ་ཉིད་དོ་ཞེ་ན། གཞན་གྱི་འདོད་པ་ལ་ནི་ཡིད་ཀྱི་དབང་པོ་ཡོད་ལ་རག་ན་དེ་ལྟ་ན་ནི། དབང་པོ་གཞན་གྱི་སྒྲ་དོན་མེད། །གལ་ཏེ་གཞན་གྱིས་སྨྲས་པའི་ཡིད་ལ་བཀག་པ་མེད་པའི་ཕྱིར་དབང་པོ་ཡིན་ན་དེས་རྣ་བ་ལ་སོགས་དབང་པོར་བརྗོད་དོ་ཞེས་བསྟན་པ་དོན་མེད་པར་འགྱུར་ཏེ། བཀག་པ་མེད་པ༌[^98]ཉིད་ལས་དེ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 152 [VERSE]]
དོན་དེས་འབྲས་བུ་ཡོད་མིན་པས། །
ཤེས་པའི་ཡང་ནི་ཚད་ཉིད་ལས། །
དོན་གཞན་འབྲས་བུ་སྨྲ་བར་འགྱུར། །

[Block 153]
ངེས་པའི་བདག་ཉིད་ཅན་གྱི་ཤེས་པ་ནི་ཚད་མ་སྟེ། ཚད་མ་དེ་སྐྱེས་ཀྱི་རྗེས་ལ་དོན་ལྷག་ཏུ་རྟོགས་སོ་ཞེས་བྱ་བ་ནི་འབྲས་བུ་མེད་པར་འགྱུར་རོ། །

[Block 154]
གལ་ཏེ་ཁྱད་པར་དུ་བྱེད་པའི་ཤེས་པ་ཚད་མ་ཡིན་ཏེ། གང་སྤྱི་ལ་སོགས་པ་ཁྱད་པར་དུ་བྱེད་པའི་ཤེས་པ་དེ་ནི་ཚད་མ་ཡིན་ལ། གང་རྫས་ལ་སོགས་པ་ཁྱད་པར་དུ་བྱ་བའི་ཤེས་པ་དེ་ནི་འབྲས་བུ་ཡིན་ནོ་ཞེ་ན། དེ་ཡི༌[^99]ཁྱད་པར་ལ་མིན་ཐ་དད་ཕྱིར། །ཐ་དད་པ་ནི་ཁྱད་པར་དུ་བྱེད་པ་ཁྱད་པར་དུ་བྱ་བ༌[^100]ཐ་དད་པ་ཡིན་ལ་ཡུལ་གཞན་ལ་ཚད་མར་འགྱུར་ཞིང་གཞན་ལ་འབྲས་བུར་འགྱུར་བ་ཡང་རིགས་པ་མ་ཡིན་ཏེ། དཔེར་ན་སེང་ལྡེང་གི་ཡུལ༌[^101]བཅད་ཅིང་གཤགས་པས༌[^102]པ་ལ་ཤ་ཆོད་པ༌[^103]ནི་མ་མཐོང་ངོ་། །ཇི་སྟེ་ཁྱད་པར་དུ༌[^104]བྱ་བའི་ཤེས་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་དེའི་ཡུལ་ཉིད་ཀྱང་ཡིན་ནོ་ཞེ་ན་མ་ཡིན་ཏེ། ཧ་ཅང་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 155]
དེ་ལྟ་ན་ནི་བྱེད་པ་པོ་ཐམས་ཅད་གཅིག་ཏུ་འགྱུར་ཏེ། ཁྱད་པར་དུ་བྱ་བའི་ཤེས་པའི་རྒྱུ་ཡིན་པ་ཉིད་ཀྱིས་དེའི་བྱེད་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 156]
དེའི་ཕྱིར་གང་ལ་ལས་ཀྱི་བྱ་བ་ཡོད་པར་བརྗོད་པ་དེ་ཉིད་དེའི་འབྲས་བུ་ཉིད་དུ་རིགས་སོ། །

[Block 157]
གཞན་ཡང་དེ་ལ་ཡོད་མིན། དེ་ལ་ཡང༌[^105]ཁྱད་པར་དུ་བྱེད་པ་ལྷག་པར་རྟོགས་པ་མེད་པའི་འབྲས་བུ་ཡང་མེད་ལ་ཚད་མ་ཡང་མེད་དོ། །

[Block 158]
གཉིས་ཤེ་ན། ཅི་སྟེ་ཡང་ཁྱད་པར་དུ་བྱེད་པའི་ཤེས་པ་ཉིད་ཚད་མ་དང་གཞལ་བྱ་གཉིས་ཀར་ཡང་འགྱུར་ཏེ། དཔེར་ན་བདག༌[^106]གིས་བདག་ཁོང་དུ་ཆུད་པར་བྱེད་ཙམ་ན། གཞལ་བར་བྱ་བར༌[^107]ཡང་འགྱུར་ཞིང་འཛིན་པ་པོ་ཡང་ཡིན་པ་བཞིན་ནོ་ཞེ་ན། མ་ཡིན་ཁྱད་པར་བྱ་ལའང༌[^108]འགྱུར། །དེ་ལྟ་ན་ནི་ཁྱད་པར་དུ་བྱ་བའི་ཤེས་པ་ལའང་ཚད་མ་དང་གཞལ་བྱ་གཉིས་ཀ་ཐོབ༌[^109]པར་འགྱུར་རོ། །

[Block 159]
གལ་ཏེ་ཤེས་པ་དང་ཤེས་བྱ་དོན་གཞན་ཡིན་ཡང་ཚད་མ་དང་གཞལ་བྱ་ཉིད་དུ་འགྱུར་བ་སྟེ། རང་གིས་བདག་ཁོང་དུ་ཆུད་པའི་ཤེས་པ་བཞིན་ནོ་ཞེས་པ་དེ་ཉིད་དངོས་པོ་གཉིས་ཀ་ལ་ཡང་འགྱུར་བ་ཡིན་ནོ། །

[Block 160]
ཁྱད་པར་དུ་བྱེད་པའི་ཤེས་པ་བདག་དང་མཚུངས་སོ་ཞེས་པ་ནི་མ་ཡིན་གྱིས༌[^110]གཉིས་ཀ་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 161]
དེ་ལྟ་ན་ནི་ཤེས་བྱ་ཁོང་དུ་ཆུད་ཀྱང་གང༌[^111]མ་རྟོགས་པ་དང་ཐེ་ཚོམ་ཟ་བ་དང་ལོག་པར་རྟོགས་པ༌[^112]ལས་ལོག་པ་དེ་འབྲས་བུར་འགྱུར་ན། དེ་ཡང་མི་རིགས་ཏེ། གང་གི༌[^113]ཕྱིར། མ་རྟོགས་ལ་སོགས་ཀུན་ལ་མིན། །རེ་ཞིག་ཐམས་ཅད་དུ་མ་རྟོགས་པ་ལ་སོགས་པ་ལས་འབྱུང་བའི་ངེས་པ་དེ་དག་ནི་ཡོད་པ་མ་ཡིན་ཏེ། ཁ་ཅིག་ཏུ་བཟས་པ༌[^114]ཙམ་གྱིས་ཤེས་པ་སྐྱེ་བས༌[^115]སོ། །

[Block 162]
མ་རྟོགས་པ་ལ་སོགས་པ་ཡོད་དུ་ཆུག་ན་ཡང་། ལོག་པ་འབྲས་བུར་ཡོད་མ་ཡིན། །ལོག་པ་ཞེས་བྱ་བ་ནི༌[^116]མ་རྟོགས་པ་ལ་སོགས་པ་མེད་པ་ལ་བྱ་ན། ཡོད་པ་མ་ཡིན་པ་དེ་ནི་འབྲས་བུ་མ་ཡིན་ཏེ། དེ་གཞལ་བྱར་འགྱུར་བ་ནི་མི་དཔྱོད་པའི་ཕྱིར་རོ། །

[Block 163]
དེ་ལྟར་ན་རེ་ཞིག་རིགས་པ་ཅན་རྣམས་ཀྱི་མངོན་སུམ་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 164 [HEADING]]
#### བྱེ་བྲག་པའི་མངོན་སུམ། ^1-4-3-0

[Block 165]
བྱེ་བྲག་པ་རྣམས་ཀྱི་མདོ་ལས་རེ་ཞིག་གང་འབྲེལ་པ་འབའ་ཞིག་ལས་གྲུབ་པ་དེ་རྫས་ལ་མངོན་སུམ་མོ་ཞེས་སོ། །

[Block 166]
བདག་དང་དབང་པོ༌[^117]དོན་དུ་ཕྲད་པ་ལས་གང་གྲུབ་པ་དེ་གཞན་ཡིན༌[^118]ནོ་ཞེས་སོ། །

[Block 167]
ཁ་ཅིག་ནི་ཚད་མ་ལས་དོན་གཞན་དུ་འདོད་དེ། ཐུན་མོང་མ་ཡིན་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་དབང་པོ་དང་དོན་དུ་ཕྲད་པ་ཚད་མར་རྟོག་པར་བྱེད་དོ། །

[Block 168]
གཞན་དག་ནི་གཙོ་བོ་ཡིན་པའི་ཕྱིར་བདག་དང་ཡིད་དུ་ཕྲད་པ་ཚད་མའོ་ཞེས་ཟེར་རོ། །

[Block 169]
དེ་ལྟར་ན་ནི་གང་འདི་སྐད་ཐེ་ཚོམ་དང་གཏན་ལ་འབེབས་པའི་ཤེས་པ་དག་ལས་གྲུབ་པ་ནི་མངོན་སུམ་དང་རྟགས་ཅན་གྱི་ཤེས་པ་དག་གོ་ཞེས་བཤད་པ་དང་འགལ་ལོ། །

[Block 170]
བཞི་པོ་ཕྲད་པ་ལས་སྐྱེས་པའི་ཤེས་པ་དང་། གཏན་ལ་འབེབས་པ་ལས་སྐྱེས་པ་མཚུངས་པ་མ་ཡིན་ཏེ། གཏན་ལ་འབེབས་པ་ནི་བརྟག་པ་སྔོན་དུ་འགྲོ་བ་ཡིན་པའི་ཕྱིར་ལ། མངོན་སུམ་ནི་ཡུལ༌[^119]ལྟ་བ་ཙམ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 171]
ཡུལ་ལ་ལྟ་བ་ཙམ་ཞེས་པ་པ༌[^120]ནི་བཞི་པོ་ཕྲད་པ་ལས་སྐྱེས་པ་སྟེ། དེ་ལ་བརྟག་ཅིང་དཔྱོད་པ་གང་ལ་སྲིད། །དབང་པོ་དང་དོན་དུ་ཕྲད་པ་ཚད་མར་སྨྲ་བས་ནི་ལྷག་པར་བསྟན་ལ༌[^121]ཅི་ཡང་མེད་པ་ཉིད་དོ། །

[Block 172]
དབང་པོ་དང་དོན་དུ་ཕྲད་པ་ཚད་མར་སྨྲ་བའི་ལྟར་ན་ནི་འདི་ཅི་ཞིག་ཅེས་ཤེས་པར་འདོད་པའི་ཚེ་དོན་མཐའ་དག་འཛིན་པར་འགྱུར་ཏེ། ཐམས་ཅད་ཀྱི་བདག་ཉིད་དང་ཕྲད་པའི་ཕྱིར་རོ། །

[Block 173]
བདག་དང་ཡིད་དུ་ཕྲད་པར་སྨྲ་བ་ལ་ཡང༌[^122]ཡུལ་ཐ་དད་ལ་ཡུལ་གཞན་ལ་ཚད་མར་འགྱུར་ཞིང་གཞན་ལ་འབྲས་བུར་འགྱུར་བ་ནི་མེད་དོ་ཞེས་སྔར་སྨྲས་ཟིན་ཏོ། །

[Block 174]
གཞན་ཡང་སྤྱིའི་ཁྱད་པར་ལ་ལྟོས་པ་དང་རྫས་དང་ཡོན་ཏན་དང་ལས་ལ་ལྟོས་པ་མངོན་སུམ་ཞེས་ནི་སྦྱར་བར་མི་བྱ་སྟེ། གང་གི་ཕྱིར་དབང་པོ་དང་ཡུལ་དུ་ཕྲད་པ་ལས་སྐྱེས་པ་ནི།

[Block 175 [VERSE]]
ཡུལ་ལ་ལྟ་བའི་དོན་ཅན་ཕྱིར། །
ཁྱད་པར་རྣམས་དང་སྦྱར་མི་བྱ། །

[Block 176]
དབང་པོའི་བློ་རྣམས་ནི་རང་གི་དོན་ཙམ་འཛིན་པར་བྱེད་པ་ཡིན་པའི༌[^123]ཕྱིར། །ཁྱད་པར་རྣམས་དང་ལྷན་ཅིག་ཏུ་སྦྱོར་བ་ནི་མི་འཐད་དོ། །

[Block 177]
འདི་ནི་འདིའི་སྤྱི་ཡིན་ཞིང་རྫས་ལ་སོགས་པ་རྣམས་དང་འབྲེལ་པའོ་ཞེས་དང་གི་དོན་གཉིས་ངེས་པར་བཟུང་ནས་དེ་བཞིན་དུ་བརྟག་པར་བྱའོ། །

[Block 178]
དེ་ཡང་དྲན་པ་ལ་སོགས་པ༌[^124]ཡིན་པའི་ཕྱིར་འདི་ལ་ཡིད་ཀྱི་བློས་ཁྱད་པར་དུ་བྱས་ལ༌[^125]འཐད་པ་ཁོ་ན་སྟེ། གཞན་དུ་ན་དྲི༌[^126]མངར་རོ་ཞེས་འཛིན་པ་ཡང་མངོན་སུམ་དུ་འགྱུར་ལ། དེ་ལྟར་འགྱུར་བར་ཡང་མི་རིགས་ཏེ། ཁྱད་པར་དུ་བྱེད་པ་དང་ཁྱད་པར་དུ༌[^127]བྱ་བ་དག་དབང་པོ་ཐ་དད་ཀྱི་ཡུལ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 179]
གལ་ཏེ་ཡང་རྫས་གཅིག་པས༌[^128]དབང་པོ་དུ་མའི་གཟུང་བྱ་ཡིན་ནོ་ཞེ་ན། དེ་ལྟ་ན་ནི་གཅིག་མིན་ཏེ་གཟུགས་ལ་སོགས་པ་བཞིན་དུ་དུ་མར་འགྱུར་རོ། །

[Block 180]
གཟུགས་ལ་སོགས་པ་ལ་ནི་དབང་པོ་དུ་མས་གཟུང་བར་བྱ་བའི་གཅིག་ཉིད་གང་དུ༌[^129]མཐོང་ངོ་། །གཅིག་མིན་གཟུགས་སོགས་ཀྱང་གཅིག་འགྱུར། །གལ་ཏེ་དབང་པོ་དུ་མའི་གཟུང་བྱ་ཡིན་ཀྱང་ཐ་མི་དད་པར་འདོད་ན་ནི་གཟུགས་ལ་སོགས་པ་ཡང་རྫས་བཞིན་གཅིག་ཉིད་དུ་འགྱུར་རོ། །
--- END BLOCKS ---

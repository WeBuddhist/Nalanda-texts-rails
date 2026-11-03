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
[Block 841]
སྡོམ་པ་མ་གཏོགས་པར་ནི་གཅིག་དང་ལྷན་ཅིག་འབྱུང་བ་ཡང་ཡོད་དེ། སེམས་གཞན་དང་ལྡན་པ་སྤོང་བའི་ཡན་ལག་གཅིག་ཡང་དག་པར་ལེན་པ་ནའོ། །

[Block 842]
ལྔ་དང་བརྒྱད་དང་ལྷན་ཅིག་འབྱུང་བ་ཡང་ཡོད་དེ། དགེ་བའི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དང་ལྡན་པ་ཅིག་ཅར་དུ་ཡན་ལག་གཉིས་དང་ལྔ་ཡང་དག་པར་ལེན་པ་ནའོ། །

[Block 843 [HEADING]]
### འགྲོ་བ་གང་ན་ལས་ཀྱི་ལམ་ཡོད་པ། ^1-53-0

[Block 844]
འགྲོ་བ་གང་ན་དགེ་བའམ་མི་དགེ་བའི་ལས་ཀྱི་ལམ་དུ་ཞིག་མངོན་སུམ་དུ་གྱུར་པའམ་ལྡན་པའི་སྒོ་ནས་ཡོད་ཅེ་ན།

[Block 845 [VERSE]]
དམྱལ་བ་ན་ནི་ཀྱལ་པ་དང་། །
ཚིག་རྩུབ་གནོད་སེམས་རྣམ་གཉིས་སོ། །

[Block 846]
དམྱལ་བ་ན་ནི་ལས་ཀྱི་ལམ་འདི་གསུམ་མངོན་སུམ་དུ་གྱུར་པ་དང་ལྡན་པ་དང་རྣམ་པ་གཉི་གའི༌[^634]སྒོ་ནས་ཡོད་དེ། སྨྲེ་སྔགས་འདོན་པའི་ཕྱིར་ཚིག་ཀྱལ་པ་ཡིན་ནོ། །

[Block 847]
ཕན་ཚུན་བརྒྱད་གགས༌[^635]བྱེད་པའི་ཕྱིར་ཚིག་རྩུབ་པོ་ཡིན་ནོ། །

[Block 848]
གཅིག་ལ་གཅིག་སེམས་ཀྱི་རྒྱུད་རྩུབ་པོས་ཞེ་སྡང་བའི་ཕྱིར་གནོད་སེམས་ཡིན་ནོ། །

[Block 849]
བརྣབ་སེམས་ལོག་ལྟ་ལྡན་པས་སོ། །

[Block 850]
ཆགས་པར་བྱ་བའི་དངོས་པོ་མེད་པའི་ཕྱིར་དང་། ལས་ཀྱི་འབྲས་བུ་མངོན་སུམ་དུ་གྱུར་པའི་ཕྱིར་མངོན་སུམ་དུ་གྱུར་པའི་སྒོ་ནས་ནི་མེད་དོ། །

[Block 851]
ལས་ཟད་ནས་འཆི་བའི་ཕྱིར་དང་། རྫས་དང་བུད་མེད་ཡོངས་སུ་གཟུང་བ༌[^636]མེད་པའི་ཕྱིར་སྲོག་གཅོད་པ་དང་། མ་བྱིན་པར་ལེན་པ་དང་། འདོད་པས་ལོག་པར་གཡེམ་པ་དག་མེད་དོ། །

[Block 852]
དགོས་པ་མེད་པའི་ཕྱིར་བརྫུན་དུ་སྨྲ་བ་མེད་དོ། །

[Block 853]
དེ་ཉིད་ཀྱི་ཕྱིར་དང་། རྟག་ཏུ་བྱེད་ཟིན་པའི་ཕྱིར་ཕྲ་མ་མེད་དོ། །

[Block 854]
སྒྲ་མི་སྙན་ན༌[^637]གསུམ་ཡོད་དོ། །

[Block 855]
བརྣབ་སེམས་དང་། གནོད་སེམས་དང་ལོག་པར་ལྟ་བ་དག་སྟེ། ལྡན་པའི་སྒོ་ནས་ཡོད་པར་སྦྱར་གྱི་ང་ཡིར་འཛིན་པ་མེད་པའི་ཕྱིར་དང་། རྒྱུད་འཇམ་པའི་ཕྱིར་དང་། ཀུན་ནས་མནར་སེམས་ཀྱི་དངོས་པོ་མེད་པའི་ཕྱིར་དང་། སྡིག་པ་ཅན་གྱི་བསམ་པ་མ་ཡིན་པའི་ཕྱིར་མངོན༌[^638]དུ་གྱུར་པའི་སྒོ་ནས་ནི་མེད་དོ། །

[Block 856]
དེ་ན་བདུན་པ་དངོས་སུ་ཡང་། །དེ་ན་ཚིག་ཀྱལ་པ་ནི༌[^639]མངོན་སུམ་དུ་གྱུར་པའི་སྒོ་ནས་ཡང༌[^640]ཡོད་དེ། ཉོན་མོངས་པ་ཅན་གྱི་སེམས་སུ་གྱུར་པ་དེ་དག་ནི་རེས་འགའ་གླུ་དག༌[^641]ལེན་ཏོ། །

[Block 857]
སྡིག་པ་ཅན་གྱི་བསམ་པ་མ་ཡིན་པའི་ཕྱིར་དང་། ཚེ་ངེས་པའི་ཕྱིར་དང་། རྫས་དང་བུད་མེད་ཡོངས་སུ་གཟུང་བ་མེད་པའི་ཕྱིར་དང་། དགོས་པ་མེད་པའི་ཕྱིར་སྲོག་གཅོད་པ་ལ་སོགས་པ༌[^642]མེད་དོ། །ཇི་ལྟར་འདི་དག་མི་ཚངས་པར་སྤྱོད་པ་ཡིན་ཞེ་ན། དེ་དག་ནི་བུད་མེད་གང་དག་ལྷན་ཅིག་དགའ་བར་འདོད་པ་དེའི་ལག་ནས་གཟུང་ནས་ཤིང་གི་དྲུང་དུ་འགྲོ་སྟེ། གལ་ཏེ་བགྲོད་པར་བྱ་བ་ཞིག་ཡིན་ན་ནི༌[^643]ཤིང་གིས་སྒྲིབ་པར་བྱེད་པས་དེ་དག་དེ་ལ་ཉལ་པོ་བྱེད་དོ། །

[Block 858]
ཅི་སྟེ་བགྲོད་པར་བྱ་བ་མ་ཡིན་པ་ཞིག་ཡིན་ན་ནི་སྒྲིབ་པར་མི་བྱེད་པས་ནི༌[^644]དེ་དག་དེ་ལ་ཉལ་པོ་མི་བྱེད་དོ། །

[Block 859]
འདོད་པ་གཞན་ན་མི་དགེ་བཅུ། །དངོས་སུ་ཡང་ཡོད་ཅེས་བྱ་བར་སྦྱར་ཏེ། དམྱལ་བ་དང་བྱང་གི་སྒྲ་མི་སྙན་དག་ལས་གཞན་པའི་འདོད་པའི་ཁམས་ན་ནི་མི་དགེ་བའི་ལས་ཀྱི་ལམ་བཅུ་མངོན་སུམ་དུ་འགྱུར་བའི༌[^645]སྒོ་ནས་ཀྱང་ཡོད་དེ། དུད་འགྲོ་དང་ཡི་དགས་དང༌[^646]ལྷ་དག་གི་ནང་ན་ནི་སྡོམ་པ་མ་ཡིན་པ་མ་གཏོགས་སོ། །

[Block 860]
མི་དག་གི་ནང་ན་ནི་སྡོམ་པ་མ་ཡིན་པས་བསྡུས་པ་ཡང་ཡོད་དོ། །

[Block 861]
གལ་ཏེ་ཡང་ལྷས་ལྷ་མི་གསོད་ཀྱང་འགྲོ་བ་གཞན་ན་གནས་ན༌[^647]ནི་གསོད་པར་བྱེད་དོ། །

[Block 862]
གཞན་དག་ན་རེ་ལྷ་ཡང་མགོ་དང་རྐེད་པ་བཅད་ན་འཆིའོ་ཞེས་ཟེར་རོ། །

[Block 863]
མི་དགེ་བ་རྣམས་བཤད་ཟིན་ཏོ། །

[Block 864 [VERSE]]
དགེ་བ་གསུམ་ནི་ཐམས་ཅད་ན། །
རྙེད་དང་མངོན་དུ་གྱུར་སྒོ་ནས། །

[Block 865]
བརྣབ་སེམས་མེད་པ་དང་། གནོད་སེམས་མེད་པ་དང་། ཡང་དག་པའི་ལྟ་བ་རྣམས་ནི་ཁམས་གསུམ་པོ༌[^648]ཐམས་ཅད་ན།[^649] འགྲོ་བ་ལྔ་ཆར་དུ་ནི༌[^650]མངོན་དུ་གྱུར་པ་དང་ལྡན་པའི་སྒོ་ནས་ཡོད་དོ། །

[Block 866]
གཟུགས་མེད་འདུ་ཤེས་མེད་སེམས་ཅན། །རྙེད་པ༌[^651]བདུན་ཡོད། གཟུགས་མེད་པ་དང་འདུ་ཤེས་མེད༌[^652]པའི་སེམས་ཅན་དག་ན་ནི་ལུས་དང་ངག་གི་དགེ་བའི༌[^653]ལས་ཀྱི་ལམ་བདུན་ལྡན་པའི་སྒོ་ཁོ་ན་ནས་ཡོད་དེ། གཟུགས་མེད་པར་སྐྱེས་པའི༌[^654]འཕགས་པ་རྣམས་ལ་ཟག་པ་མེད་པའི་སྡོམ་པ་འདས་པ་དང་མ་འོངས་པ་དག༌[^655]དང་ལྡན་པའི༌[^656]ཕྱིར་དང་། འདུ་ཤེས་མེད་པའི་སེམས་ཅན་རྣམས་ཀྱང་བསམ་གཏན་གྱི་སྡོམ་པ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 867]
གཟུགས་མེད་པ་དག་ན་འཕགས་པས་གང་ལ་བརྟེན་པ་ཅན་གྱི་ཟག་པ་མེད་པའི་ཚུལ་ཁྲིམས་བསྐྱེད་དེ་འགག་པ༌[^657]ནི་འདས་པ༌[^658]དེ་དང་ལྡན་ནོ། །

[Block 868]
ས་ལྔ་ཆར་ལ་བརྟེན་པ་ཅན་དང་མ་འདས༌[^659]པ་དང་ལྡན་ནོ། །

[Block 869]
ལྷག་པར་བྱས་ན་མངོན་དུ་གྱུར་པའི་སྒོ་ནས་ཀྱང་། །དམྱལ་བཅས་སྒྲ་མི་སྙན་མ་གཏོགས། །ལྷག་མར་བྱས་པས་ན་ལྷག་བྱས་ཏེ་ལྷག་མར་བྱས་པས༌[^660]ནི་ཁམས་སམ་འགྲོ་བ་གཞན་གང་ཡིན་པའོ། །

[Block 870]
དམྱལ་བ་དང་བྱང་གི་སྒྲ་མི་སྙན་པ་དག་མ་གཏོགས་པ་དེ༌[^661]ན་ནི་དགེ་བའི་ལས་ཀྱི་ལམ་བདུན་པོ་འདི་དག་མངོན་དུ་གྱུར་པའི་སྒོ་ནས་ཀྱང་ཡོད་དེ། [^662]དེ་དག་ཀྱང་དུད་འགྲོ་དང་ཡི་དགས་ཀྱི་ནང་དག་ན་ནི་སྡོམ་པས་བསྡུས་པ་མ་གཏོགས་པ་རྣམས་སོ། །

[Block 871]
གཟུགས་ཀྱི་ཁམས་ན་ནི་སྡོམ་པས་བསྡུས་པ་རྣམས་སོ། །

[Block 872]
གཞན་ན་ནི་གཉིས་ཀ་ཡོད་དོ། །

[Block 873 [HEADING]]
### བདག་པོ་དང་རྒྱུ་མཐུན་དང་རྣམ་སྨིན་གྱི་འབྲས་བུ། ^1-54-0

[Block 874]
དགེ་བ་དང་མི་དགེ་བའི་ལས་ཀྱི་ལམ་བཅུ་པོ་འདི་དག་ནི།

[Block 875 [VERSE]]
ཐམས་ཅད་བདག་པོ་རྒྱུ་མཐུན་དང་། །
རྣམ་སྨིན་འབྲས་བུ་འབྱིན་པར་འདོད། །

[Block 876]
རེ་ཞིག་མི་དགེ་བ་ཀུན་དུ་བསྟན་པ་དང་གོམས་པར་བྱས་པ་དང་། ལན་མང་དུ་བྱས་པ་ཐམས་ཅད་ཀྱིས་ནི་དམྱལ་བ་དག་གི་ནང་དུ་སྐྱེ་བར་འགྱུར་ཏེ། འདི་ནི་དེ་དག་གི་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་ཡིན་ནོ། །

[Block 877]
བརྒྱ་ལ་འདི་ལྟ་བུར་མི་རྣམས་དང་སྐལ་བ་མཉམ་པར་འོངས་ན༌[^663]ཡང་སྲོག་གཅོད་པས་ནི་ཚེ་ཐུང་བར་འགྱུར་རོ། །

[Block 878]
མ་བྱིན་པར་ལེན་པས་ནི་ལོངས་སྤྱོད་ཀྱིས་ཕོངས་པར་འགྱུར་རོ། །

[Block 879]
འདོད་པས་ལོག་པར་གཡེམ་པས་ནི་དགྲ་དང་བཅས་པའི་ཆུང་མ་ཅན་དུ་འགྱུར་རོ། །

[Block 880]
བརྫུན་དུ་སྨྲ་བས་ནི་སྐུར་བ་མང་པོར་འགྱུར་རོ། །
--- END BLOCKS ---

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
[Block 946]
ཆོས་བསྟན་པ་དེ་དག༌[^357]གང་ཡིན་སྙོམ་པ༌[^358]ལ། སེམས་དང་སེམས་ལས་བྱུང་བ་ཡིན།[^359] །འོ་ན་གང་དག་སེམས་དང་ལྡན་པ་མ་ཡིན་པ་དང་། གཟུགས་ཅན་གྱི་ཆོས་དེ་དག་ཇི་ལྟ་བུ་ཞེ་ན། མཚུངས་ལྡན་མ་གཏོགས་གཞན་དེ་བཞིན། །མཚུངས་པར་ལྡན་པའི་རྒྱུ་གཅིག་པུ་མ་གཏོགས་པ་ཆོས་ཉོན་མོངས་པ་ཅན་ལ་སོགས་པ་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་ཇི་ལྟ་བ་དེ་ཁོ་ན་བཞིན་དུ་སྐྱེ་སྟེ། རྒྱུ་རྒྱ་ཆེར་བཤད་པ་རྫོགས་སོ།། །།

[Block 947 [HEADING]]
#### རྐྱེན་བཞི། ^2-3-4-0

[Block 948]
རྐྱེན་རྣམས་གང་ཞེ་ན། རྐྱེན་ནི་བཞི་པོ་དག་ཏུ་གསུངས། །

[Block 949]
གང་ནས་གསུངས་ཤེ་ན། མདོ་ལས་རྐྱེན་ཉིད་ནི་བཞི་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 950]
དེ་ལ་རྒྱུ་ཞེས་བྱ་བ་རྒྱུ་ལྔ་ཡིན། །བྱེད་རྒྱུའི་རྒྱུ་མ་གཏོགས་པ་རྒྱུ་ལྔ་ནི་རྒྱུའི་རྐྱེན་ཡིན་ནོ། །

[Block 951 [VERSE]]
སེམས་དང་སེམས་བྱུང་སྐྱེས་པ་རྣམས། །
ཐ་མ་མིན་མཚུངས་དེ་མ་ཐག །

[Block 952]
དགྲ་བཅོམ་པའི་ཐ་མ་མ་གཏོགས་པ་སེམས་དང་སེམས་ལས་བྱུང་བ་སྐྱེས་པ་རྣམས་ནི་མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་ཡིན་ནོ། །

[Block 953]
དམིགས་པ་ཆོས་རྣམས་ཐམས་ཅད་དོ། །

[Block 954]
ཅི་རིགས་པར་མིག་གི་རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་རྣམས་ཀྱི་ནི་གཟུགས་ལ་སོགས་པའོ། །

[Block 955]
ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ནི་ཆོས་ཐམས་ཅད་དོ། །

[Block 956]
བྱེད་རྒྱུ་ཞེས་བྱ༌[^360]བདག་པོར་བཤད། །བྱེད་པའི་རྒྱུ་གང་ཡིན་པ་དེ་ནི་བདག་པོའི་རྐྱེན་ཡིན་ནོ། །

[Block 957]
ཡང་རྐྱེན་འདི་དག་བྱ་བ་བྱེད་པས་ན་གནས་སྐབས་གང་གི་ཆོས་ལ་བྱེད་ཅེ་ན།

[Block 958]
རེ་ཞིག་རྒྱུའི་རྐྱེན་རྣམ་པ་ལྔར༌[^361]བཤད་པ་དེ་ལས།

[Block 959]
རྒྱུ་གཉིས་པོ་དག་འགག་པ་ལ། [^362]བྱ་བ་བྱེད་དོ། །

[Block 960]
འགག་པ་ཞེས་བྱ་བ་ནི་ད་ལྟར་ཡིན་ཏེ། འགག་པ་ལ་མངོན་དུ་ཕྱོགས་པའི་ཕྱིར་རོ། །

[Block 961]
དེ་ལ་ལྷན་ཅིག་འབྱུང་བ་དང་མཚུངས་པར་ལྡན་པའི་རྒྱུ་དག་བྱ་བ་བྱེད་དེ། དེ་གཉིས་ནི་ལྷན་ཅིག་འབྱུང་བའི་འབྲས་བུ་ལ་བྱ་བ་བྱེད་པའི་ཕྱིར་རོ། །

[Block 962]
གསུམ་པོ་ནི་སྐྱེ་བ༌[^363]ལའོ་ཞེས་བྱ་བ་ནི་མ་འོངས་པ་སྟེ། སྐྱེ་བ་ལ་མངོན་དུ་ཕྱོགས་པའི་ཕྱིར་རོ། །

[Block 963]
དེ་ལ་ནི་སྐལ་བ་མཉམ་པ་དང་། ཀུན་དུ་འགྲོ་བ་དང་། རྣམ་པར་སྨིན་པའི་རྒྱུ་རྣམས་བྱ་བ་བྱེད་དེ། རྒྱུའི་རྐྱེན་ནི་དེ་ཙམ་ཞིག་ཡིན་ནོ། །

[Block 964]
དེ་ལས་གཞན་པ་ཡི། །རྐྱེན་དག་དེ་ལས་བཟློག་པ་ཡིན། །མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་ནི་སྐབས་འབྱེད་པའི༌[^364]ཕྱིར་སྐྱེ་བ་ལ་བྱ་བ་བྱེད་དོ། །

[Block 965]
དམིགས་པའི་རྐྱེན་ནི་ད་ལྟར་གྱི་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་ཀྱིས་འཛིན་པའི་ཕྱིར་འགག་པ་ལ་བྱ་བ་བྱེད་དོ། །

[Block 966]
བདག་པོའི་རྐྱེན་ནི་གནས་སྐབས་ཐམས་ཅད་དུ་མི་སྒྲིབ་པའི་ངོ་བོར་གནས་པས་འདིའི་བྱ་བ་དེ༌[^365]ནི་དེ་ཉིད་ཡིན་ནོ། །

[Block 967]
རྐྱེན་རྣམས་བྱེད༌[^366]པ་དང་བཅས་པ་བཤད་ཟིན་ཏོ། །

[Block 968]
ཡང་ཆོས་གང་ཞིག་རྐྱེན་དུ་ཞིག་གིས་བསྐྱེད་ཅེ་ན། བཞི་ཡིས་སེམས་དང་སེམས་བྱུང་རྣམས། །སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་ནི་ཅི་རིགས་པར་རྐྱེན་བཞི་པོས་སྐྱེད༌[^367]དོ། །

[Block 969]
གསུམ་གྱིས་སྙོམས་པར་འཇུག་པ་གཉིས། །དམིགས་པའི་རྐྱེན་མ་གཏོགས་པ་སྙོམས་པར་འཇུག་པ་འདི་དག་ནི་སེམས་ཀྱི་མངོན་པར་འདུ་བྱེད་པ་ལས་སྐྱེ་བའི་ཕྱིར་སེམས་ཀྱི་དེ་མ་ཐག་པ་ཅན་དག་ཡིན་ནོ། །

[Block 970]
གཞན་ནི་གཉིས་པོ་དག་ལས་སྐྱེ།[^368] །ཆོས་གཞན་ལྡན་པ་མ་ཡིན་པ་རྣམས་དང་། གཟུགས་ཅན་རྣམས་ནི་རྒྱུ་དང་། བདག་པོའི་རྐྱེན་དག་ལས་སྐྱེའོ། །

[Block 971]
རྒྱུ་དང་རྐྱེན་དག་ཁོ་ན་ལས་ཆོས་ཐམས་ཅད་ཀྱང་སྐྱེའོ།[^369] །

[Block 972]
དབང་ཕྱུག་སོགས་མིན་རིམ་སོགས་ཕྱིར། །དབང་ཕྱུག་ལ་སོགས་པ་གཅིག་ཁོ་ན་རྒྱུ་ཡིན་ན་འགྲོ་བ་ཐམས་ཅད་ཅིག་ཅར་འབྱུང་བར་འགྱུར༌[^370]བ་ཞིག་ན་དངོས་པོ་རྣམས་རིམ་གྱིས་འབྱུང་བར་ཡང་སྣང་ངོ་། །དབང་ཕྱུག་དག་ཀྱང་ཐོག་མ་མེད་པས་ཀྱང་གཞན་ལ་མ་ལྟོས་པས༌[^371]འབྱིན་པ་ཐོག་མ་མེད་པར་འགྱུར་བ་དང་འབྱིན་པ་ལ་དགོས་པ་མེད་པའི་ཕྱིར་དབང་ཕྱུག་ལ་སོགས་པ་ནི་རྒྱུ་མ་ཡིན་ནོ། །

[Block 973]
ཡང་གཞན་ནི་གཉིས་པོ་དག་ལས་སྐྱེ་ཞེས་གང་བཤད་པ་དེ་ཇི་ལྟར་ན༌[^372]འབྱུང་བ་རྣམས་འབྱུང་བ་རྣམས་ཀྱི་རྒྱུའི༌[^373]རྐྱེན་ཡིན་ཞེ་ན། དེའི་རྒྱུ་འབྱུང་བ་རྣམ་པ་གཉིས། །འབྱུང་བའི་རྒྱུ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 974]
སྐལ་བ་མཉམ་པ་དང་།

[Block 975 [VERSE]]
ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་དག་གིས་སོ། །
འབྱུང་ལས་གྱུར་པའི་རྣམ་པ་ལྔ། །

[Block 976]
འབྱུང་བ་རྣམས་འབྱུང་བ་ལས་གྱུར་པའི་རྒྱུ་རྣམ་པ་ལྔ་ཡིན་ཏེ། སྐྱེད་པའི༌[^374]རྒྱུ་ཡིན་ཏེ། དེ་ལས་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 977]
བརྟེན་པའི་རྒྱུ་ཡིན་ཏེ། སྐྱེས་པ་འབྱུང་བའི་རྗེས་སུ་མཐུན་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 978]
གནས་པའི་རྒྱུ་ཡིན་ཏེ། རྟེན་དུ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 979]
རྟོན་པའི་རྒྱུན༌[^375]ཡིན་ཏེ། རྒྱུན་མི་འཆད་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 980]
ཉེ་བར་འཕེལ་བའི་རྒྱུ་ཡིན་ཏེ། དེ་ནི་བྱེད་རྒྱུ་ཁོ་ན་རྣམ་པ་ལྔ་རུ་ཕྱེ་བའོ། །

[Block 981]
འབྱུང་གྱུར༌[^376]རྣམ་གསུམ་ཕན་ཚུན་དུ། །ལྷན་ཅིག་འབྱུང་བ་དང་། སྐལ་བ་མཉམ་པ་དང་། རྣམ་པར་སྨིན་པའི་རྒྱུ་དག་གིས་སོ། །

[Block 982]
དེ་ལ་ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་ནི་ལུས་དང་ངག་གི༌[^377]ལས་སེམས་ཀྱི་རྗེས་སུ་འཇུག་པ་ཕན་ཚུན་དུ་ཡིན་གྱི་གཞན་ནི་མ་ཡིན་ནོ། །

[Block 983]
སྐལ༌[^378]པ་མཉམ་པའིའོ། །

[Block 984]
རྣམ་པར་སྨིན་པའི་རྒྱུ་ནི་ལུས་དང་ངག་གི་ལས་གང་གི་རྣམ་པར་སྨིན་པ་མིག་ལ་སོགས་པ་གང་ཡིན་པའོ། །

[Block 985]
འབྱུང་བ་རྣམས་ཀྱི་དེ་རྣམས་གཅིག །འབྱུང་བ་ལས་གྱུར་པའི་གཟུགས་འབྱུང་བ་རྣམས་ཀྱི་ནི་རྣམ་པར་སྨིན་པའི་རྒྱུ་ཁོ་ན་ཡིན་ཏེ། ལུས་དང་ངག་གི་ལས་གང་གིས་འབྱུང་བ་རྣམས་རྣམ་པར་སྨིན་པའོ། །
--- END BLOCKS ---

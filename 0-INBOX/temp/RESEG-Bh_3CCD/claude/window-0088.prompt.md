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
[Block 3081]
འོད་གསལ་བ་ལ་གནས་པའི་རྣལ་འབྱོར་པས་སེམས་ཅན་གྱི་དོན་གྱི་བྱ་བ༌[^2008]བསྟན་པའི་ཕྱིར། ཛྲེ། སྒྱུ་མ་ལྟ་བུ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། རྣལ་འབྱོར་པ་དེས་སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་གྱི་སྒོ་ནས་དངོས་པོ་ཐམས་ཅད་དང་སངས་རྒྱས་ཀྱི་བྱ་བ་ནི་བསྟན་པ་དང་། ཡོངས་སུ་སྨིན་པ་དང་། རྣམ་པར་གྲོལ་བ་ལ་སོགས་པ་བྱེད་པ་ནི་མཛད་པའོ། །

[Block 3082]
གཏན་ལ་དབབ་པའི་གཞི་ནི་གྲུབ་པའི་མཐའ་སྟེ། དེ་ཉིད་མི་འཕོ་བའི་ཕྱིར་གནས་པའོ། །

[Block 3083]
དེ་ལ་གནས་པ་ནི་ངལ་སོ་བའོ། །

[Block 3084]
རིམ་པ་གཉིས་པ༌[^2009]གོམས་པས་གསུམ་པ་ཐོབ་ནས་དེ་ཉིད་འདོར་བ༌[^2010]བྱེད་དོ༌[^2011]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3085]
བསྐྱེད་པའི་རིམ་པའི་རྣལ་འབྱོར༌[^2012]བཞི་ལས་ཁྱད་པར་བསྟན་པར་བྱ་བའི་ཕྱིར། ཡོ། རྣལ་འབྱོར་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། བསྐྱེད་པའི་རིམ་པ༌[^2013]རྣལ་འབྱོར་བཞི་སྟེ། གང་གིས་དང་པོའི་སྦྱོར་བ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཏིང་ངེ་འཛིན་འགྲུབ་པར་འགྱུར་རོ། །

[Block 3086]
འདིར་རྣལ་འབྱོར་ནི་ཐབས་སོ། །

[Block 3087]
རྗེས་སུ་རྣལ་འབྱོར་ནི་ཤེས་རབ་བོ། །

[Block 3088]
ཤིན་ཏུ་རྣལ་འབྱོར་ནི་དེ་དག་གི་སྙོམས་པར་ཞུགས་པའོ། །

[Block 3089]
རྣལ་འབྱོར་ཆེན་པོ་ནི་སྙོམས་པར་ཞུགས་པ་ལས་བདེ་བ་ཆེན་པོ་ཐོབ་པའོ། །

[Block 3090]
དེ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར་དང་། རྡོ་རྗེ་ཅན་ནི་སྐྱེས་བུའོ། །

[Block 3091]
མཁའ་འགྲོ་ནི་ཤེས་རབ་བོ། །

[Block 3092]
དེ་རང་ཉིད་ནི་རྡོ་རྗེ་དང་པདྨ་སྙོམས་པར་ཞུགས་པའོ། །

[Block 3093]
ཡང་གི་སྒྲས་ནི་བདེ་བ་ཆེན་པོའོ། །

[Block 3094]
རྣལ་འབྱོར་གྱི་སྒྲས་ནི་རྗེས་སུ་རྣལ་འབྱོར་དུ་ཤེས་པར་བྱའོ། །

[Block 3095]
དེ་ལྟར་གྱུར་པའི་རྣལ་འབྱོར་པ་རང་དབང་དུ་སྤྱོད་པ་ནི༌[^2014]ཡང་མ་གོས་པ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར། ཥིཌ། བཀག་པ༌[^2015]ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། བཀག་པ༌[^2016]ནི་འཇིག་རྟེན་དང་འགལ་བའི་ལས་སོ། །

[Block 3096]
དཔེར་ན་དཀོན་མཆོག་གསུམ་ལ་གནོད་པ་ཅན་རྣམས་ལ་རྣམ་པར་འཚེ་བ་དང་། སེར་སྣ་ཅན་ལ་རྫས་འཕྲོག་པ༌[^2017]དང་། འདོད་ཆགས་ཅན་ལ་བུ་སྨད་འཕྲོག་པ་དང་། ང་རྒྱལ་ཅན་ལ་ང་རྒྱལ་གཅོག་པ༌[^2018]དང་། ཕྲག་དོག་ཅན་ལ་རྩུབ་མོ་སྨྲ་བ་དང་། དེ་ལ་སོགས་པ་འཇིག་རྟེན་དང་འགལ་བའི་ལས་རྣམས་ཐམས་ཅད༌[^2019]ཐབས་ལ་མཁས་པའི་དབང་གིས་བྱས་ཏེ་གོས་པར་མི་འགྱུར་ཏེ། སྙིང་རྗེ་ཆེན་པོའི་དབང་གིས་བྱས་པར་གྱུར་ན་སྒྲིབ་པར་མི་འགྱུར་རོ། །

[Block 3097]
བྱ་དང་བྱ་མིན་རྣམ་སྤངས་ལ། །ཞེས་པ་ལ། བགྲོད་པ་དང་བགྲོད་པར་བྱ་བ་མ་ཡིན་པ་ལ་སོགས་པའི་རྣམ་པར་རྟོག་པ་སྤངས་པ་ཡིན་ཏེ།

[Block 3098 [VERSE]]
ངོ་བོ་ཉིད་ཤེས་པའི་ཕྱིར་རོ། །
པདྨ་ལ་ནི་འདམ་གྱིས་བཞིན། །

[Block 3099]
ཞེས་བསྟན་ཏོ། །

[Block 3100]
དེའི་ཕན་ཡོན་བསྟན་པར་བྱ་བའི་ཕྱིར། བྷ། ཡོན་ཏན་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། ཕྲ་བ་ལ་སོགས་པ་ཡོན་ཏན་བརྒྱད་ཀྱི་དབང་ཕྱུག་གམ་སྐུའི་དབང་ཕྱུག་ལ་སོགས་པ་དེ་དང་ལྡན་པའོ། །

[Block 3101]
སེམས་ཅན་ཐམས་ཅད་རིག་འགྱུར་ཞེས་པ་ནི་འདས་པ་ལ་སོགས་པའི་དུས་གསུམ་གྱི་ནང་ན་གནས་པའི་སེམས་ཅན་ཐམས་ཅད་ཀྱི་སེམས་ཀྱི་སྤྱོད་པ་དང་འཆི་འཕོ་བ་དང་སྐྱེ་བ་ལ་སོགས་པ་ཤེས་པར་འགྱུར་རོ། །

[Block 3102]
དེ་བཞིན་དུ་ཡང་སེམས་ཅན་གྱི་དོན་བྱ་བའི༌[^2020]ཕྱིར། བདག་ཉིད་ཡེ་ཤེས་ལུས་ཀྱི་སྤྱོད། །ཅེས་པ་ནི་སྒྱུ་མ་ལྟ་བུའི་རྣམ་པས་འཇིག་རྟེན་གྱི་ཁམས་མ་ལུས་པ་སྟེ། སངས་རྒྱས་ཀྱི་ཞིང་རྣམས་སུ༌[^2021]ཡོངས་སུ་སྤྱོད་དོ། །

[Block 3103]
ཕྱི་དང་ནང་གི་རིམ་པས་དེའི་གཞི་བསྟན་པར་བྱ་བའི་ཕྱིར། གེ། གཙོ་བོ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ།

[Block 3104 [VERSE]]
ནམ་མཁའ་ནི་ནམ་མཁའི་དབྱིངས་སོ། །
དེ་ཡི་ཁྱིམ་ནི་བཞུགས་གནས་སོ། །
གཙོ་བོ་གང་དུ་སྤྱོད་པ་ཡི། །

[Block 3105]
ཞེས་པ་ལ། མི་བསྐྱོད་པ་ལ་སོགས་པ་ལྔའི་གཙོ་བོ་དཔལ་རྡོ་རྗེ་སེམས་དཔའ། འགྲོ་བའི་དོན་མཛད་པའི་ཕྱིར་གང་དུ་སྤྱོད་པ༌[^2022]ཞེས་པ་ནི་བཞུགས་ཤིང་གནས་པ་འཚོ་ཞེས་བྱ་བའི་བར་དུའོ། །

[Block 3106 [VERSE]]
བདེ་བ་ཆེན་པོའི་ཏིང་འཛིན༌[^2023]གྱིས། །
དེ་ཉིད་དུ་ནི་རྟག་ཏུ་རོལ། །

[Block 3107]
ཞེས་པ་ལ། །འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་མངོན་དུ་བྱས་པས། སྤྲོ་བ་དང་བསྡུ་བའི་རིམ་པས༌[^2024]རོལ་པར་འགྱུར་རོ་ཞེས་ཕྱིའི་དོན་ཏོ། །

[Block 3108]
དེ་བཞིན་དུ་རྣལ་འབྱོར་པ་དེའི་ནམ་མཁའ༌[^2025]དང་འདྲ་བའི་ཁོང་སྟོང་པདྨ་ནི་ཁྱིམ་སྟེ། བཞུགས་པས་སོ། །

[Block 3109]
གཙོ་བོ་གང་དུ་སྤྱོད་པ་ཡི། །[^2026]ཞེས་པ་ལ། ཕྱག་རྒྱའི་པདྨ་གང་དུ་དཔལ་རྡོ་རྗེ་འཛིན་པ་སྟེང་དང་འོག་ཏུ་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི༌[^2027]གཟུགས་ཀྱིས་ཡོངས་སུ་སྤྱོད་པའོ། །

[Block 3110]
ཇི་སྐད་དུ།

[Block 3111 [VERSE]]
བྷ་གའི་དབུས་སུ་ནམ་མཁའ་གང་། །
ནམ་མཁའ་ལྔ་ཡིས་རྣམ་པར་བརྒྱན། །

[Block 3112]
ཞེས་འབྱུང་བས་སོ། །

[Block 3113]
དེ་བཞིན་དུ་ཡང་།

[Block 3114 [VERSE]]
ཆོས་དབྱིངས་འདི་ནི་རྣམ་པར་དག །
སེམས་ཅན་ཁམས་ནི་གྲོལ་བྱེད་པ། །
རང་ཉིད་རྡོ་རྗེ་འཛིན་རྒྱལ་པོ། །
དངོས་ཀུན་གྱིས་ནི་འདི་ལ་བཞུགས། །

[Block 3115]
ཞེས་འབྱུང་ངོ་། །དེ་ལ་ཕྱག་རྒྱའི་པདྨར་བདེ་བ་ཆེན་པོའི་ཏིང་ངེ་འཛིན་གྱིས་ནི་སྣང་བ་ལ་སོགས་པའི་ཡེ་ཤེས་གསུམ་རྣམ་པར་དག་པར་བྱེད་པ་བདེ་བ་ཆེན་པོའི་རྣམ་གྲངས་ཅན་འོད་གསལ་བ་ཉམས་སུ་མྱོང་བས་རོལ་ཏེ། རང་རིག་པའི་ངོ་བོ་ཉིད་ཀྱིས་གནས་སོ་ཞེས་ནང་གི་དོན་ཏོ། །

[Block 3116]
བདག་བྱིན༌[^2028]གྱིས་རློབ་པའི་རིམ་པའི་རྣལ་འབྱོར་པས་བར་བར་དུ་སེམས་རྣམ་པར་དག་པ་ཡང་མངོན་དུ་བྱ་བའི་ཕྱིར། ཥྱ། འདི་ལ་སྣང་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། སྣང་བ་ལ་སོགས་པའི་ཡེ་ཤེས་གསུམ་པོ་མཚམས་ལ་སོགས་པའི་སྒྲས་ཐ་སྙད་དུ་བྱའོ། །

[Block 3117]
འཇིག་རྟེན་ན་མཚམས་ལ་སོགས་པ་གཞན་མེད་དེ་ཡེ་ཤེས་གསུམ་དུ་མཐོང་བའི་ཕྱིར་རོ་ཞེས་པ་ལ། འཇུག་པའི༌[^2029]རྣམ་པར་ཤེས་པ་ལ་སོགས་པའི་བཟློག་པས་སྤངས་པའི་ཕྱིར་རོ། །

[Block 3118]
དེ་དང་དེའི་རྗེས་སུ་མཐུན་པ་སྣང་བ་གསུམ་བཞིན་དུ་ཕྱིའི་མཚམས་ལ་སོགས་པའི་རྣམ་པར་རྟོག་པ་བརྫུན་པ་ཉིད་དོ། །

[Block 3119]
འདས་པ་ལ་སོགས་པ་ཡང་ཡེ་ཤེས་གསུམ་གྱི་རྣམ་པར་དག་པ་བསྟན་པར་བྱ་བའི་ཕྱིར། ཝི། སྣ་ཚོགས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། སྣ་ཚོགས་པ་ཡི་ཐ་སྙད་ནི། །ལུས་དང་ངག་དང་ཡིད་ཀྱི་བྱ་བ་སྟེ། སྤྱོད་ལམ་བཞིའི་མཚན་ཉིད་ཅན་དེ་དག་ཆགས་པ་དང་བྲལ་བ་ལ་སོགས་པའི་རང་བཞིན་གྱི་དབྱེ་བས་སྣ་ཚོགས་ཅན་ཏེ། དགེ་བ་དང་མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པ་ཞེས་བྱ་བའི་བར་རོ། །

[Block 3120]
འཇིག་རྟེན་པས་ནི་ཡོངས་བརྟགས་པ། །ཞེས་པས་ནི་སོ་སོའི་སྐྱེ་བོས་བརྟགས་པ༌[^2030]གང་ཡིན་པ་དེ་དག་དུས་གསུམ་གྱི་དབྱེ་བས་ནི། ཡེ་ཤེས་རྣམ་པ་གསུམ་ལས་འབྱུང་། །ཞེས་རིག་པར་བྱའོ། །
--- END BLOCKS ---

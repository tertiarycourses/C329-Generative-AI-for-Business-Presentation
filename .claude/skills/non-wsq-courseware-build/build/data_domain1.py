"""
Domain 1 — Getting Started with Generative AI for Presentations. Labs 1-5.

THE CONNECTED PROJECT STARTS HERE, IN LAB 1.

Every lab in this course takes one connected deliverable — the Meridian Fresh
pitch deck, a business presentation for a fictional Singapore healthy meal-kit
startup seeking approval to expand into three new neighbourhoods — one stage
further. Lab 1 sets up the AI presentation toolkit; Lab 2 builds a reusable
prompt library; Lab 3 researches the topic and audience and fact-checks the
content; Lab 4 shapes the core message and story; Lab 5 turns the story into a
complete slide-by-slide outline. A Meridian Fresh brief with the facts and
figures you need is supplied; use your own non-confidential presentation instead
wherever you prefer.
"""

SCENARIO = (
 "Meridian Fresh is a fictional Singapore healthy meal-kit startup. It delivers chef-designed, ready-to-cook "
 "healthy meal kits to busy professionals, and after two strong years in its first neighbourhood it wants to "
 "expand into three new ones. You are the person preparing the business presentation — the Meridian Fresh pitch "
 "deck — a roughly twelve-slide deck for the company's quarterly strategy review, where you must persuade the "
 "leadership team and a visiting investor to approve the expansion and its budget. The deck must tell a clear "
 "story: the problem busy Singaporeans face, Meridian Fresh's solution, the traction so far, the market "
 "opportunity, the expansion plan, the numbers, the roadmap and a clear ask. Across this course you take that "
 "presentation from a blank page to a finished, rehearsed deck using ChatGPT, Claude, Gemini and an AI slide "
 "generator such as Gamma. Use this scenario only if you cannot use a real, non-confidential presentation of "
 "your own; your own topic is always welcome."
)

PROJECT_NOTE = (
 "BUILDING BLOCK — what you create in this lab becomes part of your Meridian Fresh pitch deck, "
 "the connected presentation you assemble across all 10 labs."
)

DOMAIN1 = [
 dict(
 num=1, topic=1,
 title="Set Up Your AI Presentation Toolkit",
 objective="Sign in to ChatGPT, Claude, Gemini and an AI slide generator (Gamma), run your first prompts, and learn the generate–review–refine loop that every later lab uses.",
 desc="This lab gets you comfortable with the tools before any real presentation work begins. You open the "
 "chat assistants (ChatGPT, Claude and Gemini), confirm you are signed in, and run a simple prompt so you see "
 "how each drafts presentation content, then run the same prompt in a second assistant to feel how they "
 "differ. You open an AI slide generator (Gamma), sign in, and generate a quick throwaway deck from a one-line "
 "prompt so you can see what a slide generator does. You note what AI is genuinely good at for presentations "
 "(a fast draft, structure, design) and where it needs you (real facts, your audience, your judgement). By the "
 "end you understand the describe -> generate -> review -> refine loop that is the heart of every lab. " + PROJECT_NOTE,
 build="Your AI presentation toolkit set up and tested — at least one chat assistant and one AI slide generator signed in and responding — a first throwaway AI-generated deck, and a clear, written understanding of the generate–review–refine loop and what AI can and cannot do for you.",
 services="ChatGPT, Claude, Gemini, Gamma (AI slide generator), account sign-in, first prompts, comparing assistants, the generate–review–refine loop",
 steps=[
 ("Create a project folder on your machine called 'Meridian-Fresh-Deck' so every file and note you make today stays together. Open ChatGPT (chat.openai.com), Claude (claude.ai) and Gemini (gemini.google.com) in browser tabs and confirm you are signed in to at least one.", ""),
 ("In one chat assistant, run a simple first prompt to see how it drafts presentation content. Paste the prompt below and read the reply.",
  "You are a presentation coach. In five short bullet points, explain what makes a business pitch deck persuasive to a startup's leadership team and an investor. Keep each bullet to one sentence."),
 ("Run the exact same prompt in a second assistant and compare the two replies. Notice differences in tone, length and structure — the skill you learn transfers across all of them, so use whichever you prefer.",
  "You are a presentation coach. In five short bullet points, explain what makes a business pitch deck persuasive to a startup's leadership team and an investor. Keep each bullet to one sentence."),
 ("Open the AI slide generator Gamma (gamma.app), sign in, and use 'Generate' to make a quick throwaway deck from a one-line prompt, so you can see what a slide generator produces. Paste the prompt below.",
  "A short five-slide business pitch deck for a healthy meal-kit startup expanding into new neighbourhoods, high level and clean."),
 ("Look at what Gamma produced — designed slides with layout, theme, fonts and spacing generated in seconds. Note that it is a fast starting point, not a finished deck. You will not keep this one; it is only to feel the tool.", ""),
 ("In one line each, write what the AI did well (fast draft, structure, instant design) and where it needs you (it does not know Meridian Fresh's real numbers, your audience, or your judgement). This good/not-good picture guides how you use AI all day.", ""),
 ("Open the supplied Meridian Fresh brief (labs/reference-pack/): the company story, the audience, the traction and financial figures, and the expansion plan. Skim it so you know the presentation you are about to build.", ""),
 ("Save your notes into your Meridian-Fresh-Deck folder. Write one line, in your own words, describing the generate -> review -> refine loop — you rely on it in every later lab.", ""),
 ],
 test="You have signed in to at least one chat assistant and to an AI slide generator, run the same prompt in two assistants and compared them, generated a throwaway deck in Gamma, written a one-line note on what AI is and is not good at for presentations, skimmed the Meridian Fresh brief, and described the generate–review–refine loop in your own words — all saved in your Meridian-Fresh-Deck folder.",
 ),
 dict(
 num=2, topic=1,
 title="Write Effective Prompts for Presentations",
 objective="Turn a vague ask into a strong, structured prompt (role, context, task, format, constraints) for presentation tasks, and save a reusable prompt library for the work you repeat every deck.",
 desc="A good result starts with a good prompt, not a lucky one. In this lab you read the Meridian Fresh brief "
 "and write a deliberately vague prompt first, so you see how generic the result is. You then rebuild it with "
 "five clear parts — a role for the AI, the context (audience, goal, tone), the exact task, the format you "
 "want back, and any constraints — and watch the draft become genuinely usable. You run small single-change "
 "edits to feel how each part matters, then save your best versions as a reusable prompt library with clearly "
 "marked slots, covering the tasks you repeat for every presentation: research, outline, slide copy, speaker "
 "notes and Q&A prep. " + PROJECT_NOTE,
 build="A structured presentation prompt built from role, context, task, format and constraints, plus a reusable prompt library with clearly marked slots for the recurring presentation tasks, saved in your project folder.",
 services="ChatGPT / Claude / Gemini, the structured prompt framework (role, context, task, format, constraints), prompt iteration, a reusable prompt library",
 steps=[
 ("Open the Meridian Fresh brief and note two things you will reuse in every prompt: who the audience is (the leadership team plus an investor) and the goal (approve the expansion).", ""),
 ("Write a deliberately vague first prompt in any assistant and generate, so you can see the generic result. Paste the prompt below and read how unfocused the reply is.",
  "Write a pitch deck for a meal-kit company."),
 ("Rebuild the prompt with a role and the context, and regenerate. Paste the prompt below and compare it with the vague version.",
  "You are an experienced startup pitch-deck writer. Context: Meridian Fresh is a Singapore healthy meal-kit startup with two strong years in one neighbourhood, now seeking its leadership team's and an investor's approval to expand into three more. Draft the high-level sections a persuasive expansion pitch deck should contain."),
 ("Now add the exact task, the format you want back, and clear constraints, and regenerate. Paste the prompt below.",
  "As the same pitch-deck writer, list the 10 to 12 slides this deck should have. For each slide give a headline that states the slide's point and one line on what it should contain. Present it as a numbered list, keep it concise, and do not invent specific financial figures — leave clear placeholders where real numbers are needed."),
 ("Put the vague result and the structured result side by side. Note in one line how much more usable the structured prompt was — this is the core lesson of the day.", ""),
 ("Run two or three single-change edits to feel how each part steers the result — for example change the audience to 'a room of potential customers', or change the tone to 'formal and data-heavy' — and note which you would keep for Meridian Fresh.", ""),
 ("Save a reusable prompt library in your project folder: templates for research, outline, slide copy, speaker notes and Q&A prep, each with clearly marked slots — [ROLE], [CONTEXT], [AUDIENCE], [TASK], [FORMAT], [CONSTRAINTS] — that you fill in for any future presentation.", ""),
 ],
 test="You have compared a vague prompt with a structured one built from role, context, task, format and constraints, seen how much better the structured prompt performs, run single-change edits to feel each part, and saved a reusable prompt library with marked slots for the recurring presentation tasks in your project folder.",
 ),
 dict(
 num=3, topic=1,
 title="Research Your Topic and Audience with AI",
 objective="Use AI to research the audience, the topic and the key points, gather supporting material, and fact-check it so the deck stands on solid, honest ground rather than invented figures.",
 desc="A persuasive deck rests on understanding the audience and getting the facts right. In this lab you use "
 "a chat assistant to profile your audience (the leadership team and a visiting investor), surface the "
 "questions they will ask and what would make them say yes or no, and research the meal-kit market and the "
 "problem it solves at a high level. Crucially, you then fact-check: you ask the AI to label which of its own "
 "claims and numbers are reliable and which you must verify, and you cross-check every figure against the "
 "supplied Meridian Fresh brief — replacing anything the AI invented with the brief's real numbers or a clear "
 "[VERIFY] placeholder. This is where you learn to use AI for research without letting it make up your facts. " + PROJECT_NOTE,
 build="An audience profile, a short researched brief of the market and the problem with the key supporting points, and a fact-check pass that labels every claim and number as verified, needing a source, or taken from the supplied brief.",
 services="ChatGPT / Claude / Gemini, audience analysis, topic research, source and fact checking, separating supplied facts from AI-generated claims",
 steps=[
 ("Open the Meridian Fresh brief and note the audience: the leadership team plus one visiting investor at the quarterly strategy review.", ""),
 ("Profile the audience with AI so you know what will land. Paste the prompt below.",
  "You are a communications strategist. My audience is the leadership team of a small Singapore startup plus one visiting investor, at a quarterly strategy review. Profile this audience: what they care about, what they already know, their likely priorities and concerns, and the tone that would land best. Keep it to a short, structured summary."),
 ("Ask what this audience will probe, so you can prepare. Paste the prompt below.",
  "For that same audience and a proposal to expand a meal-kit business into three new neighbourhoods, list the eight toughest questions they are likely to ask, and note what each question is really testing."),
 ("Research the problem and market at a high level, keeping general knowledge separate from anything that needs a source. Paste the prompt below.",
  "Give me a concise, neutral briefing on the healthy meal-kit market and the problem it solves for busy urban professionals. Clearly separate widely-accepted general points from anything that would need a specific source or a recent statistic. Do not invent precise figures."),
 ("Fact-check the AI's own briefing — this is the key step. Paste the prompt below and read the labels critically.",
  "Review the briefing you just gave me. For each factual claim or number, label it [GENERAL KNOWLEDGE], [NEEDS A SOURCE], or [POSSIBLY OUTDATED], and tell me which ones I must verify myself before putting them in a pitch deck."),
 ("Cross-check every figure against the supplied Meridian Fresh brief. Use the brief's real traction and financial numbers, and replace any figure the AI invented with the brief's value or a clear [VERIFY] placeholder. Never present an AI-invented number as fact.", ""),
 ("Save three things in your project folder: the audience profile, the short researched brief of the market and problem, and your fact-check notes marking what is verified, what needs a source, and what came from the brief.", ""),
 ],
 test="You have used AI to profile the audience and surface their toughest questions, researched the market and problem, run a fact-check pass that labels each claim, and cross-checked every figure against the supplied brief — replacing invented numbers with the brief's real figures or a [VERIFY] placeholder — all saved in your project folder.",
 ),
 dict(
 num=4, topic=1,
 title="Structure Your Message and Story",
 objective="Use AI to find one clear core message and a simple, audience-centred narrative arc, so the presentation persuades rather than just informs — before you build a single slide.",
 desc="Slides come later; the story comes first. In this lab you use AI to draft the presentation's core "
 "message — the single sentence you want the audience to remember, which is really your ask — generating a "
 "few options and refining one. You then ask the AI for two or three alternative narrative structures (for "
 "example Situation → Complication → Solution → Proof → Ask, or Problem → Solution → Proof), choose the arc "
 "that fits Meridian Fresh, and map your intended sections onto it. Finally you pressure-test the story: you "
 "ask the AI which sections do not support the core message so you can cut or merge them, leaving a tight "
 "story that flows from a hook to a clear ask. " + PROJECT_NOTE,
 build="One clear, one-sentence core message and a chosen narrative arc (for example situation → complication → solution → proof → ask) for the Meridian Fresh deck, with each planned section mapped to the part of the story it carries.",
 services="ChatGPT / Claude / Gemini, core-message crafting, narrative arc and storytelling structures (SCR, problem–solution–proof–ask), message testing",
 steps=[
 ("Bring the audience profile and the objective from Lab 3 to hand — the story has to serve that audience and that ask.", ""),
 ("Draft the core message with AI: the one thing the audience should remember. Paste the prompt below, then pick and refine the strongest option.",
  "You are a presentation storytelling coach. In one sentence each, give me three options for the single core message a Meridian Fresh expansion pitch should leave in the audience's mind — the one thing they remember. Make them specific and persuasive, not generic."),
 ("Ask for alternative story structures and when each works. Paste the prompt below.",
  "Suggest three ways to structure this pitch as a story — for example Situation–Complication–Resolution, or Problem–Solution–Proof–Ask. For each, give the sequence of sections and one line on when it works best."),
 ("Choose one arc and have AI map your sections onto it. Paste the prompt below.",
  "I'll use a Situation → Complication → Solution → Proof → Ask arc. Map a Meridian Fresh expansion pitch onto it: for each stage, say which section or slide belongs there and the single point it makes."),
 ("Pressure-test the story so it stays tight. Paste the prompt below, filling in your planned sections and message.",
  "Here is my planned section list: [PASTE SECTIONS]. Which of these do not clearly support my core message '[PASTE MESSAGE]', and which could I cut or merge to make the story tighter?"),
 ("Refine: cut or merge the weak sections the AI flagged, and confirm the story flows from an opening hook to a clear closing ask, with each section earning its place.", ""),
 ("Save your final core message, the chosen narrative arc, and the section-to-story map in your project folder — this is the spine you turn into a slide outline in Lab 5.", ""),
 ],
 test="You have a single, clear one-sentence core message, a chosen narrative arc, and a map of each section to the part of the story it carries — pressure-tested so every section supports the message — saved in your project folder.",
 ),
 dict(
 num=5, topic=1,
 title="Build the Presentation Outline with AI",
 objective="Turn the message and story into a complete, slide-by-slide outline — each slide's headline message, supporting points and suggested visual — that you will design in Topic 2.",
 desc="Now you bring the research, the message and the arc together into one concrete plan. In this lab you "
 "prompt the AI to produce a slide-by-slide outline for the roughly twelve-slide deck: for each slide, a "
 "headline written as the point it makes, two or three supporting bullets, and a suggested visual. You review "
 "it hard — rewriting any topic-label headline into a real message, enforcing one idea per slide, marking "
 "where charts and images belong, and inserting the brief's real figures as placeholders for the data slide. "
 "You check the flow and length so the deck opens with a hook and closes with the ask. This outline is the "
 "spine of everything you design, write and rehearse in Topic 2. " + PROJECT_NOTE,
 build="A complete, slide-by-slide outline for the roughly twelve-slide Meridian Fresh deck — each slide with a message headline, two or three supporting points and a suggested visual — reviewed for one idea per slide and a clear hook-to-ask flow, ready to design in Topic 2.",
 services="ChatGPT / Claude / Gemini, slide-by-slide outlining, headline-as-message, one idea per slide, mapping visuals and data placeholders",
 steps=[
 ("Gather your inputs from Labs 3-4: the core message, the narrative arc and section map, and the fact-checked research and figures.", ""),
 ("Prompt the AI to produce the full slide-by-slide outline. Paste the prompt below, filling in your message, arc and points.",
  "You are a pitch-deck writer. Using this core message: '[PASTE MESSAGE]', this story arc: '[PASTE ARC]', and these researched points and figures: '[PASTE POINTS]', produce a slide-by-slide outline for a 10 to 12 slide Meridian Fresh expansion pitch. For each slide give: (1) a headline written as the point the slide makes, (2) two or three supporting bullet points, (3) a suggested visual — chart, image, diagram or none. Number the slides."),
 ("Fix the headlines: make every one a message, not a topic label. Paste the prompt below.",
  "Review the slide headlines in this outline. Rewrite any that are topic labels (like 'Market' or 'Financials') into headlines that state the actual point (like 'The healthy meal-kit market is growing fast'). Return the revised outline."),
 ("Enforce one idea per slide: split any slide carrying two ideas into two, and merge any thin slide into its neighbour, so each slide makes exactly one point.", ""),
 ("Mark the visuals: confirm which slide carries the data chart and which carry images, and paste the brief's real figures into the chart slide as a placeholder so you have them ready for Lab 8.", ""),
 ("Check flow and length: aim for about 10 to 12 slides, confirm it opens with a hook and closes with the ask, and read the headlines alone top to bottom — they should tell the whole story on their own.", ""),
 ("Save the final outline in your project folder. This is the spine of your deck — you generate its copy in Lab 6, design it in Lab 7, and add charts, images and notes in Labs 8-9.", ""),
 ],
 test="You have a complete, numbered slide-by-slide outline of about 10 to 12 slides, every headline written as a message, one idea per slide, with charts and images marked and the brief's real figures placed on the data slide — and reading the headlines alone tells the whole story from hook to ask. Saved in your project folder.",
 ),
]

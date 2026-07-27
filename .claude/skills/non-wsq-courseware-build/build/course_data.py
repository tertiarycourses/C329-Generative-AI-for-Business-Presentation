"""
SINGLE SOURCE OF TRUTH — C329 Generative AI for Business Presentation (non-WSQ).

An intensive, one-day, hands-on course on using generative AI to plan, write,
design and deliver a polished business presentation end to end. Using general
chat assistants (ChatGPT, Claude and Gemini) and AI slide generators (Gamma,
Microsoft Copilot in PowerPoint and Canva), learners take one business
presentation — the Meridian Fresh pitch deck — from a blank page to a finished,
rehearsed deck: setting up an AI toolkit and prompt library, researching the
topic and audience, shaping a persuasive message and story, building a slide
outline, generating slide content, designing professional slides, creating
charts, images and speaker notes, and rehearsing and delivering with confidence.
Every artifact (PPT, LP, LG, LG.md) and every lab is generated from this module
+ data_domainN.py so they stay 100% aligned.

NON-WSQ RULES — the engine enforces these, do not reintroduce them here:
  * NO assessment of any kind (no WA/SAQ, no PP, no case study, no marking).
  * NO SSG / SkillsFuture / WSQ funding or subsidy content.
  * NO TRAQOM survey, NO digital attendance, NO 75% attendance rule.
  * NO TGS course reference — this course carries the plain code C329.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Generative AI for Business Presentation (C329)"
SHORT_TITLE  = "Generative AI for Business Presentation (C329)"   # used in output filenames
COURSE_CODE  = "C329"                                             # non-WSQ code — never a TGS- ref
VERSION      = "v1.0"
VERSION_DATE = "27 July 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 1
MODE         = "Instructor-led, hands-on practical labs"

DARK_THEME = False

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Explain how generative AI supports business presentations, and set up an AI toolkit — general chat assistants (ChatGPT, Claude, Gemini) and an AI slide generator — for presentation work.",
    "LO2: Write effective, structured prompts for presentation tasks and build a reusable prompt library.",
    "LO3: Use generative AI to research a topic and audience and gather validated, fact-checked content for a presentation.",
    "LO4: Shape a clear, audience-centred core message and narrative story for a business presentation with AI.",
    "LO5: Build a complete, slide-by-slide presentation outline from the story with AI.",
    "LO6: Generate concise, on-message slide content and copy with AI, applying the 'one idea per slide' discipline.",
    "LO7: Design professional slides with an AI slide generator and apply visual-design best practices.",
    "LO8: Create clear, honest charts and data visuals from numbers with AI.",
    "LO9: Create on-brand images and per-slide speaker notes with AI.",
    "LO10: Rehearse and deliver the presentation with confidence using AI as a rehearsal partner, and finalise and export the deck.",
]
LO_TITLES = [
    "AI presentation toolkit",
    "Prompting for slides",
    "Research & content",
    "Message & story",
    "Presentation outline",
    "Slide content & copy",
    "AI slide design",
    "Charts & data",
    "Images & speaker notes",
    "Rehearse & deliver",
]

# ------------------------------------------------------------------ topics
# `concepts` are plain strings ("Title — explanation.") so they render cleanly
# as both slide tiles and Learner-Guide bullets. `weighting` = share of course time.
TOPICS = [
    dict(num=1, code="01",
         title="Getting Started with Generative AI for Presentations",
         subtitle="Introduction to generative AI for business presentations · Popular GenAI tools (ChatGPT, Claude and AI slide generators) · Writing effective prompts for presentations · Structuring your message and story",
         weighting="50%",
         concepts=[
            "Generative AI for presentations — a generative AI assistant is a drafting and design partner across the whole presentation workflow; it researches, writes, structures, designs, illustrates and even helps you rehearse, turning hours of slide-making into a fast first draft you refine.",
            "What AI is good (and not good) at — AI is strong at drafting text, structuring ideas, generating layouts and images and suggesting improvements; it does not know your real numbers, your audience or your intent, so you supply the facts and own every claim.",
            "Two kinds of tool, one workflow — general chat assistants (ChatGPT, Claude, Gemini) draft the words, story and data; AI slide generators (Gamma, Microsoft Copilot in PowerPoint, Canva) turn that content into designed slides. A modern presentation workflow uses both together.",
            "Popular GenAI tools — ChatGPT, Claude and Gemini all take a text prompt and return a draft; Gamma, Copilot and Canva generate and design slides from a prompt or outline. The prompting and review skills you learn here transfer across all of them.",
            "The generate–review–refine loop — every AI task follows the same loop: you prompt, the AI drafts, you review it critically, and you refine with follow-up prompts and your own edits until it is right. This loop drives every lab in the course.",
            "Prompting is the core skill — a good presentation prompt gives the AI a role, the context (audience, goal, tone), the exact task, the format you want back and any constraints; a vague ask gives a generic deck, a structured ask gives a usable one.",
            "A reusable prompt library — the same presentation tasks recur every time (research, outline, slide copy, speaker notes, Q&A prep), so you save your best prompts as reusable templates you can run for any future presentation.",
            "Audience first — a business presentation exists to change what one specific audience thinks or does; before any slide you use AI to get clear on who they are, what they care about, and the single action you want from them.",
            "Message and story — a strong presentation carries one core message supported by a simple narrative arc (for example situation → complication → solution → proof → ask); AI helps you find that through-line so the deck persuades rather than just informs.",
            "Human judgement and honesty — AI drafts and suggests, but you check every fact and figure, remove anything invented (a 'hallucination'), keep confidential data out of public tools, and stand behind every claim you present.",
         ]),
    dict(num=2, code="02",
         title="Designing and Delivering AI-Powered Presentations",
         subtitle="Generating slide content and visuals · Designing professional slides with AI · Creating charts, images and speaker notes · Rehearsing and delivering with confidence",
         weighting="50%",
         concepts=[
            "From outline to slide content — AI turns your approved outline into concrete slide copy: a clear headline that states the slide's one idea, a few tight supporting points, and no wall of text; you enforce 'one message per slide'.",
            "Writing for slides, not documents — AI helps you cut wordy paragraphs to scannable phrases, sharpen each headline into a message rather than a topic, and keep a consistent, professional tone across every slide.",
            "AI slide generators — tools such as Gamma, Microsoft Copilot in PowerPoint and Canva take a prompt or an outline and generate a fully designed deck — layouts, theme, fonts and spacing — in seconds, giving you a polished starting point to refine.",
            "Designing professional slides — good slides follow simple rules (clear hierarchy, generous white space, consistent colour and type, one idea per slide); the AI applies a theme and layout, and you refine so each slide is clean, readable and on-brand.",
            "Charts and data visuals — AI helps you turn numbers into the right chart (a trend as a line, parts of a whole as a bar or stacked bar, comparisons as columns), titled and labelled so the chart makes your point at a glance.",
            "Honest data visualisation — AI can format a chart, but you make sure it is truthful: correct numbers, an un-manipulated axis starting at a sensible baseline, and a title that states the real takeaway rather than overselling it.",
            "Images and visuals — AI image generation and stock/icon tools produce on-brand images, icons and backgrounds that support the message; a visual should illustrate the point, not decorate the slide for its own sake.",
            "Speaker notes and script — AI drafts speaker notes or a talking script for each slide, so you say more than the slide shows, keep to time, and sound natural instead of reading bullets aloud.",
            "Rehearsing with AI — you use AI as a rehearsal partner: it anticipates the audience's tough questions, drills your answers, tightens your timing and flow, and gives feedback on clarity so you deliver with confidence.",
            "Delivering and finalising — you finalise and export the deck, prepare a delivery cheat-sheet and a Q&A crib, and remember the room, not the AI, carries the presentation: the tools prepared you, but the delivery is yours.",
         ]),
]

# ------------------------------------------------------------------ day themes
DAY_THEMES = {
    1: "Build the Meridian Fresh pitch deck end to end with AI — set up an AI presentation toolkit and prompt library, research the topic and audience, shape a persuasive message and story, and turn it into a full slide-by-slide outline; then generate the slide content, design the deck with an AI slide generator, create charts, images and speaker notes, and rehearse and deliver it with confidence",
}

# ------------------------------------------------------------------ schedule
# NON-WSQ: no assessment blocks. The day totals exactly 480 scheduled minutes
# (excluding the 1-hour lunch); the 30 minutes of tea breaks sit inside that, so
# the instructional total is 7.5 hours.
def SCHEDULE(lab_titles):
    return {
     1: (DAY_THEMES[1], [
        ("9:00","9:20",20,"admin","Welcome, course introduction, ground rules, and setup: signing in to ChatGPT, Claude and Gemini and to an AI slide generator (Gamma), and confirming each tool is ready for the labs"),
        ("9:20","10:00",40,"topic","TOPIC 01 — Getting Started with Generative AI for Presentations: introduction to generative AI for business presentations; popular GenAI tools (ChatGPT, Claude and AI slide generators); writing effective prompts for presentations; structuring your message and story (concepts + live demo)"),
        ("10:00","10:45",45,"lab","Hands-on: "+lab_titles([1])),
        ("10:45","11:00",15,"break","Tea break"),
        ("11:00","13:00",120,"lab","Hands-on: "+lab_titles([2,3,4])),
        ("13:00","14:00",60,"lunch","Lunch break"),
        ("14:00","14:35",35,"lab","Hands-on: "+lab_titles([5])),
        ("14:35","15:05",30,"topic","TOPIC 02 — Designing and Delivering AI-Powered Presentations: generating slide content and visuals; designing professional slides with AI; creating charts, images and speaker notes; rehearsing and delivering with confidence (concepts + live demo)"),
        ("15:05","16:15",70,"lab","Hands-on: "+lab_titles([6,7])),
        ("16:15","16:30",15,"break","Tea break"),
        ("16:30","17:50",80,"lab","Hands-on: "+lab_titles([8,9,10])),
        ("17:50","18:00",10,"recap","Course wrap-up, delivering the Meridian Fresh pitch deck, responsible-AI and honesty recap, and next steps"),
     ]),
    }

# ------------------------------------------------------------------ deck content
COURSE_OVERVIEW = dict(
    section_title="Course Fundamentals",
    concepts_title="What Generative AI for Presentations Really Is",
    concepts=[
        "A partner for the whole workflow — you describe a presentation task in words and AI returns a usable first draft (research, an outline, slide copy, a chart, images, speaker notes) in seconds, which you then refine.",
        "Two toolsets, one deck — chat assistants (ChatGPT, Claude, Gemini) draft the thinking and words; AI slide generators (Gamma, Copilot, Canva) design the slides. You learn to move content smoothly between them.",
        "Prompt, review, own — the workflow is always the same: give a structured prompt, review and correct the draft, and take ownership of the result. The AI drafts; you decide, fact-check and present.",
        "Story before slides — the craft is not making slides faster; it is being clear on your audience, your one message and your story first, then using AI to build and design a deck that persuades.",
    ],
    framework_title="The AI-Assisted Presentation Workflow",
    framework=[
        ("Research", "Use AI to understand the audience, the topic and the key points, and gather fact-checked material — you supply and verify the real facts and numbers."),
        ("Structure", "Shape one core message and a simple narrative arc, then a slide-by-slide outline, so the deck has a clear through-line before any design."),
        ("Generate", "Turn the outline into concise slide copy, then let an AI slide generator design the deck, and create the charts, images and speaker notes."),
        ("Refine", "Review every slide for message, design, honesty and clarity; tighten copy, fix charts and correct anything the AI invented."),
        ("Deliver", "Rehearse with AI, prepare for questions and timing, finalise and export the deck, and present it with confidence — the delivery is yours."),
    ],
    statement=dict(
        headline="Generative AI gives you a fast first draft of every part of a presentation — the craft is prompting well, telling a clear story, checking the facts, and delivering it yourself with confidence.",
        body="This course is hands-on: you take one business presentation — the pitch deck for Meridian Fresh, a fictional Singapore healthy meal-kit startup seeking approval to expand into three new neighbourhoods — from a blank page to a finished, rehearsed deck, using ChatGPT, Claude, Gemini and an AI slide generator such as Gamma.",
        kicker="THE PRESENTATION RULE",
    ),
    pillars_title="What You'll Build",
    pillars=[
        ("An AI presentation toolkit", ["ChatGPT, Claude, Gemini and Gamma set up", "A reusable presentation prompt library", "Fact-checked research on topic and audience"]),
        ("A clear message and story", ["An audience and objective brief", "One core message and a narrative arc", "A complete slide-by-slide outline"]),
        ("A designed, AI-built deck", ["Concise, on-message slide copy", "A professionally designed slide deck", "Honest charts and on-brand images"]),
        ("A rehearsed, deliverable deck", ["Per-slide speaker notes and a script", "A Q&A crib and a delivery cheat-sheet", "A finalised, exported Meridian Fresh deck"]),
    ],
    arc_title="How Every Lab Works",
    arc=[
        "The trainer demonstrates the AI technique on the shared Meridian Fresh example.",
        "You run it yourself in ChatGPT, Claude, Gemini or your AI slide generator using the supplied Meridian Fresh brief.",
        "You verify the result against the lab's explicit 'Test it' check.",
        "You review and refine — correct the draft, fix any invented fact or figure, and adapt it — until it meets the standard.",
        "You keep the reviewed output — each becomes the next part of your Meridian Fresh pitch deck.",
    ],
)

# ------------------------------------------------------------------ LG content
LG_INTRO = (
    "This Learner Guide accompanies the Generative AI for Business Presentation (C329) course, conducted by "
    "Tertiary Infotech Academy Pte Ltd. It carries the full detail of all 10 hands-on labs, in the order you "
    "will run them, together with the concepts each lab depends on."
)
LG_INTRO2 = (
    "The labs build a single, connected deliverable — the Meridian Fresh pitch deck, a business presentation "
    "for a fictional Singapore healthy meal-kit startup seeking approval to expand into three new "
    "neighbourhoods. You start in Lab 1 by setting up ChatGPT, Claude, Gemini and an AI slide generator as a "
    "presentation toolkit, then in every lab you take the deck one stage further — a reusable prompt library, "
    "fact-checked research on the topic and audience, a clear core message and narrative story, a slide-by-slide "
    "outline, concise slide copy, a professionally designed deck, honest charts, on-brand images, per-slide "
    "speaker notes, and finally a rehearsed, exported presentation ready to deliver. A Meridian Fresh brief "
    "with the facts and figures you need is supplied in labs/reference-pack/; you may substitute your own "
    "non-confidential presentation wherever you prefer."
)
LG_SETUP = dict(
    needs=[
        "A laptop (Windows or Mac) with a modern web browser (Chrome, Edge, Safari or Firefox) and a reliable internet connection — every generative feature runs in the cloud.",
        "Access to at least one general chat assistant — ChatGPT (chat.openai.com), Claude (claude.ai) or Gemini (gemini.google.com); a free account for each is enough to follow the labs, and the trainer will confirm what is available.",
        "Access to one AI slide generator — Gamma (gamma.app) is used in the labs; Microsoft Copilot in PowerPoint or Canva (canva.com) work as alternatives. A free Gamma account is enough to build the deck.",
        "A signed-in account for each tool you will use, tested before Lab 1 with a simple 'hello' prompt so you know it responds, plus somewhere to keep your work (a documents folder or notes app).",
        "The supplied Meridian Fresh brief and fact sheet (company story, audience, traction and financial figures, and expansion plan) in labs/reference-pack/ — or a few notes and non-confidential facts from your own presentation to use instead.",
    ],
    verify_text="Before Lab 1, confirm you can sign in to at least one chat assistant and to an AI slide generator, send a simple prompt and get a reply, and that you have the Meridian Fresh brief to hand. If anything is missing, tell the trainer.",
    verify_code="Open chat.openai.com (ChatGPT) · claude.ai (Claude) · gemini.google.com (Gemini) · gamma.app (Gamma)  ·  sign in  ·  send \"Hello, are you ready to help me build a business presentation?\"  ·  confirm a reply",
    conventions=[
        "Placeholders such as <YOUR TOPIC>, <YOUR AUDIENCE> or <PASTE OUTLINE> are replaced with your own values before you send a prompt.",
        "Prompts to paste into ChatGPT, Claude, Gemini or your AI slide generator are shown in the 'Prompt to use' blocks — adapt the bracketed parts to your own presentation.",
        "Where a lab says 'any assistant', use whichever chat tool you prefer; the AI slide generator steps use Gamma, but Copilot or Canva follow the same idea.",
        "Every lab ends with a 'Test it' step — an explicit check that the reviewed output meets the standard before you move on.",
        "Keep every reviewed output and prompt in one project folder (Meridian-Fresh-Deck) so your presentation and its material stay together and consistent.",
    ],
)
LAB_NOTE = (
    "Use only topics, data and material you are authorised to use. Do not paste confidential company data, "
    "personal information, credentials or unpublished financials into a public AI tool. Use the supplied "
    "Meridian Fresh brief rather than real client material, treat every AI output — especially facts, figures "
    "and charts — as a first draft to be reviewed and fact-checked, and be transparent about AI assistance "
    "where appropriate before the presentation goes to a real audience."
)
LG_WRAPUP = dict(
    title="Wrap-Up",
    intro="You have taken one business presentation — the Meridian Fresh pitch deck — from a blank page to a finished, rehearsed deck in a single day, using ChatGPT, Claude, Gemini and an AI slide generator as drafting and design partners while keeping the story, the facts and the delivery your own.",
    sections=[
        dict(title="What you built", bullets=[
            "An AI presentation toolkit — ChatGPT, Claude, Gemini and an AI slide generator set up, plus a reusable presentation prompt library.",
            "A clear foundation — fact-checked research on the topic and audience, one core message, a narrative story, and a complete slide-by-slide outline.",
            "A designed deck — concise, on-message slide copy turned into a professionally designed presentation with honest charts and on-brand images.",
            "A deliverable deck — per-slide speaker notes and a script, a Q&A crib and delivery cheat-sheet, and a finalised, exported Meridian Fresh pitch deck.",
            "One connected presentation that carries the whole story, slide by slide, ready to present.",
        ]),
        dict(title="What to do next", bullets=[
            "Rebuild a deck for a real, non-confidential presentation of your own using the same workflow and prompt library.",
            "Introduce your saved prompts to your team so everyone drafts research, outlines, copy and speaker notes the same way.",
            "Always start with audience, message and story before you make a single slide — AI makes a clear story faster, not a missing one.",
            "Keep the honesty habit: check every fact, figure and chart, and stand behind every claim before you present it.",
        ]),
    ],
)
LG_NEXT_STEPS = [
    "First pass: complete every lab yourself, following the steps and verifying each 'Test it' check.",
    "Second pass: rebuild the deck for your own real, non-confidential presentation, from research and story to a rehearsed delivery.",
    "Introduce your prompt library and the research → structure → generate → refine → deliver workflow to your team so the practice sticks.",
    "Review each lab's detailed steps in this guide and re-create the presentation in your own AI tools.",
]
LG_GLOSSARY = [
    ("Generative AI assistant", "A general-purpose chat tool (ChatGPT, Claude, Gemini) that generates text drafts and analysis from a prompt."),
    ("AI slide generator", "A tool (Gamma, Microsoft Copilot in PowerPoint, Canva) that generates a fully designed slide deck from a prompt or an outline."),
    ("ChatGPT / Claude / Gemini", "The three widely-used chat assistants used in this course to research, write, structure and refine presentation content."),
    ("Gamma", "The AI slide generator used in the labs (gamma.app); it turns an outline or prompt into a designed deck you then refine."),
    ("Prompt", "The instruction you give the AI; a structured prompt with role, context, task, format and constraints produces a far better draft than a vague one."),
    ("Prompt library", "A saved, reusable set of prompt templates for the recurring presentation tasks — research, outline, slide copy, speaker notes, Q&A prep."),
    ("Generate–review–refine loop", "The core AI workflow — prompt, review the draft critically, then refine with follow-up prompts and your own edits until it is right."),
    ("Audience", "The specific people you are presenting to; their needs, knowledge and priorities shape every decision about message, content and design."),
    ("Objective / the ask", "The single thing you want the audience to think, feel or do as a result of the presentation."),
    ("Core message", "The one sentence you want the audience to remember; every slide should support it."),
    ("Narrative arc / story", "The structure that carries the audience through the presentation, for example situation → complication → solution → proof → ask."),
    ("Situation–Complication–Resolution (SCR)", "A common storytelling structure: set the scene, introduce the problem or tension, then present the resolution."),
    ("Outline", "The slide-by-slide plan of the deck — each slide's headline message, supporting points and suggested visual — agreed before any design."),
    ("Slide copy", "The actual words on a slide: a headline that states the slide's one idea, plus a few concise supporting points."),
    ("One idea per slide", "The discipline of limiting each slide to a single message, so it is clear and easy to follow."),
    ("Headline as a message", "Writing a slide title as the point it makes ('Demand grew 40% in a year') rather than a topic label ('Demand')."),
    ("Speaker notes", "The talking points or script attached to each slide that the presenter uses to say more than the slide shows."),
    ("Chart type", "The form of a data visual chosen to fit the message — line for trends, bar/column for comparisons, stacked bar or pie for parts of a whole."),
    ("Honest data visualisation", "Presenting data truthfully — correct numbers, a sensible axis baseline, and a title that states the real takeaway, not an exaggerated one."),
    ("AI image generation", "Creating images from a text prompt (for example DALL·E in ChatGPT, or the image tools in Gamma and Canva) to illustrate slides."),
    ("Theme / template", "A consistent set of colours, fonts, spacing and layouts applied across the deck to make it look professional and unified."),
    ("Visual hierarchy", "Arranging size, weight, colour and position so the eye sees the most important thing on a slide first."),
    ("White space", "The empty area on a slide; generous white space makes a slide calmer, clearer and more readable."),
    ("Rehearsal", "Practising the delivery — timing, flow and answers to likely questions — here with AI as a rehearsal partner."),
    ("Q&A crib", "A prepared set of the audience's likely questions and your concise answers, ready for the discussion after the talk."),
    ("Human-in-the-loop", "Keeping a person responsible for reviewing, fact-checking, correcting and approving every AI output before it is used."),
    ("Hallucination", "A confident but false or invented statement, fact or figure from an AI, which is why every output must be fact-checked."),
    ("Responsible AI use", "Using AI safely and ethically — protecting confidential data, checking facts, being honest with data, and being transparent about AI assistance."),
    ("Export / deliver", "Saving the finished deck in a presentable format (PowerPoint, PDF or the slide tool's own format) ready to present live or share."),
]

# ------------------------------------------------------------------ version history
VERSION_HISTORY = [
    ("1.0", VERSION_DATE, "Initial release — C329 Generative AI for Business Presentation courseware.", TRAINER),
]

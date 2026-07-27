# Generative AI for Business Presentation (C329) — Learner Guide

**Course Code:** C329  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v1.0 · 27 July 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Preparation](#before-you-start--preparation)
- [Topic 01 — Getting Started with Generative AI for Presentations  (50%)](#topic-01--getting-started-with-generative-ai-for-presentations--50)
  - [Lab 1 — Set Up Your AI Presentation Toolkit](#lab-1--set-up-your-ai-presentation-toolkit)
  - [Lab 2 — Write Effective Prompts for Presentations](#lab-2--write-effective-prompts-for-presentations)
  - [Lab 3 — Research Your Topic and Audience with AI](#lab-3--research-your-topic-and-audience-with-ai)
  - [Lab 4 — Structure Your Message and Story](#lab-4--structure-your-message-and-story)
  - [Lab 5 — Build the Presentation Outline with AI](#lab-5--build-the-presentation-outline-with-ai)
- [Topic 02 — Designing and Delivering AI-Powered Presentations  (50%)](#topic-02--designing-and-delivering-ai-powered-presentations--50)
  - [Lab 6 — Generate Slide Content and Copy with AI](#lab-6--generate-slide-content-and-copy-with-ai)
  - [Lab 7 — Design Professional Slides with an AI Slide Generator](#lab-7--design-professional-slides-with-an-ai-slide-generator)
  - [Lab 8 — Create Charts and Data Visuals with AI](#lab-8--create-charts-and-data-visuals-with-ai)
  - [Lab 9 — Create Images and Speaker Notes with AI](#lab-9--create-images-and-speaker-notes-with-ai)
  - [Lab 10 — Rehearse and Deliver with Confidence](#lab-10--rehearse-and-deliver-with-confidence)
- [Wrap-Up](#wrap-up)
- [Next Steps](#next-steps)
- [Glossary](#glossary)


## Introduction

This Learner Guide accompanies the Generative AI for Business Presentation (C329) course, conducted by Tertiary Infotech Academy Pte Ltd. It carries the full detail of all 10 hands-on labs, in the order you will run them, together with the concepts each lab depends on.

The labs build a single, connected deliverable — the Meridian Fresh pitch deck, a business presentation for a fictional Singapore healthy meal-kit startup seeking approval to expand into three new neighbourhoods. You start in Lab 1 by setting up ChatGPT, Claude, Gemini and an AI slide generator as a presentation toolkit, then in every lab you take the deck one stage further — a reusable prompt library, fact-checked research on the topic and audience, a clear core message and narrative story, a slide-by-slide outline, concise slide copy, a professionally designed deck, honest charts, on-brand images, per-slide speaker notes, and finally a rehearsed, exported presentation ready to deliver. A Meridian Fresh brief with the facts and figures you need is supplied in labs/reference-pack/; you may substitute your own non-confidential presentation wherever you prefer.


## Course Learning Outcomes

- LO1: Explain how generative AI supports business presentations, and set up an AI toolkit — general chat assistants (ChatGPT, Claude, Gemini) and an AI slide generator — for presentation work.
- LO2: Write effective, structured prompts for presentation tasks and build a reusable prompt library.
- LO3: Use generative AI to research a topic and audience and gather validated, fact-checked content for a presentation.
- LO4: Shape a clear, audience-centred core message and narrative story for a business presentation with AI.
- LO5: Build a complete, slide-by-slide presentation outline from the story with AI.
- LO6: Generate concise, on-message slide content and copy with AI, applying the 'one idea per slide' discipline.
- LO7: Design professional slides with an AI slide generator and apply visual-design best practices.
- LO8: Create clear, honest charts and data visuals from numbers with AI.
- LO9: Create on-brand images and per-slide speaker notes with AI.
- LO10: Rehearse and deliver the presentation with confidence using AI as a rehearsal partner, and finalise and export the deck.


## Before You Start — Preparation

**What you need**

- A laptop (Windows or Mac) with a modern web browser (Chrome, Edge, Safari or Firefox) and a reliable internet connection — every generative feature runs in the cloud.
- Access to at least one general chat assistant — ChatGPT (chat.openai.com), Claude (claude.ai) or Gemini (gemini.google.com); a free account for each is enough to follow the labs, and the trainer will confirm what is available.
- Access to one AI slide generator — Gamma (gamma.app) is used in the labs; Microsoft Copilot in PowerPoint or Canva (canva.com) work as alternatives. A free Gamma account is enough to build the deck.
- A signed-in account for each tool you will use, tested before Lab 1 with a simple 'hello' prompt so you know it responds, plus somewhere to keep your work (a documents folder or notes app).
- The supplied Meridian Fresh brief and fact sheet (company story, audience, traction and financial figures, and expansion plan) in labs/reference-pack/ — or a few notes and non-confidential facts from your own presentation to use instead.

**Verify your setup**

Before Lab 1, confirm you can sign in to at least one chat assistant and to an AI slide generator, send a simple prompt and get a reply, and that you have the Meridian Fresh brief to hand. If anything is missing, tell the trainer.

```bash
Open chat.openai.com (ChatGPT) · claude.ai (Claude) · gemini.google.com (Gemini) · gamma.app (Gamma)  ·  sign in  ·  send "Hello, are you ready to help me build a business presentation?"  ·  confirm a reply
```

**Conventions used in every lab**

- Placeholders such as <YOUR TOPIC>, <YOUR AUDIENCE> or <PASTE OUTLINE> are replaced with your own values before you send a prompt.
- Prompts to paste into ChatGPT, Claude, Gemini or your AI slide generator are shown in the 'Prompt to use' blocks — adapt the bracketed parts to your own presentation.
- Where a lab says 'any assistant', use whichever chat tool you prefer; the AI slide generator steps use Gamma, but Copilot or Canva follow the same idea.
- Every lab ends with a 'Test it' step — an explicit check that the reviewed output meets the standard before you move on.
- Keep every reviewed output and prompt in one project folder (Meridian-Fresh-Deck) so your presentation and its material stay together and consistent.


## Topic 01 — Getting Started with Generative AI for Presentations  (50%)

Introduction to generative AI for business presentations · Popular GenAI tools (ChatGPT, Claude and AI slide generators) · Writing effective prompts for presentations · Structuring your message and story

**Key concepts**

- Generative AI for presentations — a generative AI assistant is a drafting and design partner across the whole presentation workflow; it researches, writes, structures, designs, illustrates and even helps you rehearse, turning hours of slide-making into a fast first draft you refine.
- What AI is good (and not good) at — AI is strong at drafting text, structuring ideas, generating layouts and images and suggesting improvements; it does not know your real numbers, your audience or your intent, so you supply the facts and own every claim.
- Two kinds of tool, one workflow — general chat assistants (ChatGPT, Claude, Gemini) draft the words, story and data; AI slide generators (Gamma, Microsoft Copilot in PowerPoint, Canva) turn that content into designed slides. A modern presentation workflow uses both together.
- Popular GenAI tools — ChatGPT, Claude and Gemini all take a text prompt and return a draft; Gamma, Copilot and Canva generate and design slides from a prompt or outline. The prompting and review skills you learn here transfer across all of them.
- The generate–review–refine loop — every AI task follows the same loop: you prompt, the AI drafts, you review it critically, and you refine with follow-up prompts and your own edits until it is right. This loop drives every lab in the course.
- Prompting is the core skill — a good presentation prompt gives the AI a role, the context (audience, goal, tone), the exact task, the format you want back and any constraints; a vague ask gives a generic deck, a structured ask gives a usable one.
- A reusable prompt library — the same presentation tasks recur every time (research, outline, slide copy, speaker notes, Q&A prep), so you save your best prompts as reusable templates you can run for any future presentation.
- Audience first — a business presentation exists to change what one specific audience thinks or does; before any slide you use AI to get clear on who they are, what they care about, and the single action you want from them.
- Message and story — a strong presentation carries one core message supported by a simple narrative arc (for example situation → complication → solution → proof → ask); AI helps you find that through-line so the deck persuades rather than just informs.
- Human judgement and honesty — AI drafts and suggests, but you check every fact and figure, remove anything invented (a 'hallucination'), keep confidential data out of public tools, and stand behind every claim you present.


### Lab 1 — Set Up Your AI Presentation Toolkit

Learning outcome: Sign in to ChatGPT, Claude, Gemini and an AI slide generator (Gamma), run your first prompts, and learn the generate–review–refine loop that every later lab uses..

Goal: This lab gets you comfortable with the tools before any real presentation work begins. You open the chat assistants (ChatGPT, Claude and Gemini), confirm you are signed in, and run a simple prompt so you see how each drafts presentation content, then run the same prompt in a second assistant to feel how they differ. You open an AI slide generator (Gamma), sign in, and generate a quick throwaway deck from a one-line prompt so you can see what a slide generator does. You note what AI is genuinely good at for presentations (a fast draft, structure, design) and where it needs you (real facts, your audience, your judgement). By the end you understand the describe -> generate -> review -> refine loop that is the heart of every lab. BUILDING BLOCK — what you create in this lab becomes part of your Meridian Fresh pitch deck, the connected presentation you assemble across all 10 labs.

**What you'll build**

Your AI presentation toolkit set up and tested — at least one chat assistant and one AI slide generator signed in and responding — a first throwaway AI-generated deck, and a clear, written understanding of the generate–review–refine loop and what AI can and cannot do for you.   (Tools: ChatGPT, Claude, Gemini, Gamma (AI slide generator), account sign-in, first prompts, comparing assistants, the generate–review–refine loop.)

**Step-by-step**

1. Create a project folder on your machine called 'Meridian-Fresh-Deck' so every file and note you make today stays together. Open ChatGPT (chat.openai.com), Claude (claude.ai) and Gemini (gemini.google.com) in browser tabs and confirm you are signed in to at least one.
2. In one chat assistant, run a simple first prompt to see how it drafts presentation content. Paste the prompt below and read the reply.

   ```bash
   You are a presentation coach. In five short bullet points, explain what makes a business pitch deck persuasive to a startup's leadership team and an investor. Keep each bullet to one sentence.
   ```

3. Run the exact same prompt in a second assistant and compare the two replies. Notice differences in tone, length and structure — the skill you learn transfers across all of them, so use whichever you prefer.

   ```bash
   You are a presentation coach. In five short bullet points, explain what makes a business pitch deck persuasive to a startup's leadership team and an investor. Keep each bullet to one sentence.
   ```

4. Open the AI slide generator Gamma (gamma.app), sign in, and use 'Generate' to make a quick throwaway deck from a one-line prompt, so you can see what a slide generator produces. Paste the prompt below.

   ```bash
   A short five-slide business pitch deck for a healthy meal-kit startup expanding into new neighbourhoods, high level and clean.
   ```

5. Look at what Gamma produced — designed slides with layout, theme, fonts and spacing generated in seconds. Note that it is a fast starting point, not a finished deck. You will not keep this one; it is only to feel the tool.
6. In one line each, write what the AI did well (fast draft, structure, instant design) and where it needs you (it does not know Meridian Fresh's real numbers, your audience, or your judgement). This good/not-good picture guides how you use AI all day.
7. Open the supplied Meridian Fresh brief (labs/reference-pack/): the company story, the audience, the traction and financial figures, and the expansion plan. Skim it so you know the presentation you are about to build.
8. Save your notes into your Meridian-Fresh-Deck folder. Write one line, in your own words, describing the generate -> review -> refine loop — you rely on it in every later lab.

**Test it**

You have signed in to at least one chat assistant and to an AI slide generator, run the same prompt in two assistants and compared them, generated a throwaway deck in Gamma, written a one-line note on what AI is and is not good at for presentations, skimmed the Meridian Fresh brief, and described the generate–review–refine loop in your own words — all saved in your Meridian-Fresh-Deck folder.

> **Note:** Full commands and screenshots are in labs/lab-01-*.md. Use only topics, data and material you are authorised to use. Do not paste confidential company data, personal information, credentials or unpublished financials into a public AI tool. Use the supplied Meridian Fresh brief rather than real client material, treat every AI output — especially facts, figures and charts — as a first draft to be reviewed and fact-checked, and be transparent about AI assistance where appropriate before the presentation goes to a real audience.

---


### Lab 2 — Write Effective Prompts for Presentations

Learning outcome: Turn a vague ask into a strong, structured prompt (role, context, task, format, constraints) for presentation tasks, and save a reusable prompt library for the work you repeat every deck..

Goal: A good result starts with a good prompt, not a lucky one. In this lab you read the Meridian Fresh brief and write a deliberately vague prompt first, so you see how generic the result is. You then rebuild it with five clear parts — a role for the AI, the context (audience, goal, tone), the exact task, the format you want back, and any constraints — and watch the draft become genuinely usable. You run small single-change edits to feel how each part matters, then save your best versions as a reusable prompt library with clearly marked slots, covering the tasks you repeat for every presentation: research, outline, slide copy, speaker notes and Q&A prep. BUILDING BLOCK — what you create in this lab becomes part of your Meridian Fresh pitch deck, the connected presentation you assemble across all 10 labs.

**What you'll build**

A structured presentation prompt built from role, context, task, format and constraints, plus a reusable prompt library with clearly marked slots for the recurring presentation tasks, saved in your project folder.   (Tools: ChatGPT / Claude / Gemini, the structured prompt framework (role, context, task, format, constraints), prompt iteration, a reusable prompt library.)

**Step-by-step**

1. Open the Meridian Fresh brief and note two things you will reuse in every prompt: who the audience is (the leadership team plus an investor) and the goal (approve the expansion).
2. Write a deliberately vague first prompt in any assistant and generate, so you can see the generic result. Paste the prompt below and read how unfocused the reply is.

   ```bash
   Write a pitch deck for a meal-kit company.
   ```

3. Rebuild the prompt with a role and the context, and regenerate. Paste the prompt below and compare it with the vague version.

   ```bash
   You are an experienced startup pitch-deck writer. Context: Meridian Fresh is a Singapore healthy meal-kit startup with two strong years in one neighbourhood, now seeking its leadership team's and an investor's approval to expand into three more. Draft the high-level sections a persuasive expansion pitch deck should contain.
   ```

4. Now add the exact task, the format you want back, and clear constraints, and regenerate. Paste the prompt below.

   ```bash
   As the same pitch-deck writer, list the 10 to 12 slides this deck should have. For each slide give a headline that states the slide's point and one line on what it should contain. Present it as a numbered list, keep it concise, and do not invent specific financial figures — leave clear placeholders where real numbers are needed.
   ```

5. Put the vague result and the structured result side by side. Note in one line how much more usable the structured prompt was — this is the core lesson of the day.
6. Run two or three single-change edits to feel how each part steers the result — for example change the audience to 'a room of potential customers', or change the tone to 'formal and data-heavy' — and note which you would keep for Meridian Fresh.
7. Save a reusable prompt library in your project folder: templates for research, outline, slide copy, speaker notes and Q&A prep, each with clearly marked slots — [ROLE], [CONTEXT], [AUDIENCE], [TASK], [FORMAT], [CONSTRAINTS] — that you fill in for any future presentation.

**Test it**

You have compared a vague prompt with a structured one built from role, context, task, format and constraints, seen how much better the structured prompt performs, run single-change edits to feel each part, and saved a reusable prompt library with marked slots for the recurring presentation tasks in your project folder.

> **Note:** Full commands and screenshots are in labs/lab-02-*.md. Use only topics, data and material you are authorised to use. Do not paste confidential company data, personal information, credentials or unpublished financials into a public AI tool. Use the supplied Meridian Fresh brief rather than real client material, treat every AI output — especially facts, figures and charts — as a first draft to be reviewed and fact-checked, and be transparent about AI assistance where appropriate before the presentation goes to a real audience.

---


### Lab 3 — Research Your Topic and Audience with AI

Learning outcome: Use AI to research the audience, the topic and the key points, gather supporting material, and fact-check it so the deck stands on solid, honest ground rather than invented figures..

Goal: A persuasive deck rests on understanding the audience and getting the facts right. In this lab you use a chat assistant to profile your audience (the leadership team and a visiting investor), surface the questions they will ask and what would make them say yes or no, and research the meal-kit market and the problem it solves at a high level. Crucially, you then fact-check: you ask the AI to label which of its own claims and numbers are reliable and which you must verify, and you cross-check every figure against the supplied Meridian Fresh brief — replacing anything the AI invented with the brief's real numbers or a clear [VERIFY] placeholder. This is where you learn to use AI for research without letting it make up your facts. BUILDING BLOCK — what you create in this lab becomes part of your Meridian Fresh pitch deck, the connected presentation you assemble across all 10 labs.

**What you'll build**

An audience profile, a short researched brief of the market and the problem with the key supporting points, and a fact-check pass that labels every claim and number as verified, needing a source, or taken from the supplied brief.   (Tools: ChatGPT / Claude / Gemini, audience analysis, topic research, source and fact checking, separating supplied facts from AI-generated claims.)

**Step-by-step**

1. Open the Meridian Fresh brief and note the audience: the leadership team plus one visiting investor at the quarterly strategy review.
2. Profile the audience with AI so you know what will land. Paste the prompt below.

   ```bash
   You are a communications strategist. My audience is the leadership team of a small Singapore startup plus one visiting investor, at a quarterly strategy review. Profile this audience: what they care about, what they already know, their likely priorities and concerns, and the tone that would land best. Keep it to a short, structured summary.
   ```

3. Ask what this audience will probe, so you can prepare. Paste the prompt below.

   ```bash
   For that same audience and a proposal to expand a meal-kit business into three new neighbourhoods, list the eight toughest questions they are likely to ask, and note what each question is really testing.
   ```

4. Research the problem and market at a high level, keeping general knowledge separate from anything that needs a source. Paste the prompt below.

   ```bash
   Give me a concise, neutral briefing on the healthy meal-kit market and the problem it solves for busy urban professionals. Clearly separate widely-accepted general points from anything that would need a specific source or a recent statistic. Do not invent precise figures.
   ```

5. Fact-check the AI's own briefing — this is the key step. Paste the prompt below and read the labels critically.

   ```bash
   Review the briefing you just gave me. For each factual claim or number, label it [GENERAL KNOWLEDGE], [NEEDS A SOURCE], or [POSSIBLY OUTDATED], and tell me which ones I must verify myself before putting them in a pitch deck.
   ```

6. Cross-check every figure against the supplied Meridian Fresh brief. Use the brief's real traction and financial numbers, and replace any figure the AI invented with the brief's value or a clear [VERIFY] placeholder. Never present an AI-invented number as fact.
7. Save three things in your project folder: the audience profile, the short researched brief of the market and problem, and your fact-check notes marking what is verified, what needs a source, and what came from the brief.

**Test it**

You have used AI to profile the audience and surface their toughest questions, researched the market and problem, run a fact-check pass that labels each claim, and cross-checked every figure against the supplied brief — replacing invented numbers with the brief's real figures or a [VERIFY] placeholder — all saved in your project folder.

> **Note:** Full commands and screenshots are in labs/lab-03-*.md. Use only topics, data and material you are authorised to use. Do not paste confidential company data, personal information, credentials or unpublished financials into a public AI tool. Use the supplied Meridian Fresh brief rather than real client material, treat every AI output — especially facts, figures and charts — as a first draft to be reviewed and fact-checked, and be transparent about AI assistance where appropriate before the presentation goes to a real audience.

---


### Lab 4 — Structure Your Message and Story

Learning outcome: Use AI to find one clear core message and a simple, audience-centred narrative arc, so the presentation persuades rather than just informs — before you build a single slide..

Goal: Slides come later; the story comes first. In this lab you use AI to draft the presentation's core message — the single sentence you want the audience to remember, which is really your ask — generating a few options and refining one. You then ask the AI for two or three alternative narrative structures (for example Situation → Complication → Solution → Proof → Ask, or Problem → Solution → Proof), choose the arc that fits Meridian Fresh, and map your intended sections onto it. Finally you pressure-test the story: you ask the AI which sections do not support the core message so you can cut or merge them, leaving a tight story that flows from a hook to a clear ask. BUILDING BLOCK — what you create in this lab becomes part of your Meridian Fresh pitch deck, the connected presentation you assemble across all 10 labs.

**What you'll build**

One clear, one-sentence core message and a chosen narrative arc (for example situation → complication → solution → proof → ask) for the Meridian Fresh deck, with each planned section mapped to the part of the story it carries.   (Tools: ChatGPT / Claude / Gemini, core-message crafting, narrative arc and storytelling structures (SCR, problem–solution–proof–ask), message testing.)

**Step-by-step**

1. Bring the audience profile and the objective from Lab 3 to hand — the story has to serve that audience and that ask.
2. Draft the core message with AI: the one thing the audience should remember. Paste the prompt below, then pick and refine the strongest option.

   ```bash
   You are a presentation storytelling coach. In one sentence each, give me three options for the single core message a Meridian Fresh expansion pitch should leave in the audience's mind — the one thing they remember. Make them specific and persuasive, not generic.
   ```

3. Ask for alternative story structures and when each works. Paste the prompt below.

   ```bash
   Suggest three ways to structure this pitch as a story — for example Situation–Complication–Resolution, or Problem–Solution–Proof–Ask. For each, give the sequence of sections and one line on when it works best.
   ```

4. Choose one arc and have AI map your sections onto it. Paste the prompt below.

   ```bash
   I'll use a Situation → Complication → Solution → Proof → Ask arc. Map a Meridian Fresh expansion pitch onto it: for each stage, say which section or slide belongs there and the single point it makes.
   ```

5. Pressure-test the story so it stays tight. Paste the prompt below, filling in your planned sections and message.

   ```bash
   Here is my planned section list: [PASTE SECTIONS]. Which of these do not clearly support my core message '[PASTE MESSAGE]', and which could I cut or merge to make the story tighter?
   ```

6. Refine: cut or merge the weak sections the AI flagged, and confirm the story flows from an opening hook to a clear closing ask, with each section earning its place.
7. Save your final core message, the chosen narrative arc, and the section-to-story map in your project folder — this is the spine you turn into a slide outline in Lab 5.

**Test it**

You have a single, clear one-sentence core message, a chosen narrative arc, and a map of each section to the part of the story it carries — pressure-tested so every section supports the message — saved in your project folder.

> **Note:** Full commands and screenshots are in labs/lab-04-*.md. Use only topics, data and material you are authorised to use. Do not paste confidential company data, personal information, credentials or unpublished financials into a public AI tool. Use the supplied Meridian Fresh brief rather than real client material, treat every AI output — especially facts, figures and charts — as a first draft to be reviewed and fact-checked, and be transparent about AI assistance where appropriate before the presentation goes to a real audience.

---


### Lab 5 — Build the Presentation Outline with AI

Learning outcome: Turn the message and story into a complete, slide-by-slide outline — each slide's headline message, supporting points and suggested visual — that you will design in Topic 2..

Goal: Now you bring the research, the message and the arc together into one concrete plan. In this lab you prompt the AI to produce a slide-by-slide outline for the roughly twelve-slide deck: for each slide, a headline written as the point it makes, two or three supporting bullets, and a suggested visual. You review it hard — rewriting any topic-label headline into a real message, enforcing one idea per slide, marking where charts and images belong, and inserting the brief's real figures as placeholders for the data slide. You check the flow and length so the deck opens with a hook and closes with the ask. This outline is the spine of everything you design, write and rehearse in Topic 2. BUILDING BLOCK — what you create in this lab becomes part of your Meridian Fresh pitch deck, the connected presentation you assemble across all 10 labs.

**What you'll build**

A complete, slide-by-slide outline for the roughly twelve-slide Meridian Fresh deck — each slide with a message headline, two or three supporting points and a suggested visual — reviewed for one idea per slide and a clear hook-to-ask flow, ready to design in Topic 2.   (Tools: ChatGPT / Claude / Gemini, slide-by-slide outlining, headline-as-message, one idea per slide, mapping visuals and data placeholders.)

**Step-by-step**

1. Gather your inputs from Labs 3-4: the core message, the narrative arc and section map, and the fact-checked research and figures.
2. Prompt the AI to produce the full slide-by-slide outline. Paste the prompt below, filling in your message, arc and points.

   ```bash
   You are a pitch-deck writer. Using this core message: '[PASTE MESSAGE]', this story arc: '[PASTE ARC]', and these researched points and figures: '[PASTE POINTS]', produce a slide-by-slide outline for a 10 to 12 slide Meridian Fresh expansion pitch. For each slide give: (1) a headline written as the point the slide makes, (2) two or three supporting bullet points, (3) a suggested visual — chart, image, diagram or none. Number the slides.
   ```

3. Fix the headlines: make every one a message, not a topic label. Paste the prompt below.

   ```bash
   Review the slide headlines in this outline. Rewrite any that are topic labels (like 'Market' or 'Financials') into headlines that state the actual point (like 'The healthy meal-kit market is growing fast'). Return the revised outline.
   ```

4. Enforce one idea per slide: split any slide carrying two ideas into two, and merge any thin slide into its neighbour, so each slide makes exactly one point.
5. Mark the visuals: confirm which slide carries the data chart and which carry images, and paste the brief's real figures into the chart slide as a placeholder so you have them ready for Lab 8.
6. Check flow and length: aim for about 10 to 12 slides, confirm it opens with a hook and closes with the ask, and read the headlines alone top to bottom — they should tell the whole story on their own.
7. Save the final outline in your project folder. This is the spine of your deck — you generate its copy in Lab 6, design it in Lab 7, and add charts, images and notes in Labs 8-9.

**Test it**

You have a complete, numbered slide-by-slide outline of about 10 to 12 slides, every headline written as a message, one idea per slide, with charts and images marked and the brief's real figures placed on the data slide — and reading the headlines alone tells the whole story from hook to ask. Saved in your project folder.

> **Note:** Full commands and screenshots are in labs/lab-05-*.md. Use only topics, data and material you are authorised to use. Do not paste confidential company data, personal information, credentials or unpublished financials into a public AI tool. Use the supplied Meridian Fresh brief rather than real client material, treat every AI output — especially facts, figures and charts — as a first draft to be reviewed and fact-checked, and be transparent about AI assistance where appropriate before the presentation goes to a real audience.

---


## Topic 02 — Designing and Delivering AI-Powered Presentations  (50%)

Generating slide content and visuals · Designing professional slides with AI · Creating charts, images and speaker notes · Rehearsing and delivering with confidence

**Key concepts**

- From outline to slide content — AI turns your approved outline into concrete slide copy: a clear headline that states the slide's one idea, a few tight supporting points, and no wall of text; you enforce 'one message per slide'.
- Writing for slides, not documents — AI helps you cut wordy paragraphs to scannable phrases, sharpen each headline into a message rather than a topic, and keep a consistent, professional tone across every slide.
- AI slide generators — tools such as Gamma, Microsoft Copilot in PowerPoint and Canva take a prompt or an outline and generate a fully designed deck — layouts, theme, fonts and spacing — in seconds, giving you a polished starting point to refine.
- Designing professional slides — good slides follow simple rules (clear hierarchy, generous white space, consistent colour and type, one idea per slide); the AI applies a theme and layout, and you refine so each slide is clean, readable and on-brand.
- Charts and data visuals — AI helps you turn numbers into the right chart (a trend as a line, parts of a whole as a bar or stacked bar, comparisons as columns), titled and labelled so the chart makes your point at a glance.
- Honest data visualisation — AI can format a chart, but you make sure it is truthful: correct numbers, an un-manipulated axis starting at a sensible baseline, and a title that states the real takeaway rather than overselling it.
- Images and visuals — AI image generation and stock/icon tools produce on-brand images, icons and backgrounds that support the message; a visual should illustrate the point, not decorate the slide for its own sake.
- Speaker notes and script — AI drafts speaker notes or a talking script for each slide, so you say more than the slide shows, keep to time, and sound natural instead of reading bullets aloud.
- Rehearsing with AI — you use AI as a rehearsal partner: it anticipates the audience's tough questions, drills your answers, tightens your timing and flow, and gives feedback on clarity so you deliver with confidence.
- Delivering and finalising — you finalise and export the deck, prepare a delivery cheat-sheet and a Q&A crib, and remember the room, not the AI, carries the presentation: the tools prepared you, but the delivery is yours.


### Lab 6 — Generate Slide Content and Copy with AI

Learning outcome: Turn the approved outline into concrete slide copy — a message headline and a few tight supporting points per slide — applying 'one idea per slide' and cutting every wall of text..

Goal: With the outline agreed, you write the words that actually go on the slides. In this lab you feed your Lab 5 outline to a chat assistant and have it draft per-slide copy: a headline that states the slide's one point and up to four short supporting bullets. You then edit hard — this is where the discipline lives. You check each slide carries one idea, ask the AI to cut every bullet to a scannable phrase, run a consistency pass so the tone and voice match across the deck, and remove or mark any claim or number you cannot back with the brief. The result is clean, on-message copy ready to pour into an AI slide generator in Lab 7. BUILDING BLOCK — what you create in this lab becomes part of your Meridian Fresh pitch deck, the connected presentation you assemble across all 10 labs.

**What you'll build**

Concise, on-message slide copy for every slide of the Meridian Fresh deck — a headline and a few tight supporting points each — edited for one idea per slide and a consistent, professional tone.   (Tools: ChatGPT / Claude / Gemini, slide copywriting, headline writing, bullet tightening, one idea per slide, consistent tone.)

**Step-by-step**

1. Open your Lab 5 slide-by-slide outline — it is the input for every step of this lab.
2. Generate the slide copy for the whole deck. Paste the prompt below, with your outline pasted in.

   ```bash
   You are a slide copywriter. For each slide in this outline: '[PASTE OUTLINE]', write the on-slide copy — a headline that states the slide's one point, and up to four short supporting bullets. Do not write paragraphs; this is text for slides, not a document.
   ```

3. Review each slide for one idea. If a slide's copy is really making two points, split it into two slides; if a slide is thin, merge it into a neighbour. The copy must respect one idea per slide.
4. Tighten every bullet. Paste the prompt below.

   ```bash
   Tighten this slide copy: cut every bullet to a scannable phrase of at most about eight words, keep the meaning, and remove filler words. Return the revised copy.
   ```

5. Run a consistency pass. Paste the prompt below.

   ```bash
   Make the tone consistent and professional across all slides, and flag any bullet that is really two ideas so I can split it onto separate slides.
   ```

6. Do an honesty pass: remove or replace any claim or number you cannot back with the Meridian Fresh brief, inserting a clear [VERIFY] placeholder where you still need to confirm a figure. Nothing you cannot defend stays on a slide.
7. Save the finished slide copy in your project folder. This is exactly what you pour into the AI slide generator in Lab 7.

**Test it**

You have concise, on-message copy for every slide — a message headline plus a few tight bullets — respecting one idea per slide, with a consistent professional tone and every unverifiable claim removed or marked [VERIFY]. Saved and ready to design.

> **Note:** Full commands and screenshots are in labs/lab-06-*.md. Use only topics, data and material you are authorised to use. Do not paste confidential company data, personal information, credentials or unpublished financials into a public AI tool. Use the supplied Meridian Fresh brief rather than real client material, treat every AI output — especially facts, figures and charts — as a first draft to be reviewed and fact-checked, and be transparent about AI assistance where appropriate before the presentation goes to a real audience.

---


### Lab 7 — Design Professional Slides with an AI Slide Generator

Learning outcome: Import your outline and copy into an AI slide generator (Gamma, or Copilot/Canva), generate a designed deck, apply a consistent theme, and refine the layout using visual-design best practices..

Goal: Now you turn the words into a designed deck. In this lab you paste your Lab 6 slide copy into Gamma (Microsoft Copilot in PowerPoint or Canva work the same way) and generate a fully designed presentation — layouts, theme, fonts and spacing — in seconds. You choose a theme whose colours and fonts suit Meridian Fresh: fresh, healthy and premium but approachable. Then you refine, because a generated deck is a strong start, not the finish: you fix any slide that breaks one-idea-per-slide, improve the visual hierarchy so the headline reads first, add generous white space, and make headings, alignment and spacing consistent across every slide. You leave clear placeholders where the chart and images will go. BUILDING BLOCK — what you create in this lab becomes part of your Meridian Fresh pitch deck, the connected presentation you assemble across all 10 labs.

**What you'll build**

A professionally designed Meridian Fresh deck generated with an AI slide generator, with a consistent theme (colours, fonts, spacing) and each slide refined for clear visual hierarchy, generous white space and one idea per slide — with placeholders where the chart and images belong.   (Tools: Gamma (or Microsoft Copilot in PowerPoint / Canva), generating a deck from an outline, themes and templates, visual hierarchy, white space, consistency.)

**Step-by-step**

1. Open Gamma (gamma.app), start a new presentation, and choose the option to generate from pasted text or an outline (in Copilot or Canva, choose the equivalent 'create from outline / text' option).
2. Paste your Lab 6 slide copy and generate the deck, guiding the design with a short instruction. Paste the instruction below along with your copy.

   ```bash
   Generate a clean, professional business pitch deck from this content. Keep one idea per slide, minimal text, a clear headline on each slide, and leave room for a chart and images. [PASTE SLIDE COPY]
   ```

3. Choose a theme whose colours and fonts suit Meridian Fresh — fresh and healthy, premium but approachable (for example a clean green-and-neutral palette with a friendly, readable font) — and apply it across all slides so the deck is unified.
4. Refine the layout slide by slide: confirm one idea per slide, make the headline the most prominent element (clear visual hierarchy), and give each slide generous white space so it is not cramped. Change the card or layout on any slide that is too busy.
5. Make it consistent: the same heading style, alignment and spacing on every slide, and remove any clutter or default filler text the generator added. Consistency is what makes a deck look professional.
6. Leave clear placeholders where the outline marked a chart (the data slide) and images (title, problem, solution, expansion). You build the chart in Lab 8 and add images in Lab 9.
7. Name and save the deck in your slide generator (for example 'Meridian Fresh — Expansion Pitch'). This designed deck is the canvas for the rest of the course.

**Test it**

You have generated a designed Meridian Fresh deck with an AI slide generator, applied a consistent on-brand theme, refined every slide for one idea per slide, clear hierarchy and white space, made headings and spacing consistent, and left clear placeholders for the chart and images — saved in the tool.

> **Note:** Full commands and screenshots are in labs/lab-07-*.md. Use only topics, data and material you are authorised to use. Do not paste confidential company data, personal information, credentials or unpublished financials into a public AI tool. Use the supplied Meridian Fresh brief rather than real client material, treat every AI output — especially facts, figures and charts — as a first draft to be reviewed and fact-checked, and be transparent about AI assistance where appropriate before the presentation goes to a real audience.

---


### Lab 8 — Create Charts and Data Visuals with AI

Learning outcome: Turn the Meridian Fresh figures into one clear, honest chart — the right type, titled and labelled to make its point — and place it on the data slide of the deck..

Goal: A pitch needs a convincing data slide, and this is where honesty matters most. In this lab you take the real traction and financial figures from the Meridian Fresh brief, ask the AI which chart type best carries your message and why, and have it structure the numbers into a clean table — without changing a single figure. You create the chart in your slide tool (or in Excel/Sheets and paste it in), title it as its takeaway rather than a label, and label the axes and units. Then you run an honesty check: you ask the AI to critique the chart for anything misleading — a truncated axis, a cherry-picked range, an overstated title — and you fix it, so the chart makes your point truthfully. BUILDING BLOCK — what you create in this lab becomes part of your Meridian Fresh pitch deck, the connected presentation you assemble across all 10 labs.

**What you'll build**

One clear, honest chart built from the Meridian Fresh figures — the right chart type for the message, titled as its takeaway and correctly labelled — placed on the data slide of the deck.   (Tools: ChatGPT / Claude / Gemini, Gamma / Canva / Excel charts, choosing a chart type, chart titling and labelling, honest data visualisation.)

**Step-by-step**

1. Open the Meridian Fresh brief and copy out the real figures you will chart — for example the subscriber or revenue numbers over the last eight quarters, and the expansion projection. Keep the numbers exactly as the brief states them.
2. Ask the AI which chart type fits your message. Paste the prompt below.

   ```bash
   I want to show that Meridian Fresh's subscriber base has grown steadily over eight quarters. Which chart type best communicates a trend over time to a leadership audience, and why? Suggest a clear title that states the takeaway.
   ```

3. Have the AI structure your numbers into a clean table, without changing them. Paste the prompt below with your figures.

   ```bash
   Here are my figures: [PASTE FIGURES FROM BRIEF]. Put them into a clean table ready to turn into a chart. Do not change any number; if anything is unclear, ask rather than guess.
   ```

4. Create the chart: in Gamma or Canva insert a chart and enter the table, or build it in Excel/Google Sheets and paste it onto the slide. Choose the chart type the AI recommended and confirm every value matches the brief.
5. Title the chart as its takeaway, not a label — for example 'Subscribers grew three-fold in two years' rather than 'Subscribers' — and label the axes with their units so the chart is readable on its own.
6. Run the honesty check. Paste the prompt below and fix whatever it flags.

   ```bash
   Critique this chart for honesty and clarity: is the axis baseline sensible, is the time range fair, is anything exaggerated or missing, and does the title match the data? Suggest fixes.
   ```

7. Place the finished, corrected chart on the data slide of your deck and save. The chart should make your growth point truthfully and at a glance.

**Test it**

You have chosen the right chart type for your message, built the chart from the brief's exact figures, titled it as its takeaway and labelled the axes, run an honesty check and fixed any misleading element, and placed the finished chart on the data slide of the deck.

> **Note:** Full commands and screenshots are in labs/lab-08-*.md. Use only topics, data and material you are authorised to use. Do not paste confidential company data, personal information, credentials or unpublished financials into a public AI tool. Use the supplied Meridian Fresh brief rather than real client material, treat every AI output — especially facts, figures and charts — as a first draft to be reviewed and fact-checked, and be transparent about AI assistance where appropriate before the presentation goes to a real audience.

---


### Lab 9 — Create Images and Speaker Notes with AI

Learning outcome: Generate on-brand images that support the message and draft per-slide speaker notes, so the slides look right and you can present them without reading the bullets aloud..

Goal: Two finishing layers turn a designed deck into one you can stand up and deliver. First, you use AI image generation (DALL·E in ChatGPT, or the image tools in Gamma or Canva) to create on-brand visuals for the key slides — title, problem, solution and expansion — keeping the style consistent and making sure each image supports the point rather than decorating the slide. You check the images are appropriate and licence-clear (no real logos or identifiable people) and disclose AI use where appropriate. Then you generate speaker notes for every slide: a short spoken script in your own voice, timed to your slot, that says more than the slide shows so you never simply read the bullets. BUILDING BLOCK — what you create in this lab becomes part of your Meridian Fresh pitch deck, the connected presentation you assemble across all 10 labs.

**What you'll build**

On-brand images placed on the key slides (supporting the message, appropriate and licence-checked), plus concise per-slide speaker notes or a script that let you present without reading the slides and keep to time.   (Tools: AI image generation (DALL·E / Gamma / Canva), image prompting, image licensing and appropriateness check, speaker-notes / script generation, timing.)

**Step-by-step**

1. Decide which slides need an image — usually the title, the problem, the solution and the expansion slides — and note in one line what each image should show and the mood it should set.
2. Generate an on-brand image for one slide. Paste the image prompt below into your image tool.

   ```bash
   A clean, warm, photographic-style image of a freshly prepared healthy meal kit with fresh vegetables on a bright kitchen counter, appetising and premium but approachable, no text and no logos, suitable as a title-slide background for a food brand.
   ```

3. Generate the other images the same way, keeping the style consistent (same look, lighting and palette) so the deck feels like one brand. Check each image genuinely supports its slide's point rather than just decorating it.
4. Check appropriateness and licensing: no real company logos or identifiable real people, confirm your tool's usage terms allow business use, and note where you will disclose that images are AI-generated. Replace anything you are unsure about.
5. Place the images on their slides, keeping the layout clean — the image supports the headline, it does not bury it. Adjust size and position so text stays readable.
6. Generate per-slide speaker notes. Paste the prompt below with your outline or slide copy.

   ```bash
   You are a presentation coach. For each slide in this deck: '[PASTE OUTLINE OR COPY]', write speaker notes of two or three sentences that expand on the slide without repeating the bullets, in a warm, confident spoken voice. Note roughly how many seconds each slide should take so the whole talk fits in 12 minutes.
   ```

7. Review the notes: make sure they sound like you, fit your time slot, and add to the slide rather than reading it. Trim anything that overruns, then save the deck with its images and speaker notes.

**Test it**

You have generated consistent, on-brand images that support the key slides and are appropriate and licence-checked, placed them cleanly, and drafted concise per-slide speaker notes timed to a 12-minute talk that expand on the slides rather than repeat them — all saved with the deck.

> **Note:** Full commands and screenshots are in labs/lab-09-*.md. Use only topics, data and material you are authorised to use. Do not paste confidential company data, personal information, credentials or unpublished financials into a public AI tool. Use the supplied Meridian Fresh brief rather than real client material, treat every AI output — especially facts, figures and charts — as a first draft to be reviewed and fact-checked, and be transparent about AI assistance where appropriate before the presentation goes to a real audience.

---


### Lab 10 — Rehearse and Deliver with Confidence

Learning outcome: Use AI as a rehearsal partner to anticipate tough questions, tighten timing and flow, build a Q&A crib and a delivery cheat-sheet, then finalise and export the deck ready to present..

Goal: The last mile is delivery, and AI makes a strong rehearsal partner. In this lab you give the AI a short summary of your deck, then run a mock Q&A in which it plays a sceptical investor and drills you with hard questions one at a time. You build a Q&A crib of the likely questions and honest answers in your own words, get feedback on where the story drags or where you will overrun your time, and turn that into a one-page delivery cheat-sheet — your opening line, key transitions, the ask, and per-section timing. Finally you finalise the deck with a proofreading and consistency pass, confirm every fact and figure is verified, and export it (PowerPoint or PDF). That completes the Meridian Fresh pitch deck, end to end. BUILDING BLOCK — what you create in this lab becomes part of your Meridian Fresh pitch deck, the connected presentation you assemble across all 10 labs.

**What you'll build**

A rehearsed presentation — a Q&A crib of likely questions and your answers, a one-page delivery cheat-sheet (opening, transitions, timing, the ask), a final proofread and consistency pass, and the finished Meridian Fresh deck exported (PowerPoint or PDF) ready to present.   (Tools: ChatGPT / Claude / Gemini as a rehearsal partner, mock Q&A, timing and flow feedback, a Q&A crib, a delivery cheat-sheet, finalising and exporting the deck.)

**Step-by-step**

1. Write a short summary of your deck — the core message, the sections in order, and the ask — to give the AI the context it needs to rehearse you well.
2. Run a live mock Q&A. Paste the prompt below and answer each question out loud before reading the next.

   ```bash
   You are a sceptical investor at a startup strategy review. I'm pitching Meridian Fresh's expansion into three neighbourhoods. Ask me your toughest questions one at a time, wait for my answer, then push back if it is weak. Start now.
   ```

3. Build a Q&A crib. Paste the prompt below, then edit the answers into your own words.

   ```bash
   Based on this deck summary: '[PASTE SUMMARY]', list the ten questions this audience is most likely to ask, and draft a concise, honest answer to each that I can adapt into my own words.
   ```

4. Get flow and timing feedback. Paste the prompt below with your outline and notes.

   ```bash
   Here is my outline and speaker notes: '[PASTE]'. My slot is 12 minutes plus Q&A. Tell me where the story drags, where I risk running over time, and what to cut or shorten.
   ```

5. Build a one-page delivery cheat-sheet: your opening line, the key transitions between sections, the exact wording of your ask, and a per-section timing plan so you land inside 12 minutes.
6. Finalise the deck. Paste the prompt below to proofread, fix what it finds, and confirm every fact and number is verified against the brief with no [VERIFY] placeholders left.

   ```bash
   Proofread all the copy in this deck: '[PASTE COPY]'. Fix spelling, grammar and inconsistent capitalisation or tone, and flag any claim that sounds too strong to defend. Return a clean version.
   ```

7. Export the finished deck (PowerPoint or PDF from Gamma) and save it with your cheat-sheet and Q&A crib in your project folder. This complete, rehearsed presentation is the deliverable the whole course set out to build — and remember, the room carries the talk, not the AI.

**Test it**

You have rehearsed with a mock Q&A, built a Q&A crib and a one-page delivery cheat-sheet, tightened the story and timing to fit 12 minutes, proofread and finalised the deck with every figure verified and no [VERIFY] placeholders left, and exported the finished Meridian Fresh pitch deck (PowerPoint or PDF) ready to present.

> **Note:** Full commands and screenshots are in labs/lab-10-*.md. Use only topics, data and material you are authorised to use. Do not paste confidential company data, personal information, credentials or unpublished financials into a public AI tool. Use the supplied Meridian Fresh brief rather than real client material, treat every AI output — especially facts, figures and charts — as a first draft to be reviewed and fact-checked, and be transparent about AI assistance where appropriate before the presentation goes to a real audience.

---


## Wrap-Up

You have taken one business presentation — the Meridian Fresh pitch deck — from a blank page to a finished, rehearsed deck in a single day, using ChatGPT, Claude, Gemini and an AI slide generator as drafting and design partners while keeping the story, the facts and the delivery your own.

**What you built**

- An AI presentation toolkit — ChatGPT, Claude, Gemini and an AI slide generator set up, plus a reusable presentation prompt library.
- A clear foundation — fact-checked research on the topic and audience, one core message, a narrative story, and a complete slide-by-slide outline.
- A designed deck — concise, on-message slide copy turned into a professionally designed presentation with honest charts and on-brand images.
- A deliverable deck — per-slide speaker notes and a script, a Q&A crib and delivery cheat-sheet, and a finalised, exported Meridian Fresh pitch deck.
- One connected presentation that carries the whole story, slide by slide, ready to present.

**What to do next**

- Rebuild a deck for a real, non-confidential presentation of your own using the same workflow and prompt library.
- Introduce your saved prompts to your team so everyone drafts research, outlines, copy and speaker notes the same way.
- Always start with audience, message and story before you make a single slide — AI makes a clear story faster, not a missing one.
- Keep the honesty habit: check every fact, figure and chart, and stand behind every claim before you present it.

---


## Next Steps

- First pass: complete every lab yourself, following the steps and verifying each 'Test it' check.
- Second pass: rebuild the deck for your own real, non-confidential presentation, from research and story to a rehearsed delivery.
- Introduce your prompt library and the research → structure → generate → refine → deliver workflow to your team so the practice sticks.
- Review each lab's detailed steps in this guide and re-create the presentation in your own AI tools.


## Glossary

- **Generative AI assistant** — A general-purpose chat tool (ChatGPT, Claude, Gemini) that generates text drafts and analysis from a prompt.
- **AI slide generator** — A tool (Gamma, Microsoft Copilot in PowerPoint, Canva) that generates a fully designed slide deck from a prompt or an outline.
- **ChatGPT / Claude / Gemini** — The three widely-used chat assistants used in this course to research, write, structure and refine presentation content.
- **Gamma** — The AI slide generator used in the labs (gamma.app); it turns an outline or prompt into a designed deck you then refine.
- **Prompt** — The instruction you give the AI; a structured prompt with role, context, task, format and constraints produces a far better draft than a vague one.
- **Prompt library** — A saved, reusable set of prompt templates for the recurring presentation tasks — research, outline, slide copy, speaker notes, Q&A prep.
- **Generate–review–refine loop** — The core AI workflow — prompt, review the draft critically, then refine with follow-up prompts and your own edits until it is right.
- **Audience** — The specific people you are presenting to; their needs, knowledge and priorities shape every decision about message, content and design.
- **Objective / the ask** — The single thing you want the audience to think, feel or do as a result of the presentation.
- **Core message** — The one sentence you want the audience to remember; every slide should support it.
- **Narrative arc / story** — The structure that carries the audience through the presentation, for example situation → complication → solution → proof → ask.
- **Situation–Complication–Resolution (SCR)** — A common storytelling structure: set the scene, introduce the problem or tension, then present the resolution.
- **Outline** — The slide-by-slide plan of the deck — each slide's headline message, supporting points and suggested visual — agreed before any design.
- **Slide copy** — The actual words on a slide: a headline that states the slide's one idea, plus a few concise supporting points.
- **One idea per slide** — The discipline of limiting each slide to a single message, so it is clear and easy to follow.
- **Headline as a message** — Writing a slide title as the point it makes ('Demand grew 40% in a year') rather than a topic label ('Demand').
- **Speaker notes** — The talking points or script attached to each slide that the presenter uses to say more than the slide shows.
- **Chart type** — The form of a data visual chosen to fit the message — line for trends, bar/column for comparisons, stacked bar or pie for parts of a whole.
- **Honest data visualisation** — Presenting data truthfully — correct numbers, a sensible axis baseline, and a title that states the real takeaway, not an exaggerated one.
- **AI image generation** — Creating images from a text prompt (for example DALL·E in ChatGPT, or the image tools in Gamma and Canva) to illustrate slides.
- **Theme / template** — A consistent set of colours, fonts, spacing and layouts applied across the deck to make it look professional and unified.
- **Visual hierarchy** — Arranging size, weight, colour and position so the eye sees the most important thing on a slide first.
- **White space** — The empty area on a slide; generous white space makes a slide calmer, clearer and more readable.
- **Rehearsal** — Practising the delivery — timing, flow and answers to likely questions — here with AI as a rehearsal partner.
- **Q&A crib** — A prepared set of the audience's likely questions and your concise answers, ready for the discussion after the talk.
- **Human-in-the-loop** — Keeping a person responsible for reviewing, fact-checking, correcting and approving every AI output before it is used.
- **Hallucination** — A confident but false or invented statement, fact or figure from an AI, which is why every output must be fact-checked.
- **Responsible AI use** — Using AI safely and ethically — protecting confidential data, checking facts, being honest with data, and being transparent about AI assistance.
- **Export / deliver** — Saving the finished deck in a presentable format (PowerPoint, PDF or the slide tool's own format) ready to present live or share.

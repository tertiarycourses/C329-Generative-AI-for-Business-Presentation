"""
Domain 2 — Designing and Delivering AI-Powered Presentations. Labs 6-10.

THE CONNECTED PROJECT CONTINUES — the same Meridian Fresh pitch deck, now built,
designed and delivered.

Lab 6 turns the outline into concise slide copy; Lab 7 designs the deck with an
AI slide generator; Lab 8 creates an honest data chart from the brief's figures;
Lab 9 adds on-brand images and per-slide speaker notes; Lab 10 rehearses with AI,
builds a Q&A crib and delivery cheat-sheet, and finalises and exports the deck.
Use your own non-confidential presentation instead of Meridian Fresh wherever you
prefer.
"""

PROJECT_NOTE = (
 "BUILDING BLOCK — what you create in this lab becomes part of your Meridian Fresh pitch deck, "
 "the connected presentation you assemble across all 10 labs."
)

DOMAIN2 = [
 dict(
 num=6, topic=2,
 title="Generate Slide Content and Copy with AI",
 objective="Turn the approved outline into concrete slide copy — a message headline and a few tight supporting points per slide — applying 'one idea per slide' and cutting every wall of text.",
 desc="With the outline agreed, you write the words that actually go on the slides. In this lab you feed your "
 "Lab 5 outline to a chat assistant and have it draft per-slide copy: a headline that states the slide's one "
 "point and up to four short supporting bullets. You then edit hard — this is where the discipline lives. You "
 "check each slide carries one idea, ask the AI to cut every bullet to a scannable phrase, run a consistency "
 "pass so the tone and voice match across the deck, and remove or mark any claim or number you cannot back "
 "with the brief. The result is clean, on-message copy ready to pour into an AI slide generator in Lab 7. " + PROJECT_NOTE,
 build="Concise, on-message slide copy for every slide of the Meridian Fresh deck — a headline and a few tight supporting points each — edited for one idea per slide and a consistent, professional tone.",
 services="ChatGPT / Claude / Gemini, slide copywriting, headline writing, bullet tightening, one idea per slide, consistent tone",
 steps=[
 ("Open your Lab 5 slide-by-slide outline — it is the input for every step of this lab.", ""),
 ("Generate the slide copy for the whole deck. Paste the prompt below, with your outline pasted in.",
  "You are a slide copywriter. For each slide in this outline: '[PASTE OUTLINE]', write the on-slide copy — a headline that states the slide's one point, and up to four short supporting bullets. Do not write paragraphs; this is text for slides, not a document."),
 ("Review each slide for one idea. If a slide's copy is really making two points, split it into two slides; if a slide is thin, merge it into a neighbour. The copy must respect one idea per slide.", ""),
 ("Tighten every bullet. Paste the prompt below.",
  "Tighten this slide copy: cut every bullet to a scannable phrase of at most about eight words, keep the meaning, and remove filler words. Return the revised copy."),
 ("Run a consistency pass. Paste the prompt below.",
  "Make the tone consistent and professional across all slides, and flag any bullet that is really two ideas so I can split it onto separate slides."),
 ("Do an honesty pass: remove or replace any claim or number you cannot back with the Meridian Fresh brief, inserting a clear [VERIFY] placeholder where you still need to confirm a figure. Nothing you cannot defend stays on a slide.", ""),
 ("Save the finished slide copy in your project folder. This is exactly what you pour into the AI slide generator in Lab 7.", ""),
 ],
 test="You have concise, on-message copy for every slide — a message headline plus a few tight bullets — respecting one idea per slide, with a consistent professional tone and every unverifiable claim removed or marked [VERIFY]. Saved and ready to design.",
 ),
 dict(
 num=7, topic=2,
 title="Design Professional Slides with an AI Slide Generator",
 objective="Import your outline and copy into an AI slide generator (Gamma, or Copilot/Canva), generate a designed deck, apply a consistent theme, and refine the layout using visual-design best practices.",
 desc="Now you turn the words into a designed deck. In this lab you paste your Lab 6 slide copy into Gamma "
 "(Microsoft Copilot in PowerPoint or Canva work the same way) and generate a fully designed presentation — "
 "layouts, theme, fonts and spacing — in seconds. You choose a theme whose colours and fonts suit Meridian "
 "Fresh: fresh, healthy and premium but approachable. Then you refine, because a generated deck is a strong "
 "start, not the finish: you fix any slide that breaks one-idea-per-slide, improve the visual hierarchy so "
 "the headline reads first, add generous white space, and make headings, alignment and spacing consistent "
 "across every slide. You leave clear placeholders where the chart and images will go. " + PROJECT_NOTE,
 build="A professionally designed Meridian Fresh deck generated with an AI slide generator, with a consistent theme (colours, fonts, spacing) and each slide refined for clear visual hierarchy, generous white space and one idea per slide — with placeholders where the chart and images belong.",
 services="Gamma (or Microsoft Copilot in PowerPoint / Canva), generating a deck from an outline, themes and templates, visual hierarchy, white space, consistency",
 steps=[
 ("Open Gamma (gamma.app), start a new presentation, and choose the option to generate from pasted text or an outline (in Copilot or Canva, choose the equivalent 'create from outline / text' option).", ""),
 ("Paste your Lab 6 slide copy and generate the deck, guiding the design with a short instruction. Paste the instruction below along with your copy.",
  "Generate a clean, professional business pitch deck from this content. Keep one idea per slide, minimal text, a clear headline on each slide, and leave room for a chart and images. [PASTE SLIDE COPY]"),
 ("Choose a theme whose colours and fonts suit Meridian Fresh — fresh and healthy, premium but approachable (for example a clean green-and-neutral palette with a friendly, readable font) — and apply it across all slides so the deck is unified.", ""),
 ("Refine the layout slide by slide: confirm one idea per slide, make the headline the most prominent element (clear visual hierarchy), and give each slide generous white space so it is not cramped. Change the card or layout on any slide that is too busy.", ""),
 ("Make it consistent: the same heading style, alignment and spacing on every slide, and remove any clutter or default filler text the generator added. Consistency is what makes a deck look professional.", ""),
 ("Leave clear placeholders where the outline marked a chart (the data slide) and images (title, problem, solution, expansion). You build the chart in Lab 8 and add images in Lab 9.", ""),
 ("Name and save the deck in your slide generator (for example 'Meridian Fresh — Expansion Pitch'). This designed deck is the canvas for the rest of the course.", ""),
 ],
 test="You have generated a designed Meridian Fresh deck with an AI slide generator, applied a consistent on-brand theme, refined every slide for one idea per slide, clear hierarchy and white space, made headings and spacing consistent, and left clear placeholders for the chart and images — saved in the tool.",
 ),
 dict(
 num=8, topic=2,
 title="Create Charts and Data Visuals with AI",
 objective="Turn the Meridian Fresh figures into one clear, honest chart — the right type, titled and labelled to make its point — and place it on the data slide of the deck.",
 desc="A pitch needs a convincing data slide, and this is where honesty matters most. In this lab you take the "
 "real traction and financial figures from the Meridian Fresh brief, ask the AI which chart type best carries "
 "your message and why, and have it structure the numbers into a clean table — without changing a single "
 "figure. You create the chart in your slide tool (or in Excel/Sheets and paste it in), title it as its "
 "takeaway rather than a label, and label the axes and units. Then you run an honesty check: you ask the AI "
 "to critique the chart for anything misleading — a truncated axis, a cherry-picked range, an overstated "
 "title — and you fix it, so the chart makes your point truthfully. " + PROJECT_NOTE,
 build="One clear, honest chart built from the Meridian Fresh figures — the right chart type for the message, titled as its takeaway and correctly labelled — placed on the data slide of the deck.",
 services="ChatGPT / Claude / Gemini, Gamma / Canva / Excel charts, choosing a chart type, chart titling and labelling, honest data visualisation",
 steps=[
 ("Open the Meridian Fresh brief and copy out the real figures you will chart — for example the subscriber or revenue numbers over the last eight quarters, and the expansion projection. Keep the numbers exactly as the brief states them.", ""),
 ("Ask the AI which chart type fits your message. Paste the prompt below.",
  "I want to show that Meridian Fresh's subscriber base has grown steadily over eight quarters. Which chart type best communicates a trend over time to a leadership audience, and why? Suggest a clear title that states the takeaway."),
 ("Have the AI structure your numbers into a clean table, without changing them. Paste the prompt below with your figures.",
  "Here are my figures: [PASTE FIGURES FROM BRIEF]. Put them into a clean table ready to turn into a chart. Do not change any number; if anything is unclear, ask rather than guess."),
 ("Create the chart: in Gamma or Canva insert a chart and enter the table, or build it in Excel/Google Sheets and paste it onto the slide. Choose the chart type the AI recommended and confirm every value matches the brief.", ""),
 ("Title the chart as its takeaway, not a label — for example 'Subscribers grew three-fold in two years' rather than 'Subscribers' — and label the axes with their units so the chart is readable on its own.", ""),
 ("Run the honesty check. Paste the prompt below and fix whatever it flags.",
  "Critique this chart for honesty and clarity: is the axis baseline sensible, is the time range fair, is anything exaggerated or missing, and does the title match the data? Suggest fixes."),
 ("Place the finished, corrected chart on the data slide of your deck and save. The chart should make your growth point truthfully and at a glance.", ""),
 ],
 test="You have chosen the right chart type for your message, built the chart from the brief's exact figures, titled it as its takeaway and labelled the axes, run an honesty check and fixed any misleading element, and placed the finished chart on the data slide of the deck.",
 ),
 dict(
 num=9, topic=2,
 title="Create Images and Speaker Notes with AI",
 objective="Generate on-brand images that support the message and draft per-slide speaker notes, so the slides look right and you can present them without reading the bullets aloud.",
 desc="Two finishing layers turn a designed deck into one you can stand up and deliver. First, you use AI "
 "image generation (DALL·E in ChatGPT, or the image tools in Gamma or Canva) to create on-brand visuals for "
 "the key slides — title, problem, solution and expansion — keeping the style consistent and making sure each "
 "image supports the point rather than decorating the slide. You check the images are appropriate and "
 "licence-clear (no real logos or identifiable people) and disclose AI use where appropriate. Then you "
 "generate speaker notes for every slide: a short spoken script in your own voice, timed to your slot, that "
 "says more than the slide shows so you never simply read the bullets. " + PROJECT_NOTE,
 build="On-brand images placed on the key slides (supporting the message, appropriate and licence-checked), plus concise per-slide speaker notes or a script that let you present without reading the slides and keep to time.",
 services="AI image generation (DALL·E / Gamma / Canva), image prompting, image licensing and appropriateness check, speaker-notes / script generation, timing",
 steps=[
 ("Decide which slides need an image — usually the title, the problem, the solution and the expansion slides — and note in one line what each image should show and the mood it should set.", ""),
 ("Generate an on-brand image for one slide. Paste the image prompt below into your image tool.",
  "A clean, warm, photographic-style image of a freshly prepared healthy meal kit with fresh vegetables on a bright kitchen counter, appetising and premium but approachable, no text and no logos, suitable as a title-slide background for a food brand."),
 ("Generate the other images the same way, keeping the style consistent (same look, lighting and palette) so the deck feels like one brand. Check each image genuinely supports its slide's point rather than just decorating it.", ""),
 ("Check appropriateness and licensing: no real company logos or identifiable real people, confirm your tool's usage terms allow business use, and note where you will disclose that images are AI-generated. Replace anything you are unsure about.", ""),
 ("Place the images on their slides, keeping the layout clean — the image supports the headline, it does not bury it. Adjust size and position so text stays readable.", ""),
 ("Generate per-slide speaker notes. Paste the prompt below with your outline or slide copy.",
  "You are a presentation coach. For each slide in this deck: '[PASTE OUTLINE OR COPY]', write speaker notes of two or three sentences that expand on the slide without repeating the bullets, in a warm, confident spoken voice. Note roughly how many seconds each slide should take so the whole talk fits in 12 minutes."),
 ("Review the notes: make sure they sound like you, fit your time slot, and add to the slide rather than reading it. Trim anything that overruns, then save the deck with its images and speaker notes.", ""),
 ],
 test="You have generated consistent, on-brand images that support the key slides and are appropriate and licence-checked, placed them cleanly, and drafted concise per-slide speaker notes timed to a 12-minute talk that expand on the slides rather than repeat them — all saved with the deck.",
 ),
 dict(
 num=10, topic=2,
 title="Rehearse and Deliver with Confidence",
 objective="Use AI as a rehearsal partner to anticipate tough questions, tighten timing and flow, build a Q&A crib and a delivery cheat-sheet, then finalise and export the deck ready to present.",
 desc="The last mile is delivery, and AI makes a strong rehearsal partner. In this lab you give the AI a short "
 "summary of your deck, then run a mock Q&A in which it plays a sceptical investor and drills you with hard "
 "questions one at a time. You build a Q&A crib of the likely questions and honest answers in your own words, "
 "get feedback on where the story drags or where you will overrun your time, and turn that into a one-page "
 "delivery cheat-sheet — your opening line, key transitions, the ask, and per-section timing. Finally you "
 "finalise the deck with a proofreading and consistency pass, confirm every fact and figure is verified, and "
 "export it (PowerPoint or PDF). That completes the Meridian Fresh pitch deck, end to end. " + PROJECT_NOTE,
 build="A rehearsed presentation — a Q&A crib of likely questions and your answers, a one-page delivery cheat-sheet (opening, transitions, timing, the ask), a final proofread and consistency pass, and the finished Meridian Fresh deck exported (PowerPoint or PDF) ready to present.",
 services="ChatGPT / Claude / Gemini as a rehearsal partner, mock Q&A, timing and flow feedback, a Q&A crib, a delivery cheat-sheet, finalising and exporting the deck",
 steps=[
 ("Write a short summary of your deck — the core message, the sections in order, and the ask — to give the AI the context it needs to rehearse you well.", ""),
 ("Run a live mock Q&A. Paste the prompt below and answer each question out loud before reading the next.",
  "You are a sceptical investor at a startup strategy review. I'm pitching Meridian Fresh's expansion into three neighbourhoods. Ask me your toughest questions one at a time, wait for my answer, then push back if it is weak. Start now."),
 ("Build a Q&A crib. Paste the prompt below, then edit the answers into your own words.",
  "Based on this deck summary: '[PASTE SUMMARY]', list the ten questions this audience is most likely to ask, and draft a concise, honest answer to each that I can adapt into my own words."),
 ("Get flow and timing feedback. Paste the prompt below with your outline and notes.",
  "Here is my outline and speaker notes: '[PASTE]'. My slot is 12 minutes plus Q&A. Tell me where the story drags, where I risk running over time, and what to cut or shorten."),
 ("Build a one-page delivery cheat-sheet: your opening line, the key transitions between sections, the exact wording of your ask, and a per-section timing plan so you land inside 12 minutes.", ""),
 ("Finalise the deck. Paste the prompt below to proofread, fix what it finds, and confirm every fact and number is verified against the brief with no [VERIFY] placeholders left.",
  "Proofread all the copy in this deck: '[PASTE COPY]'. Fix spelling, grammar and inconsistent capitalisation or tone, and flag any claim that sounds too strong to defend. Return a clean version."),
 ("Export the finished deck (PowerPoint or PDF from Gamma) and save it with your cheat-sheet and Q&A crib in your project folder. This complete, rehearsed presentation is the deliverable the whole course set out to build — and remember, the room carries the talk, not the AI.", ""),
 ],
 test="You have rehearsed with a mock Q&A, built a Q&A crib and a one-page delivery cheat-sheet, tightened the story and timing to fit 12 minutes, proofread and finalised the deck with every figure verified and no [VERIFY] placeholders left, and exported the finished Meridian Fresh pitch deck (PowerPoint or PDF) ready to present.",
 ),
]

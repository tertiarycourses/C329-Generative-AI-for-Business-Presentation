#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generate the labs/ markdown from the SAME single source as the deck/LP/LG
(course_data.py + data_domainN.py), so labs stay 100% aligned with the other
artifacts. Emits labs/lab-NN-*.md, labs/README.md and refreshes nothing else
(tools.md and the brief pack are hand-authored). Enrichment sections
(Prerequisites, Troubleshooting, Challenge, Reflection, Deliverable) live in the
ENRICH table below, keyed by lab number.

Run:  python gen_labs.py
"""
import os, re, sys, glob, importlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import course_data as C


def find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env):
        return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return os.path.dirname(os.path.dirname(start))


REPO = find_repo(HERE)
LABS = os.path.join(REPO, "labs")

# ------------------------------------------------------------------ load labs
DOMS = []
for f in sorted(glob.glob(os.path.join(HERE, "data_domain[0-9]*.py"))):
    mod = importlib.import_module(os.path.splitext(os.path.basename(f))[0])
    key = [k for k in dir(mod) if k.startswith("DOMAIN")][0]
    DOMS.append((getattr(mod, key), getattr(mod, "SCENARIO", None)))

LABSLIST = []
SCENARIO = None
for dom, scen in DOMS:
    if scen and not SCENARIO:
        SCENARIO = scen
    LABSLIST.extend(dom)

TOPIC_TITLE = {t["num"]: t["title"] for t in C.TOPICS}

# ------------------------------------------------------------------ approx minutes per lab
# Derived from the schedule lab blocks so the labs match the Lesson Plan timing.
def lab_titles(nums):
    return "; ".join("" for _ in nums)


def approx_minutes():
    sched = C.SCHEDULE(lambda nums: "\x00".join(str(n) for n in nums))
    mins = {}
    for _day, (_theme, rows) in sched.items():
        for row in rows:
            if row[3] == "lab":
                nums = [int(x) for x in row[4].split("Hands-on: ")[-1].split("\x00")]
                per = round(row[2] / len(nums))
                for n in nums:
                    mins[n] = per
    return mins


MINS = approx_minutes()

# ------------------------------------------------------------------ per-lab enrichment
ENRICH = {
 1: dict(
    prereqs=[
        "A laptop with a modern web browser (Chrome, Edge, Safari or Firefox) and a reliable internet connection.",
        "An account for at least one chat assistant (ChatGPT, Claude or Gemini) and one AI slide generator (Gamma).",
        "The supplied Meridian Fresh brief to hand (labs/reference-pack/).",
    ],
    trouble=[
        "**A tool won't let you sign in or generate.** Try a different one — you only need one chat assistant and one slide generator to follow the labs; tell the trainer what you have.",
        "**Gamma's deck looks nothing like a real pitch.** That's expected from a one-line prompt — it's only a warm-up; you build the real deck from a proper outline in Labs 5-7.",
        "**The two assistants give very different answers.** That's normal — they differ in tone and length; the prompting and review skills you learn work across all of them.",
    ],
    challenge="Ask a third assistant the same question and rank the three answers — which was most useful, and why?",
    lo=1,
    deliverable="Keep your Meridian-Fresh-Deck folder with your toolkit notes and the brief — it is the home for everything you build across the next labs.",
 ),
 2: dict(
    prereqs=[
        "Completed Lab 1 (your tools are set up and responding).",
        "The supplied Meridian Fresh brief open (labs/reference-pack/).",
    ],
    trouble=[
        "**The AI's draft is generic.** Add a role and real context (audience, goal, tone); a vague prompt always gives a generic deck.",
        "**The AI invents specific numbers.** Tell it explicitly not to invent figures and to leave placeholders — you add the brief's real numbers in Lab 3.",
        "**The reply is the wrong length or format.** State the format you want (a numbered list, a word limit, bullets only) as a constraint and regenerate.",
    ],
    challenge="Write a structured prompt for a completely different presentation of your own using the same five parts, proving the template travels beyond Meridian Fresh.",
    lo=2,
    deliverable="Keep your reusable prompt library — you run its templates for research, outline, copy, notes and Q&A in every later lab.",
 ),
 3: dict(
    prereqs=[
        "Completed Lab 2 (you can write structured prompts).",
        "The supplied Meridian Fresh brief with the real figures to hand.",
    ],
    trouble=[
        "**The AI states a statistic as fact.** Treat every number it produces as unverified — label it, and use only the brief's figures or a [VERIFY] placeholder in the deck.",
        "**The audience profile is generic.** Give more context about the specific people (their roles, what they have seen before, their concerns) and regenerate.",
        "**Research drifts off-topic.** Narrow the prompt to the one question you need answered, and ask for general knowledge kept separate from anything needing a source.",
    ],
    challenge="Ask the AI to argue the investor's case against your proposal, then note the two objections you most need to answer in the deck.",
    lo=3,
    deliverable="Keep your audience profile, researched brief and fact-check notes — the honest foundation the rest of the deck rests on.",
 ),
 4: dict(
    prereqs=[
        "Completed Lab 3 (you know the audience and the verified facts).",
        "Your objective — the single action you want from the audience — clear.",
    ],
    trouble=[
        "**The core message is vague.** Push for specificity — name the audience, the change and the ask in one sentence; reject generic 'we should grow' statements.",
        "**The story doesn't flow.** Try a different arc (SCR, or problem–solution–proof–ask) and see which carries your points more naturally.",
        "**Every section feels essential.** Ask the AI which single section to cut if you had only half the time — it forces priorities.",
    ],
    challenge="Rewrite your core message for a different audience (say, potential customers instead of investors) and note how the whole story would change.",
    lo=4,
    deliverable="Keep your core message, chosen arc and section map — the spine you turn into a slide outline in Lab 5.",
 ),
 5: dict(
    prereqs=[
        "Completed Lab 4 (you have a core message and a story arc).",
        "Your fact-checked figures ready to place on the data slide.",
    ],
    trouble=[
        "**The outline has too many slides.** Ask the AI to cut it to 10-12 slides, keeping one idea per slide; a shorter deck is almost always stronger.",
        "**Headlines are topic labels, not messages.** Rewrite each as the point it makes; read alone, the headlines should tell the whole story.",
        "**Two ideas are crammed on one slide.** Split it — one idea per slide keeps the audience with you.",
    ],
    challenge="Read only your slide headlines aloud, top to bottom. If they don't tell the story on their own, revise them until they do.",
    lo=5,
    deliverable="Keep the final slide-by-slide outline — it is the spine you design, write, chart, illustrate and rehearse across Topic 2.",
 ),
 6: dict(
    prereqs=[
        "Completed Lab 5 (you have an approved slide-by-slide outline).",
        "Any chat assistant open.",
    ],
    trouble=[
        "**Slides are walls of text.** Cut every bullet to a scannable phrase; if you are writing sentences, they belong in speaker notes, not on the slide.",
        "**The copy repeats the headline.** Bullets should add to the headline, not restate it — ask the AI to make each a distinct supporting point.",
        "**Tone drifts across slides.** Run the consistency-pass prompt so voice and capitalisation match everywhere.",
    ],
    challenge="Take your busiest slide and cut it to a single sentence plus one image — often the strongest version of a slide.",
    lo=6,
    deliverable="Keep the finished slide copy — it is exactly what you pour into the AI slide generator in Lab 7.",
 ),
 7: dict(
    prereqs=[
        "Completed Lab 6 (you have clean, one-idea-per-slide copy).",
        "An AI slide generator account (Gamma, or Microsoft Copilot in PowerPoint / Canva).",
    ],
    trouble=[
        "**The generated design is cluttered.** Pick a simpler theme and reduce text per slide; the generator reflects what you gave it, so tighten the copy first.",
        "**Slides look inconsistent.** Apply one theme across the whole deck and fix heading style, alignment and spacing slide by slide.",
        "**A generated layout buries the headline.** Change the card or layout so the headline is the largest, first thing the eye meets.",
    ],
    challenge="Regenerate the same content with a second theme and compare — a quick way to see which visual style suits the brand.",
    lo=7,
    deliverable="Keep the designed deck in your slide generator, with placeholders for the chart and images — the canvas for Labs 8-9.",
 ),
 8: dict(
    prereqs=[
        "Completed Lab 7 (you have a designed deck with a data-slide placeholder).",
        "The brief's real figures ready to chart.",
    ],
    trouble=[
        "**The chart type doesn't fit the message.** Match the type to the point — line for a trend, column/bar for comparisons, stacked bar or pie for parts of a whole.",
        "**The chart looks impressive but misleading.** Start the axis at a sensible baseline and show a fair time range; run the honesty-check prompt and fix what it flags.",
        "**The numbers don't match the brief.** Re-enter them exactly — never let the AI 'tidy' or round your real figures.",
    ],
    challenge="Make a second chart of the same data with a truncated axis, then compare — see for yourself how easily a chart can mislead, and why the honest version matters.",
    lo=8,
    deliverable="Keep the honest, titled chart on the data slide — the evidence your whole pitch leans on.",
 ),
 9: dict(
    prereqs=[
        "Completed Lab 8 (the deck has its data slide).",
        "An image tool (DALL·E in ChatGPT, or the image features in Gamma / Canva).",
    ],
    trouble=[
        "**The image looks off-brand.** Add style, mood and palette words to the image prompt and regenerate; keep every image in the same style.",
        "**The image has garbled text or a fake logo.** Prompt 'no text, no logos' and regenerate; AI image text is unreliable — add real text on the slide instead.",
        "**Speaker notes just repeat the bullets.** Ask for notes that expand on the slide in a spoken voice and add what the slide doesn't say.",
    ],
    challenge="Generate an alternative image for your title slide in a completely different style, and decide which better fits Meridian Fresh.",
    lo=9,
    deliverable="Keep the deck with on-brand images and per-slide speaker notes — it now looks right and is ready to rehearse.",
 ),
 10: dict(
    prereqs=[
        "Completed Labs 1-9 (you have a finished, illustrated, annotated deck).",
        "Somewhere you can rehearse the mock Q&A aloud.",
    ],
    trouble=[
        "**The mock investor is too easy.** Tell it to be tougher and more sceptical, and to challenge every unsupported claim.",
        "**You keep running over 12 minutes.** Cut slides or trim speaker notes; a tight, shorter talk beats a rushed full one.",
        "**A [VERIFY] placeholder is still in the deck.** Do not present it — confirm the figure against the brief or remove the claim before you finalise.",
    ],
    challenge="Record yourself delivering the pitch once, then ask the AI to critique a transcript of it for clarity and filler words.",
    lo=10,
    deliverable="Keep the complete, exported Meridian Fresh pitch deck with its cheat-sheet and Q&A crib — the finished, rehearsed presentation the course set out to build.",
 ),
}


def slug(title):
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    if len(s) > 60:
        s = s[:60].rstrip("-")
    return s


def steps_md(steps):
    out = []
    for i, (instr, cmd) in enumerate(steps, 1):
        out.append(f"### Step {i}\n\n{instr}")
        if cmd:
            out.append("Prompt to use (paste into your AI assistant — ChatGPT, Claude, Gemini or your slide generator):\n\n```text\n" + cmd + "\n```")
    return "\n\n".join(out)


def lab_filename(lab):
    return f"lab-{lab['num']:02d}-{slug(lab['title'])}.md"


def build_lab(lab):
    e = ENRICH[lab["num"]]
    topic = lab["topic"]
    mins = MINS.get(lab["num"], 40)
    parts = []
    parts.append(f"# Lab {lab['num']} — {lab['title']}\n")
    parts.append(
        f"**Topic 0{topic}:** {TOPIC_TITLE[topic]}  |  **Day 1**  |  "
        f"**Approx. {mins} min**  |  **Course:** {C.TITLE}\n"
    )
    if SCENARIO:
        parts.append("## Scenario\n\n" + SCENARIO + "\n")
    parts.append("## Goal\n\n" + lab["objective"] + "\n")
    parts.append("## What you'll build\n\n" + lab["build"] + "\n")
    parts.append("**Tools and techniques:** " + lab["services"] + "\n")
    parts.append("## Prerequisites\n\n" + "\n".join("- " + p for p in e["prereqs"]) + "\n")
    parts.append("## Steps\n\n" + steps_md(lab["steps"]) + "\n")
    parts.append("## Test it\n\n" + lab["test"] + "\n")
    parts.append("## Troubleshooting\n\n" + "\n".join("- " + t for t in e["trouble"]) + "\n")
    parts.append("## Challenge\n\n" + e["challenge"] + "\n")
    lo = C.LEARNING_OUTCOMES[e["lo"] - 1]
    lo_text = lo.split(":", 1)[1].strip().rstrip(".")
    parts.append(f"## Reflection\n\nLO{e['lo']} — In your own words: {lo_text}?\n")
    parts.append("## Deliverable\n\n" + e["deliverable"] + "\n")
    parts.append("---\n")
    parts.append(
        f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · © 2026 {C.ORG}*"
    )
    return "\n".join(parts) + "\n"


def build_readme(files):
    rows = []
    for lab in LABSLIST:
        fn = files[lab["num"]]
        rows.append(
            f"| 1 | 0{lab['topic']} | {lab['num']:02d} | [{lab['title']}]({fn}) |"
        )
    md = []
    md.append(f"# Labs — {C.TITLE}\n")
    md.append(f"**Course Code:** {C.COURSE_CODE}  |  **Version {C.VERSION} · {C.VERSION_DATE}**\n")
    md.append(
        "All 10 labs build one connected **Meridian Fresh pitch deck**, which you begin in Lab 1 and finish in "
        "Lab 10 — from a blank page, through ChatGPT, Claude and Gemini for research, story and slide copy, into "
        "an AI slide generator (Gamma) for a designed deck, and out as a deck with honest charts, on-brand "
        "images and speaker notes, rehearsed with AI and exported ready to present. A Meridian Fresh brief with "
        "the facts and figures you need is supplied in `reference-pack/`; use your own non-confidential "
        "presentation wherever you prefer. There is **no assessment** — each lab verifies itself with a 'Test "
        "it' step.\n"
    )
    md.append("| Day | Topic | Lab | Title |")
    md.append("|---:|---|---:|---|")
    md.extend(rows)
    md.append("")
    md.append("## Tools\n")
    md.append("See [tools.md](tools.md) for the accounts and tools used across the labs, and "
              "[reference-pack/](reference-pack/) for the Meridian Fresh brief.")
    return "\n".join(md) + "\n"


def main():
    os.makedirs(LABS, exist_ok=True)
    # remove stale lab-*.md so renamed labs don't linger
    for old in glob.glob(os.path.join(LABS, "lab-*.md")):
        os.remove(old)
    files = {}
    for lab in LABSLIST:
        fn = lab_filename(lab)
        files[lab["num"]] = fn
        with open(os.path.join(LABS, fn), "w", encoding="utf-8") as fh:
            fh.write(build_lab(lab))
        print("wrote labs/" + fn)
    with open(os.path.join(LABS, "README.md"), "w", encoding="utf-8") as fh:
        fh.write(build_readme(files))
    print("wrote labs/README.md")


if __name__ == "__main__":
    main()

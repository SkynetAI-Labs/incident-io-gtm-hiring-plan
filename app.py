from html import escape
import json
from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(page_title="incident.io | Four live searches | Adam Baig", page_icon="◎", layout="wide")
ROOT = Path(__file__).resolve().parent
ROLES = json.loads(r'''[
  {
    "name": "Account Executive",
    "short": "Commercial AE",
    "pay": "£155k–£170k",
    "url": "https://incident.io/careers/98029f7e-a460-4785-bc95-6cc813ff8d4b",
    "fact": "Full-cycle outbound selling to technical buyers; the role page describes $40k–$50k deals and roughly 45-day cycles, working with a BDR and Solutions Engineer.",
    "share": 30,
    "target": 45,
    "outcome": "Add productive closing capacity without hiring someone who depends on inbound.",
    "signals": [
      "Personally built pipeline and closed comparable deals; distinguish sourced, influenced and closed revenue.",
      "Can explain a technical buyer’s problem in plain language and work effectively with an SE.",
      "Knows why a deal was lost and what they changed afterwards."
    ],
    "question": "Walk me through one deal you sourced yourself: first contact, buyer, deal value, sales cycle, objections and your own contribution.",
    "pools": "Developer tools and infrastructure SaaS teams: Datadog, Grafana Labs, Sentry, GitLab and PostHog. Verify UK team presence and each person’s deal motion before outreach.",
    "query": "site:linkedin.com/in (\"account executive\" OR \"commercial account executive\") (\"developer tools\" OR observability OR infrastructure) (London OR \"United Kingdom\") -jobs -recruiter",
    "assessment": "A short discovery role-play with an engineering leader, followed by a deal review. Sales leadership owns the assessment of commercial depth.",
    "message": "Hi [Name], your work on [verified account or market detail] caught my attention. incident.io is hiring a London AE to own outbound deals with engineering leaders, working in a BDR/AE/SE pod. If you’re looking for more ownership, would a short conversation be useful?",
    "risk": "Good CVs but little self-generated revenue",
    "trigger": "After eight screens, fewer than two show credible outbound ownership",
    "action": "Recalibrate the source companies and test self-generated pipeline earlier."
  },
  {
    "name": "Business Development Representative",
    "short": "BDR",
    "pay": "£65k–£70k",
    "url": "https://incident.io/careers/9310b907-e008-4d7d-a898-e82db447d97f",
    "fact": "A phone-led outbound role with account research, personalised outreach and a development path into the wider GTM team.",
    "share": 15,
    "target": 30,
    "outcome": "Build qualified pipeline and a future AE talent bench.",
    "signals": [
      "Can research an account and explain why a particular person should take a call.",
      "Responds constructively to feedback and rejection.",
      "Shows clear motivation for sales; consider credible career changers alongside existing BDRs."
    ],
    "question": "Pick an engineering-led company. Who would you call, why now, and how would you open the conversation?",
    "pools": "London SDR/BDR teams selling technical software, plus referral and career-change channels. Assess candidates on evidence rather than university, hobbies or employer prestige.",
    "query": "site:linkedin.com/in (SDR OR BDR OR \"sales development\") (SaaS OR software OR cloud) London -jobs -recruiter",
    "assessment": "A brief research task and cold-call role-play. Give feedback and repeat part of the call to see how they apply coaching.",
    "message": "Hi [Name], I noticed [verified example of initiative]. incident.io is growing its London BDR team. It’s a researched, phone-led role with close AE support and a genuine development path. Would you be open to hearing what the work involves?",
    "risk": "Lots of replies, weak motivation or call readiness",
    "trigger": "Positive replies do not translate into qualified screens",
    "action": "Clarify the phone-led nature of the role in the first message and add a short coaching exercise."
  },
  {
    "name": "Commercial Customer Success Manager",
    "short": "Commercial CSM",
    "pay": "£85k–£118k",
    "url": "https://incident.io/careers/932fa4f8-f583-411d-bcd6-03a459fabcd1",
    "fact": "The role covers 70–80 commercial accounts, combining adoption, scalable customer programmes, risk identification and expansion partnership.",
    "share": 25,
    "target": 45,
    "outcome": "Protect the customer experience as the commercial customer base grows.",
    "signals": [
      "Can prioritise a sizeable account book without only serving the loudest customers.",
      "Uses adoption and account signals to identify risk and opportunity.",
      "Can work credibly with technical users and describe personal ownership of a renewal or onboarding outcome."
    ],
    "question": "You inherit 75 accounts. Which do you contact first, what information do you need, and what can be handled through a shared programme?",
    "pools": "Commercial CS teams at developer-tool, API, cloud and observability vendors. Include scaled-CS operators with relevant technical customers, not only people carrying an identical title.",
    "query": "site:linkedin.com/in (\"customer success manager\" OR \"commercial CSM\") (API OR developer OR observability OR cloud) (London OR \"United Kingdom\") -jobs",
    "assessment": "An anonymised portfolio-prioritisation exercise. Ask for a plan covering at-risk accounts, onboarding and a one-to-many programme.",
    "message": "Hi [Name], your experience with [verified customer segment] looks relevant to a Commercial CSM role at incident.io. The work combines technical customers, account ownership and building a more scalable CS approach. Open to a quick conversation about the scope?",
    "risk": "Strong relationship skills but weak portfolio discipline",
    "trigger": "Candidates cannot explain how they prioritise a large account book",
    "action": "Screen for an actual portfolio example and expand mapping into scaled-CS teams."
  },
  {
    "name": "Customer Success Engineer",
    "short": "Customer Success Engineer",
    "pay": "£100k–£130k",
    "url": "https://incident.io/careers/30dda1df-3d27-4054-ac40-1afac9103ae6",
    "fact": "The first EMEA Customer Success Engineer is a post-sales technical partner for complex migrations, onboarding architecture and scalable customer configuration.",
    "share": 30,
    "target": 60,
    "outcome": "Add technical capacity for complex implementations and reduce migration risk.",
    "signals": [
      "Has personally designed or led a complex SaaS migration or implementation.",
      "Can explain operational continuity, ownership and trade-offs to a customer.",
      "Distinguishes technical architecture work from CSM relationship ownership and reactive support."
    ],
    "question": "Talk me through a migration you owned: the starting system, risks, design decisions, rollout, rollback and how you knew it worked.",
    "pools": "Customer engineers, technical account managers, implementation architects and professional services engineers in infrastructure SaaS. Adjacent pools to validate: PagerDuty, Atlassian, Datadog and Grafana Labs.",
    "query": "site:linkedin.com/in (\"customer engineer\" OR \"implementation architect\" OR \"technical account manager\" OR \"professional services engineer\") (SaaS OR observability OR \"incident management\") (London OR \"United Kingdom\") -jobs",
    "assessment": "A hypothetical migration discussion with an engineering assessor. Test clear thinking, safe rollout and stakeholder communication; do not ask for confidential customer designs.",
    "message": "Hi [Name], your experience with [verified implementation detail] stood out. incident.io is hiring its first EMEA Customer Success Engineer to help customers design migrations and scale their setup. It looks like a chance to shape the function as well as deliver the work. Worth a brief conversation?",
    "risk": "Mapping drifts into support-only or pre-sales-only profiles",
    "trigger": "Early profiles lack personal implementation ownership",
    "action": "Compare adjacent titles in calibration and put a migration example at the centre of screening."
  }
]''')
st.markdown("""
    <style>
    :root { color-scheme: light; }
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] { background:#F8F7F4!important; color:#242329!important; }
    [data-testid="stHeader"] { background:transparent!important; }
    .block-container { max-width:1240px; padding:2.5rem 2.5rem 4rem; }
    .stApp { font-family:Inter,Arial,sans-serif; }
    .stApp p,.stApp li,.stApp label,.stApp [data-testid="stCaptionContainer"] { color:#514D4A; line-height:1.75; }
    .stApp h1,.stApp h2,.stApp h3,.stApp h4 { color:#242329; letter-spacing:-.035em; }
    .stApp h2 { font-size:1.85rem; padding-top:.5rem; }
    .stApp h3 { font-size:1.2rem; margin-top:1rem; }
    .stApp a { color:#BD412F; text-underline-offset:4px; }
    .banner { position:relative; overflow:hidden; background:linear-gradient(115deg,#242329 15%,#41312F 70%,#BD412F); border-radius:24px; padding:3rem 3.2rem 2.6rem; margin-bottom:1.4rem; box-shadow:0 16px 40px #24232914; border:1px solid #ffffff28; }
    .banner:after { content:""; position:absolute; width:350px; height:350px; border:1px solid #8DB0F230; border-radius:50%; right:-160px; top:-110px; box-shadow:0 0 0 60px #8DB0F20a,0 0 0 120px #8DB0F208; pointer-events:none; }
    .stApp .banner h1 { position:relative; z-index:1; color:#FFFFFF!important; -webkit-text-fill-color:#FFFFFF!important; font-size:clamp(2rem,3.7vw,3.25rem); line-height:1.12; max-width:850px; margin:.95rem 0 1.1rem; padding:0; font-weight:750; letter-spacing:-.045em; }
    .stApp .banner .sub { color:#F2E8E1!important; font-size:1.06rem; max-width:720px; line-height:1.6; }
    .stApp .banner .tag { display:inline-block; color:#FFB49C!important; background:#FFB49C12; border:1px solid #FFB49C55; font-size:.68rem; text-transform:uppercase; letter-spacing:.15em; font-weight:700; padding:.45rem .75rem; border-radius:6px; }
    .stApp .banner .by,.stApp .banner .by b { color:#FFFFFF!important; font-size:.88rem; line-height:1.8; }
    .stApp .banner .by { border-top:1px solid #ffffff25; padding-top:1.3rem; margin-top:1.8rem; margin-bottom:0; }
    .stApp .banner a { color:#FFB49C!important; text-decoration:none; font-weight:600; }
    .banner a:hover { text-decoration:underline; }
    .kpis { display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:14px; margin-bottom:1.8rem; }
    .kpi { background:#FFFFFF; border:1px solid #E5E0DA; border-radius:14px; padding:1.3rem 1.4rem; position:relative; }
    .kpi:before { content:""; display:block; width:25px; height:4px; border-radius:4px; background:#FFB49C; margin-bottom:.75rem; }
    .kpi .v { color:#242329; font-weight:750; font-size:1.95rem; letter-spacing:-.045em; line-height:1.15; }
    .kpi .l { color:#706964; font-size:.78rem; margin-top:.5rem; }
    .stTabs [data-baseweb="tab-list"] { gap:5px; flex-wrap:wrap; height:auto; background:transparent; padding:0 0 1.1rem; }
    .stTabs [data-baseweb="tab"] { background:#FFFFFF; border:1px solid #E5E0DA; border-radius:8px; padding:.6rem .85rem; height:auto; min-height:42px; white-space:normal; }
    .stTabs [data-baseweb="tab"] p { color:#615A55!important; font-size:.77rem; font-weight:600; line-height:1.4; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { background:#242329!important; border-color:#242329; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] p { color:#FFFFFF!important; }
    .stTabs [data-baseweb="tab"]:focus-visible { outline:3px solid #BD412F; outline-offset:3px; }
    .stTabs [data-baseweb="tab-highlight"],.stTabs [data-baseweb="tab-border"] { display:none; }
    .stTabs [data-baseweb="tab-panel"] { background:#FFFFFF; border:1px solid #E5E0DA; border-radius:18px; padding:1.7rem 2rem 2rem; box-shadow:0 8px 24px #24232904; }
    .lead { font-size:1.08rem; max-width:950px; }
    .card { background:#FAF7F3; border:1px solid #E5E0DA; border-radius:12px; padding:1.3rem; height:100%; color:#514D4A; font-size:.93rem; line-height:1.7; }
    .card h4 { color:#242329!important; font-size:1rem; margin:0 0 .65rem; padding:0; letter-spacing:-.02em; }
    .note,.good,.quote { border-radius:10px; padding:1.1rem 1.3rem; margin:1rem 0; line-height:1.75; color:#242329; background:#F8F7F4; border-left:3px solid #BD412F; }
    .good { background:#FFF1E8; border-color:#FFB49C; }
    .quote { background:#FFF1E8; border-color:#FFB49C; font-size:1.02rem; }
    .table-scroll { overflow-x:auto; width:100%; margin:.75rem 0 1.2rem; border:1px solid #E5E0DA; border-radius:12px; }
    table.t { width:100%; border-collapse:collapse; font-size:.87rem; background:#FFFFFF; color:#514D4A; }
    table.t th { background:#242329; color:#FFFFFF!important; text-align:left; font-size:.74rem; letter-spacing:.03em; padding:1rem; font-weight:600; }
    table.t td { border-bottom:1px solid #EBE5DF; padding:1rem; vertical-align:top; line-height:1.65; min-width:110px; }
    table.t td:first-child { color:#242329; font-weight:650; }
    table.t tr:nth-child(even) td { background:#FAF8F5; }
    table.t tr:last-child td { border-bottom:0; }
    .stApp [data-testid="stCode"],.stApp pre { background:#F8F7F4!important; border:1px solid #E5E0DA; border-radius:12px; }
    .stApp pre,.stApp code,.stApp pre span { color:#242329!important; }
    .footer { color:#706964; font-size:.78rem; text-align:center; padding:1.8rem 0 .5rem; }
    @media(min-width:1600px) { .block-container { padding-top:3rem; } }
    @media(max-width:850px) { .block-container { padding:1.2rem 1rem 3rem; } .banner { padding:2rem 1.6rem; } .kpis { grid-template-columns:repeat(2,minmax(0,1fr)); } .stTabs [data-baseweb="tab-panel"] { padding:1.2rem; } }
    @media(max-width:480px) { .kpi { padding:1rem; } .kpi .v { font-size:1.6rem; } .banner h1 { font-size:2rem!important; } }
    @media(prefers-reduced-motion:reduce) { * { scroll-behavior:auto!important; } }
    </style>

<style>.stApp .banner .tag,.stApp .banner a{color:#FFB49C!important}.stApp .banner .tag{background:#FFB49C12;border-color:#FFB49C55}.banner:after{border-color:#FFB49C30;box-shadow:0 0 0 60px #FFB49C0a,0 0 0 120px #FFB49C08}.stApp [data-testid="stExpander"]{background:#FFF;border:1px solid #E5E0DA;border-radius:12px}.stApp [data-baseweb="select"]>div{background:#FFFFFF;color:#242329}.stApp [data-testid="stMetricValue"]{color:#242329!important}.source-date{font-size:.78rem;color:#706964;padding:.3rem 0 1rem}</style>""", unsafe_allow_html=True)


def table(rows, columns):
    df = pd.DataFrame(rows, columns=columns)
    head = "".join(f"<th>{escape(str(c))}</th>" for c in df.columns)
    body = "".join("<tr>" + "".join(f"<td>{escape(str(v))}</td>" for v in row) + "</tr>" for row in df.values.tolist())
    st.markdown(f'<div class="table-scroll"><table class="t"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>', unsafe_allow_html=True)


def note(text):
    st.markdown(f'<div class="note">{escape(text)}</div>', unsafe_allow_html=True)


def card(title, text):
    st.markdown(f'<div class="card"><h4>{escape(title)}</h4>{escape(text)}</div>', unsafe_allow_html=True)


st.markdown('''<div class="banner">
<span class="tag">Prepared for the incident.io Talent Team</span>
<h1>Four live searches.<br>One joined-up hiring plan.</h1>
<p class="sub">A 90-day approach to UK Sales, Customer Success and technical customer hiring, built around current London vacancies.</p>
<p class="by"><b>Adam Baig</b> · GTM Recruiter &amp; Outbound Headhunter<br>
<a href="https://www.linkedin.com/in/adambaiguk">LinkedIn</a> ·
<a href="https://github.com/SkynetAI-Labs">GitHub</a> ·
<a href="https://gitlab.com/SkynetAI-Labs">GitLab</a></p></div>
<div class="kpis">
<div class="kpi"><div class="v">4 searches</div><div class="l">One coordinated portfolio</div></div>
<div class="kpi"><div class="v">90 days</div><div class="l">Proposed delivery horizon</div></div>
<div class="kpi"><div class="v">≥70%</div><div class="l">Proposed outbound pipeline target</div></div>
<div class="kpi"><div class="v">48 hours</div><div class="l">Proposed candidate update standard</div></div>
</div>''', unsafe_allow_html=True)
st.caption("Vacancy snapshot: 21 November 2026. Published role requirements are linked below; priorities, targets and exercises are my proposed approach.")

tabs = st.tabs(["1. Live vacancies", "2. Priorities", "3. Hiring bars", "4. Sourcing", "5. Outreach & events", "6. Assessment", "7. Four at once", "8. 30 / 60 / 90", "9. Measures & sources"])

with tabs[0]:
    st.header("Hire for the whole customer journey")
    st.write("I would run these as four connected searches. A BDR creates opportunities, an AE closes them, a CSM helps customers get value, and a Customer Success Engineer handles the complex technical work after the sale.")
    table([[r["name"], "London", r["pay"], r["outcome"]] for r in ROLES], ["Published vacancy", "Location", "Published annual range", "Why I would prioritise it"])
    st.caption("These are the ranges displayed by incident.io, with equity also listed. Base/variable splits and offer details need confirmation before discussing compensation with candidates.")
    for r in ROLES:
        st.markdown(f'**[{r["name"]}]({r["url"]})** — {r["fact"]}')
    note("Customer Success Engineer is post-sales, not a substitute title for Sales Engineer. The Solutions Engineer vacancy found in this snapshot is in San Francisco. I would confirm future UK Sales Engineering demand at intake rather than invent a London opening.")
    st.markdown("Other London GTM openings on the careers listing include Enterprise Account Executive, Enterprise CSM, Strategic CSM and VP of Sales, EMEA. I would review ownership and business urgency with the Talent team before adding them to this portfolio.")

with tabs[1]:
    st.header("Agree the bottleneck before choosing the priority")
    st.write("A vacancy list does not tell me which team is under the most pressure. In the first two days I would agree the approved headcount, hiring owner, start-date need and customer or revenue consequence of each gap.")
    table([["Customer Success Engineer", "30%", "Start specialist mapping immediately; confirm migration workload and current technical coverage."], ["Commercial AE", "30%", "Confirm the territory, pipeline available and the BDR/SE capacity needed around the hire."], ["Commercial CSM", "25%", "Review customer allocations, onboarding demand and any uncovered renewals."], ["BDR", "15%", "Keep a steady sourcing lane; align the start with AE capacity and onboarding support."]], ["Search", "Share of sourcing time", "Initial working assumption"])
    note("This is a starting allocation, not incident.io’s actual priority order. A renewal risk, committed customer migration or urgent territory gap would change it. Agree the ranking weekly and record the reason.")
    st.subheader("Questions I would ask at intake")
    st.markdown("- What is blocked while this role is open, and who is covering it?\n- Is this one hire or a repeatable hiring cohort?\n- Which capabilities are essential on day one, and which can be coached?\n- What are the approved compensation split, location expectations and interview stages?\n- Who can interview this week, and who makes the final decision?")

with tabs[2]:
    st.header("Four roles need four different hiring bars")
    chosen = st.selectbox("Explore the scorecard", [r["name"] for r in ROLES], key="scorecard")
    r = next(r for r in ROLES if r["name"] == chosen)
    st.subheader(r["name"])
    for signal in r["signals"]:
        st.markdown(f"- {signal}")
    note(r["question"])
    st.write("I would use a simple four-point evidence scale: 1 = no relevant example, 2 = partial evidence with important gaps, 3 = meets the agreed requirement, 4 = exceeds it with clear personal contribution. An unknown stays unknown until tested; it is not a reason to guess a score.")
    st.write("Advance when essential requirements have evidence. Hold only with a named question, owner and review date. Decline with a specific job-related reason. The hiring manager makes the hiring decision; I keep the evidence and process clear.")
    st.subheader("Look for the next step, without lowering the bar")
    st.write("A strong commercial AE may be ready for a more demanding technical sales environment; a capable TAM may be ready to own implementation design. I would assess the missing responsibilities directly and explain where support is needed. A bigger title alone is not evidence of readiness.")

with tabs[3]:
    st.header("Build a separate outbound lane for each search")
    name = st.selectbox("Choose a sourcing lane", [r["name"] for r in ROLES], key="sourcing")
    r = next(r for r in ROLES if r["name"] == name)
    st.write(r["pools"])
    st.caption("Suggested research pools, not confirmed candidate supply. Check current employment, UK remit, role relevance and any partner or no-approach restrictions before contacting people.")
    st.code(r["query"], language="text")
    table([["Map", "Build a 20-company starting map per role; identify relevant teams and adjacent titles."], ["Qualify", "Check actual responsibilities, location and evidence against the agreed scorecard."], ["Approach", "Use a specific reason to contact each person; record source, contact date and next action."], ["Learn", "Review replies and screen outcomes weekly; adjust the pool before increasing volume."]], ["Step", "What I would do"])
    st.write("I would use AI for a first pass at public company research, search variations and draft messages. I would check every claim, write the final outreach myself and assess candidates against agreed evidence. Use approved tools; keep private candidate information out of unapproved systems.")

with tabs[4]:
    st.header("Give good people a reason to reply")
    role = st.selectbox("Outreach example", [r["name"] for r in ROLES], key="outreach")
    r = next(r for r in ROLES if r["name"] == role)
    st.markdown(f'<div class="quote">{escape(r["message"])}</div>', unsafe_allow_html=True)
    st.write("Replace every bracketed detail with something verified. Follow up around days four and nine with useful context, then stop if there is no interest. Respect opt-outs immediately.")
    st.subheader("A small event I would test: selling to engineers")
    st.write("Invite a small group of relevant London GTM people to an Old Street breakfast with an AE and a technical customer-facing colleague. Discuss one real, approved customer problem and how the team handled it. Make it useful even for people who never apply.")
    table([["Before", "Agree speakers, audience, opt-in process and a small budget with Talent and Marketing."], ["During", "Keep it practical: a short customer story, open questions and conversations with the team."], ["After", "Follow up with consent, make relevant introductions and measure qualified conversations—not attendee volume."]], ["Stage", "Execution"])
    st.write("Suggested pilot: 12 attendees and a £300 spending cap, subject to approval. Aim for four agreed follow-up conversations and two qualified screens; review cost per qualified screen before repeating. These are test assumptions, not forecast results.")

with tabs[5]:
    st.header("Calibrate early. Keep the interviews useful.")
    table([["Days 1–3", "Agree the brief and interview evidence", "Hiring manager + recruiter"], ["Days 3–5", "Review 4–6 varied profiles per search before scaling outreach", "Hiring manager + recruiter"], ["Recruiter screen", "Motivation, personal contribution, location, compensation and relevant examples", "Recruiter"], ["Role assessment", "A short exercise designed around the actual job", "Role specialist"], ["Decision and close", "Written evidence, timely decision, references with consent, offer discussion", "Hiring manager + recruiter"]], ["Stage", "Purpose", "Owner"])
    for r in ROLES:
        st.markdown(f'**{r["name"]}:** {r["assessment"]}')
    note("Proposed process, to fit around incident.io’s existing interview approach. Agree adjustments with candidates, use the same core criteria and avoid excessive unpaid work. Technical interviewers assess technical depth; my own projects help me ask better questions.")
    st.subheader("Close from the first conversation")
    st.write("Understand what would make a move worthwhile, other processes, notice period and compensation expectations early. Before offer, check the role, package and timing again. Explain progression honestly, with the hiring manager confirming the scope; do not promise a promotion or equity outcome.")

with tabs[6]:
    st.header("How I would keep four searches moving")
    st.write("The portfolio needs protected sourcing time as well as room for interviews and closing. This is a working 40-hour capacity model, to adjust to the real workload and the team’s working pattern.")
    table([["Outbound sourcing and mapping", "16 hours"], ["Screens", "8 hours"], ["Hiring manager calibration and coordination", "6 hours"], ["Offers, references and candidate follow-up", "4 hours"], ["ATS records and reporting", "4 hours"], ["Unplanned work and event preparation", "2 hours"]], ["Activity", "Weekly allocation"])
    st.subheader("Rebalance sourcing time")
    hours = st.slider("Available sourcing hours per week", min_value=8, max_value=24, value=16, step=1)
    table([[r["name"], f'{r["share"]}%', f'{hours*r["share"]/100:.1f} hours'] for r in ROLES], ["Search", "Starting allocation", "Sourcing time"])
    st.caption("These percentages allocate sourcing time only; they are not headcount targets or a promise to split every working hour in the same way.")
    st.write("On office days, I would use proximity to hiring managers for short calibration conversations, interview debriefs and introductions. Keep sourcing blocks protected. Log feedback and next actions in the ATS the same day, with a weekly written view across all four roles.")
    st.subheader("If one search starts slipping")
    table([[r["short"],r["trigger"],r["action"]] for r in ROLES], ["Search", "Early warning to review", "My response"])
    note("Every active candidate needs a named owner and dated next step. If feedback is late, chase the decision and update the candidate even when there is no final answer. Rebalance this week’s work around real bottlenecks, not the loudest request.")

with tabs[7]:
    st.header("First 30 / 60 / 90 days")
    cols = st.columns(3)
    phases = [("Days 1–30: build conviction", "Learn the product and customer journey. Agree four briefs, sourcing maps and interview capacity. Start all four outbound lanes, calibrate early profiles and produce a first funnel review."), ("Days 31–60: turn pipelines into decisions", "Move qualified candidates through assessments, references and offers. Review where candidates drop out. Run the small event only if the qualified pipeline justifies the effort."), ("Days 61–90: make it repeatable", "Support starts, review manager feedback and improve the source maps. Reuse the working parts for the next approved vacancies. Agree hiring capacity for the next quarter.")]
    for c,(title,body) in zip(cols,phases):
        with c:
            card(title,body)
    st.subheader("Initial time-to-accept planning ranges")
    table([["BDR", "30–45 days"], ["Commercial AE", "45–60 days"], ["Commercial CSM", "45–60 days"], ["Customer Success Engineer", "60–90 days"]], ["Search", "Proposed planning range"])
    st.caption("Measured from agreed intake to accepted offer. These are starting assumptions to test with the Talent team, not guarantees or incident.io historical data. Notice periods mean start dates can fall later.")
    st.write("I would not call the quarter successful just because four offers went out. The hiring managers should be confident in the evidence, candidates should understand the job they accepted, and each search should leave a better map for the next one.")

with tabs[8]:
    st.header("Measure the search, then improve it")
    table([["Outbound share", "Proposed target ≥70%", "Recruiter-sourced qualified candidates / all qualified candidates entering the recruiter screen stage; count each person once per search."], ["Qualified reply rate", "Baseline in first two weeks", "Positive replies that meet agreed basic criteria / delivered approaches; compare by role and source."], ["Screen-to-assessment", "Review weekly", "Candidates advanced / completed recruiter screens; low conversion prompts calibration."], ["Offer acceptance", "Working target ≥85% across the portfolio", "Accepted / decided offers; show raw counts because a four-search sample is small."], ["Time to accept", "Role-specific planning ranges", "Agreed intake to accepted offer; report start dates separately."], ["Candidate updates", "Within 48 working hours", "Active candidates updated or given a dated next step; explain delays promptly."], ["Pipeline records", "Same-day updates", "Stage, evidence, owner and next action current in the approved ATS."]], ["Measure", "Proposed standard", "Definition"])
    st.subheader("A simple funnel to test, not a forecast")
    approached = st.slider("Illustrative personalised approaches for one search", 40, 160, 80, 10)
    reply = st.slider("Assumed positive reply rate (%)", 10, 50, 25, 5)
    qualified = st.slider("Assumed qualification rate among positive replies (%)", 20, 80, 50, 5)
    st.write(f"{approached} approaches × {reply}% positive replies × {qualified}% qualification ≈ {approached*reply/100*qualified/100:.1f} qualified conversations. Replace the assumptions with actual data once outreach starts; this does not predict hires.")
    st.subheader("Research behind the plan")
    st.markdown("Vacancies checked on **21 November 2026**. Role pages may change or close; revisit them before using this snapshot.")
    for r in ROLES:
        st.markdown(f'- [{r["name"]} — official role page]({r["url"]})')
    st.markdown('- [Open vacancies](https://incident.io/careers#open-roles)\n- [GTM Candidate Hub](https://incident.io/careers/candidate-hub/gtm)\n- [GTM Talent Partner — role this plan supports](https://jobs.ashbyhq.com/incident/eff33405-6b14-42ba-a3a0-89ab8697a8a9)')
    st.write("The brief is based on public vacancies and the GTM Talent Partner posting. The plan does not assume access to incident.io’s internal headcount, candidate pipeline or hiring performance.")

st.markdown('<div class="footer">Prepared by Adam Baig · London, UK · GTM hiring plan</div>', unsafe_allow_html=True)

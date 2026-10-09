"""CSS tokens and responsive layout rules for the Streamlit workspace.

Keep the visual system here so layout and color can be adjusted without editing
the Python view code. Streamlit widgets retain their native semantics and states.
"""

APP_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;500;600;700&family=Fraunces:opsz,wght@9..144,500;9..144,600&display=swap');

:root {
  --ink: #202b2a;
  --muted: #687370;
  --line: #dce3df;
  --paper: #f5f7f3;
  --white: #ffffff;
  --forest: #286657;
  --forest-dark: #1d4f44;
  --mint: #dfece5;
  --coral: #ca7058;
  --amber: #b07b34;
  --mono: 'DM Mono', monospace;
  --sans: 'DM Sans', sans-serif;
  --display: 'Fraunces', Georgia, serif;
}

html, body, [class*="css"] { font-family: var(--sans); color: var(--ink); }
.stApp { background: var(--paper); }
header[data-testid="stHeader"] { background: transparent; }
section[data-testid="stSidebar"] { background: #edf2ed; border-right: 1px solid var(--line); }
section[data-testid="stSidebar"] > div { padding: 1.45rem 1.15rem; }
section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: .75rem; }

.brand-lockup { display: flex; align-items: center; gap: .72rem; padding: .2rem 0 1.1rem; }
.brand-mark { display: grid; place-items: center; width: 2.15rem; height: 2.15rem; background: var(--forest); color: white; font-family: var(--display); font-size: 1.3rem; border-radius: 4px; }
.brand-lockup strong { display: block; font-size: 1rem; line-height: 1.15; }
.brand-lockup small, .sidebar-label, .eyebrow, .field-label { display: block; font: 500 .62rem var(--mono); letter-spacing: .08em; color: var(--muted); }
.brand-lockup small { margin-top: .2rem; font-size: .55rem; }
.sidebar-label { margin: .25rem 0 0; }
.sidebar-rule { border-top: 1px solid var(--line); margin: .25rem 0; }
.sidebar-library { display: flex; align-items: center; justify-content: space-between; color: var(--muted); font-size: .72rem; }
.sidebar-library div { display: flex; align-items: baseline; gap: .45rem; }
.sidebar-library strong { font: 600 1.15rem var(--display); color: var(--ink); }
.sidebar-library small { font: .62rem var(--mono); }
.status-line { display: flex; align-items: center; gap: .5rem; color: var(--muted); font-size: .72rem; }
.status-dot { width: .48rem; height: .48rem; border-radius: 50%; background: var(--amber); flex: 0 0 auto; }
.status-ready { background: var(--forest); }
.status-error { background: var(--coral); }
.status-sidebar { padding: .6rem .65rem; background: rgba(255,255,255,.62); border: 1px solid var(--line); border-radius: 4px; color: var(--ink); }

.main .block-container { max-width: 1440px; padding: 2.4rem 3.2rem 4rem; }
.page-heading { padding: .2rem 0 1.55rem; border-bottom: 1px solid var(--line); margin-bottom: 1.2rem; }
.eyebrow { color: var(--forest); margin: 0 0 .55rem; }
.page-heading h1 { margin: 0; font: 500 clamp(2.15rem, 2.75rem, 2.75rem)/1.08 var(--display); letter-spacing: 0; }
.page-description { max-width: 44rem; margin: .65rem 0 0; color: var(--muted); font-size: .94rem; line-height: 1.55; }
.metric-strip { min-height: 6rem; display: flex; flex-direction: column; justify-content: center; padding: .9rem 1.1rem; border: 1px solid var(--line); background: rgba(255,255,255,.62); border-radius: 4px; }
.metric-strip span, .metric-strip small { color: var(--muted); font: .59rem var(--mono); }
.metric-strip strong { margin: .25rem 0 .1rem; font: 500 1.5rem var(--display); color: var(--ink); }
.metric-status strong { font: 600 .95rem var(--sans); }
.section-gap { height: 1rem; }
.panel-heading { display: flex; gap: .75rem; align-items: flex-start; margin: .1rem 0 1rem; }
.panel-heading > span { padding-top: .2rem; color: var(--coral); font: .65rem var(--mono); }
.panel-heading h2 { margin: 0; font: 500 1.32rem var(--display); }
.panel-heading p { margin: .25rem 0 0; color: var(--muted); font-size: .78rem; line-height: 1.45; }
.field-label { margin: .9rem 0 .4rem; }

div[data-testid="stTextArea"] textarea { border-color: var(--line); background: var(--white); border-radius: 4px; font-size: .92rem; line-height: 1.5; }
div[data-testid="stTextArea"] textarea:focus { border-color: var(--forest); box-shadow: 0 0 0 1px var(--forest); }
div[data-testid="stButton"] button { min-height: 2.55rem; border-radius: 4px; font-weight: 600; font-size: .78rem; border-color: var(--line); color: var(--ink); }
div[data-testid="stButton"] button[kind="primary"] { background: var(--forest); color: white; border-color: var(--forest); }
div[data-testid="stButton"] button[kind="primary"]:hover { background: var(--forest-dark); border-color: var(--forest-dark); }
div[data-testid="stFileUploader"] section { border-color: #bdcbc3; background: rgba(255,255,255,.5); border-radius: 4px; }
div[data-testid="stFileUploader"] section small { color: var(--muted); }
.evidence-empty { min-height: 18.2rem; padding: 1.3rem; border: 1px dashed #bdcbc3; background: rgba(255,255,255,.48); border-radius: 4px; display: flex; flex-direction: column; justify-content: center; }
.evidence-index { font: .59rem var(--mono); color: var(--coral); }
.evidence-empty h3 { max-width: 16rem; margin: .75rem 0 .45rem; font: 500 1.45rem/1.2 var(--display); }
.evidence-empty p { max-width: 19rem; color: var(--muted); font-size: .78rem; line-height: 1.6; }
.citation-sample { display: flex; justify-content: space-between; align-items: center; gap: .5rem; margin-top: .8rem; padding-top: .8rem; border-top: 1px solid var(--line); }
.citation-sample span { color: var(--muted); font: .55rem var(--mono); }
.citation-sample strong { color: var(--forest-dark); font-size: .7rem; }
.empty-list { padding: 1.1rem; border: 1px dashed #bdcbc3; color: var(--muted); font-size: .8rem; border-radius: 4px; }
.paper-row { display: flex; align-items: center; gap: .8rem; min-width: 0; padding: .85rem 0; border-bottom: 1px solid var(--line); }
.pdf-mark { display: grid; place-items: center; width: 2.4rem; height: 2.7rem; flex: 0 0 auto; border: 1px solid #e5c5b8; border-radius: 3px; background: #fbf0eb; color: #9b573f; font: .6rem var(--mono); }
.paper-copy { display: flex; min-width: 0; flex: 1; flex-direction: column; gap: .2rem; }
.paper-copy strong { overflow-wrap: anywhere; font-size: .82rem; font-weight: 600; }
.paper-copy small { color: var(--muted); font-size: .68rem; }
.paper-state { flex: 0 0 auto; color: var(--forest); font: .55rem var(--mono); }
.notes-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1px; background: var(--line); border: 1px solid var(--line); }
.notes-grid article { min-height: 12rem; padding: 1.2rem; background: var(--paper); }
.notes-grid article span { color: var(--coral); font: .58rem var(--mono); }
.notes-grid article h3 { margin: 1.7rem 0 .45rem; font: 500 1.22rem var(--display); }
.notes-grid article p { margin: 0; color: var(--muted); font-size: .78rem; line-height: 1.55; }
div[data-testid="stAlert"] { border-radius: 4px; }

@media (max-width: 900px) {
  .main .block-container { padding: 1.6rem 1.5rem 3rem; }
  .page-heading h1 { font-size: 2.35rem; }
}
@media (max-width: 640px) {
  .main .block-container { padding: 1.15rem 1rem 2rem; }
  .page-heading { padding-bottom: 1.1rem; }
  .page-heading h1 { font-size: 2rem; }
  .page-description { font-size: .83rem; }
  .metric-strip { min-height: 5.1rem; padding: .65rem; }
  .metric-strip strong { font-size: 1.2rem; }
  .metric-status strong { font-size: .78rem; }
  .metric-status small { line-height: 1.3; }
  .panel-heading h2 { font-size: 1.18rem; }
  .evidence-empty { min-height: 14rem; padding: 1rem; }
  .notes-grid { grid-template-columns: 1fr; }
  .notes-grid article { min-height: auto; }
  .notes-grid article h3 { margin-top: .75rem; }
  .paper-state { max-width: 4rem; text-align: right; line-height: 1.3; }
}
</style>
"""
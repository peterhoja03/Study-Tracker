"""
AI Tools Page — standalone page for weekly analysis and vocab drill.
Add to app.py sidebar nav and main() router.
"""

import streamlit as st
from datetime import date
from ai_helper import generate_weekly_analysis, check_korean_writing


def page_ai_tools():
    st.markdown("# 🤖 AI Tools")
    st.markdown("*Analysis, drills, and insights across all three streams*")
    st.markdown("---")

    tab1, tab2 = st.tabs(["📊 Weekly Analysis", "🇰🇷 Korean Vocab Drill"])

    # ── Weekly Analysis ────────────────────────────────────────────────────────
    with tab1:
        st.markdown("### 📊 Weekly Analysis")
        st.markdown("Claude reads your session history and weakness log and writes a frank analysis.")

        try:
            from app import load_sessions, load_progress
            sessions = load_sessions()
            progress = load_progress()
        except Exception:
            sessions = []
            progress = {}

        # Load weakness log
        weakness_log = _load_weakness_log()

        if st.button("Generate this week's analysis", use_container_width=True, key="gen_weekly"):
            with st.spinner("Claude is analysing your week..."):
                analysis = generate_weekly_analysis(sessions, weakness_log, progress)
            st.session_state["_weekly_analysis"] = analysis

        if st.session_state.get("_weekly_analysis"):
            st.markdown(f"""
            <div style="background:var(--background-color);border:1px solid #e0e0e0;border-radius:12px;
                        padding:1.4rem 1.8rem;margin-top:1rem;font-size:.93rem;line-height:1.8">
            {st.session_state['_weekly_analysis'].replace(chr(10), '<br>')}
            </div>""", unsafe_allow_html=True)

    # ── Korean Vocab Drill ─────────────────────────────────────────────────────
    with tab2:
        st.markdown("### 🇰🇷 Korean Vocab Production Drill")
        st.markdown("Enter an English word or phrase — write it in Korean from memory, then get feedback.")

        english_prompt = st.text_input("English prompt:", placeholder="e.g. I eat rice every day", key="vocab_eng")

        # Embed the Korean keyboard
        _render_korean_keyboard("vocab_korean_input")

        korean_answer = st.text_input(
            "Your Korean:",
            value=st.session_state.get("vocab_korean_input", ""),
            placeholder="Type or use the keyboard above",
            key="vocab_kor_answer"
        )

        if st.button("Get feedback", use_container_width=True, key="vocab_check") and english_prompt and korean_answer:
            # Use a minimal lesson context for standalone vocab drill
            dummy_lesson = {
                "id": "U_vocab",
                "knowledge_bank": {
                    "facts": ["Korean uses SOV sentence order", "Particles attach to nouns to show their role"],
                    "grammar_rules": ["Topic marker: 은/는", "Object marker: 을/를", "Subject marker: 이/가"],
                }
            }
            with st.spinner("Checking..."):
                result = check_korean_writing(dummy_lesson, korean_answer, english_prompt)
            _render_korean_feedback(result)


def _load_weakness_log() -> list:
    """Load weakness_log from Supabase or session state."""
    try:
        from app import _sb
        sb = _sb()
        if sb:
            res = sb.table("weakness_log").select("*").order("date", desc=True).execute()
            return res.data
    except Exception:
        pass
    return st.session_state.get("_weakness_log", [])


def _render_korean_feedback(result: dict):
    """Render Korean writing feedback."""
    if result.get("error"):
        st.error(f"Could not get feedback: {result['error']}")
        return
    corrected = result.get("corrected", "")
    errors = result.get("errors", [])
    verdict = result.get("verdict", "")
    alternatives = result.get("natural_alternatives", [])

    if corrected:
        st.markdown(f"**Corrected:** {corrected}")
    if verdict:
        st.info(verdict)
    if errors:
        st.markdown("**Errors:**")
        for e in errors:
            if isinstance(e, dict):
                st.markdown(f"- `{e.get('original')}` → `{e.get('correction')}` — {e.get('rule', '')}")
    if alternatives:
        st.markdown("**More natural phrasing:** " + " / ".join(alternatives))


def _render_korean_keyboard(state_key: str):
    """Embed the Korean Dubeolsik keyboard as an HTML component."""
    import streamlit.components.v1 as components
    kb_html = """
<style>
*{box-sizing:border-box;}
.output-box{background:#f8f9fa;border:1px solid #dee2e6;border-radius:8px;padding:8px 12px;
  font-size:18px;min-height:48px;margin-bottom:8px;color:#212529;word-break:break-all;cursor:text;}
.cursor{display:inline-block;width:2px;height:1.1em;background:#212529;vertical-align:text-bottom;
  animation:blink 1s step-end infinite;margin-left:1px;}
@keyframes blink{0%,100%{opacity:1}50%{opacity:0}}
.kb-rows{display:flex;flex-direction:column;gap:4px;}
.kb-row{display:flex;gap:3px;justify-content:center;}
.key{background:#fff;border:1px solid #ced4da;border-radius:5px;cursor:pointer;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  width:50px;height:46px;transition:background 0.1s;flex-shrink:0;user-select:none;position:relative;}
.key:hover{background:#e9ecef;}
.key:active,.key.pressed{background:#dee2e6;transform:scale(0.95);}
.key .ko-main{font-size:15px;color:#212529;line-height:1;}
.key .ko-shift{font-size:9px;color:#8a6700;position:absolute;top:4px;right:6px;}
.key .en{font-size:9px;color:#6c757d;margin-top:2px;}
.key.sp{width:180px;}.key.fn{background:#e9ecef;}
.key.fn .ko-main{font-size:11px;color:#495057;}
.actions{display:flex;gap:6px;margin-top:6px;}
.actions button{padding:4px 10px;font-size:12px;border:1px solid #ced4da;border-radius:4px;
  background:#fff;cursor:pointer;}
.actions button:hover{background:#e9ecef;}
</style>
<div class="output-box" id="output"></div>
<div class="kb-rows" id="keyboard"></div>
<div class="actions">
  <button onclick="doBackspace()">← Del</button>
  <button onclick="clearAll()">Clear</button>
  <button id="shift-btn" onclick="toggleShift()">Shift ⇧</button>
  <button onclick="copyText()">Copy</button>
</div>
<script>
const NORMAL={q:'ㅂ',w:'ㅈ',e:'ㄷ',r:'ㄱ',t:'ㅅ',y:'ㅛ',u:'ㅕ',i:'ㅑ',o:'ㅐ',p:'ㅔ',
  a:'ㅁ',s:'ㄴ',d:'ㅇ',f:'ㄹ',g:'ㅎ',h:'ㅗ',j:'ㅓ',k:'ㅏ',l:'ㅣ',
  z:'ㅋ',x:'ㅌ',c:'ㅊ',v:'ㅍ',b:'ㅠ',n:'ㅜ',m:'ㅡ'};
const SHIFTED={q:'ㅃ',w:'ㅉ',e:'ㄸ',r:'ㄲ',t:'ㅆ',o:'ㅒ',p:'ㅖ'};
const rows=[
  [{n:'ㅂ',s:'ㅃ',e:'q'},{n:'ㅈ',s:'ㅉ',e:'w'},{n:'ㄷ',s:'ㄸ',e:'e'},{n:'ㄱ',s:'ㄲ',e:'r'},{n:'ㅅ',s:'ㅆ',e:'t'},{n:'ㅛ',e:'y'},{n:'ㅕ',e:'u'},{n:'ㅑ',e:'i'},{n:'ㅐ',s:'ㅒ',e:'o'},{n:'ㅔ',s:'ㅖ',e:'p'}],
  [{n:'ㅁ',e:'a'},{n:'ㄴ',e:'s'},{n:'ㅇ',e:'d'},{n:'ㄹ',e:'f'},{n:'ㅎ',e:'g'},{n:'ㅗ',e:'h'},{n:'ㅓ',e:'j'},{n:'ㅏ',e:'k'},{n:'ㅣ',e:'l'}],
  [{n:'ㅋ',e:'z'},{n:'ㅌ',e:'x'},{n:'ㅊ',e:'c'},{n:'ㅍ',e:'v'},{n:'ㅠ',e:'b'},{n:'ㅜ',e:'n'},{n:'ㅡ',e:'m'}]
];
const CHOSUNG=['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ'];
const JUNGSUNG=['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ'];
const JONGSUNG=['','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ'];
const CJ={'ㄱ+ㅅ':'ㄳ','ㄴ+ㅈ':'ㄵ','ㄴ+ㅎ':'ㄶ','ㄹ+ㄱ':'ㄺ','ㄹ+ㅁ':'ㄻ','ㄹ+ㅂ':'ㄼ','ㄹ+ㅅ':'ㄽ','ㄹ+ㅌ':'ㄾ','ㄹ+ㅍ':'ㄿ','ㄹ+ㅎ':'ㅀ','ㅂ+ㅅ':'ㅄ'};
const CV={'ㅗ+ㅏ':'ㅘ','ㅗ+ㅐ':'ㅙ','ㅗ+ㅣ':'ㅚ','ㅜ+ㅓ':'ㅝ','ㅜ+ㅔ':'ㅞ','ㅜ+ㅣ':'ㅟ','ㅡ+ㅣ':'ㅢ'};
function isV(c){return JUNGSUNG.includes(c);}
function isC(c){return CHOSUNG.includes(c);}
function compose(cho,jung,jong){
  const ci=CHOSUNG.indexOf(cho),vi=JUNGSUNG.indexOf(jung),ji=JONGSUNG.indexOf(jong||'');
  if(ci<0||vi<0||ji<0)return(cho||'')+(jung||'')+(jong||'');
  return String.fromCharCode(0xAC00+ci*21*28+vi*28+ji);
}
let text='',composing=null,shiftOn=false;
function fullText(){return text+(composing?composing.preview||'':'');}
function updateDisplay(){document.getElementById('output').innerHTML=fullText()+'<span class="cursor"></span>';}
function addChar(ch){
  if(shiftOn&&!isV(ch))setShift(false);
  if(!isV(ch)&&!isC(ch)){if(composing){text+=composing.preview||'';composing=null;}text+=ch;updateDisplay();return;}
  if(!composing){if(isC(ch))composing={cho:ch,jung:null,jong:null,preview:ch};else text+=ch;updateDisplay();return;}
  const c=composing;
  if(c.cho&&!c.jung){
    if(isV(ch)){c.jung=CV[c.cho+'+'+ch]||ch;c.preview=compose(c.cho,c.jung,'');updateDisplay();return;}
    text+=c.cho;composing={cho:ch,jung:null,jong:null,preview:ch};updateDisplay();return;
  }
  if(c.cho&&c.jung&&!c.jong){
    if(isC(ch)){c.jong=ch;c.preview=compose(c.cho,c.jung,c.jong);updateDisplay();return;}
    if(isV(ch)){
      const comp=CV[c.jung+'+'+ch];
      if(comp){c.jung=comp;c.preview=compose(c.cho,c.jung,'');updateDisplay();return;}
      text+=compose(c.cho,c.jung,'');composing={cho:null,jung:ch,jong:null,preview:ch};updateDisplay();return;
    }
  }
  if(c.cho&&c.jung&&c.jong){
    if(isV(ch)){
      const ck=Object.entries(CJ).find(([k,v])=>v===c.jong);
      let sc=c.jong,rj='';if(ck){[sc,rj]=ck[0].split('+');}
      text+=compose(c.cho,c.jung,rj);composing={cho:sc,jung:ch,jong:null,preview:compose(sc,ch,'')};updateDisplay();return;
    }
    if(isC(ch)){
      const comp=CJ[c.jong+'+'+ch];
      if(comp){c.jong=comp;c.preview=compose(c.cho,c.jung,c.jong);updateDisplay();return;}
      text+=c.preview;composing={cho:ch,jung:null,jong:null,preview:ch};updateDisplay();return;
    }
  }
  if(composing){text+=composing.preview||'';composing=null;}addChar(ch);
}
function doBackspace(){
  if(composing){
    const c=composing;
    if(c.jong){const ck=Object.entries(CJ).find(([k,v])=>v===c.jong);if(ck){c.jong=ck[0].split('+')[0];c.preview=compose(c.cho,c.jung,c.jong);}else{c.jong=null;c.preview=compose(c.cho,c.jung,'');}updateDisplay();return;}
    if(c.jung){const ck=Object.entries(CV).find(([k,v])=>v===c.jung);if(ck){c.jung=ck[0].split('+')[0];c.preview=c.cho?compose(c.cho,c.jung,''):c.jung;updateDisplay();return;}c.jung=null;c.preview=c.cho||'';updateDisplay();return;}
    composing=null;updateDisplay();return;
  }
  if(text.length>0){text=text.slice(0,-1);updateDisplay();}
}
function clearAll(){text='';composing=null;setShift(false);updateDisplay();}
function copyText(){
  const full=fullText();
  navigator.clipboard.writeText(full).catch(()=>{});
}
function setShift(v){shiftOn=v;document.getElementById('shift-btn').style.background=v?'#ffc107':'';}
function toggleShift(){setShift(!shiftOn);}
document.addEventListener('keydown',e=>{
  if(e.key==='Shift'){setShift(true);return;}
  if(e.key==='Backspace'){e.preventDefault();doBackspace();return;}
  if(e.key===' '){e.preventDefault();if(composing){text+=composing.preview||'';composing=null;}text+=' ';updateDisplay();return;}
  const k=e.key.toLowerCase();
  const ch=shiftOn?(SHIFTED[k]||NORMAL[k]):NORMAL[k];
  if(ch){e.preventDefault();addChar(ch);}
});
document.addEventListener('keyup',e=>{if(e.key==='Shift')setShift(false);});
const kb=document.getElementById('keyboard');
rows.forEach((row,ri)=>{
  const rowEl=document.createElement('div');rowEl.className='kb-row';
  if(ri===2){const shk=document.createElement('div');shk.className='key fn';shk.style.width='58px';shk.innerHTML='<span class="ko-main">⇧</span>';shk.addEventListener('mousedown',e=>{e.preventDefault();setShift(!shiftOn);});rowEl.appendChild(shk);}
  row.forEach(k=>{
    const key=document.createElement('div');key.className='key';key.dataset.kn=k.n;if(k.s)key.dataset.ks=k.s;
    key.innerHTML=`${k.s?`<span class="ko-shift">${k.s}</span>`:''}<span class="ko-main">${k.n}</span><span class="en">${k.e}</span>`;
    key.addEventListener('mousedown',e=>{e.preventDefault();const ch=shiftOn&&k.s?k.s:k.n;addChar(ch);if(shiftOn)setShift(false);});
    rowEl.appendChild(key);
  });
  if(ri===1){const bs=document.createElement('div');bs.className='key fn';bs.style.width='64px';bs.innerHTML='<span class="ko-main">←del</span>';bs.addEventListener('mousedown',e=>{e.preventDefault();doBackspace();});rowEl.appendChild(bs);}
  if(ri===2){const sp=document.createElement('div');sp.className='key fn sp';sp.innerHTML='<span class="ko-main">space</span>';sp.addEventListener('mousedown',e=>{e.preventDefault();if(composing){text+=composing.preview||'';composing=null;}text+=' ';updateDisplay();});rowEl.appendChild(sp);}
  kb.appendChild(rowEl);
});
updateDisplay();
</script>
"""
    components.html(kb_html, height=220)

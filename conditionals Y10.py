import streamlit as st
import random
import re

# --- HILFSFUNKTION FÜR TOLERANTE PRÜFUNG ---
def check_answer(user_input, correct_answer):
    def normalize(text):
        text = text.lower().strip()
        # Auflösung von Kurzformen für faire Bewertung
        replacements = {
            "n't": " not", "'ll": " will", "'d": " would",
            "won't": "will not", "can't": "cannot", "don't": "do not",
            "doesn't": "does not", "didn't": "did not", "wouldn't": "would not",
            "it's": "it is", "she's": "she is", "he's": "he is"
        }
        for k, v in replacements.items():
            text = text.replace(k, v)
        text = re.sub(r'[^\w\s]', '', text)
        return " ".join(text.split())
    return normalize(user_input) == normalize(correct_answer)

# --- DATENPOOL (120 SÄTZE) ---
def get_full_pool():
    # Struktur: (Text, Lösung, Typ, Position [0=If-Clause, 1=Main-Clause])
    data = [
        # --- TYP I (40 Sätze) ---
        ("If it ___ (rain), we will stay at home.", "rains", 1, 0),
        ("If you study, you ___ (pass) the exam.", "will pass", 1, 1),
        ("She will be angry if he ___ (be) late.", "is", 1, 0),
        ("If I find it, I ___ (tell) you.", "will tell", 1, 1),
        ("If the sun shines, we ___ (go) outside.", "will go", 1, 1),
        ("They will miss the bus if they ___ (not/hurry).", "do not hurry", 1, 0),
        ("If you ___ (eat) too much, you'll feel sick.", "eat", 1, 0),
        ("I will call you if I ___ (have) time.", "have", 1, 0),
        ("If he ___ (cook), I will wash the dishes.", "cooks", 1, 0),
        ("The chocolate ___ (melt) if you leave it here.", "will melt", 1, 1),
        ("If we ___ (not/leave) now, we will be late.", "do not leave", 1, 0),
        ("She ___ (be) happy if you call her.", "will be", 1, 1),
        ("If you help me, I ___ (finish) faster.", "will finish", 1, 1),
        ("If it ___ (be) cold, wear a coat.", "is", 1, 0),
        ("If they ___ (find) the ball, they will play.", "find", 1, 0),
        ("If I ___ (not/see) him, I'll send an email.", "do not see", 1, 0),
        ("You ___ (feel) better if you sleep.", "will feel", 1, 1),
        ("If she ___ (forget) her key, she'll be stuck.", "forgets", 1, 0),
        ("I ___ (buy) milk if I go to the shop.", "will buy", 1, 1),
        ("If we win, we ___ (celebrate).", "will celebrate", 1, 1),
        ("If it ___ (snow), we will build a snowman.", "snows", 1, 0),
        ("I will lend you the book if you ___ (promise) to return it.", "promise", 1, 0),
        ("If you ___ (ask) him, he will help.", "ask", 1, 0),
        ("The glass ___ (break) if you drop it.", "will break", 1, 1),
        ("If you ___ (not/study), you'll fail.", "do not study", 1, 0),
        ("I'll be surprised if it ___ (happen).", "happens", 1, 0),
        ("If he ___ (call), I will answer.", "calls", 1, 0),
        ("If we ___ (take) a map, we won't get lost.", "take", 1, 0),
        ("If you stay here, you ___ (see) her.", "will see", 1, 1),
        ("If she ___ (sing), everyone will listen.", "sings", 1, 0),
        ("If they ___ (try) hard, they will succeed.", "try", 1, 0),
        ("I ___ (help) you if you are in trouble.", "will help", 1, 1),
        ("If you ___ (drink) this, you will feel better.", "drink", 1, 0),
        ("The dog ___ (bark) if someone knocks.", "will bark", 1, 1),
        ("If you ___ (touch) that, you will get hurt.", "touch", 1, 0),
        ("If the bus ___ (not/come), we will walk.", "does not come", 1, 0),
        ("You ___ (get) a prize if you win.", "will get", 1, 1),
        ("If she ___ (practice), she will improve.", "practices", 1, 0),
        ("If it ___ (be) sunny, we will go for a walk.", "is", 1, 0),
        ("I ___ (visit) you if I have time.", "will visit", 1, 1),

        # --- TYP II (40 Sätze) ---
        ("If I ___ (be) you, I would go home.", "were", 2, 0),
        ("If I won the lottery, I ___ (travel) the world.", "would travel", 2, 1),
        ("If she ___ (have) time, she would learn it.", "had", 2, 0),
        ("We ___ (buy) a house if we were rich.", "would buy", 2, 1),
        ("If it ___ (snow) in July, I would be surprised.", "snowed", 2, 0),
        ("I would help you if I ___ (can).", "could", 2, 0),
        ("If they ___ (live) here, they'd be happy.", "lived", 2, 0),
        ("If he ___ (be) taller, he'd play basketball.", "were", 2, 0),
        ("I ___ (not/do) that if I were you.", "would not do", 2, 1),
        ("If we ___ (have) a garden, we'd have a dog.", "had", 2, 0),
        ("If she ___ (know) his name, she'd tell you.", "knew", 2, 0),
        ("If I ___ (be) a bird, I would fly.", "were", 2, 0),
        ("You ___ (feel) better if you exercised.", "would feel", 2, 1),
        ("If he ___ (ask) her, she would say yes.", "asked", 2, 0),
        ("If I ___ (not/have) to work, I'd go out.", "did not have", 2, 0),
        ("They ___ (be) happy if you visited.", "would be", 2, 1),
        ("If it ___ (be) warmer, we would swim.", "were", 2, 0),
        ("If she ___ (see) a ghost, she'd scream.", "saw", 2, 0),
        ("I ___ (call) him if I had his number.", "would call", 2, 1),
        ("If we ___ (lose), we would be sad.", "lost", 2, 0),
        ("If you ___ (speak) louder, I could hear you.", "spoke", 2, 0),
        ("If I ___ (find) a wallet, I'd give it back.", "found", 2, 0),
        ("If she ___ (need) help, she would ask.", "needed", 2, 0),
        ("We ___ (go) out if it didn't rain.", "would go", 2, 1),
        ("If I ___ (own) a company, I'd hire you.", "owned", 2, 0),
        ("If you ___ (stop) smoking, you'd be healthy.", "stopped", 2, 0),
        ("If he ___ (study) more, he'd get better grades.", "studied", 2, 0),
        ("I ___ (tell) you the truth if I knew it.", "would tell", 2, 1),
        ("If they ___ (have) wings, they'd fly.", "had", 2, 0),
        ("If she ___ (be) my sister, I'd tell her.", "were", 2, 0),
        ("If I ___ (get) the job, I'd celebrate.", "got", 2, 0),
        ("If we ___ (win), we would be famous.", "won", 2, 0),
        ("If it ___ (be) easy, everyone would do it.", "were", 2, 0),
        ("If you ___ (paint) it blue, it'd look better.", "painted", 2, 0),
        ("If I ___ (know) how to cook, I'd make dinner.", "knew", 2, 0),
        ("If she ___ (wear) that, she'd look great.", "wore", 2, 0),
        ("If they ___ (arrive) early, they'd wait.", "arrived", 2, 0),
        ("If he ___ (be) here, he'd know what to do.", "were", 2, 0),
        ("If I ___ (see) him, I would say hello.", "saw", 2, 0),
        ("If you ___ (want) to learn, you'd listen.", "wanted", 2, 0),

        # --- TYP III (40 Sätze) ---
        ("If you had studied, you ___ (pass) the exam.", "would have passed", 3, 1),
        ("If I ___ (see) him, I would have told him.", "had seen", 3, 0),
        ("We'd have arrived if we ___ (take) the bus.", "had taken", 3, 0),
        ("If she ___ (ask) me, I'd have helped.", "had asked", 3, 0),
        ("If they had known, they ___ (not/come).", "would not have come", 3, 1),
        ("I ___ (buy) it if I had had the money.", "would have bought", 3, 1),
        ("If it ___ (not/rain), we'd have gone out.", "had not rained", 3, 0),
        ("If he ___ (be) careful, he wouldn't have fallen.", "had been", 3, 0),
        ("She'd have won if she ___ (run) faster.", "had run", 3, 0),
        ("If we ___ (leave) earlier, we'd have caught it.", "had left", 3, 0),
        ("If you ___ (tell) me, I would have understood.", "had told", 3, 0),
        ("I ___ (bake) a cake if I had known.", "would have baked", 3, 1),
        ("They'd have stayed if it ___ (be) warmer.", "had been", 3, 0),
        ("If he ___ (not/forget) it, he could've gone.", "had not forgotten", 3, 0),
        ("If she ___ (study) harder, she'd have succeeded.", "had studied", 3, 0),
        ("I ___ (call) you if I hadn't lost my phone.", "would have called", 3, 1),
        ("If we ___ (pay) attention, we'd have learned.", "had paid", 3, 0),
        ("If he ___ (stop), it wouldn't have happened.", "had stopped", 3, 0),
        ("If you ___ (listen), you'd have known.", "had listened", 3, 0),
        ("She ___ (be) happy if you had remembered.", "would have been", 3, 1),
        ("If I ___ (find) it, I'd have given it to you.", "had found", 3, 0),
        ("If they ___ (play) better, they'd have won.", "had played", 3, 0),
        ("We ___ (not/get) lost if we'd used a map.", "would not have gotten", 3, 1),
        ("If he ___ (work) harder, he'd have been promoted.", "had worked", 3, 0),
        ("If you ___ (not/eat) so much, you'd be fine.", "had not eaten", 3, 0),
        ("If she ___ (go) to bed, she'd have been rested.", "had gone", 3, 0),
        ("I ___ (visit) you if I had known.", "would have visited", 3, 1),
        ("If we ___ (have) time, we'd have finished.", "had had", 3, 0),
        ("If they ___ (invited) us, we would have gone.", "had invited", 3, 0),
        ("If it ___ (be) sunny, we'd have gone out.", "had been", 3, 0),
        ("If he ___ (tell) the truth, he'd be safe.", "had told", 3, 0),
        ("If I ___ (not/break) it, I'd have played.", "had not broken", 3, 0),
        ("If she ___ (call) earlier, I'd have answered.", "had called", 3, 0),
        ("If you ___ (be) there, you'd have seen it.", "had been", 3, 0),
        ("If they ___ (wait), they'd have met him.", "had waited", 3, 0),
        ("If I ___ (study) law, I'd have been a lawyer.", "had studied", 3, 0),
        ("If we ___ (book) early, it'd have been cheaper.", "had booked", 3, 0),
        ("If he ___ (not/miss) the bus, he'd be here.", "had not missed", 3, 0),
        ("If she ___ (try), she would have won.", "had tried", 3, 0),
        ("If you ___ (asked), I would have told you.", "had asked", 3, 0),
    ]
    return data

# --- APP SETUP ---
st.set_page_config(page_title="Conditional Trainer", layout="centered")

if 'phase' not in st.session_state:
    st.session_state.phase = "START"
    st.session_state.pool = get_full_pool()
    st.session_state.used_indices = set()
    st.session_state.current_q = None
    st.session_state.score = 0
    st.session_state.counter = 0
    st.session_state.last_gap_pos = 1 

def get_next_question(target_type=None):
    # Wechselt konsequent die Lückenposition (0 -> 1 -> 0)
    target_pos = 1 if st.session_state.last_gap_pos == 0 else 0
    available = [
        i for i, q in enumerate(st.session_state.pool)
        if i not in st.session_state.used_indices 
        and (target_type is None or q[2] == target_type)
        and q[3] == target_pos
    ]
    if not available: # Fallback falls Position im Pool gerade fehlt
        available = [i for i, q in enumerate(st.session_state.pool) 
                     if i not in st.session_state.used_indices 
                     and (target_type is None or q[2] == target_type)]
    if not available: return None

    idx = random.choice(available)
    st.session_state.used_indices.add(idx)
    q = st.session_state.pool[idx]
    st.session_state.last_gap_pos = q[3]
    return {"text": q[0], "answer": q[1], "type": q[2]}

# --- UI HEADER ---
col_title, col_logo = st.columns([4, 1])
with col_logo:
    try:
        st.image("schullogo.png", width=120)
    except:
        st.info("Logo hier")

with col_title:
    st.title("🇬🇧 Conditionals Trainer")

st.write("---")

# --- APP LOGIK ---
if st.session_state.phase == "START":
    st.subheader("Möchtest du die Typen einzeln üben?")
    col1, col2 = st.columns(2)
    if col1.button("Ja"):
        st.session_state.phase = "DRILL_1"
        st.rerun()
    if col2.button("Nein (direkt 20er Mix)"):
        st.session_state.phase = "MIXED"
        st.rerun()

elif st.session_state.phase in ["DRILL_1", "DRILL_2", "DRILL_3", "MIXED"]:
    config = {
        "DRILL_1": (1, 5, "Typ I", "DRILL_2"),
        "DRILL_2": (2, 5, "Typ II", "DRILL_3"),
        "DRILL_3": (3, 5, "Typ III", "MIXED_INFO"),
        "MIXED": (None, 20, "Gemischtes Training", "FINISHED")
    }
    t_type, limit, label, next_ph = config[st.session_state.phase]
    
    if st.session_state.current_q is None:
        st.session_state.current_q = get_next_question(t_type)

    if st.session_state.current_q:
        st.info(f"Bereich: **{label}** | Aufgabe {st.session_state.counter + 1} von {limit}")
        with st.form(key=f"q_{st.session_state.phase}_{st.session_state.counter}"):
            st.markdown(f"### {st.session_state.current_q['text']}")
            user_input = st.text_input("Antwort hier eintippen:")
            submit = st.form_submit_button("Prüfen")
            
            if submit:
                if check_answer(user_input, st.session_state.current_q['answer']):
                    st.success("✨ Sehr gut! Das ist richtig.")
                    st.session_state.score += 1
                else:
                    st.error(f"❌ Nicht ganz. Richtig wäre: {st.session_state.current_q['answer']}")
                
                st.session_state.counter += 1
                if st.session_state.counter >= limit:
                    st.session_state.phase = next_ph
                    st.session_state.counter = 0 
                st.session_state.current_q = None
                st.form_submit_button("Weiter")

elif st.session_state.phase == "MIXED_INFO":
    st.success("Einzelübungen beendet! Jetzt folgen 20 gemischte Sätze.")
    if st.button("Start"):
        st.session_state.phase = "MIXED"
        st.rerun()

elif st.session_state.phase == "FINISHED":
    st.balloons()
    st.header("Geschafft!")
    st.metric("Dein Score", f"{st.session_state.score} Punkte")
    
    if st.button("Weitere 20 Sätze üben"):
        st.session_state.phase = "MIXED"
        st.session_state.counter = 0
        st.session_state.current_q = None
        st.rerun()
    
    if st.button("Zurück zum Hauptmenü"):
        st.session_state.clear()
        st.rerun()
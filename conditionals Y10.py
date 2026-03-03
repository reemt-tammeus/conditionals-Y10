import streamlit as st
import random

import streamlit as st
from PIL import Image
# Schullogo anzeigen
try:
 logo = Image.open('schullogo.png')
 st.image(logo, width=150)
except:
 pass # Falls das Bild fehlt, wird dieser Teil übersprungen
    
# --- DATENPOOL (210 SÄTZE) ---
def get_full_sentence_pool():
    # Typ 1: Realis (70 Sätze)
    t1 = [
        ("If it rains, we ___ (stay) at home.", ["will stay", "can stay", "must stay"], 1),
        ("If you study hard, you ___ (pass) the exam.", ["will pass", "can pass"], 1),
        ("If she ___ (arrive) late, the teacher will be angry.", ["arrives"], 1),
        ("I will help you if you ___ (ask) me.", ["ask"], 1),
        ("If they don't hurry, they ___ (miss) the train.", ["will miss", "might miss"], 1),
        ("If I find your key, I ___ (tell) you.", ["will tell", "can tell"], 1),
        ("If he ___ (have) enough money, he will buy a car.", ["has"], 1),
        ("The chocolate ___ (melt) if you leave it in the sun.", ["will melt", "can melt"], 1),
        ("If you ___ (eat) too much, you will feel sick.", ["eat"], 1),
        ("If we ___ (not/leave) now, we'll be late.", ["do not leave", "don't leave"], 1),
        ("She will be happy if you ___ (call) her.", ["call"], 1),
        ("If the sun shines, we ___ (go) for a walk.", ["will go", "can go"], 1),
        ("If you help me, I ___ (finish) sooner.", ["will finish", "can finish"], 1),
        ("If it ___ (be) cold, I will wear a coat.", ["is"], 1),
        ("They will play football if they ___ (find) a ball.", ["find"], 1),
        ("If I ___ (not/see) him, I will call him.", ["do not see", "don't see"], 1),
        ("If you drink this, you ___ (feel) better.", ["will feel", "should feel"], 1),
        ("If she ___ (forget) her umbrella, she'll get wet.", ["forgets"], 1),
        ("I ___ (buy) some milk if I go to the shop.", ["will buy", "can buy"], 1),
        ("If we win, we ___ (celebrate).", ["will celebrate", "can celebrate"], 1),
        ("If you ___ (not/go) to bed, you'll be tired.", ["do not go", "don't go"], 1),
        ("If he ___ (cook) dinner, I'll do the dishes.", ["cooks"], 1),
        ("The dog will bark if someone ___ (knock).", ["knocks"], 1),
        ("If you ___ (touch) that, you'll get hurt.", ["touch"], 1),
        ("If I have time, I ___ (visit) you.", ["will visit", "can visit"], 1),
        ("If the bus ___ (not/come), we'll walk.", ["does not come", "doesn't come"], 1),
        ("You ___ (get) a prize if you win.", ["will get"], 1),
        ("If she ___ (practice), she will improve.", ["practices"], 1),
        ("If it ___ (snow), we will build a snowman.", ["snows"], 1),
        ("I will lend you the book if you ___ (promise) to return it.", ["promise"], 1),
        ("If you ___ (ask) politely, he will help.", ["ask"], 1),
        ("If they ___ (watch) this movie, they will like it.", ["watch"], 1),
        ("The glass ___ (break) if you drop it.", ["will break"], 1),
        ("If you ___ (not/study), you will fail.", ["do not study", "don't study"], 1),
        ("I'll be surprised if it ___ (happen).", ["happens"], 1),
        ("If he ___ (call) me, I will answer.", ["calls"], 1),
        ("If we ___ (take) the map, we won't get lost.", ["take"], 1),
        ("If you stay here, you ___ (see) her.", ["will see", "can see"], 1),
        ("If she ___ (sing), everyone will listen.", ["sings"], 1),
        ("If they ___ (try) hard, they will succeed.", ["try"], 1),
        ("If you ___ (be) late, we will start without you.", ["are"], 1),
        ("I ___ (send) you a message if I hear anything.", ["will send", "can send"], 1),
        ("If he ___ (not/stop) shouting, I'll leave.", ["does not stop", "doesn't stop"], 1),
        ("The plants ___ (die) if you don't water them.", ["will die", "might die"], 1),
        ("If I ___ (win) the race, I'll be famous.", ["win"], 1),
        ("If the water ___ (boil), turn off the gas.", ["boils"], 1),
        ("If you ___ (want) coffee, I'll make some.", ["want"], 1),
        ("He will be upset if you ___ (lose) his book.", ["lose"], 1),
        ("If we ___ (get) lost, we'll use GPS.", ["get"], 1),
        ("I'll buy that shirt if it ___ (not/cost) too much.", ["does not cost", "doesn't cost"], 1),
        ("If she ___ (pass) the test, she will celebrate.", ["passes"], 1),
        ("You ___ (burn) yourself if you touch the stove.", ["will burn"], 1),
        ("If they ___ (arrive) early, they can wait in the hall.", ["arrive"], 1),
        ("I ___ (go) to the party if I'm invited.", ["will go"], 1),
        ("If the dog ___ (see) a cat, it will run away.", ["sees"], 1),
        ("If you ___ (tell) the truth, you'll feel better.", ["tell"], 1),
        ("We ___ (go) to the park if it's sunny.", ["will go", "can go"], 1),
        ("If she ___ (buy) the tickets, I will pay her back.", ["buys"], 1),
        ("If you ___ (need) help, just call me.", ["need"], 1),
        ("The baby ___ (cry) if she is hungry.", ["will cry"], 1),
        ("If I ___ (be) free tomorrow, I'll help you.", ["am"], 1),
        ("If he ___ (come) home, we will have dinner.", ["comes"], 1),
        ("I ___ (take) an aspirin if my head still hurts.", ["will take"], 1),
        ("If you ___ (not/hurry), you'll miss the show.", ["do not hurry", "don't hurry"], 1),
        ("If it ___ (get) dark, we will turn on the lights.", ["gets"], 1),
        ("You ___ (make) a mistake if you don't listen.", ["will make"], 1),
        ("If the car ___ (break) down, we'll call a mechanic.", ["breaks"], 1),
        ("If she ___ (look) at the map, she'll find the way.", ["looks"], 1),
        ("I ___ (wait) for you if you are late.", ["will wait"], 1),
        ("If we ___ (save) money, we will go on holiday.", ["save"], 1)
    ]

    # Typ 2: Irrealis Gegenwart (70 Sätze)
    t2 = [
        ("If I ___ (be) you, I would go home.", ["were", "was"], 2),
        ("If I won the lottery, I ___ (travel) the world.", ["would travel", "could travel", "might travel"], 2),
        ("If she ___ (have) more time, she would learn Spanish.", ["had"], 2),
        ("We ___ (buy) a house if we were rich.", ["would buy", "could buy"], 2),
        ("If it ___ (snow) in summer, I would be surprised.", ["snowed"], 2),
        ("I would help you if I ___ (can).", ["could"], 2),
        ("If they ___ (live) in France, they would speak French.", ["lived"], 2),
        ("If he ___ (be) taller, he ___ (play) basketball.", ["would play", "could play"], 2),
        ("I ___ (not/do) that if I were you.", ["would not do", "wouldn't do"], 2),
        ("If we ___ (have) a garden, we would have a dog.", ["had"], 2),
        ("If she ___ (know) his name, she would tell you.", ["knew"], 2),
        ("If I ___ (be) a bird, I would fly to Africa.", ["were", "was"], 2),
        ("You ___ (feel) better if you exercised more.", ["would feel", "might feel"], 2),
        ("If he ___ (ask) her, she would say yes.", ["asked"], 2),
        ("If I ___ (not/have) to work, I would go to the beach.", ["did not have", "didn't have"], 2),
        ("They ___ (be) happy if you visited them.", ["would be", "could be"], 2),
        ("If it ___ (be) warmer, we would swim.", ["were", "was"], 2),
        ("If she ___ (see) a ghost, she would scream.", ["saw"], 2),
        ("I ___ (call) him if I had his number.", ["would call", "might call"], 2),
        ("If we ___ (lose) the game, we would be sad.", ["lost"], 2),
        ("If I ___ (find) a wallet, I ___ (take) it to the police.", ["would take", "could take"], 2),
        ("If you ___ (speak) louder, I could hear you.", ["spoke"], 2),
        ("If she ___ (need) help, she would ask.", ["needed"], 2),
        ("We ___ (go) out if it didn't rain.", ["would go", "could go"], 2),
        ("If I ___ (own) a company, I would hire you.", ["owned"], 2),
        ("If you ___ (stop) smoking, you would be healthier.", ["stopped"], 2),
        ("If he ___ (study) more, he would get better grades.", ["studied"], 2),
        ("I ___ (tell) you the truth if I knew it.", ["would tell", "could tell"], 2),
        ("If they ___ (have) wings, they would fly.", ["had"], 2),
        ("If she ___ (be) my sister, I would tell her.", ["were", "was"], 2),
        ("If I ___ (get) the job, I would celebrate.", ["got"], 2),
        ("If we ___ (win), we would be famous.", ["won"], 2),
        ("If it ___ (be) easy, everyone would do it.", ["were", "was"], 2),
        ("If you ___ (paint) the room blue, it would look better.", ["painted"], 2),
        ("If I ___ (know) how to cook, I would make dinner.", ["knew"], 2),
        ("If she ___ (wear) that dress, she would look great.", ["wore"], 2),
        ("If they ___ (arrive) early, they would wait.", ["arrived"], 2),
        ("If he ___ (be) here, he would know what to do.", ["were", "was"], 2),
        ("If I ___ (see) him, I would say hello.", ["saw"], 2),
        ("If you ___ (want) to learn, you would listen.", ["wanted"], 2),
        ("If I ___ (have) a car, I wouldn't take the bus.", ["had"], 2),
        ("She ___ (be) angry if she knew about this.", ["would be", "might be"], 2),
        ("If we ___ (buy) the tickets now, they would be cheaper.", ["bought"], 2),
        ("If he ___ (not/smoke), he would feel better.", ["did not smoke", "didn't smoke"], 2),
        ("If it ___ (be) my birthday, I would throw a party.", ["were", "was"], 2),
        ("I ___ (buy) that laptop if I had the money.", ["would buy", "could buy"], 2),
        ("If you ___ (tell) me the secret, I wouldn't tell anyone.", ["told"], 2),
        ("If she ___ (speak) English, she could work in London.", ["spoke"], 2),
        ("If they ___ (not/shout), I would help them.", ["did not shout", "didn't shout"], 2),
        ("What ___ (you/do) if you found a diamond?", ["would you do"], 2),
        ("If I ___ (be) a millionaire, I would buy a boat.", ["were", "was"], 2),
        ("If he ___ (run) faster, he would win.", ["ran"], 2),
        ("I ___ (help) you if I wasn't so busy.", ["would help", "could help"], 2),
        ("If she ___ (ask) nicely, I would say yes.", ["asked"], 2),
        ("If we ___ (not/go) to school, we would play all day.", ["did not go", "didn't go"], 2),
        ("If I ___ (know) his address, I would visit him.", ["knew"], 2),
        ("He ___ (not/be) so tired if he went to bed early.", ["would not be", "wouldn't be"], 2),
        ("If they ___ (sell) their house, they would be rich.", ["sold"], 2),
        ("If you ___ (eat) a lemon, your face would look funny.", ["ate"], 2),
        ("If I ___ (be) a chef, I would make great pizza.", ["were", "was"], 2),
        ("She ___ (travel) more if she wasn't afraid of flying.", ["would travel", "might travel"], 2),
        ("If we ___ (have) a map, we wouldn't be lost.", ["had"], 2),
        ("If he ___ (play) the guitar, he would be in a band.", ["played"], 2),
        ("If it ___ (not/rain), we would have a picnic.", ["did not rain", "didn't rain"], 2),
        ("I ___ (lend) you my phone if I didn't need it.", ["would lend"], 2),
        ("If they ___ (invite) me, I would go.", ["invited"], 2),
        ("If you ___ (exercise) more, you'd be fit.", ["exercised"], 2),
        ("If she ___ (practice) more, she would be a pro.", ["practiced"], 2),
        ("If I ___ (see) him tomorrow, I'd be surprised.", ["saw"], 2),
        ("We ___ (stay) longer if we had time.", ["would stay", "could stay"], 2)
    ]

    # Typ 3: Irrealis Vergangenheit (70 Sätze)
    t3 = [
        ("If you had studied, you ___ (pass) the exam.", ["would have passed", "could have passed"], 3),
        ("If I ___ (see) him, I would have told him.", ["had seen"], 3),
        ("We would have arrived on time if we ___ (take) the bus.", ["had taken"], 3),
        ("If she ___ (ask) me, I would have helped her.", ["had asked"], 3),
        ("If they had known, they ___ (not/come).", ["would not have come", "wouldn't have come"], 3),
        ("I ___ (buy) that car if I had had enough money.", ["would have bought", "could have bought"], 3),
        ("If it ___ (not/rain), we would have gone out.", ["had not rained", "hadn't rained"], 3),
        ("If he ___ (be) careful, he wouldn't have fallen.", ["had been"], 3),
        ("She would have won if she ___ (run) faster.", ["had run"], 3),
        ("If we ___ (leave) earlier, we wouldn't have missed the flight.", ["had left"], 3),
        ("If you ___ (tell) me, I would have understood.", ["had told"], 3),
        ("If I ___ (know) you were coming, I would have baked a cake.", ["had known"], 3),
        ("They would have stayed if it ___ (be) warmer.", ["had been"], 3),
        ("If he ___ (not/forget) his passport, he could have traveled.", ["had not forgotten", "hadn't forgotten"], 3),
        ("If she ___ (study) harder, she would have succeeded.", ["had studied"], 3),
        ("I ___ (call) you if I hadn't lost my phone.", ["would have called", "might have called"], 3),
        ("If we ___ (pay) attention, we would have learned more.", ["had paid"], 3),
        ("If the driver ___ (stop), the accident wouldn't have happened.", ["had stopped"], 3),
        ("If you ___ (listen) to me, you wouldn't have made that mistake.", ["had listened"], 3),
        ("She ___ (be) happy if you had remembered her birthday.", ["would have been"], 3),
        ("If I ___ (find) the book, I would have given it to you.", ["had found"], 3),
        ("If they ___ (play) better, they would have won.", ["had played"], 3),
        ("We ___ (not/get) lost if we had used a map.", ["would not have gotten", "wouldn't have gotten"], 3),
        ("If he ___ (work) harder, he would have been promoted.", ["had worked"], 3),
        ("If you ___ (not/eat) so much, you wouldn't have felt sick.", ["had not eaten", "hadn't eaten"], 3),
        ("If she ___ (go) to bed earlier, she wouldn't have been tired.", ["had gone"], 3),
        ("I ___ (visit) you if I had known you were in the hospital.", ["had visited"], 3),
        ("If we ___ (have) more time, we would have finished.", ["had had"], 3),
        ("If they ___ (invite) us, we would have gone.", ["had invited"], 3),
        ("If it ___ (be) sunny, we would have gone to the park.", ["had been"], 3),
        ("If he ___ (tell) the truth, he wouldn't have been punished.", ["had told"], 3),
        ("If I ___ (not/break) my leg, I would have played.", ["had not broken", "hadn't broken"], 3),
        ("If she ___ (call) earlier, I would have answered.", ["had called"], 3),
        ("If you ___ (be) there, you would have seen it.", ["had been"], 3),
        ("If they ___ (wait), they would have met him.", ["had waited"], 3),
        ("If I ___ (study) medicine, I would have been a doctor.", ["had studied"], 3),
        ("If we ___ (book) earlier, the tickets would have been cheaper.", ["had booked"], 3),
        ("If he ___ (not/miss) the bus, he would have been on time.", ["had not missed", "hadn't missed"], 3),
        ("If she ___ (try) harder, she would have won.", ["had tried"], 3),
        ("If you ___ (ask), I would have told you.", ["had asked"], 3),
        ("If the weather ___ (be) better, we would have stayed.", ["had been"], 3),
        ("I ___ (not/buy) that dress if I had seen the price.", ["would not have bought", "wouldn't have bought"], 3),
        ("If he ___ (speak) to me, I would have forgiven him.", ["had spoken"], 3),
        ("If she ___ (not/leave) the door open, the cat wouldn't have escaped.", ["had not left", "hadn't left"], 3),
        ("If we ___ (arrive) 5 minutes earlier, we would have seen him.", ["had arrived"], 3),
        ("They ___ (be) surprised if you had told them.", ["would have been"], 3),
        ("If I ___ (not/be) so tired, I would have come to the party.", ["had not been", "hadn't been"], 3),
        ("If he ___ (show) me the way, I would have found it.", ["had shown"], 3),
        ("If you ___ (warn) us, we wouldn't have gone there.", ["had warned"], 3),
        ("I ___ (finish) the report if my computer hadn't crashed.", ["would have finished", "could have finished"], 3),
        ("If she ___ (know) about the meeting, she would have attended.", ["had known"], 3),
        ("If they ___ (buy) the house, they would have been happy.", ["had bought"], 3),
        ("If we ___ (not/lose) our keys, we wouldn't have waited outside.", ["had not lost", "hadn't lost"], 3),
        ("If it ___ (not/be) for you, I would have failed.", ["had not been", "hadn't been"], 3),
        ("If he ___ (bring) his guitar, he would have played.", ["had brought"], 3),
        ("If you ___ (ask) the waiter, he would have helped you.", ["had asked"], 3),
        ("I ___ (go) to the concert if I had had a ticket.", ["would have gone"], 3),
        ("If she ___ (take) the medicine, she would have felt better.", ["had taken"], 3),
        ("If they ___ (see) the sign, they wouldn't have entered.", ["had seen"], 3),
        ("If the team ___ (play) better, they would have won the cup.", ["had played"], 3),
        ("If I ___ (have) your number, I would have called you.", ["had had"], 3),
        ("If he ___ (not/fall), he would have won the race.", ["had not fallen", "hadn't fallen"], 3),
        ("If we ___ (save) more, we would have bought a car.", ["had saved"], 3),
        ("If she ___ (not/be) so busy, she would have called.", ["had not been", "hadn't been"], 3),
        ("If you ___ (tell) me earlier, I would have been there.", ["had told"], 3),
        ("If I ___ (win), I would have been so happy.", ["had won"], 3),
        ("If they ___ (listen), they would have known what to do.", ["had listened"], 3),
        ("If it ___ (be) colder, it would have snowed.", ["had been"], 3),
        ("If you ___ (not/forget) the map, we wouldn't have been lost.", ["had not forgotten", "hadn't forgotten"], 3),
        ("If he ___ (ask) for help, I would have helped.", ["had asked"], 3)
    ]

    all_data = t1 + t2 + t3
    return [{"text": s[0], "answers": s[1], "type": s[2]} for s in all_data]

# --- STREAMLIT APP LOGIK ---
st.set_page_config(page_title="Conditional Trainer 210", page_icon="📝")

# Session State initialisieren
if 'phase' not in st.session_state:
    st.session_state.phase = "START"
    st.session_state.pool = get_full_sentence_pool()
    st.session_state.used_ids = []
    st.session_state.current_q = None
    st.session_state.score = 0
    st.session_state.counter = 0
    st.session_state.feedback = None
    st.session_state.mistakes = [] # Liste für die Fehleranalyse

def get_next_question(q_type=None):
    available = [i for i, s in enumerate(st.session_state.pool) if (q_type is None or s['type'] == q_type) and i not in st.session_state.used_ids]
    if not available: return None
    idx = random.choice(available)
    st.session_state.used_ids.append(idx)
    return st.session_state.pool[idx]

st.title("🇬🇧 Conditional Sentences Trainer")
st.write("---")

if st.session_state.phase == "START":
    st.write("Trainiere If-Clauses Typ I, II und III.")
    st.write("Möchtest du die Typen erst einzeln üben (je 5 Sätze pro Typ)?")
    col1, col2 = st.columns(2)
    if col1.button("Ja, Typen einzeln"):
        st.session_state.phase = "DRILL_1"
        st.rerun()
    if col2.button("Nein, direkt mischen"):
        st.session_state.phase = "MIXED"
        st.rerun()

elif st.session_state.phase in ["DRILL_1", "DRILL_2", "DRILL_3", "MIXED"]:
    # Konfiguration
    if st.session_state.phase == "DRILL_1": target, limit, label = 1, 5, "Typ I"
    elif st.session_state.phase == "DRILL_2": target, limit, label = 2, 5, "Typ II"
    elif st.session_state.phase == "DRILL_3": target, limit, label = 3, 5, "Typ III"
    else: target, limit, label = None, 20, "Gemischtes Training"

    st.subheader(f"Modus: {label}")
    st.info(f"Satz {st.session_state.counter + 1} von {limit}")

    if st.session_state.current_q is None:
        st.session_state.current_q = get_next_question(target)

    if st.session_state.current_q:
        st.markdown(f"### {st.session_state.current_q['text']}")
        user_input = st.text_input("Antwort eingeben:", key=f"q_{len(st.session_state.used_ids)}").strip()
        
        if st.button("Prüfen"):
            correct_list = st.session_state.current_q['answers']
            if user_input.lower() in [a.lower() for a in correct_list]:
                st.session_state.feedback = ("success", "Korrekt!")
                st.session_state.score += 1
            else:
                st.session_state.feedback = ("error", f"Falsch. Richtig: {' / '.join(correct_list)}")
                # Fehler für Analyse speichern
                st.session_state.mistakes.append({
                    "text": st.session_state.current_q['text'],
                    "user": user_input,
                    "correct": " / ".join(correct_list)
                })
        
        if st.session_state.feedback:
            if st.session_state.feedback[0] == "success": st.success(st.session_state.feedback[1])
            else: st.error(st.session_state.feedback[1])
            
            if st.button("Weiter"):
                st.session_state.counter += 1
                st.session_state.feedback = None
                st.session_state.current_q = None
                
                # Logik für Phasenwechsel
                if st.session_state.phase.startswith("DRILL") and st.session_state.counter >= 5:
                    if st.session_state.phase == "DRILL_1": st.session_state.phase = "DRILL_2"
                    elif st.session_state.phase == "DRILL_2": st.session_state.phase = "DRILL_3"
                    elif st.session_state.phase == "DRILL_3": 
                        st.session_state.phase = "MIXED"
                        st.session_state.counter = 0
                    st.session_state.counter = 0
                elif st.session_state.phase == "MIXED" and st.session_state.counter >= 20:
                    st.session_state.phase = "FINISHED"
                st.rerun()

elif st.session_state.phase == "FINISHED":
    st.balloons()
    st.header("Training beendet!")
    st.write(f"Du hast insgesamt {st.session_state.score} Punkte erreicht.")
    
    # Fehleranalyse anzeigen
    if st.session_state.mistakes:
        with st.expander("Deine Fehleranalyse ansehen"):
            for m in st.session_state.mistakes:
                st.write(f"**Satz:** {m['text']}")
                st.write(f"❌ Deine Antwort: {m['user']}")
                st.write(f"✅ Korrekt: {m['correct']}")
                st.write("---")
    else:
        st.success("Perfekt! Du hast keine Fehler gemacht.")

    if st.button("Noch 20 Sätze üben"):
        st.session_state.phase = "MIXED"
        st.session_state.counter = 0
        st.session_state.current_q = None
        st.session_state.mistakes = [] # Reset Fehlerliste für neue Runde
        st.rerun()
    
    if st.button("Zum Hauptmenü"):
        st.session_state.phase = "START"
        st.session_state.used_ids = []
        st.session_state.score = 0
        st.session_state.mistakes = []
        st.rerun()



from Automata import Automata
from AutomataAnimation import AutomataAnimation

for i in range(1,2):
    current_automata = f"automaton/B4-{i}.txt"
    t = Automata(source_file=current_automata, output_file=f"B4-{i}")
    print(i)
    print(t)
    print(t.transitions)
    print("--------------------------------")

    AutomataAnimation.determinize_animation(t)
    # print(f"{i} :")
    # print(repr(t))


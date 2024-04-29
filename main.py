def parse_automaton(filename):
    states = []
    alphabet = []
    hole_transitions = []
    state = "Estados"

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line == "Estados":
                state = "Estado"
            elif line == "Alfabeto":
                print("Alfabeto")
                state = "Alfabeto"
            elif line == "Transiciones":
                print("Transiciones")
                state = "Transiciones"
            else:
                if state == "Estado":
                    states.append(line)
                elif state == "Alfabeto":
                    alphabet.append(line)
                elif state == "Transiciones":
                    hole_transitions.append(line)

    return [states, alphabet, hole_transitions]

def transform_transitions(transition_strings):
    transformed_transitions = []
    for transition_str in transition_strings:
        parts = transition_str.split()
        origin = parts[0]
        symbol = parts[1]
        destination = parts[-1]
        transformed_transitions.append([origin, symbol, destination])
    return transformed_transitions

def initial_and_final_states(list_states):
    initial = []
    final = []
    for i in list_states:
        if ">" in i:
            initial.append(i)
        elif "*" in i:
            final.append(i)
        else:
            print("regular state")

    return [initial, final]

def minimize_automaton(states, alphabet, transitions, initial_state, accepting_states):
    # Step 1: Remove unreachable states
    reachable_states = {initial_state}
    pending_states = [initial_state]
    while pending_states:
        current_state = pending_states.pop()
        for transition in transitions:
            if transition[0] == current_state:
                next_state = transition[2]
                if next_state not in reachable_states:
                    reachable_states.add(next_state)
                    pending_states.append(next_state)
    
    # Remove unreachable states from the states, transitions, and accepting_states lists
    states = [state for state in states if state in reachable_states]
    transitions = [transition for transition in transitions if transition[0] in reachable_states and transition[2] in reachable_states]
    accepting_states = [state for state in accepting_states if state in reachable_states]

    # Step 2: Merge indistinguishable states
    equivalent_classes = [{state} for state in states if state not in accepting_states]
    equivalent_classes.append(set(accepting_states))

    changed = True
    while changed:
        changed = False
        for symbol in alphabet:
            new_equivalent_classes = []
            for equivalent_class in equivalent_classes:
                partitions = {}
                for state in equivalent_class:
                    for transition in transitions:
                        if transition[0] == state and transition[1] == symbol:
                            dest = transition[2]
                            for idx, ec in enumerate(equivalent_classes):
                                if dest in ec:
                                    partitions[idx] = partitions.get(idx, set()) | {state}
                                    break
                new_equivalent_classes.extend(partitions.values())
            if len(new_equivalent_classes) != len(equivalent_classes):
                changed = True
                equivalent_classes = new_equivalent_classes

    # Step 3: Create minimized transitions
    minimized_transitions = []
    for equivalent_class in equivalent_classes:
        representative_state = next(iter(equivalent_class))
        for symbol in alphabet:
            for transition in transitions:
                if transition[0] == representative_state and transition[1] == symbol:
                    dest = transition[2]
                    for idx, ec in enumerate(equivalent_classes):
                        if dest in ec:
                            minimized_transitions.append([representative_state, symbol, next(iter(ec))])
                            break

    return states, alphabet, minimized_transitions, initial_state, accepting_states


filename = "dfa_input.txt"  # Replace with the actual filename

parsing_automaton = parse_automaton(filename)
dirty_transitions = parsing_automaton[2]

states = parsing_automaton[0]
alphabet = parsing_automaton[1]
transitions = transform_transitions(dirty_transitions)

print("States:", states)
print("Alphabet:", alphabet)
print("Transitions:", transitions)

special_states = initial_and_final_states(states)
initial_state = special_states[0][0]
final_states = special_states[1]

minimized_states, minimized_alphabet, minimized_transitions, minimized_initial_state, minimized_accepting_states = minimize_automaton(states, alphabet, transitions, initial_state, final_states) 

print("Minimized States:", minimized_states)
print("Minimized Alphabet:", minimized_alphabet)
print("Minimized Transitions:", minimized_transitions)
print("Minimized Initial State:", minimized_initial_state)
print("Minimized Accepting States:", minimized_accepting_states)
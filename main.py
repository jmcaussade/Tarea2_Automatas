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
                print("dentro")
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


# Example usage
filename = "dfa_input.txt"  # Replace with the actual filename
# states, alphabet, transitions = parse_automaton(filename)

# print("States:", states)
# print("Alphabet:", alphabet)
# print("Transitions:", transitions)


parsing_automaton = parse_automaton(filename)
print(parsing_automaton)
dirty_transitions = parsing_automaton[2]
print(f"dirty_transitions: {dirty_transitions}")
transitions = transform_transitions(dirty_transitions)
print(f"transitions: {transitions}")
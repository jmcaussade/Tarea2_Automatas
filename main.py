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



# Example usage
filename = "dfa_input.txt"  # Replace with the actual filename
# states, alphabet, transitions = parse_automaton(filename)

# print("States:", states)
# print("Alphabet:", alphabet)
# print("Transitions:", transitions)


x = parse_automaton(filename)
print(x)
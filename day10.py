import itertools

machines = []
total_presses = 0

class Machine: 
    def __init__(self, lights, buttons, joltage):
        self.lights = lights
        self.buttons = buttons
        self.joltage = joltage

def button_conversion(button, lights_length):
    new_button = [0] * lights_length
    for number in button:
        new_button[int(number)] = 1
    return new_button


with open('day10input.txt', 'r') as file: 
    for row in file: 
        instruction = row.strip()
        instruction = instruction.split(" ")
        
        # Parse light indicator 
        light_indicator = instruction[0].translate(str.maketrans({"[" : "", "]" : "", "." : "0", "#" : "1"}))
        
        # Parse joltage
        joltage = instruction[-1].translate(str.maketrans({"{" : "", "}" : ""}))
        joltage_array = joltage.split(",")
        
        # Parse buttons
        buttons = []
        b = 1
        while b < len(instruction) - 1: 
            button = instruction[b].translate(str.maketrans({"(" : "", ")" : ""}))
            button = button.split(",")
            buttons.append(button)
            b += 1

        new_machine = Machine(light_indicator, buttons, joltage)
        machines.append(new_machine)


for machine in machines: 
    lights_length = len(machine.lights)
    
    # Array to compare button presses with
    target_lights = []
    for character in machine.lights:
        target_lights.append(int(character))

    # Create int array of button instructions
    button_array = []
    for button in machine.buttons:
        button_array.append(button_conversion(button, lights_length))
    
    # Simulate button presses, with increasing number of total presses 
    # until a solution is found
    presses = 1    
    solution_found = False
    while not solution_found: 
        # Find groups of buttons to press
        num_buttons = []
        i = 0
        for button in machine.buttons:
            num_buttons.append(i)
            i += 1
        groups = itertools.combinations_with_replacement(num_buttons, presses)
        
        for pair in groups:
            j = 1 # Number of buttons in combo
            button_combo = button_array[pair[0]].copy()
            while j < len(pair):
                l = 0 # Light indicator index
                while l < lights_length:
                    button_combo[l] = (button_combo[l] + button_array[pair[j]][l]) % 2 
                    l += 1
                j += 1

            # Compare with target light indicator
            if target_lights == button_combo:
                total_presses += len(pair)
                solution_found = True
                break      

        presses += 1

print("Minimum Button Presses: " + str(total_presses))
# THIS IS A WIP - SOLUTION IS NOT CORRECT

import numpy as np

machines = []
light_total_presses = 0
joltage_total_presses = 0

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

        new_machine = Machine(light_indicator, buttons, joltage_array)
        machines.append(new_machine)


for machine in machines: 
    joltage_length = len(machine.lights)

    # Joltage indicator array to compare button presses with
    target_joltage = []
    for joltage in machine.joltage:
        target_joltage.append(int(joltage))
    print(target_joltage)

    # Create int array of button instructions 
    button_array = []
    for button in machine.buttons:
        button_array.append(button_conversion(button, joltage_length))
    matrix = np.transpose(button_array)
    print(matrix)
    
    # Solve system of linear equations to find button presses
    #solution = np.linalg.solve(matrix, target_joltage)
    #print(solution)

print("Minimum Button Presses (Joltage Indicator): " + str(joltage_total_presses))

import re

import engine_generation

def strip_special_characters(string):
    # Replace spaces and special characters with underscores
    stripped_string = re.sub(r'\W+', '_', string.replace(' ', '_'))

    return stripped_string

def generate_firing_order_inline(cylinders):
    if cylinders < 2:
        print("You need at least 2 cylinders to generate a firing order")
        return
    firing_order = []

    for i in range(1, cylinders + 1, 2):
        firing_order.append(i)

    for i in range(2, cylinders + 1, 2):
        firing_order.append(i)

    return firing_order

def generate_firing_order_v(cylinders):
    if cylinders < 4:
        return "Invalid number of cylinders. Minimum of 4 cylinders required."

    left_bank = []
    right_bank = []
    for i in range(1, cylinders + 1):
        if i % 2 == 0:
            right_bank.append(i)
        else:
            left_bank.append(i)

    extra_cylinders = cylinders % 2
    if extra_cylinders == 1:
        if len(left_bank) > len(right_bank):
            right_bank.append(cylinders)
        else:
            left_bank.append(cylinders)
    
    firing_order = left_bank + right_bank
    
    return firing_order, left_bank, right_bank

def generate_inline(cylinderCount, fuel_type):
    print("Generating inline style engine...")
    cylinders = generate_firing_order_inline(cylinderCount)
    cylinders0 = []

    for i in range(1, cylinderCount + 1):
        cylinders0.append(i)
    
    bank = engine_generation.Bank(cylinders0, 0)
    engine = engine_generation.Engine([bank], cylinders, fuel_type)
    engine.engine_name = input("Engine name: ")
    engine.starter_torque = int(input("Starter torque: "))
    engine.crank_mass = int(input("Crank mass: "))
    engine.bore = float(input("Cylinder bore: "))
    engine.stroke = float(input("Cylinder stroke: "))
    engine.chamber_volume = int(input("Chamber volume: "))
    engine.rod_length = float(input("Cylinder rod length: "))
    engine.simulation_frequency = int(input("Simulation frequency (default 1200): "))
    engine.max_sle_solver_steps = int(input("Max sle solver steps (default 4): "))
    engine.fluid_simulation_steps = int(input("Fluid simulation steps (default 4): "))
    engine.idle_throttle_plate_position = float(input("Idle throttle plate position: "))

    engine.generate()
    engine.write_to_file(strip_special_characters(engine.engine_name) + ".mr")

def generate_v(cylinderCount, fuel_type):
    print("Generating V style engine...")
    cylinders, cylinders0, cylinders1 = generate_firing_order_v(cylinderCount)

    bank0 = engine_generation.Bank(cylinders0, -45)
    bank1 = engine_generation.Bank(cylinders1, 45)

    engine = engine_generation.Engine([bank0, bank1], cylinders, fuel_type)
    
    engine.engine_name = input("Engine name: ")
    engine.starter_torque = int(input("Starter torque: "))
    engine.crank_mass = int(input("Crank mass: "))
    engine.bore = float(input("Cylinder bore: "))
    engine.stroke = float(input("Cylinder stroke: "))
    engine.chamber_volume = int(input("Chamber volume: "))
    engine.rod_length = float(input("Cylinder rod length: "))
    engine.simulation_frequency = int(input("Simulation frequency (default 1200): "))
    engine.max_sle_solver_steps = int(input("Max sle solver steps (default 4): "))
    engine.fluid_simulation_steps = int(input("Fluid simulation steps (default 4): "))
    engine.idle_throttle_plate_position = float(input("Idle throttle plate position: "))

    engine.generate()
    engine.write_to_file(strip_special_characters(engine.engine_name) + ".mr")

def generate_custom_engine():
    print("Generating custom engine...")

    print("Engine Styles:\n   - Inline\n   - V")
    style = input("Enter style: ")
    if style.lower() != "inline" and style.lower() != "v":
        print("Invalid style. Must either be inline or v.")
        return
    cylinderCount = int(input("Enter cylinder count: "))
    if cylinderCount < 2:
        print("Invalid cylinders, must be greater than 1 for inline style.")
        return
    if cylinderCount < 4 and style.lower() == "v":
        print("Invalid cylinders, must be greater than 3 for V style.")
        return
    if style.lower() == "inline":
        generate_inline(cylinderCount)
    elif style.lower() == "v":
        generate_v(cylinderCount)

def generate_inline_test_engine(cylinderCount, name):
    print("Generating inline test engine...")
    cylinders = generate_firing_order_inline(cylinderCount)

    print(f"Firing order: {cylinders}")

    cylinders0 = []

    for i in range(1, cylinderCount + 1):
        cylinders0.append(i)
    
    print(f"cylinders0: {cylinders0}")

    bank = engine_generation.Bank(cylinders0, 0)
    engine = engine_generation.Engine([bank], cylinders)
    engine.engine_name = name
    engine.starter_torque = 800
    engine.crank_mass = 60
    engine.bore = 60
    engine.stroke = 60
    engine.chamber_volume = 600
    engine.rod_length = 110
    engine.simulation_frequency = 1200
    engine.max_sle_solver_steps = 4
    engine.fluid_simulation_steps = 4
    engine.idle_throttle_plate_position = 0.9

    engine.generate()
    engine.write_to_file(strip_special_characters(engine.engine_name) + ".mr")

if __name__ == "__main__":
    generate_inline_test_engine(4, "I4 Test")

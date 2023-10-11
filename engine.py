
import engine_generator
import re

import engine_generator

class Fuel_Type:
    fuel_types = {
        "regular": engine_generator.gasoline_regular,
        "midgrade": engine_generator.gasoline_midgrade,
        "premium": engine_generator.gasoline_premium,
        "hexane": engine_generator.hexane,
        "high octane": engine_generator.high_octane,
        "pure octane": engine_generator.pure_octane,
        "hydrogen": engine_generator.hydrogen,
        "oxygen": engine_generator.oxygen,
        "hydrogen oxygen": engine_generator.hydrogen_oxygen,
        "hydrazine": engine_generator.hydrazine,
        "ethanol": engine_generator.ethanol,
        "isopropyl alcohol": engine_generator.isopropyl_alcohol,
        "butyl alcohol": engine_generator.butyl_alcohol,
        "kerosene": engine_generator.kerosene,
        "nos": engine_generator.nos,
        "nos octane": engine_generator.nos_octane,
        "diesel": engine_generator.diesel
    }

    @staticmethod
    def getFuelType(fuel_type):
        fuel_type = fuel_type.lower()
        if fuel_type in Fuel_Type.fuel_types:
            return Fuel_Type.fuel_types[fuel_type]
        else:
            print(f"{fuel_type} is an invalid fuel type")

    @staticmethod
    def printAvailableFuelTypes():
        print("Available fuel types:")
        for fuel_type in Fuel_Type.fuel_types:
            print(f"- {fuel_type.capitalize()}")


def strip_special_characters(string):
    # Replace spaces and special characters with underscores
    stripped_string = re.sub(r'\W+', '_', string.replace(' ', '_'))

    return stripped_string

def generate_firing_order_inline(cylinders):
    if cylinders < 2:
        print("You need at least 2 cylinders to generate a firing order")
        return
    firing_order = []

    firing_order.append(0)

    for i in range(cylinders):
        if i % 2 != 0 and i not in firing_order:
            firing_order.append(i)
        
    for i in range(cylinders):
        if i % 2 == 0 and i not in firing_order:
            firing_order.append(i)


    return firing_order

def generate_firing_order_v(cylinders):
    if cylinders < 4:
        return "Invalid number of cylinders. Minimum of 4 cylinders required."

    left_bank = []
    right_bank = []
    for i in range(cylinders):
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

    for i in range(cylinderCount):
        cylinders0.append(i)
    
    bank = engine_generator.Bank(cylinders0, 0)
    engine = engine_generator.Engine([bank], cylinders, fuel_type)
    default_values = {
    "engine_name": engine.engine_name,
    "starter_torque": engine.starter_torque,
    "crank_mass": engine.crank_mass,
    "bore": engine.bore,
    "stroke": engine.stroke,
    "chamber_volume": engine.chamber_volume,
    "rod_length": engine.rod_length,
    "simulation_frequency": engine.simulation_frequency,
    "max_sle_solver_steps": engine.max_sle_solver_steps,
    "fluid_simulation_steps": engine.fluid_simulation_steps,
    "idle_throttle_plate_position": engine.idle_throttle_plate_position
    }

    print("CONFIGURING ENGINE... (LEAVE BLANK IF YOU WANT TO USE ENGINE'S DEFAULT VALUES)")
    
    for key, value in default_values.items():
        user_input = input(f"{key} DEFAULT VALUE({value}): ")
        if user_input:
            setattr(engine, key, user_input)


    engine.generate()
    engine.write_to_file(strip_special_characters(engine.engine_name) + ".mr")

def generate_v(cylinderCount, fuel_type):
    print("Generating V style engine...")
    cylinders, cylinders0, cylinders1 = generate_firing_order_v(cylinderCount)

    bank0 = engine_generator.Bank(cylinders0, -45)
    bank1 = engine_generator.Bank(cylinders1, 45)

    engine = engine_generator.Engine([bank0, bank1], cylinders, fuel_type)
    
    default_values = {
    "engine_name": engine.engine_name,
    "starter_torque": engine.starter_torque,
    "crank_mass": engine.crank_mass,
    "bore": engine.bore,
    "stroke": engine.stroke,
    "chamber_volume": engine.chamber_volume,
    "rod_length": engine.rod_length,
    "simulation_frequency": engine.simulation_frequency,
    "max_sle_solver_steps": engine.max_sle_solver_steps,
    "fluid_simulation_steps": engine.fluid_simulation_steps,
    "idle_throttle_plate_position": engine.idle_throttle_plate_position
    }

    print("CONFIGURING ENGINE... (LEAVE BLANK IF YOU WANT TO USE ENGINE'S DEFAULT VALUES)")
    
    for key, value in default_values.items():
        user_input = input(f"{key}: ")
        if user_input:
            setattr(engine, key, user_input)

    engine.generate()
    engine.write_to_file(strip_special_characters(engine.engine_name) + ".mr")

def generate_custom_engine():
    print("Generating custom engine...")

    Fuel_Type.printAvailableFuelTypes()
    fuel_type = Fuel_Type.getFuelType(input("Fuel type: "))

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
        generate_inline(cylinderCount, fuel_type)
    elif style.lower() == "v":
        generate_v(cylinderCount, fuel_type)

def generate_inline_test_engine(cylinderCount, fuel_type, name):
    print("Generating inline test engine...")
    cylinders = generate_firing_order_inline(cylinderCount)

    print(f"Firing order: {cylinders}")

    cylinders0 = []

    for i in range(1, cylinderCount + 1):
        cylinders0.append(i)
    
    print(f"cylinders0: {cylinders0}")

    bank = engine_generator.Bank(cylinders0, 0)
    engine = engine_generator.Engine([bank], cylinders)
    engine.fuel = fuel_type
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
    generate_custom_engine()

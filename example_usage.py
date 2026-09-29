from client import AutonomousTestGenerator

int_inputs = AutonomousTestGenerator.generate_fuzz_inputs("int")
str_inputs = AutonomousTestGenerator.generate_fuzz_inputs("str")

print("Synthesized Integer Boundary Cases:", int_inputs)
print("Synthesized String Boundary Cases:", str_inputs)

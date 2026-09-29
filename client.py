"""Autonomous Test Suite & Boundary Value Fuzz Input Synthesizer.
100% Python Standard Library.
"""

class AutonomousTestGenerator:
    """Generates boundary value fuzz inputs across scalar and sequence types."""
    @staticmethod
    def generate_fuzz_inputs(type_name, count=5):
        if type_name == "int":
            return [0, 1, -1, 2**31 - 1, -2**31]
        elif type_name == "str":
            return ["", "a", "Hello World", "!@#$%^&*()", "A" * 256]
        elif type_name == "list":
            return [[], [0], [1, 2, 3], [-1, -2]]
        elif type_name == "float":
            return [0.0, 1.0, -1.0, 1e-6, 1e6]
        return [None] * count

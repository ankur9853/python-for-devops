import importlib

calc_new = importlib.import_module("calculator-new")

print(f"Result of addition: {calc_new.addition(5, 3)}")

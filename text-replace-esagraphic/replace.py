import re

original_text = 'A dogmatic dog buys dogecoin to become rich and buy hotdogs every day.'

modified_text = re.sub(r'\bdog\b', 'cat', original_text)

print(f"Modified text: {modified_text}")


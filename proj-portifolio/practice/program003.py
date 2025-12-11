import sys
import subprocess

# insteresting, you can change the list of the function inside the module
# sys.argv = sys.argv[1:]
# print(sys.argv)

subprocess.run(
    "cls",
    shell=True
)

sys.argv = sys.argv[1:]
print('\n\n')
print(sys.argv[0].replace("/", '\\'))
print("\n\n")

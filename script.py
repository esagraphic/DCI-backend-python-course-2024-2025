import os
import subprocess

# List of submodule folders to clean up
submodule_folders = [
    "algorithmic-thinking-algorithm-efficiency-esagraphic",
    "collections-basics-1-esagraphic",
    "collections-swap-esagraphic",
    "comparison-operators-esagraphic",
    "control-flow-esagraphic","algorithmic-thinking-algorithm-efficiency-esagraphic", 
    "datetime-creation-esagraphic",
    "datetime-manipulation-esagraphic",
    "digit-filter-esagraphic",
    "dirk@chlosta.live\\012015221373907",
    "function-intermediate-1-esagraphic",
    "functions-decorators-i-esagraphic",
    "functions-decorators-ii-esagraphic",
    "functions-lambda-i-esagraphic",
    "functions-lambda-ii-esagraphic",
    "functions-parameters-i-esagraphic",
    "functions-parameters-ii-esagraphic",
    "functions-recursion-i-esagraphic",
    "functions-recursion-ii-esagraphic",
    "ipdb-debugging-esagraphic",
    "logical-thinking-i-esagraphic",
    "logical-thinking-ii-esagraphic",
    "oop-concepts-class-vs-instance-esagraphic",
    "python-algorithmic-thinking-quicksort-esagraphic",
    "python-basic-oop-1-esagraphic",
    "python-calendar-esagraphic",
    "python-debugging-esagraphic",
    "python-exceptions-esagraphic",
    "python-introduction-bug-fixing-esagraphic",
    "python-introduction-hello-world-comments-esagraphic",
    "python-introduction-math-operators-esagraphic",
    "python-oop-01-inheritance-v2-esagraphic",
    "python-oop-02-inheritance-esagraphic",
    "python-oop-advanced-abstract-class-esagraphic",
    "python-oop-basic-03-applicant-app-esagraphic",
    "python-oop-design-patterns-esagraphic",
    "python-testing-tdd-part-1-esagraphic",
    "python-testing-unittest-01-esagraphic",
    "python-testing-unittest-02-esagraphic",
    "statements-and-loops-for-loop-esagraphic",
    "statements-and-loops-while-loop-esagraphic",
    "text-capslockday-esagraphic",
    "text-case-esagraphic",
    "text-inator-esagraphic",
    "text-join-esagraphic",
    "text-lenth-esagraphic",
    "text-replace-esagraphic",
    "texts-basics-2-esagraphic",
    "texts-regex-1-esagraphic",
    "timezone-esagraphic",
    "warehouse-project-collections-esagraphic",
    "warehouse-project-introduction-esagraphic" # Add all submodule folder names here
    # Add other submodule directories if needed
]

# Function to clean up a submodule
def clean_submodule(submodule_path):
    print(f"Cleaning submodule: {submodule_path}")
    
    # Deinitialize the submodule
    subprocess.run(["git", "submodule", "deinit", "-f", submodule_path], check=True)
    
    # Remove it from the index
    subprocess.run(["git", "rm", "--cached", submodule_path], check=True)
    
    # Remove any remaining files in the submodule folder
    subprocess.run(["rm", "-rf", f".git/modules/{submodule_path}"], check=True)

    print(f"Submodule {submodule_path} cleaned.")

# Function to reinitialize submodules if needed
def reinitialize_submodules():
    print("Reinitializing submodules...")
    subprocess.run(["git", "submodule", "init"], check=True)
    subprocess.run(["git", "submodule", "update", "--recursive"], check=True)
    print("Submodules reinitialized.")

# Function to check and fix the .gitmodules file (if necessary)
def check_gitmodules():
    print("Checking .gitmodules file...")
    with open(".gitmodules", "r") as file:
        content = file.read()
    
    for submodule_path in submodule_folders:
        if submodule_path not in content:
            print(f"Submodule entry missing for {submodule_path}. Adding it...")
            with open(".gitmodules", "a") as file:
                file.write(f"[submodule \"{submodule_path}\"]\n")
                file.write(f"    path = {submodule_path}\n")
                file.write(f"    url = <url-of-the-submodule-repository>\n")
    
    print(".gitmodules file checked.")

# Function to commit the changes
def commit_changes():
    print("Committing changes...")
    subprocess.run(["git", "add", ".gitmodules"], check=True)
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Fix submodule references"], check=True)
    print("Changes committed.")

# Main execution
if __name__ == "__main__":
    for folder in submodule_folders:
        clean_submodule(folder)
    
    # Optionally reinitialize submodules if needed
    reinitialize_submodules()
    
    # Check and fix .gitmodules file if necessary
    check_gitmodules()
    
    # Commit changes
    commit_changes()

    print("Submodule cleanup process completed.")

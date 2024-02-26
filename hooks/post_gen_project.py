#!/usr/bin/env python
import os
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

if __name__ == "__main__":
    # Run the rest of the setup here
    subprocess.call(["git", "init"])
    subprocess.call(["git", "branch", "-m", "main"])
    subprocess.call(["python", "-m", "pip", "install", "pip", "wheel", "--upgrade"])
    subprocess.call(["poetry", "install", "--no-root"])
    subprocess.call(["pre-commit", "install"])
    subprocess.call(["pre-commit", "autoupdate"])
    subprocess.call(["pre-commit", "run", "-a"])
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", "feat: Project initialisation"])
    subprocess.call(["git", "tag", "-a", "0.0.1", "-m", "feat: Project initialisation"])
    print(
        """
                    Happy Coding!
        """
    )

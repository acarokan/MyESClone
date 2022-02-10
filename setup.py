from cx_Freeze import setup, Executable

executables = [
    Executable(
        script="main.py",
        icon="assets/app-icon.ico"
    )
]

setup(
    name="MyESClone",
    version="0.1",
    executables=executables
)
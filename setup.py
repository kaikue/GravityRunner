from cx_Freeze import setup, Executable
includes = ["re"]
includefiles = ["img"]

setup(name = "Gravity Runner",version = "1",description = "Collect coins for high score",executables = [Executable("Game.py")], options = {"build_exe": {"includes":includes, 'include_files':includefiles}})
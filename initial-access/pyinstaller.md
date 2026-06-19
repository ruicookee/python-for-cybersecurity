

# os Handbook
Main Job: Interacts With OS
- `os.getcwd()`
- `os.chdir("C:Fart")` changes directory
- `os.listdir()` or `os.listdir("C:Fart")` lists files
- `os.mkdir("foldername")`
- `os.mkdirs("build/dist/logs")` 
- `os.remove("temp.exe")`
- `os.path.exists("file.txt")` returns bool
- `os.path.isfile()` or `os.path.isdir()`
- `os.path.join(folder, file)`
- `os.path.basename("John/Desktop/kities.png")` returns the last slash

# shutil Handbook
Main Job: High Level Files Operations
- `shutil.move("a.py", "b.py")` is mv
- `shutil.copy("source.txt", "copy.txt")` is cp
- `shutil.rmtree("build")` whole tree gone bruh
- `shutil.which("executable")` finds and returns path of executables

# PyInstaller.__main__ Handbook
Main Job: Build Python Scripts into Executables
- `PyInstaller.__main__.run(["main.py"])`
- `[, "--onefile"]` compresses an entire program (including all its code, libraries, dependencies) into a single exe
- `[, "--noconsole"]`
- `[, "--name=MyFile"]` custom name MyFile.exe
- `[, "--clean"]` removes old cache
- `[, "--icon=MyIcon"]`
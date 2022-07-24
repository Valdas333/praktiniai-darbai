import os

cwd = os.getcwd()

print("Current working directory:", cwd)


os.chdir("C:/Users/Valdemaras/Desktop/Mokslai/code_academy_Python/Praktines_uzduotys/OS_modulis")

cwd1 = os.getcwd()
print("Current working directory1:", cwd1)
demofile = open("demofile.txt", "w")
demofile.write("Teksto papildymas faile!")
demofile.close()

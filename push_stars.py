import os

repos = [
    r'c:\Users\Arslan Malik\Desktop\lumushopifytheme',
    r'c:\Users\Arslan Malik\Desktop\lumushopifytheme\other_stores\lumushopifythemeforUK',
    r'c:\Users\Arslan Malik\Desktop\lumushopifytheme\other_stores\lumushopifythemeforUS'
]

for repo in repos:
    print(f"Pushing {repo}")
    os.chdir(repo)
    os.system("git add .")
    os.system('git commit -m "Fix fake full stars in review sections to mix 4-star ratings"')
    os.system("git push")

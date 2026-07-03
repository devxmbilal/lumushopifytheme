import os
import re

repos = [
    r'c:\Users\Arslan Malik\Desktop\lumushopifytheme',
    r'c:\Users\Arslan Malik\Desktop\lumushopifytheme\other_stores\lumushopifythemeforUK',
    r'c:\Users\Arslan Malik\Desktop\lumushopifytheme\other_stores\lumushopifythemeforUS'
]

# A sequence to make it look random but deterministic across 16 reviews
# We'll use 5, 4, 5, 5, 3, 5, 4, 5, 5, 4, 5, 3, 5, 5, 4, 5
stars_sequence = [
    '★★★★★', # 1
    '★★★★☆', # 2
    '★★★★★', # 3
    '★★★★★', # 4
    '★★★☆☆', # 5
    '★★★★★', # 6
    '★★★★☆', # 7
    '★★★★★', # 8
    '★★★★★', # 9
    '★★★★☆', # 10
    '★★★★★', # 11
    '★★★☆☆', # 12
    '★★★★★', # 13
    '★★★★★', # 14
    '★★★★☆', # 15
    '★★★★★'  # 16
]

counter = 0
def repl(match):
    global counter
    seq_index = counter % len(stars_sequence)
    stars = stars_sequence[seq_index]
    counter += 1
    return f'<div class="lumu-review-stars">{stars}</div>'

for repo in repos:
    cr_path = os.path.join(repo, 'sections', 'lumu-customer-reviews.liquid')
    if os.path.exists(cr_path):
        counter = 0
        with open(cr_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # We need to match any existing stars div
        new_content = re.sub(r'<div class="lumu-review-stars">.*?</div>', repl, content)
        with open(cr_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {cr_path}")
        
    # Also we'll commit and push here
    print(f"Pushing {repo}")
    os.chdir(repo)
    os.system("git add .")
    os.system('git commit -m "Mix up stars in customer reviews to include 3 and 4 stars"')
    os.system("git push")

print("Done updating and pushing.")

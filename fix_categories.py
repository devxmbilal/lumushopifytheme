import os
import re

repos = [
    r'c:\Users\Arslan Malik\Desktop\lumushopifytheme',
    r'c:\Users\Arslan Malik\Desktop\lumushopifytheme\other_stores\lumushopifythemeforUK',
    r'c:\Users\Arslan Malik\Desktop\lumushopifytheme\other_stores\lumushopifythemeforUS'
]

for repo in repos:
    liquid_path = os.path.join(repo, 'sections', 'lumu-categories.liquid')
    if os.path.exists(liquid_path):
        with open(liquid_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Change grid-template-columns: 1fr; to repeat(2, 1fr);
        content = re.sub(
            r'(@media\s*\(\s*max-width:\s*549px\s*\)\s*\{\s*\.lumu-cats__grid\s*\{\s*grid-template-columns:)\s*1fr;',
            r'\1 repeat(2, 1fr);',
            content
        )
        
        # Also let's adjust padding and font sizes for 2-column on mobile
        content = re.sub(
            r'(\.lumu-cat-card__body\s*\{\s*padding:)\s*14px;',
            r'\1 10px;',
            content
        )
        
        content = re.sub(
            r'(\.lumu-cat-card__name\s*\{\s*font-size:)\s*1\.4rem;',
            r'\1 1.25rem;',
            content
        )
        
        # Write back
        with open(liquid_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Fixed Categories in {repo}")
    else:
        print(f"Not found: {liquid_path}")

import os
import re

repos = [
    r'c:\Users\Arslan Malik\Desktop\lumushopifytheme',
    r'c:\Users\Arslan Malik\Desktop\lumushopifytheme\other_stores\lumushopifythemeforUK',
    r'c:\Users\Arslan Malik\Desktop\lumushopifytheme\other_stores\lumushopifythemeforUS'
]

for repo in repos:
    css_path = os.path.join(repo, 'assets', 'lumu-custom.css')
    if os.path.exists(css_path):
        with open(css_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix 1: Change grid-template-columns: 1fr; to 1fr 1fr; in max-width: 549px media query
        content = re.sub(
            r'(@media\s*\(\s*max-width:\s*549px\s*\)\s*\{\s*\.lumu-pfp__grid\s*\{[^}]*?)grid-template-columns:\s*1fr;',
            r'\1grid-template-columns: repeat(2, 1fr);',
            content
        )
        
        # Fallback Fix 2: Just append the !important override if it doesn't exist
        if "/* Trending Now 2 columns on Mobile */" not in content:
            content += """\n
/* Trending Now 2 columns on Mobile */
@media screen and (max-width: 767px) {
  .lumu-pfp__grid {
    display: grid !important;
    grid-template-columns: repeat(2, 1fr) !important;
  }
}
"""
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Fixed Trending Now in {repo}")
    else:
        print(f"Not found: {css_path}")

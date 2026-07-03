import os
import re

repos = [
    r'c:\Users\Arslan Malik\Desktop\lumushopifytheme',
    r'c:\Users\Arslan Malik\Desktop\lumushopifytheme\other_stores\lumushopifythemeforUK',
    r'c:\Users\Arslan Malik\Desktop\lumushopifytheme\other_stores\lumushopifythemeforUS'
]

counter = 0

def repl(match):
    global counter
    counter += 1
    if counter in [2, 5, 8, 12, 14]:
        return '<div class="lumu-review-stars">★★★★☆</div>'
    return match.group(0)

for repo in repos:
    # Reset counter for each repo
    counter = 0
    
    # 1. Update lumu-customer-reviews.liquid (Text stars)
    cr_path = os.path.join(repo, 'sections', 'lumu-customer-reviews.liquid')
    if os.path.exists(cr_path):
        with open(cr_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = re.sub(r'<div class="lumu-review-stars">★★★★★</div>', repl, content)
        with open(cr_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {cr_path}")
        
    # 2. Update lumu-product-reviews.liquid (SVG stars)
    pr_path = os.path.join(repo, 'sections', 'lumu-product-reviews.liquid')
    if os.path.exists(pr_path):
        with open(pr_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Add opacity to 5th star in the Overall Rating Header
        header_parts = content.split('Based on 128 Reviews')
        if len(header_parts) == 2:
            header_svgs = header_parts[0].split('</svg>')
            if len(header_svgs) >= 6:
                header_svgs[4] = header_svgs[4].replace('<svg width="20"', '<svg width="20" style="opacity: 0.3;"')
                header_parts[0] = '</svg>'.join(header_svgs)
                content = 'Based on 128 Reviews'.join(header_parts)
        
        # Add opacity to 5th star in Review 2
        parts = content.split('<!-- Review 2 -->')
        if len(parts) == 2:
            review2 = parts[1]
            svgs = review2.split('</svg>')
            if len(svgs) >= 6:
                svgs[4] = svgs[4].replace('<svg width="16"', '<svg width="16" style="opacity: 0.3;"')
                new_review2 = '</svg>'.join(svgs)
                content = parts[0] + '<!-- Review 2 -->' + new_review2
                
        with open(pr_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {pr_path}")

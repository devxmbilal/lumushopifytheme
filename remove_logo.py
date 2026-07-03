import os
import re

repos = [
    r'c:\Users\Arslan Malik\Desktop\lumushopifytheme',
    r'c:\Users\Arslan Malik\Desktop\lumushopifytheme\other_stores\lumushopifythemeforUK',
    r'c:\Users\Arslan Malik\Desktop\lumushopifytheme\other_stores\lumushopifythemeforUS'
]

for repo in repos:
    liquid_path = os.path.join(repo, 'sections', 'lumu-hero-slider.liquid')
    if os.path.exists(liquid_path):
        with open(liquid_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove the lumu-slider__logo div and its contents completely
        # It looks like:
        # <div class="lumu-slider__logo">
        #   <img src="{{ 'lumulogo.png' | asset_img_url: '200x' }}" alt="Lumu Logo" width="120" height="52" loading="lazy">
        # </div>
        
        new_content = re.sub(
            r'<div class="lumu-slider__logo">\s*<img[^>]*>\s*</div>',
            '',
            content
        )
        
        with open(liquid_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Removed logo from hero slider in {repo}")
    else:
        print(f"Not found: {liquid_path}")

import os
import re

repos = [
    r'c:\Users\Arslan Malik\Desktop\lumushopifytheme\other_stores\lumushopifythemeforUK',
    r'c:\Users\Arslan Malik\Desktop\lumushopifytheme\other_stores\lumushopifythemeforUS',
    r'c:\Users\Arslan Malik\Desktop\lumushopifytheme'
]

for repo in repos:
    liquid_path = os.path.join(repo, 'sections', 'lumu-categories.liquid')
    if os.path.exists(liquid_path):
        with open(liquid_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Let's just append the override right before </style>
        if "/* Force 2 columns on mobile */" not in content:
            override = """
  /* Force 2 columns on mobile */
  @media screen and (max-width: 767px) {
    .lumu-cats__grid {
      grid-template-columns: repeat(2, 1fr) !important;
      gap: 12px !important;
      padding: 0 10px !important;
    }
    .lumu-cat-card__body { padding: 12px !important; }
    .lumu-cat-card__name { font-size: 1.25rem !important; margin-bottom: 2px !important; }
    .lumu-cat-card__desc { font-size: 1.1rem !important; margin-bottom: 6px !important; }
    .lumu-cat-card__link { font-size: 1.1rem !important; }
    .lumu-cats__title h2 { font-size: 2.2rem !important; }
  }
</style>"""
            content = content.replace("</style>", override)
            
            with open(liquid_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Fixed Categories robustly in {repo}")
        else:
            print(f"Already fixed in {repo}")
    else:
        print(f"Not found: {liquid_path}")

#!/usr/bin/env python3
"""
Injects the sticky lead-capture bar + quick enquiry modal into every
public-facing page of the Golden Years main site.
Run this from inside your ~/Golden-Years repo folder.
"""
import re, sys

PAGES = ['index.html','about.html','services.html','skilled-nursing.html',
         'nurse-delegation.html','hca-training.html','resources.html',
         'careers.html','contact.html','article.html','articles.html','job.html']

css = open('quickbar-assets/css_addition.css', encoding='utf-8').read()
snippet = open('quickbar-assets/injection_snippet.html', encoding='utf-8').read()
js = open('quickbar-assets/js_snippet.html', encoding='utf-8').read()

# 1) Append the CSS to the shared stylesheet (once)
with open('css/styles.css', encoding='utf-8') as f:
    style_content = f.read()
if '.quickbar{' not in style_content:
    with open('css/styles.css', 'a', encoding='utf-8') as f:
        f.write(css)
    print("CSS appended to css/styles.css")
else:
    print("CSS already present in css/styles.css — skipped")

# 2) Inject modal + JS into each public page, right before </body>
for page in PAGES:
    try:
        with open(page, encoding='utf-8') as f:
            s = f.read()
    except FileNotFoundError:
        print(f"SKIP (not found): {page}")
        continue
    if 'mainQuickbar' in s:
        print(f"SKIP (already has it): {page}")
        continue
    if '</body>' not in s:
        print(f"SKIP (no </body> tag found): {page}")
        continue
    s = s.replace('</body>', snippet + '\n' + js + '\n</body>', 1)
    with open(page, 'w', encoding='utf-8') as f:
        f.write(s)
    print(f"INJECTED: {page}")

print("\nDone. Remember to paste your real Web3Forms key into the injected")
print("access_key fields (search for 40d97e85-xxxx across your pages).")

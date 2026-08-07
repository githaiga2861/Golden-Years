#!/usr/bin/env python3
"""Adds a 'Reviews' nav link (desktop + mobile) to every main-site public page.
Run from inside ~/Golden-Years after placing reviews.html and index.html."""
PAGES = ['index.html','about.html','services.html','skilled-nursing.html',
         'nurse-delegation.html','hca-training.html','resources.html',
         'careers.html','contact.html','article.html','articles.html',
         'job.html','reviews.html']
for page in PAGES:
    try:
        with open(page, encoding='utf-8') as f: s = f.read()
    except FileNotFoundError:
        print(f"SKIP (not found): {page}"); continue
    if '/reviews">Reviews' in s or '"/reviews"' in s:
        print(f"SKIP (already has Reviews link): {page}"); continue
    changed = False
    if '<li><a href="/careers">Careers</a></li>' in s:
        s = s.replace('<li><a href="/careers">Careers</a></li>',
                       '<li><a href="/careers">Careers</a></li>\n      <li><a href="/reviews">Reviews</a></li>', 1)
        changed = True
    if '<a class="mm-item" href="/careers">Careers</a>' in s:
        s = s.replace('<a class="mm-item" href="/careers">Careers</a>',
                       '<a class="mm-item" href="/careers">Careers</a><a class="mm-item" href="/reviews">Reviews</a>', 1)
        changed = True
    if changed:
        with open(page, 'w', encoding='utf-8') as f: f.write(s)
        print(f"UPDATED: {page}")
    else:
        print(f"NO MATCH FOUND (check manually): {page}")

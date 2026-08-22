#!/usr/bin/env python3
"""One-time fix: the opt-in checkbox on the main site's contact.html was
read via a class selector that changed during restyling.
Run from inside ~/Golden-Years ONLY (this bug is specific to that site)."""
f = 'contact.html'
s = open(f, encoding='utf-8').read()
old = '''form.querySelector('.optin-field input[type="checkbox"]')'''
new = '''form.querySelector('.optin input[type="checkbox"]')'''
if old in s:
    s = s.replace(old, new, 1)
    open(f, 'w', encoding='utf-8').write(s)
    print("Fixed the opt-in checkbox selector")
else:
    print("Already fixed or not applicable — nothing to do")

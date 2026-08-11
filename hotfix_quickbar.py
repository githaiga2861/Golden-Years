#!/usr/bin/env python3
"""HOTFIX: the previous quickbar compaction rules were applying at ALL
screen widths instead of only mobile (<=600px), because the @media
wrapper was missing. This wraps them correctly.
Run from inside the repo root, targeting css/styles.css."""

f = 'css/styles.css'
s = open(f, encoding='utf-8').read()

old = '''.quickbar__inner{flex-wrap:nowrap;justify-content:space-between;align-items:center;padding:8px 12px;gap:8px;overflow-x:auto}
  .quickbar__txt{font-size:0;gap:0;flex-shrink:0}
  .quickbar__txt svg{width:20px;height:20px}
  .quickbar__cta{gap:6px;flex-wrap:nowrap;flex-shrink:0}
  .quickbar .btn{padding:7px 12px;font-size:.72rem;white-space:nowrap}
  .chat-trigger{width:34px;height:34px;flex-shrink:0}
  .chat-trigger svg{width:17px;height:17px}
  .chat-badge{width:15px;height:15px;font-size:.6rem;top:-3px;right:-3px}'''

new = '''@media(max-width:600px){
  .quickbar__inner{flex-wrap:nowrap;justify-content:space-between;align-items:center;padding:8px 12px;gap:8px;overflow-x:auto}
  .quickbar__txt{font-size:0;gap:0;flex-shrink:0}
  .quickbar__txt svg{width:20px;height:20px}
  .quickbar__cta{gap:6px;flex-wrap:nowrap;flex-shrink:0}
  .quickbar .btn{padding:7px 12px;font-size:.72rem;white-space:nowrap}
  .chat-trigger{width:34px;height:34px;flex-shrink:0}
  .chat-trigger svg{width:17px;height:17px}
  .chat-badge{width:15px;height:15px;font-size:.6rem;top:-3px;right:-3px}
}'''

count = s.count(old)
if count == 0:
    print("PATTERN NOT FOUND — file may already be fixed, or formatting differs. No changes made.")
elif count > 1:
    print(f"WARNING: found {count} matches, expected 1. Aborting to avoid wrong edit — check manually.")
else:
    s = s.replace(old, new, 1)
    open(f, 'w', encoding='utf-8').write(s)
    print("FIXED: mobile-only rules now correctly wrapped in @media(max-width:600px)")

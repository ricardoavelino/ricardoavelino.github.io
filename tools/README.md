# Publications: one source of truth

Bibliographic facts live in **one** file, used by both the CV and this website:

```
~/Code/latex/application/shared/publications.bib     <-- edit papers HERE
```

The CV (`~/Code/latex`) reads it directly via biblatex. This website can't run a
BibTeX plugin on GitHub Pages, so `sync_publications.py` copies the canonical
BibTeX into each `_publications/*.md` instead.

## Workflow when a paper changes (new DOI, title, author, or a new paper)

1. Edit the entry in `publications.bib`.
2. Sync this site:
   ```
   python3 tools/sync_publications.py            # dry run — shows what would change
   python3 tools/sync_publications.py --write     # apply
   ```
3. Rebuild the CV:
   ```
   cd ~/Code/latex/application && make cv
   ```
4. Commit both repos.

## What the sync does

- **Writes** the `bibtex:` block of every `_publications/*.md` verbatim from the
  matching `.bib` entry (matched by cite-key, minus the CV-only `keywords` line).
  This is the copy that used to drift.
- **Reports** (never overwrites) when a `.md`'s display `title:` or `authors:`
  differs from the `.bib` — because those are curated for the web (full titles,
  `<span class="me">` highlighting, occasional "et al." on long lists). Fix
  whichever side is actually wrong. Cosmetic-only differences (HTML entities vs
  Unicode, en-dash vs hyphen) are ignored.
- Leaves every other field (venue, date, teaser, featured, links, permalink)
  exactly as-is.

The `.bib` path can be overridden with `PUBLICATIONS_BIB=/path/to/publications.bib`.

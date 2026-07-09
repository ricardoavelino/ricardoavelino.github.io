#!/usr/bin/env python3
"""
sync_publications.py — keep the website's publication entries in sync with the
canonical BibTeX source used by the CV.

Single source of truth:
    ../latex/application/shared/publications.bib   (edit facts HERE)

What it WRITES (the real duplication that used to drift):

    bibtex:   <- the verbatim .bib entry (minus the CV-only `keywords` line)

What it only REPORTS (curated display fields — you reconcile deliberately):

    title:    the .bib title differs from the site's display title
    authors:  the .bib author list differs from the site's display list
              (the site intentionally abbreviates some long lists with "et al.")

Every other front-matter field (venue, date, teaser, featured, paperurl, pdf,
code, video, webpage, slides, projectpage, permalink, collection...) is left
exactly as you curated it.

Usage:
    python3 tools/sync_publications.py            # dry run: show bibtex changes + reconcile report
    python3 tools/sync_publications.py --write     # apply bibtex changes
"""

import os
import re
import sys
import difflib

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
PUBDIR = os.path.join(SITE, "_publications")
# Canonical .bib lives in the sibling LaTeX repo; override with $PUBLICATIONS_BIB.
DEFAULT_BIB = os.path.normpath(
    os.path.join(SITE, "..", "latex", "application", "shared", "publications.bib")
)
BIB = os.environ.get("PUBLICATIONS_BIB", DEFAULT_BIB)

# Family name to highlight as "me" in author lists (wrapped in <span class="me">).
ME_FAMILY = "Maia Avelino"

# LaTeX -> Unicode for DISPLAY fields only (title/authors). The bibtex block is
# kept verbatim so it stays valid LaTeX for anyone copying it.
ACCENTS = {
    r'\"o': "ö", r'\"u': "ü", r'\"a': "ä", r'\"O': "Ö", r'\"U': "Ü",
    r"\'e": "é", r"\'E": "É", r"\'a": "á", r"\'o": "ó", r"\'i": "í",
    r"\`e": "è", r"\`a": "à",
    r"\^e": "ê", r"\^o": "ô", r"\^i": "î",
    r"\~a": "ã", r"\~o": "õ", r"\~n": "ñ",
    r"\c c": "ç",
}


def clean_latex(s):
    """Turn a LaTeX title/name fragment into display Unicode."""
    for tex, uni in ACCENTS.items():
        s = s.replace("{" + tex + "}", uni).replace(tex, uni)
    s = s.replace("--", "–")          # en dash
    s = s.replace(r"\&", "&")
    s = re.sub(r"\{([A-Za-z0-9 ]+)\}", r"\1", s)  # drop protective braces {AI}
    s = s.replace("{", "").replace("}", "")
    return re.sub(r"\s+", " ", s).strip()


# ----------------------------------------------------------------------------- bib parsing
def parse_bib(text):
    """Return {citekey: (entrytype, raw_entry_text, {field: value})}."""
    entries = {}
    i = 0
    n = len(text)
    while True:
        at = text.find("@", i)
        if at == -1:
            break
        brace = text.find("{", at)
        if brace == -1:
            break
        entrytype = text[at + 1:brace].strip().lower()
        # walk to the matching closing brace
        depth = 0
        j = brace
        while j < n:
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        raw = text[at:j + 1]
        body = text[brace + 1:j]
        key = body.split(",", 1)[0].strip()
        fields = parse_fields(body[len(body.split(",", 1)[0]) + 1:])
        entries[key] = (entrytype, raw, fields)
        i = j + 1
    return entries


def parse_fields(body):
    """Parse 'name = {value}, ...' honouring nested braces."""
    fields = {}
    i, n = 0, len(body)
    while i < n:
        eq = body.find("=", i)
        if eq == -1:
            break
        name = body[i:eq].strip().rstrip(",").strip().lower()
        k = eq + 1
        while k < n and body[k] in " \t\n":
            k += 1
        if k >= n:
            break
        if body[k] == "{":
            depth, m = 0, k
            while m < n:
                if body[m] == "{":
                    depth += 1
                elif body[m] == "}":
                    depth -= 1
                    if depth == 0:
                        break
                m += 1
            val = body[k + 1:m]
            i = m + 1
        else:
            m = k
            while m < n and body[m] != ",":
                m += 1
            val = body[k:m].strip()
            i = m
        while i < n and body[i] in " \t\n,":
            i += 1
        if name:
            fields[name] = val.strip()
    return fields


# ----------------------------------------------------------------------------- formatting
def format_authors(bib_authors):
    """'Maia Avelino, R. and Van Mele, T.' -> 'R. Maia Avelino, T. Van Mele'
    with the own name wrapped in <span class="me">."""
    out = []
    for person in re.split(r"\s+and\s+", bib_authors.strip()):
        if "," in person:
            family, given = [p.strip() for p in person.split(",", 1)]
        else:
            parts = person.split()
            family, given = parts[-1], " ".join(parts[:-1])
        inits = []
        for tok in given.split():
            if tok.endswith("."):
                inits.append(tok)
            elif len(tok) == 1:
                inits.append(tok + ".")
            else:
                inits.append(tok[0] + ".")
        disp = (" ".join(inits) + " " + family).strip()
        disp = clean_latex(disp)
        if clean_latex(family) == ME_FAMILY:
            disp = '<span class="me">%s</span>' % disp
        out.append(disp)
    return ", ".join(out)


def canonical_bibtex(raw):
    """The .bib entry, verbatim, minus the CV-only `keywords` line, reindented
    to two spaces to match the existing block style."""
    lines = raw.strip("\n").split("\n")
    kept = [ln for ln in lines if not ln.strip().lower().startswith("keywords")]
    # normalise trailing comma before the closing brace
    for idx in range(len(kept) - 1, -1, -1):
        if kept[idx].strip() == "}":
            continue
        if kept[idx].strip():
            kept[idx] = kept[idx].rstrip().rstrip(",") + ","
            break
    return "\n".join(kept)


# ----------------------------------------------------------------------------- front-matter surgery
def split_front_matter(md):
    m = re.match(r"^---\n(.*?\n)---\n?(.*)$", md, re.DOTALL)
    if not m:
        return None
    return m.group(1), m.group(2)


def fm_blocks(fm):
    """Split front-matter into ordered [(key, block_text)] where a block is a
    top-level key line plus any indented/continuation lines under it."""
    blocks = []
    cur_key, cur = None, []
    for line in fm.split("\n"):
        if re.match(r"^[A-Za-z0-9_]+:", line):
            if cur_key is not None or cur:
                blocks.append((cur_key, "\n".join(cur)))
            cur_key = line.split(":", 1)[0]
            cur = [line]
        else:
            cur.append(line)
    if cur_key is not None or cur:
        blocks.append((cur_key, "\n".join(cur)))
    return blocks


def rebuild_fm(blocks):
    return "\n".join(b for _, b in blocks)


def yaml_dq(s):
    """Double-quoted YAML scalar."""
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def citekey_of(md):
    m = re.search(r"@[a-z]+\{([^,]+),", md)
    return m.group(1).strip() if m else None


# ----------------------------------------------------------------------------- main
def main():
    write = "--write" in sys.argv
    if not os.path.exists(BIB):
        sys.exit("Canonical .bib not found: %s\n(set $PUBLICATIONS_BIB)" % BIB)
    entries = parse_bib(open(BIB, encoding="utf-8").read())

    changed, unmatched, total, reconcile = 0, [], 0, []
    for fn in sorted(os.listdir(PUBDIR)):
        if not fn.endswith(".md"):
            continue
        total += 1
        path = os.path.join(PUBDIR, fn)
        md = open(path, encoding="utf-8").read()
        key = citekey_of(md)
        if key not in entries:
            unmatched.append((fn, key))
            continue
        _type, raw, fields = entries[key]
        new_bib = canonical_bibtex(raw)

        fm, body = split_front_matter(md)
        blocks = fm_blocks(fm)
        bmap = dict(blocks)

        # --- collect title / author drift for the reconcile report ----------
        # (compare loosely so HTML entities / dash styles don't count as drift)
        cur_title = _scalar(bmap.get("title", ""))
        bib_title = clean_latex(fields.get("title", ""))
        if cur_title and _norm(cur_title) != _norm(bib_title):
            reconcile.append((fn, "title", cur_title, bib_title))
        if "author" in fields and "authors" in bmap:
            cur_auth = _scalar(bmap["authors"])
            bib_auth = format_authors(fields["author"])
            if (_norm(cur_auth) != _norm(bib_auth)
                    and "et al" not in cur_auth and "…" not in cur_auth):
                reconcile.append((fn, "authors", cur_auth, bib_auth))

        # --- write only the bibtex block ------------------------------------
        bib_block = "bibtex: |\n" + "\n".join("  " + ln for ln in new_bib.split("\n"))
        for idx, (bk, _) in enumerate(blocks):
            if bk == "bibtex":
                blocks[idx] = ("bibtex", bib_block)
                break

        new_md = "---\n" + rebuild_fm(blocks).rstrip("\n") + "\n---\n" + body
        if new_md != md:
            changed += 1
            print("~ %s  (%s)" % (fn, key))
            if not write:
                diff = difflib.unified_diff(
                    md.splitlines(), new_md.splitlines(),
                    lineterm="", n=0, fromfile=fn, tofile=fn)
                for ln in list(diff)[2:]:
                    if ln and ln[0] in "+-" and not ln.startswith(("+++", "---")):
                        print("    " + ln)
            if write:
                open(path, "w", encoding="utf-8").write(new_md)

    print("\nbibtex blocks: %d/%d %s; %d already in sync."
          % (changed, total, "written" if write else "would change",
             total - changed - len(unmatched)))
    for fn, key in unmatched:
        print("  ! no .bib entry for cite-key %r  (%s)" % (key, fn))

    if reconcile:
        print("\nRECONCILE — display fields differ from the .bib "
              "(not auto-changed; fix whichever side is wrong):")
        for fn, field, site, bib in reconcile:
            print("  %s  [%s]" % (fn, field))
            print("     site: %s" % site)
            print("     .bib: %s" % bib)
    if not write and changed:
        print("\nDry run. Re-run with --write to apply the bibtex changes.")


_ENTITIES = {"&eacute;": "é", "&egrave;": "è", "&auml;": "ä", "&ouml;": "ö",
             "&uuml;": "ü", "&ccedil;": "ç", "&atilde;": "ã", "&amp;": "&"}


def _norm(s):
    """Loose form for drift comparison: unify HTML entities, dashes, spaces."""
    for ent, uni in _ENTITIES.items():
        s = s.replace(ent, uni)
    s = s.replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", s).strip()


def _scalar(block):
    """Decoded value of a single-line 'key: "..."' front-matter block."""
    m = re.match(r'^[^:]+:\s*"?(.*?)"?\s*$', block.split("\n")[0])
    if not m:
        return ""
    return m.group(1).replace('\\"', '"').replace("\\\\", "\\")


if __name__ == "__main__":
    main()

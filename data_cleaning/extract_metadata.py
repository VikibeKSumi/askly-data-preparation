import re 

HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
META    = re.compile(r"^\*\*([^*]+)\*\*:\s*(.+?)\s*$")      # **Key**: value
RULE    = re.compile(r"^-{3,}\s*$")                         # --- separator
LIST_FIELDS = {"distribution", "compliance"}                 # comma-separated -> list

def header_block(raw):
    """everything above the first --- separator"""
    lines = raw.split("\n")
    end = next((i for i, l in enumerate(lines) if RULE.match(l)), 0)
    return lines[:end]


def extract_metadata(raw):
    meta = {}
    for line in header_block(raw):
        h = HEADING.match(line)
        if h and len(h.group(1)) == 1:
            meta["title"] = h.group(2).strip()
        elif h and len(h.group(1)) == 2:
            meta["organization"] = h.group(2).strip()

        m = META.match(line)
        if m:
            key = re.sub(r"[^a-z0-9]+", "_", m.group(1).lower()).strip("_")
            value = m.group(2)
            meta[key] = [v.strip() for v in value.split(",")] if key in LIST_FIELDS else value
    return meta

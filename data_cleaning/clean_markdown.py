import re

LABEL   = re.compile(r"^\*\*([^*]+)\*\*\s*$")              # line that is ONLY **bold text**
FENCE   = re.compile(r"^```")
META    = re.compile(r"^\*\*([^*]+)\*\*:\s*(.+?)\s*$")      # **Key**: value
RULE    = re.compile(r"^-{3,}\s*$")                         # --- separator
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")


def clean_markdown(raw):
    out, level, in_code, past_header_block = [], 1, False, False

    for line in raw.split("\n"):
        # 1. code blocks pass through untouched
        if FENCE.match(line):
            in_code = not in_code
            out.append(line)
            continue
        if in_code:
            out.append(line)
            continue

        # 2. drop --- separators (the first one also ends the metadata block)
        if RULE.match(line):
            past_header_block = True
            continue

        # 3. drop the metadata block at the top (**Key**: value lines)
        if not past_header_block and META.match(line):
            continue

        # 4. track heading level; promote bold labels one level below it
        h = HEADING.match(line)
        if h:
            level = len(h.group(1))
            out.append(line)
            continue

        m = LABEL.match(line)
        if m:
            out.append(f"{'#' * min(level + 1, 6)} {m.group(1).strip()}")
            continue

        out.append(line.rstrip())

    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)                   # collapse blank-line runs
    return text.strip() + "\n"


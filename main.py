#!/usr/bin/env python3
"""Write the alien one-star review sentence to entry.txt.

Competition: One Star, Five Stars for the Food (one sentence,
1-200 chars, in the voice of an alien tourist giving Earth a
one-star review while slipping in a real compliment about
the food; the judge wants the funniest, most convincingly
alien sentence that lands both the complaint and the food
compliment).
Candidates:
A) "One star: the locals breathe poison gas, queue to be
   scanned naked at borders, and worship traffic - but I
   would cross nine galaxies again for whatever a 'taco'
   is doing to my mouthparts." (em dash before 'but')
B) "One star - gravity too strong, weather unlicensed,
   humans loud in every frequency - however, their
   melted-cheese-on-bread ritual briefly made me forget
   I was stranded here."
C) "Terrible planet: the water falls from the sky without
   warning and everyone pretends this is normal, but five
   stars for ramen, which repaired damage their climate
   caused."
Selected A: the grievances are an outsider's bafflement
(oxygen as poison gas, airport scans, traffic worship),
the voice stays alien to the last word (mouthparts), and
the food compliment is genuine enough to justify crossing
nine galaxies again. B's cheese ritual is good but vaguer;
C has only one complaint and a weaker turn.
Deterministic: a fixed text, no network, no randomness.
"""
import os
from pathlib import Path

LINE = "One star: the locals breathe poison gas, queue to be scanned naked at borders, and worship traffic \u2014 but I would cross nine galaxies again for whatever a 'taco' is doing to my mouthparts."
TEXT = LINE + "\n"
MAX_CHARS = 200


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip() or "\n" in body or "\r" in body:
        raise ValueError("entry must be one non-empty line")
    if body.count(".") != 1 or not body.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    # Write bytes directly so the entry is identical on every run.
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()

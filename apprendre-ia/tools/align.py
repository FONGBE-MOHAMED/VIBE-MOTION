"""Estimate word timings of a known text on a voice montage without ASR.
Phrases = sound runs found by onsets.py (energy), each mapped by hand to its words; inside a phrase the word starts are
placed by syllable weight, then snapped onto the nearest fine sound onset (+-0.12 s)."""
import json, re, subprocess, sys
audio, out = sys.argv[1], sys.argv[2]
ONS = "/home/user/VIBE-MOTION/.claude/skills/motion-design/scripts/onsets.py"
def runs(*extra):
    txt = subprocess.run(["python3", ONS, audio, "--no-whisper", *extra], capture_output=True, text=True, check=True).stdout
    return [(float(a), float(b)) for a, b in re.findall(r"#\d+\s+([\d.]+) to\s+([\d.]+)", txt)]
phrases = runs()
fine = runs("--min-silence", "0.03", "--threshold-db", "-36")
TEXT = """Deux mille.|Un site internet ?|Pas pour moi.|Deux mille dix.|Les réseaux sociaux ?|Pas pour moi.|Deux mille vingt-six.|L'intelligence artificielle ?|Le problème ?|Le monde, lui, n'a pas attendu.|Ta présentation te prend une soirée.|Tes mails,|ta matinée.|Ta compta,|ton dimanche.|Pour d'autres, c'est réglé avant le café.|Pas cette fois.|Aujourd'hui, l'IA rédige, résume,|calcule.|Tu lui expliques avec tes mots...|elle fait le travail.|Pas besoin d'être technique :|il faut juste apprendre à lui parler.|Et tu récupères ta soirée,|ta matinée,|ton dimanche.|L'intelligence artificielle ?|Cette fois...|c'est pour toi.|Apprends l'IA dès aujourd'hui."""
groups = [g.split() for g in TEXT.split("|")]
groups = [[w for w in g if re.search(r"\w", w)] for g in groups]
assert len(groups) == len(phrases), (len(groups), len(phrases))
def syl(w):
    core = re.sub(r"[^a-zàâäéèêëîïôöùûüœç'-]", "", w.lower())
    if core in ("l'ia", "ia"): return 2
    n = len(re.findall(r"[aeiouyàâäéèêëîïôöùûüœ]+", core))
    if n > 1 and re.search(r"[^aeiouyé]e?s?$|[^é]es$|[^é]e$", core) and re.search(r"(e|es)$", core) and not core.endswith("é"):
        n -= 1
    return max(1, n)
words = []
for (a, b), g in zip(phrases, groups):
    wts = [syl(w) + 0.3 for w in g]
    tot = sum(wts); cum = 0; starts = []
    for k, wt in enumerate(wts):
        s = a + (b - a) * cum / tot
        if k:
            near = [o for o, _ in fine if a < o < b and abs(o - s) <= 0.12]
            if near: s = min(near, key=lambda o: abs(o - s))
        starts.append(max(s, starts[-1] + 0.05) if starts else s)
        cum += wt
    for k, w in enumerate(g):
        e = starts[k + 1] if k + 1 < len(g) else b
        words.append({"w": w, "s": round(starts[k], 2), "e": round(e, 2), "whisper_s": round(starts[k], 2)})
json.dump({"source": "estimated: energy phrases (onsets.py) + syllable weights, no Whisper; phrase starts exact, word starts +-0.15 s",
           "phrases": [[a, b] for a, b in phrases], "words": words}, open(out, "w"), ensure_ascii=False, indent=1)
for (a, b), g in zip(phrases, groups):
    ws = [x for x in words if a - 0.01 <= x["s"] <= b]
    print(f"{a:6.2f}-{b:6.2f}  " + " ".join(f"{x['w']}@{x['s']:.2f}" for x in ws))

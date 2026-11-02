"""Embed a grants.json into the app template.

Usage: python3 tools/build.py data/grants.json tools/app.template.html index.html [out.json]

The data is embedded exactly as the Grant Radar dashboard publishes it (ranking,
priority notes, kind, applicants, certainty). The optional out.json is a
normalised copy of the input. data/example-backup.json (next to the data file)
is embedded too and shown as example tracking on a first visit.
"""
import json, os, sys

src, tpl, out_html = sys.argv[1:4]
out_json = sys.argv[4] if len(sys.argv) > 4 else None
d = json.load(open(src, encoding="utf-8"))
if out_json:
    json.dump(d, open(out_json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
blob = json.dumps(d, ensure_ascii=False).replace("</", "<\\/")
# example tracking shown on a first visit: data/example-backup.json next to the data file, if present
ex_path = os.path.join(os.path.dirname(os.path.abspath(src)), "example-backup.json")
example = json.dumps(json.load(open(ex_path, encoding="utf-8")), ensure_ascii=False).replace("</", "<\\/") if os.path.exists(ex_path) else "null"
html = open(tpl, encoding="utf-8").read().replace("/*__DATA__*/", blob).replace("/*__EXAMPLE__*/", example)
open(out_html, "w", encoding="utf-8").write(html)
print(len(d), "rows")

# Grant Radar

**Open the app:** https://annotatebio.github.io/grant-tracker/ (once GitHub Pages is switched on), or download `index.html` and double-click it.

Grant Radar lists research-funding calls in gut and food microbiome, diet × gut, gut mycobiome, bioinformatics and general schemes. Every call is open to researchers at Polish institutions, and the list shows which calls a PhD student can lead and which need someone else (a PI, a consortium or a company) to apply.

- **Overview:** two ranked shortlists of announced calls (calls you can apply for yourself, and team & consortium calls someone else leads), a separate list of *predicted* calls that aren't announced yet, and a timeline of deadlines by topic (hollow dots = predicted dates).
- **Type and who-can-apply filters:** narrow everything to research grants, conference & travel funding or training & lab visits, and to who may apply (PhD student, early-career PhD, senior PI, consortium, industry, …).
- **All calls:** filter by topic, route or status, hide predicted calls, search, and open any call for its type, who can apply, eligibility, deadline notes and links.
- **Find calls for my field:** describe your own search (topics, country, career stage, types of funding). The app writes a prompt for Claude; Claude searches the web and gives you a `grants.json`; you load it back into the app. Your list then replaces the built-in one in your browser.
- **My topics:** filter the current list: switch off topics you don't need (their calls disappear everywhere), or add your own topic with a few keywords. This doesn't find new calls; use *Find calls for my field* for that. For example, *Fungi & yeasts* = `fungal, yeast, candida, mycology` tags every call that mentions any of them.
- **Your own tracking:** set a status (Watching, Preparing, Submitted, …), keep notes and add your own calls. All of this is saved **in your browser only**. Use *Back up my data* / *Restore* to move it to another browser or computer.
- **Export deadlines (.ics):** imports into Google Calendar, Outlook or Apple Calendar.

Deadlines were checked on funder or university pages (last check: 2 Nov 2026). Rows marked *Predicted* (`certainty: "Expected"` in the data) are estimated from earlier rounds. Always confirm on the call page before you apply.

---

## Set it up on someone else's computer

Pick the option that matches what the person needs. Nothing needs installing for options 1–2.

### 1. Just use the app (no installation)

1. Get `index.html` to them: send the file by email or chat, or put it on a shared drive. (On GitHub: open `index.html` → *Download raw file*.)
2. They save it anywhere, e.g. `Documents/Grant Radar/index.html`, and double-click it. It opens in their default browser (Chrome, Firefox, Safari or Edge).
3. Bookmark it in that browser so they always open the same file. Their statuses and notes are saved in **that browser on that computer**. A different browser, a private window, or clearing site data starts empty.

The call list is built into the file, so it works offline. To get a newer list, replace the file with a newer `index.html`. Their statuses and notes are kept as long as they open it from the same place in the same browser. Saving the new file under the same name in the same folder is enough.

If the app is published on GitHub Pages (see below), they can simply open the link instead, and they'll always see the latest list.

### 2. Move your own statuses and notes to another computer

1. On the old computer: **Back up my data** → saves `grant-radar-my-data.json`.
2. Copy that file to the new computer (email, USB, cloud drive).
3. On the new computer, open the app → **Restore** → pick the file.

Restore **replaces** whatever is saved in that browser, so do it before you start tracking on the new computer. Each person's tracking is separate. A colleague can restore your backup to start from your notes, but changes don't sync afterwards. A backup also carries your *My topics* settings.

**To see an example first:** restore `data/example-backup.json`. It has made-up statuses, notes, one hand-added call and one custom topic. Restore your real backup (or start fresh) afterwards, because restoring replaces what's saved.

### 3. Full copy of the repo (to maintain or edit the list)

Needs [Git](https://git-scm.com/downloads) and, for rebuilding the app, Python 3 (preinstalled on macOS and most Linux; on Windows install it from [python.org](https://www.python.org/downloads/)).

1. **Download:**
   ```sh
   git clone https://github.com/annotatebio/grant-tracker.git
   cd grant-tracker
   ```
   (Or use GitHub Desktop: *File → Clone repository*.)
2. **Open the app:** double-click `index.html`. To have it read `data/grants.json` directly (as it does on GitHub Pages), run a local web server instead:
   ```sh
   python3 -m http.server 8000
   ```
   then open <http://localhost:8000> and stop the server with Ctrl+C when done. On Windows, use `python` or `py` instead of `python3`.
3. **Update the list:** replace `data/grants.json` (see *Updating the call list*), rebuild the app, then commit and push:
   ```sh
   python3 tools/build.py data/grants.json tools/app.template.html index.html
   git add data/grants.json index.html
   git commit -m "Update call list"
   git push
   ```

### 4. Their own published copy

To give someone a version they control (their own list and link), they create their own repository from this one (*Fork*, or download the files and push them to a new repo) and switch on GitHub Pages there (next section). To change what the list covers, see *Customize what grants it searches for*.

### 5. The claude.ai dashboard and weekly refresh

The live Grant Radar dashboard and its weekly refresh run in the owner's claude.ai account. They can't be copied from this repo: `claude-artifacts/` only holds a backup of the dashboard page, which doesn't run outside claude.ai.

- **To let someone see it:** share the dashboard from claude.ai. They need a claude.ai account.
- **To give someone their own refreshed list:** they create their own dashboard on claude.ai and set up a weekly scheduled task with the prompt in `refresh-prompt.md`. Start them from `data/grants.json` so they don't begin from scratch.

---

## Publish with GitHub Pages

*Settings → Pages → Deploy from a branch → `main` / `(root)` → Save.* The app appears at `https://annotatebio.github.io/grant-tracker/` within a minute or two, and after that every push to `main` updates it.

GitHub Pages is free for public repositories; for a private one it needs a paid GitHub plan. The published site is public either way, so keep personal statuses and notes out of `data/grants.json`. They belong in the app's own tracking, which stays in each person's browser.

## Customize what grants it searches for

There are three levels.

**1. Your own list, from inside the app (anyone, no setup).** Click **Find calls for my field**:

1. Fill in your topics (separated by semicolons), the country of your institution, your career stage and the types of funding. For example: *Plant microbiome; Soil ecology; Bioinformatics*, *Germany*, *Postdoc*.
2. **Copy the prompt** and paste it into a new chat on [claude.ai](https://claude.ai) with web search switched on.
3. Save the `grants.json` file Claude gives you. If it shows the JSON as text instead, copy it into a plain-text file and name it `grants.json`.
4. Back in the app: **Load the call list Claude made…** and pick the file.

The app now shows your list (a bar at the top says so), with your topics as the topic filters. It's saved in your browser and included in *Back up my data*. **Back to the built-in list** switches back. Your statuses and notes are kept either way. Repeat every few weeks, since calls open and close.

**2. Filter the list you have (My topics).** Switch off topics you don't need, and add keyword topics for what you care about. This only filters the calls already in the list. Examples:

| Topic name | Keywords |
|---|---|
| Fungi & yeasts | `fungal, yeast, candida, mycology` |
| Metagenomics & sequencing | `metagenom, sequencing, shotgun, 16s` |
| Clinical / IBD | `ibd, crohn, colitis, clinical, patient` |
| Travel money | `travel, conference, congress, visit` |

Keywords match any part of a word, so `metagenom` finds both *metagenomics* and *metagenome*.

**3. The shared list, refreshed weekly (maintainers).** Edit **Your search** at the top of `refresh-prompt.md` and use it for the weekly refresh (see *The claude.ai dashboard and weekly refresh*). The topics you list there become the app's topics, and the app picks them up automatically. Examples:

```
Topics:           Plant microbiome; Soil ecology; Bioinformatics; General
Institution in:   Germany
Applicant:        Postdoc
Funders to check: DFG, BMBF, DAAD, Humboldt Foundation; Horizon Europe CL6, ERC, MSCA; foundations
Types to include: Research grant; Training / lab visit
Leave out:        calls only for permanent staff
```

```
Topics:           Neuroscience; Neuroimaging; Computational neuroscience; General
Institution in:   Czech Republic
Applicant:        PhD student
Funders to check: GAČR, TA ČR, Charles University Grant Agency; Horizon Europe CL1, ERC, MSCA; foundations and societies
Types to include: Research grant; Conference / travel; Training / lab visit
Leave out:        postdoc-only fellowships
```

The app's title and one-line description sit at the top of `tools/app.template.html` (`<h1>` and the `lede` paragraph). Change them there and rebuild. The "A PhD student can lead" counter and shortlist follow each call's `route`, so they adapt to whichever **Applicant** the refresh used.

## Updating the call list

The list is maintained in the Grant Radar dashboard on claude.ai and refreshed weekly (Mondays 08:55 Europe/Warsaw) with `refresh-prompt.md`. To bring a refresh into this repo, ask Claude to read the dashboard's `grants` data and save it as `data/grants.json`. Or replace the file yourself. Then rebuild `index.html` and push (step 3.3 above).

## Files

| Path | What it is |
|---|---|
| `index.html` | The app. It's one self-contained file with the call list built in. On GitHub Pages or a local server it also loads `data/grants.json`, so updating that file updates the app. |
| `data/grants.json` | The call list (one object per call: `call`, `funder`, `topics`, `kind`, `applicants`, `route`, `deadline`, `certainty`, `priority`, `url`, …). `kind` is one of Research grant / Conference / travel / Training / lab visit; `applicants` is a `;`-separated list of who can apply. |
| `data/example-backup.json` | A made-up backup (statuses, notes, one hand-added call, one custom topic). Restore it in the app to see how tracking looks. |
| `tools/` | `app.template.html` (the app's source) plus `build.py`, which embeds `grants.json` into `index.html` as-is. |
| `claude-artifacts/grant-radar/` | Backup of the claude.ai dashboard page (`index.html`) and its data settings (`store.json`). Runs only inside claude.ai. |
| `claude-artifacts/grant-tracker/` | Backup of the original claude.ai tracker page. Runs only inside claude.ai. |
| `refresh-prompt.md` | The prompt for the weekly refresh, with an editable *Your search* block (topics, country, applicant, funders, types). |
| `.gitignore` | Keeps a personal `data/tracking.json` and macOS `.DS_Store` files out of the repository. |

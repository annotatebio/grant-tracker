# Weekly refresh prompt

This is the prompt a weekly scheduled task on claude.ai runs to refresh the call list (here: Mondays 08:55 Europe/Warsaw). To search for different grants, edit **Your search** below and leave **The prompt** as it is. The README has filled-in examples for other fields.

## Your search

```
Dashboard name:   Grant Radar
Topics:           Gut microbiome; Food microbiome; Diet × gut; Fungi / mycobiome; Bioinformatics; General
Institution in:   Poland
Applicant:        PhD student
Funders to check: NCN, NCBR, NAWA, ABM, FNP; Horizon Europe CL1/CL6, ERC, European Partnerships; foundations and societies
Types to include: Research grant; Conference / travel; Training / lab visit
Leave out:        postdoc-only fellowships; PI-only awards that cannot fund team members or services
```

## The prompt

Refresh the dashboard named in *Your search*: read its dataset `datasets/grants`, verify every row's deadline and status on funder pages, and find new calls in the listed **Topics**, checking the listed **Funders** (plus any other funder you find that fits).

Eligibility filter: only calls open to a researcher at an institution in the listed country, of the listed **Types**, and nothing from **Leave out**. Keep uncertain ones and say what to check.

Each row: call, funder, funder_type, topics (`;`-separated, from the **Topics** list), kind (one of the **Types**), applicants (`;`-separated, from: PhD student, Early-career PhD, Mid-career PhD, Any PhD holder, Senior PI, Consortium, Industry partners welcome, Industry-led), region, eligibility, amount, opens, deadline (YYYY-MM-DD), deadline_note, certainty (Confirmed / Tentative / Expected — Expected means not yet announced, dated from earlier rounds), summary, url, last_checked, route ("You can lead" / "You can lead (conditions)" / "Via PI / postdoc", judged for the listed **Applicant**), lead_requires, priority (ranked separately per route group), priority_note.

Never invent dates; drop rows closed more than 30 days ago; keep under ~60 rows. Keep priority notes about the call itself. Personal statuses and notes belong in the tracker, not in the data, because the data may be published.

Upload grants.json as an asset, update `datasets/grants` source + updated, then summarise: top 3 the applicant can lead, top 2 with a partner, new calls, and calls closing within 14 days.

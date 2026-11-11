# Virginia Tech ISE Faculty Finder

A student-facing guide to research connections: 45 faculty, 180 keywords in eight categories, program-area filters, faculty news, videos, and a browser-local shortlist.

## Published site

Intended GitHub Pages address: https://roberthildebrand.github.io/VT-ISE/

The public files are in `docs/`. The workflow publishes only that directory when `main` changes. GitHub Pages must use **GitHub Actions** as its publishing source.

## Updating content

The reviewed editorial sources remain in the sibling `VT-ISE-Grad-Recruiting-Committee` repository, under `outputs/faculty-finder` and `outputs/faculty-brochure-20261112`. Rebuild those outputs, then run:

```sh
python3 scripts/sync.py
```

For a different source location, pass `--source /path/to/VT-ISE-Grad-Recruiting-Committee`. Review and commit the updated public files, then push to `main` to publish.

## Content and privacy

Profiles and linked news were reviewed November 11, 2026. Older publications, preprints and project announcements retain their dates and status. Research connections do not confirm advising availability. Portraits and branding come from Virginia Tech sources; source links accompany profiles.

Shortlists are stored in the student's own browser. No accounts, server, analytics or submitted student data are required.

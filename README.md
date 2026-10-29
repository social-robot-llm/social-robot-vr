# Anonymous project website

Review companion for **Multimodal Socially Aware Framework for Human-Robot Interaction in Virtual Reality**. Status: submitted to RA-L; under review.

The site uses the Academic Project Page Template layout with an anonymous paper download, project video, interaction clips, architecture pipeline and manuscript results. Code release is coming soon. Research author names, affiliations, identifying paths and named citation metadata are omitted from the public files.

## Preview locally

From the repository directory, run:

```sh
python3 scripts/site.py check
python3 scripts/site.py build
python3 scripts/site.py serve
```

Open http://127.0.0.1:4173. Python 3 standard library only; no npm dependencies. The preview serves the public allowlist from `dist/`. Keep `paper-source/`, `docs/`, `review/` and `.SuperSurfer/` private and ignored by Git.

## Update content

Edit `index.html` and `assets/project.css`. The original template CSS is vendored separately. Keep all review resources anonymous, including PDF text/metadata, captions, media metadata, file paths and commit identities. Raw manuscript sources and private provenance must not be staged.

The full video uses native HTML `<video controls playsinline>` with `assets/videos/project-video.mp4`, a poster and an optional English WebVTT caption track. Three short examples use the same player. Add any new public assets to `FILES` in `scripts/site.py`.

The Paper link downloads `assets/paper.pdf`. The manuscript pipeline is `assets/pipeline.png`; the results PNG links to `assets/results.pdf` for full resolution. Keep “submitted to RA-L” and “under review” until the status changes. Retain `noindex, nofollow` during anonymous review.

## GitHub Pages

Sign in with an anonymous project account using GitHub CLI (`gh auth login`) or a configured credential manager. Use a public repository for GitHub Free Pages. In Settings → Pages select **Deploy from a branch**, **main**, **/(root)**. `.nojekyll` is included. The site is available at `https://YOUR_ANONYMOUS_USERNAME.github.io/YOUR_REPOSITORY/` after deployment.

Use anonymous repository-local commit identity:

```sh
git config --local user.name "Anonymous Authors"
git config --local user.email "anonymous@example.invalid"
```

For future changes, stage selected public files, review `git diff --cached`, commit and push. Never merge or push a pre-anonymization clone: it can restore the old identifying history. Re-clone the cleaned repository instead. Rewriting Git history does not erase independent clones, forks, downloaded files or cached commit views.

Third-party template and dependency attribution is retained in `ATTRIBUTION.md`, `LICENSE` and `assets/vendor/BULMA-LICENSE`. These credits identify upstream software creators, not the research authors.

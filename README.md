# Social LLM project website

Review companion for **Multimodal Socially Aware Framework for Human-Robot Interaction in Virtual Reality**. Status: submitted to RA-L; under review.

The site uses the Academic Project Page Template layout with a compact publication header, a 680px-wide teaser, method-focused overview, project video, interaction clips and architecture pipeline. Results show only the two rating panels (A and B). Author names, affiliations and citation metadata are restored at the user’s request; anonymity is no longer required. Code release remains coming soon.

## Preview locally

From the repository directory, run:

```sh
python3 scripts/site.py check
python3 scripts/site.py build
python3 scripts/site.py serve
```

Open http://127.0.0.1:4173. Python 3 standard library only; no npm dependencies. The preview serves the public allowlist from `dist/`. Keep `paper-source/`, `docs/`, `review/` and `.SuperSurfer/` private and ignored by Git.

## Update content

Edit `index.html` and `assets/project.css`. The original template CSS is vendored separately. Keep paper metadata and captions grounded in the manuscript. Raw manuscript sources and private provenance must not be staged.

The full video uses native HTML `<video controls playsinline>` with `assets/videos/project-video.mp4`, a poster and an optional English WebVTT caption track. Three short examples use the same player. Add any new public assets to `FILES` in `scripts/site.py`.

The Paper button links to the verified arXiv record: https://arxiv.org/abs/2610.34534. The manuscript pipeline is `assets/pipeline.png`; `assets/results-ab.png` is a cropped rendering of panels A/B from the source composite figure, with no regenerated data. Old local paper/figure PDFs are not linked or included in the site bundle. Keep “submitted to RA-L” until the status changes. `noindex, nofollow` remains in place while the paper is under review.

## GitHub Pages

Sign in with the project account using GitHub CLI (`gh auth login`) or a configured credential manager. Use a public repository for GitHub Free Pages. In Settings → Pages select **Deploy from a branch**, **main**, **/(root)**. `.nojekyll` is included. The site is available at `https://YOUR_USERNAME.github.io/YOUR_REPOSITORY/` after deployment.

For future changes, stage selected public files, review `git diff --cached`, commit and push using the intended repository-local Git identity. The earlier anonymous root commit remains intact; no history rewrite is needed for this content revision. The former cached-commit anonymity blocker is superseded by the user’s updated direction.

Third-party template and dependency attribution is retained in `ATTRIBUTION.md`, `LICENSE` and `assets/vendor/BULMA-LICENSE`. These credits identify upstream software creators, not the research authors.

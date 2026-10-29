"""Dependency-free static site checks, packaging, and loopback preview."""
import functools
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import shutil
import sys
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
FILES = ('index.html', 'assets/vendor/bulma.min.css', 'assets/vendor/academic-template.css', 'assets/project.css',
         'assets/vendor/BULMA-LICENSE', 'assets/teaser.png', 'assets/pipeline.png',
         'assets/paper.pdf', 'assets/results.png', 'assets/results.pdf', '.nojekyll') + tuple(
    f'assets/videos/{name}{ext}'
    for name in ('project-video', 'attention', 'drink', 'making-way')
    for ext in ('.mp4', '.vtt')
) + tuple(f'assets/videos/{name}.jpg' for name in ('poster', 'attention', 'drink', 'making-way'))


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.assets, self.tags = [], [], [], []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append(tag)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'a':
            self.links.append(attrs.get('href', ''))
        if tag in ('img', 'script', 'video', 'source', 'track'):
            self.assets.append(attrs.get('src', ''))
        if tag == 'video' and attrs.get('poster'):
            self.assets.append(attrs['poster'])
        if tag == 'link':
            self.assets.append(attrs.get('href', ''))
        if tag == 'img' and not attrs.get('alt'):
            raise ValueError('Images need descriptive alt text')


def check():
    page = Page()
    source = (ROOT / 'index.html').read_text()
    page.feed(source)
    assert len(page.ids) == len(set(page.ids)), 'Duplicate IDs'
    assert page.tags.count('h1') == 1, 'Expected one h1'
    assert all(tag in page.tags for tag in ('main', 'footer')), 'Missing landmarks'
    assert 'name="viewport"' in source and '<html lang="en">' in source
    assert 'Submitted to RA-L' in source, 'Submission status missing'
    assert 'Anonymous Authors' in source, 'Anonymous review byline missing'
    assert 'citation_author' not in source and 'equal-contribution' not in source, 'Identifying author metadata must be omitted'
    assert 'BibTeX' not in source, 'Named citation must stay hidden during review'
    assert '/Users/' not in (ROOT / 'README.md').read_text(), 'README must not expose a personal local path'
    for href in page.links + page.assets:
        assert href and href != '#', 'Empty or placeholder link'
        url = urlsplit(href)
        if url.scheme:
            assert url.scheme == 'https', f'Unexpected URL scheme: {href}'
        elif href.startswith('#'):
            assert href[1:] in page.ids, f'Broken anchor: {href}'
        else:
            assert (ROOT / url.path).is_file(), f'Missing asset: {href}'
    for name in FILES:
        assert (ROOT / name).is_file(), f'Missing site file: {name}'
    print(f'PASS: site structure, {len(page.links)} links/anchors, local assets, submission status. External destinations not fetched.')


def build():
    check()
    target = ROOT / 'dist'
    target.mkdir(exist_ok=True)
    for name in FILES:
        dest = target / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / name, dest)
    print('PASS: static site packaged in dist/ (only allowlisted public site files).')


if __name__ == '__main__':
    action = sys.argv[1] if len(sys.argv) > 1 else 'check'
    if action == 'check':
        check()
    elif action == 'build':
        build()
    elif action == 'serve':
        build()
        handler = functools.partial(SimpleHTTPRequestHandler, directory=str(ROOT / 'dist'))
        print('Preview: http://127.0.0.1:4173 (Ctrl-C to stop)', flush=True)
        ThreadingHTTPServer(('127.0.0.1', 4173), handler).serve_forever()
    else:
        raise SystemExit('Usage: python3 scripts/site.py [check|build|serve]')

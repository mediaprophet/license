# GitHub Pages publishing

The public explanation is served at https://mediaprophet.github.io/license/.

The home page is rendered directly from `PROJECT-PURPOSE.md`. Other root Markdown documents become linked HTML pages, and links to source artifacts point to their files on GitHub. `PROJECT-PURPOSE.html` remains an alternative public URL for the same explanation. There is no separately maintained copy of the explanation and no client-side rendering or tracking script.

Install the documentation-only dependency and build from the repository root:

```text
python -m pip install -r site/requirements.txt
python site/build.py
python -m http.server 8765 --directory dist/pages
```

The build requires a new or empty output directory. Use `--output dist/another-preview` to build a separate preview. The documentation renderer is separate from the dependency-free licence generator.

`.github/workflows/pages.yml` builds and deploys on pushes to `main`, or through a manual workflow dispatch. GitHub Pages uses the GitHub Actions publishing source and the `github-pages` environment. Draft documents retain their status and development notices when published. Publishing them does not adopt a licence or make the rights fabric operational.

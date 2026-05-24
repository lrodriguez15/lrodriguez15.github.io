# lrodriguez15.github.io — OOP C++14 Lecture Website

## Project Overview

Static lecture website for the **Object-Oriented Programming with C++14** course at Tec de Monterrey.
Hosted on GitHub Pages. No build step, no framework, no npm — plain HTML/CSS/JS.

## Structure

```
lrodriguez15.github.io/
├── index.html              # Course landing page (lecture card grid)
├── css/style.css           # All styles (dark theme, CSS variables)
├── js/main.js              # Minimal JS
└── lectures/
    ├── 01-class-relationships.html
    ├── 02-inheritance.html
    └── 03-polymorphism.html
```

## Adding a New Lecture

1. Copy an existing lecture file, e.g.:
   ```
   cp lectures/03-polymorphism.html lectures/04-my-topic.html
   ```
2. Update the `<title>`, breadcrumb text, `lecture-num`, `<h1>`, and chip tags at the top.
3. Fill in the four sections: **Overview**, **Notes**, **Code Examples**, **Slides**, **Exercises**.
4. Add a new card to `index.html` inside `.card-grid`:
   ```html
   <div class="card">
     <span class="card-num">Lecture 04</span>
     <span class="card-title">Your Topic Title</span>
     <span class="card-desc">One-line description of the lecture.</span>
     <div class="chips">
       <span class="chip chip-blue">keyword</span>
     </div>
     <a class="card-link" href="lectures/04-my-topic.html">View lecture →</a>
   </div>
   ```
5. Naming convention: `lectures/NN-slug.html` where `NN` is zero-padded (01, 02, …).

## Syntax Highlighting

Prism.js (v1.29.0, okaidia theme) is loaded from CDN on each lecture page.
Wrap every code block like this — no extra config needed:

```html
<pre><code class="language-cpp">
// your C++ code here
</code></pre>
```

Prism autoloader handles the C++ grammar automatically.

## CSS Variables (css/style.css)

| Variable        | Value     | Usage                        |
|-----------------|-----------|------------------------------|
| `--bg`          | `#0d1117` | Page background              |
| `--surface`     | `#161b22` | Cards, code blocks           |
| `--border`      | `#30363d` | Borders, dividers            |
| `--accent`      | `#58a6ff` | Links, h3, highlights        |
| `--accent-dim`  | `#1f6feb` | Buttons                      |
| `--text`        | `#c9d1d9` | Body text                    |
| `--muted`       | `#8b949e` | Secondary text, labels       |
| `--font-sans`   | Inter     | Body font                    |
| `--font-mono`   | JetBrains Mono | Code, nav brand, chips  |
| `--max-w`       | `860px`   | Max content width            |

## Chips / Tags

Three colour variants available:

```html
<span class="chip chip-blue">keyword</span>
<span class="chip chip-green">keyword</span>
<span class="chip chip-orange">keyword</span>
```

## Adding Slides

Replace the placeholder in the slides section with a real link:

```html
<!-- Before (placeholder) -->
<span class="slide-placeholder">Slides not yet uploaded</span>

<!-- After (real link) -->
<a class="slide-btn" href="https://..." target="_blank" rel="noopener">Open slides ↗</a>
```

## Dependencies (CDN — no install required)

| Library          | CDN URL pattern                                      |
|------------------|------------------------------------------------------|
| Prism CSS        | `cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-okaidia.min.css` |
| Prism core JS    | `cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-core.min.js` |
| Prism autoloader | `cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/autoloader/prism-autoloader.min.js` |
| Google Fonts     | Inter + JetBrains Mono via `fonts.googleapis.com`   |

## Deployment

Push to the `main` branch — GitHub Pages serves the site automatically from the repo root.
No build action required.

# Golden Years Home Health Supported Living LLC — Website

> **Compassionate Care, Dignified Living, Trusted Support.**

The official website for **Golden Years Home Health Supported Living LLC**, a nurse-led home health and supported living agency based in Sumner, Washington, founded and led by **Rose Mbote, BSN, RN, RND, PDN**.

This is a fast, fully responsive, dependency-free static website (plain HTML + CSS). There is no build step and no framework to install — it runs anywhere static files can be served.

---

## Table of Contents

- [Overview](#overview)
- [Pages](#pages)
- [Project Structure](#project-structure)
- [Running It Locally](#running-it-locally)
- [Deploying the Site](#deploying-the-site)
- [Adding Your Logo](#adding-your-logo)  ← *the file naming you asked about*
- [Adding a Favicon](#adding-a-favicon)
- [Replacing the Photos](#replacing-the-photos)
- [Connecting the Forms](#connecting-the-forms)
- [Customizing Colors & Fonts](#customizing-colors--fonts)
- [SEO Files](#seo-files)
- [Contact](#contact)
- [License](#license)

---

## Overview

| | |
|---|---|
| **Type** | Static website (HTML5 + CSS3, a little vanilla JavaScript) |
| **Framework** | None — no build tools, no npm, no dependencies |
| **Fonts** | Playfair Display + Inter (loaded from Google Fonts) |
| **Palette** | Royal Blue `#3447aa` · Blush White `#fbeaeb` · Golden Brown `#b8860b` |
| **Responsive** | Yes — desktop, tablet, and mobile |
| **Accessibility** | Skip link, ARIA labels, semantic HTML, keyboard-friendly |
| **SEO** | Per-page meta tags, Open Graph tags, schema markup, sitemap, robots.txt |

---

## Pages

| File | Page |
|------|------|
| `index.html` | Home |
| `about.html` | About Us (company story + owner bio) |
| `services.html` | Services hub (all service cards + care team) |
| `skilled-nursing.html` | Skilled Nursing |
| `nurse-delegation.html` | Nurse Delegation |
| `hca-training.html` | Home Care Aide (HCA) Training |
| `resources.html` | Resources, FAQ, Insurance, HIPAA, Patient Rights |
| `contact.html` | Contact Us (inquiry form + care intake form + map) |
| `404.html` | Custom "page not found" page |

---

## Project Structure

```
goldenyears/
├── index.html
├── about.html
├── services.html
├── skilled-nursing.html
├── nurse-delegation.html
├── hca-training.html
├── resources.html
├── contact.html
├── 404.html
├── css/
│   └── styles.css          ← shared design system for every page
├── images/
│   ├── logo.png            ← YOU ADD THIS (see "Adding Your Logo")
│   └── favicon.png         ← YOU ADD THIS (see "Adding a Favicon")
├── robots.txt
├── sitemap.xml
├── CNAME                   ← only for GitHub Pages + custom domain
├── .gitignore
├── LICENSE
└── README.md
```

---

## Running It Locally

No build tools are required. Pick whichever is easiest:

**Option A — just open it**
Double-click `index.html` to open it in your browser. (Note: the contact-page map and Google Fonts need an internet connection.)

**Option B — run a tiny local server** (recommended, so links behave exactly like production)

```bash
# From inside the goldenyears folder:

# If you have Python 3:
python3 -m http.server 8000

# ...or if you have Node.js:
npx serve .
```

Then visit `http://localhost:8000` in your browser.

---

## Deploying the Site

Because it's static, you can host it almost anywhere. Three easy options:

### GitHub Pages (free)
1. Push this folder to a GitHub repository.
2. In the repo, go to **Settings → Pages**.
3. Under **Build and deployment**, set **Source = Deploy from a branch**, pick your branch (e.g. `main`) and the `/ (root)` folder, then **Save**.
4. Your site goes live at `https://<your-username>.github.io/<repo-name>/`.
5. To use your own domain (`goldenyearshomehealthllc.com`), keep the included `CNAME` file and point your domain's DNS to GitHub Pages. *(If you are **not** using GitHub Pages with a custom domain, delete the `CNAME` file.)*

### Netlify or Vercel (free)
- Drag-and-drop the `goldenyears` folder onto [app.netlify.com/drop](https://app.netlify.com/drop), **or** connect the GitHub repo on [vercel.com](https://vercel.com). No build command is needed — it deploys instantly.

### Traditional web host (cPanel / FTP)
- Upload the **contents** of the `goldenyears` folder to your `public_html` (or `www`) directory. Make sure `index.html` sits at the root.

---

## Adding Your Logo

**The site is already wired for your logo. To make it appear, name your file exactly:**

```
logo.png
```

**and place it in the `images/` folder**, so the final path is:

```
images/logo.png
```

That's it — every page (header *and* footer) will automatically display it. Until that file exists, the site gracefully shows a gold **"G"** placeholder, so nothing ever looks broken.

### For the most professional result, your `logo.png` should be:
- **A PNG with a transparent background** (so it sits cleanly on both the white header and the dark blue footer).
- **Roughly square**, about **200 × 200 px** to **512 × 512 px** (it's displayed in a 52 px rounded square and scaled down crisply).
- Your **golden-brown brand mark**. A gold/light-toned logo reads well against the dark blue footer; a very dark logo may be hard to see there.

### Notes & options
- **Have an SVG instead?** SVG is even sharper. Either export it to PNG named `logo.png`, **or** keep the SVG (e.g. `images/logo.svg`) and do a find-and-replace across the HTML files, changing `images/logo.png` → `images/logo.svg`.
- **Want the gold rounded square kept behind a transparent logo?** Open `css/styles.css`, find `.brand__mark.has-logo`, and remove the line `background: transparent;`.
- **Logo getting cropped?** It uses `object-fit: contain`, so the whole logo always shows without cropping. A wide/horizontal logo will simply appear smaller inside the square — for a wide wordmark, a square or stacked version works best in this spot.

---

## Adding a Favicon

The favicon is the small icon shown on the browser tab. The site already references it — just add a file named:

```
favicon.png
```

into the `images/` folder (final path `images/favicon.png`).

- Recommended size: a square **512 × 512 px** PNG (browsers scale it down). 32 × 32 px also works.
- A simplified version of your logo (just the "G" mark) usually makes the best favicon.

---

## Replacing the Photos

The site currently loads professional stock photos from Unsplash by URL, so they display once the site is online. For a fully self-contained, faster-loading site, you can swap them for your own images:

1. Add your photos to the `images/` folder (e.g. `images/hero.jpg`).
2. In the HTML files, find the `src="https://images.unsplash.com/..."` links and replace each with your local path (e.g. `src="images/hero.jpg"`).
3. Keep the `alt="..."` text descriptive — it helps both accessibility and SEO.

Use warm, bright, home-based photos of caregiving (not cold hospital imagery), and compress them (e.g. via [squoosh.app](https://squoosh.app)) so pages load quickly.

---

## Connecting the Forms

The two forms on `contact.html` (the general inquiry form and the care intake form) currently show a friendly "thank you" confirmation when submitted, but they do **not yet send** the information anywhere. To receive real submissions by email, connect them to a form handler — no server required:

- **[Formspree](https://formspree.io)** — easiest. Create a form, then set the `<form>` tag's `action` to your Formspree URL and `method="POST"`.
- **[Netlify Forms](https://docs.netlify.com/forms/setup/)** — if hosting on Netlify, just add `data-netlify="true"` to the `<form>` tag.
- **Google Forms / Getform / Basin** — other no-code options.

> **HIPAA note:** Standard web forms are **not** a secure channel for detailed protected health information (PHI). The care intake form is designed for *initial* contact only and already displays a PHI notice. Collect full medical details through a secure, HIPAA-compliant process during the assessment — not through the public website form.

---

## Customizing Colors & Fonts

All styling lives in **`css/styles.css`**. Brand colors are defined once at the top as CSS variables, so you can re-theme the whole site by editing a few lines:

```css
:root {
  --blue:   #3447aa;   /* primary brand blue */
  --blush:  #fbeaeb;   /* soft background    */
  --gold:   #b8860b;   /* golden-brown accent */
  /* ...etc */
}
```

Fonts are loaded in each page's `<head>` from Google Fonts (Playfair Display for headings, Inter for body text).

---

## SEO Files

- **`sitemap.xml`** — lists every page for search engines. Update the URLs if your domain differs from `goldenyearshomehealthllc.com`.
- **`robots.txt`** — allows search engines to crawl the site and points them to the sitemap.
- After going live, submit your sitemap in [Google Search Console](https://search.google.com/search-console) to help your site get indexed.

---

## Contact

**Golden Years Home Health Supported Living LLC**
📍 614 Harrison St, Suite C, Sumner, WA 98390
📞 [206-436-9751](tel:+12064369751)
✉ [rose.mbote@goldenyearshomehealthllc.com](mailto:rose.mbote@goldenyearshomehealthllc.com)

*Founder & CEO: Rose Mbote, BSN, RN, RND, PDN*

---

## License

© 2025 Golden Years Home Health Supported Living LLC. All Rights Reserved.

This website and its content are the property of Golden Years Home Health Supported Living LLC. See the [`LICENSE`](LICENSE) file for details.

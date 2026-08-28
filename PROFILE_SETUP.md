# Profile setup

## 1. Create the special repository

Create a **public** repository named exactly:

`YOUR_GITHUB_USERNAME/YOUR_GITHUB_USERNAME`

GitHub displays its root `README.md` on your profile.

## 2. Replace placeholders

Search for:

- `YOUR_GITHUB_USERNAME`
- `YOUR_LINKEDIN_USERNAME`
- `YOUR_PORTFOLIO_DOMAIN`

Also edit `scripts/make_info_card.py` when your actual stack changes.

## 3. Generate the cards

Install dependencies:

```bash
python -m pip install -r scripts/requirements.txt
```

Then:

```bash
python scripts/make_info_card.py
python scripts/fetch_contributions.py
python scripts/render_heatmap_svg.py
```

## 4. Optional real portrait

Put a photo at:

`assets/source-photo.jpg`

Then run:

```bash
python scripts/make_ascii_svg.py assets/source-photo.jpg assets/arko-ascii.svg
```

The included placeholder portrait works until you do this.

## 5. Push

```bash
git add .
git commit -m "feat: build GitHub profile"
git push
```

## 6. Automation

`.github/workflows/update-profile-art.yml` refreshes the contribution graph daily and can also be run manually from the Actions tab.

No personal access token is required by the contribution scraper; it reads GitHub's public contribution calendar.

**Never commit API keys, `.env` files, passwords, tokens, or private credentials.**

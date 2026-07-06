FounderGPT Launch Kit — repo assets

Files in /cash-launch:
- index.html — simple landing page and product summary
- product.md — prompts pack (source content)
- email_templates.md — 3-email launch sequence
- stripe_instructions.md — how to accept payments (Gumroad + Stripe)
- .env.example — placeholders for keys

Next steps (recommended):
1) Convert product.md to product.pdf (export from Markdown to PDF)
2) Create a Gumroad product (fast) or configure Stripe Checkout and webhook
3) Upload PDF and set checkout link in `index.html` or deploy the page
4) Send the email sequence to your list and promote on Twitter/LinkedIn

If you want, I can:
- Export product.md to a styled PDF
- Create ready-to-run GitHub Pages deploy config or Vercel static site
- Generate 30 social posts / short video scripts for promotion

Local payout configuration (private)
----------------------------------
Do NOT commit your real bank or payout details into the repository. Instead:

1. Copy `payouts.local.example` to `payouts.local` inside `/cash-launch/`.
2. Fill in your real values (BANK_NAME, ACCOUNT_TITLE, ACCOUNT_NUMBER, IBAN, CURRENCY, BRANCH, SWIFT_CODE).
3. `payouts.local` is listed in `/cash-launch/.gitignore` so it won't be committed.

If you want, I can generate a PDF invoice template you can send to customers including your payout instructions, or add a customer-facing "Bank transfer" payment option example to the landing page. Paste your bank details only into your local `payouts.local` file — I will not publish or commit them.

Stripe / Gumroad quick setup

Option A — Gumroad (fastest, simplest)
- Create a Gumroad account and add a new product -> Digital product
- Upload product.pdf and set price $29
- Gumroad gives you a public checkout link you can paste into the landing page
- Pros: no dev work, instant payouts (after verification), simple

Option B — Stripe Checkout (requires minimal dev)
- Create a Stripe account and get API keys (publishable + secret)
- In Stripe Dashboard create a Product and Price ($29 one-time)
- Create a simple server endpoint to create a Checkout Session

Example (Node.js / Express):

const stripe = require('stripe')(process.env.STRIPE_SECRET);
app.post('/create-checkout', async (req, res) => {
  const session = await stripe.checkout.sessions.create({
    payment_method_types: ['card'],
    line_items: [{price: 'price_XXXXX', quantity: 1}],
    mode: 'payment',
    success_url: 'https://your-site.com/success',
    cancel_url: 'https://your-site.com/cancel',
  });
  res.json({id: session.id});
});

- On success, deliver the download URL from your server or via Stripe webhooks to send the file link.

Security notes:
- Never commit your Stripe secret key to version control. Use environment variables (.env) and .gitignore.
- For immediate minimal friction use Gumroad.

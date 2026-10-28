import { chromium } from 'playwright';
const url = 'file:///workspace/transferportal/Codex/Emails/Perspective-Fall2026/index.html';
const out = process.argv[2] || '.';
const b = await chromium.launch();
for (const [name, w, h, dpr] of [['desk', 1440, 900, 1], ['mid', 1000, 800, 1], ['mob', 390, 844, 1]]) {
  const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: dpr });
  const errs = []; p.on('console', m => m.type() === 'error' && errs.push(m.text())); p.on('requestfailed', r => errs.push('FAIL ' + r.url().split('/').pop()));
  await p.goto(url, { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready);
  await p.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 30)); } window.scrollTo(0, 0); });
  await p.evaluate(async () => { const im=[...document.images]; im.forEach(i => i.loading='eager'); await Promise.all(im.map(i => i.decode().catch(()=>0))); });
  await p.waitForTimeout(300);
  await p.screenshot({ path: `${out}/${name}-full.png`, fullPage: true });
  const sw = await p.evaluate(() => document.documentElement.scrollWidth);
  const fonts = await p.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight + ' ' + f.style));
  console.log(name, 'scrollWidth', sw, 'height', await p.evaluate(() => document.body.scrollHeight), 'errors', errs.filter(e => e.startsWith('FAIL')), 'loaded', [...new Set(fonts)].join('; '));
}
await b.close();

/* Capture the actual DOM and fonts; manual observations are recorded separately. */
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const {pathToFileURL} = require('node:url');
const {chromium} = require(process.env.CODEX_READER_PLAYWRIGHT_MODULE);
const root = path.resolve(__dirname, '..');
const build = path.join(root, 'build', 'full-edition');
const sha = data => crypto.createHash('sha256').update(data).digest('hex');
const phoneSamples = new Map([
  ['OLP-0268', 'em:text-is("3-Halt")'],
  ['OLP-0605', 'em:text-is("if and only if")'],
  ['OLP-0684', '.tableau-semantic'],
  ['OLP-0708', '.proof-tree-semantic'],
]);
async function main() {
  const probesPath = path.join(build, 'VISUAL_PROBES.json');
  const probes = JSON.parse(fs.readFileSync(probesPath, 'utf8'));
  const reader = path.join(build, 'openlogic-bn-Beng-IN-complete.html');
  if (sha(fs.readFileSync(reader)) !== probes.reader_sha256) throw Error('stale probes');
  const directory = path.join(build, 'visual-renders');
  fs.mkdirSync(directory, {recursive: true});
  const browser = await chromium.launch({executablePath: process.env.CODEX_READER_CHROME_PATH, headless: true});
  const captures = [];
  try {
    const page = await browser.newPage({viewport: {width: 1400, height: 1100}, deviceScaleFactor: 1});
    for (const probe of probes.probes) {
      const source = path.resolve(build, probe.file);
      if (!source.startsWith(build + path.sep) || sha(fs.readFileSync(source)) !== probe.sha256) throw Error('stale probe ' + probe.file);
      const errors = [];
      const handler = error => errors.push(String(error));
      page.on('pageerror', handler);
      await page.goto(pathToFileURL(source).href, {waitUntil: 'load'});
      await page.evaluate(async () => {await document.fonts.ready;});
      const metrics = await page.evaluate(() => ({
        width: document.documentElement.scrollWidth,
        viewport: innerWidth,
        height: document.documentElement.scrollHeight,
        bengaliFontLoaded: document.fonts.check('18px BN', 'সিদ্ধান্ত'),
        mathCount: document.querySelectorAll('math').length,
        proofCount: document.querySelectorAll('.proof-tree-semantic').length,
        tableauCount: document.querySelectorAll('.tableau-semantic').length,
        diagramCount: document.querySelectorAll('.diagram-semantic').length,
        emptyMath: [...document.querySelectorAll('math')].filter(x => !x.textContent.trim()).length
      }));
      const stem = path.basename(source, '.html');
      const shots = [];
      async function screenshot(name, operation) {
        const file = path.join(directory, stem + '-' + name + '.png');
        await operation(file);
        shots.push({file: path.relative(build, file).split(path.sep).join('/'), sha256: sha(fs.readFileSync(file)), bytes: fs.statSync(file).size});
      }
      await screenshot('opening', file => page.screenshot({path: file}));
      if (metrics.height <= 13000) await screenshot('full', file => page.screenshot({path: file, fullPage: true}));
      for (const [selector, name] of [['.tableau-semantic', 'tableau'], ['.proof-tree-semantic', 'proof'], ['.diagram-semantic', 'diagram']]) {
        const elements = page.locator(selector);
        const count = await elements.count();
        if (count) {
          await screenshot(name + '-first', file => elements.first().screenshot({path: file}));
          if (count > 1) await screenshot(name + '-last', file => elements.last().screenshot({path: file}));
        }
      }
      for (const [symbol, name] of [['⋰', 'ascending-ellipsis'], ['↠', 'reduction'], ['⇒', 'double-line-arrow']]) {
        const elements = page.locator('math').filter({hasText: symbol});
        if (await elements.count()) await screenshot(name, file => elements.first().screenshot({path: file}));
      }
      for (const [symbol, name] of [['\uE000','boxright'], ['\uE001','fishhookright'], ['\uE002','leftrightarroweq']]) {
        const elements = page.locator('math').filter({hasText: symbol});
        if (await elements.count()) await screenshot('operator-' + name, file => elements.first().screenshot({path: file}));
      }
      if (probe.unit_id === 'OLP-0710') {
        const elements = page.locator('.proof-tree-semantic');
        if (await elements.count() !== 12) throw Error('G3c rule-table proof count changed');
        await screenshot('universal-right', file => elements.nth(9).screenshot({path: file}));
      }
      const cdp = await page.context().newCDPSession(page);
      await cdp.send('DOM.enable');
      await cdp.send('CSS.enable');
      const documentNode = await cdp.send('DOM.getDocument');
      await page.evaluate(() => {
        const element = [...document.querySelectorAll('p')].find(x => /[\u0980-\u09ff]/.test(x.textContent));
        if (element) element.setAttribute('data-qa-font-probe', '');
      });
      const selected = await cdp.send('DOM.querySelector', {nodeId: documentNode.root.nodeId, selector: 'p[data-qa-font-probe]'});
      const platformFonts = selected.nodeId ? (await cdp.send('CSS.getPlatformFontsForNode', {nodeId: selected.nodeId})).fonts : [];
      await page.evaluate(() => {document.querySelector('[data-qa-font-probe]')?.removeAttribute('data-qa-font-probe');});
      await cdp.detach();
      let phone = null;
      if (phoneSamples.has(probe.unit_id)) {
        await page.setViewportSize({width: 390, height: 844});
        const focus = page.locator(phoneSamples.get(probe.unit_id)).first();
        await focus.waitFor({state: 'visible'});
        await focus.evaluate(element => element.scrollIntoView({block: 'center', inline: 'nearest'}));
        phone = await page.evaluate(() => ({
          viewport: innerWidth,
          width: document.documentElement.scrollWidth,
          bengaliFontLoaded: document.fonts.check('18px BN', 'সিদ্ধান্ত'),
        }));
        await screenshot('phone', file => page.screenshot({path: file}));
        await page.setViewportSize({width: 1400, height: 1100});
      }
      page.off('pageerror', handler);
      captures.push({unit_id: probe.unit_id, focus: probe.focus || null, probe_sha256: probe.sha256, metrics, phone, platformFonts, errors, screenshots: shots});
    }
  } finally {await browser.close();}
  const result = {schema: 'openlogic-bn-reader-browser-captures/1', reader_sha256: probes.reader_sha256,
    probes_sha256: sha(fs.readFileSync(probesPath)), captured_at_utc: new Date().toISOString(),
    method: 'Source-bound probes at 1400x1100 with embedded fonts and native MathML. Four passages are also captured at 390x844.',
    status: 'captured; manual visual review pending', captures};
  fs.writeFileSync(path.join(build, 'BROWSER_CAPTURES.json'), JSON.stringify(result, null, 2) + '\n');
  console.log(JSON.stringify({captures: captures.length, screenshots: captures.reduce((n, r) => n + r.screenshots.length, 0), reader_sha256: result.reader_sha256}));
}
main().catch(error => {console.error(error);process.exitCode=1;});

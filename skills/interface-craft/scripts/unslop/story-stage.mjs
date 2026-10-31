// Adapted from Unslop by Damir Sokolovsky (@heydamir), CC BY 4.0.
// https://github.com/heydamir/unslop commit 4652254; modified 2026-10-31.
export function makeStage({FRAME, play, VIEW, left, top, pageWidth, pageHeight, scale, file, root}) {
return `<!doctype html><html><head><meta charset="utf-8"><style>
  html, body { margin: 0; width: ${FRAME.width}px; height: ${FRAME.height}px; overflow: hidden; background: #111; }
  ${play ? `body { transform: scale(${VIEW}); transform-origin: 0 0; }` : ""}
  #story-layer { position: absolute; inset: 0; pointer-events: none; z-index: 10; }
  #story-layer > * { position: absolute; }
  #story-layer .s-fade { opacity: 0; transition: opacity 240ms ease; }
  #story-layer.s-on .s-fade { opacity: 1; }
  #story-layer .s-x { transform: scaleX(0); transition: transform 520ms cubic-bezier(0.65, 0, 0.35, 1), background-color 300ms ease; }
  #story-layer .s-y { transform: scaleY(0); transition: transform 520ms cubic-bezier(0.65, 0, 0.35, 1), background-color 300ms ease; }
  #story-layer.s-on .s-x { transform: scaleX(1); }
  #story-layer.s-on .s-y { transform: scaleY(1); }
  #story-layer .s-tag { font: 500 15px/30px ui-monospace, "Geist Mono", "SF Mono", Menlo, monospace; height: 30px; padding: 0 12px; border-radius: 999px; white-space: nowrap; color: #fff; background: #ff4d6a; font-variant-numeric: tabular-nums; transition: opacity 220ms ease 100ms, background-color 300ms ease, color 300ms ease; }
  #story-layer.s-fixed .s-tag { background: #f5f5f5; color: #111; }
  #story-layer .s-ink { background: #ff4d6a; }
  #story-layer .s-hair { background: rgba(255,77,106,0.55); }
  #story-layer .s-fill { background: rgba(255,77,106,0.1); }
  #story-layer.s-fixed .s-ink { background: rgba(255,255,255,0.92); }
  #story-layer.s-fixed .s-hair { background: rgba(255,255,255,0.24); }
  #story-layer.s-fixed .s-fill { background: rgba(255,255,255,0.05); }
  #story-layer .s-box { border: 1.5px solid #ff4d6a; background: rgba(255,77,106,0.07); transform: scale(1.03); transition: opacity 220ms ease, transform 260ms ease, border-color 300ms ease, background-color 300ms ease; }
  #story-layer.s-on .s-box { transform: scale(1); }
  #story-layer.s-fixed .s-box { border-color: rgba(255,255,255,0.92); background: rgba(255,255,255,0.04); }
  #story-layer .s-corner { width: 8px; height: 8px; background: #fff; border: 1px solid #ff4d6a; }
  .credit { position: absolute; right: 28px; bottom: 24px; z-index: 20; padding: 7px 12px; border-radius: 999px; font: 500 15px/1 ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif; letter-spacing: 0.01em; color: rgba(255,255,255,0.86); background: rgba(12,12,14,0.62); box-shadow: 0 0 0 1px rgba(255,255,255,0.1); backdrop-filter: blur(8px); }
  iframe { position: absolute; left: ${left}px; top: ${top}px; border: 0; width: ${pageWidth}px; height: ${pageHeight}px; transform-origin: 0 0; transform: scale(${scale}); background: transparent; }
</style></head><body>
  <iframe sandbox="allow-scripts allow-same-origin" id="page" src="/__story/${encodeURIComponent(file.slice(root.length + 1))}"></iframe>
  <div id="story-layer"></div>
  <div class="credit">unslop by @heydamir</div>
  <script>
    window.__stage = { conf: { scale: ${scale}, x: ${left}, y: ${top} } };
  </script>
</body></html>`;

}

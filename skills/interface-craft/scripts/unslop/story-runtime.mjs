// Adapted from Unslop by Damir Sokolovsky (@heydamir), CC BY 4.0.
// https://github.com/heydamir/unslop commit 4652254; modified 2026-10-31.
export const runtimeTemplate = `
(() => {
  const red = "#ff4d6a";
  const spring = "cubic-bezier(0.3, 1.12, 0.45, 1)";
  const ease = "cubic-bezier(0.45, 0, 0.2, 1)";
  const layout = ["padding", "margin", "gap", "row-gap", "column-gap", "width", "height", "min-width", "min-height", "max-width", "max-height", "top", "right", "bottom", "left", "inset", "font-size", "line-height", "letter-spacing", "font-weight", "transform", "translate", "scale", "rotate", "border-width", "outline-width", "flex-basis", "grid-template-columns", "grid-template-rows"];
  const tint = ["color", "background-color", "border-color", "outline-color", "fill", "stroke", "stroke-dashoffset", "stroke-width", "box-shadow", "text-shadow", "border-radius", "opacity", "filter", "backdrop-filter", "clip-path", "text-decoration-color", "-webkit-text-fill-color"];
  const transition = [...layout.map((p) => p + " 700ms " + spring + " var(--wave, 0ms)"), ...tint.map((p) => p + " 900ms " + ease + " var(--wave, 0ms)")].join(", ");
  const rise = "cubic-bezier(0.17, 0.84, 0.44, 1)";
  const steps = __UNSLOP_STEPS__;
  let css = \`
    :root { interpolate-size: allow-keywords; }
    html.story-live *, html.story-live *::before, html.story-live *::after { transition: \${transition} !important; }
    .swap { display: inline-grid; justify-items: start; align-items: start; vertical-align: top; overflow: visible; }
    div.swap, p.swap, h1.swap, h2.swap, h3.swap, li.swap { display: grid; }
    .swap > .from, .swap > .to { grid-area: 1 / 1; }
    .swap > .to { opacity: 0; pointer-events: none; }
    .swap > .to .ch { display: inline-block; opacity: 0; transform: translateY(40%); filter: blur(8px); }
    html.story-live .swap > .to .ch { transition: opacity 700ms \${rise} calc(var(--wave, 0ms) + 140ms + var(--ci) * 16ms), transform 700ms \${rise} calc(var(--wave, 0ms) + 140ms + var(--ci) * 16ms), filter 700ms \${rise} calc(var(--wave, 0ms) + 140ms + var(--ci) * 16ms) !important; }
    [data-in] { opacity: 0; transform: translateY(10px) scale(0.98); }
  \`;
  steps.forEach((_, index) => {
    const k = index + 1;
    css += \`
      html.s\${k} .swap[data-at="\${k}"] > .from { opacity: 0; filter: blur(10px); transform: translateY(-14px); }
      html.s\${k} .swap[data-at="\${k}"] > .to { opacity: 1; }
      html.s\${k} .swap[data-at="\${k}"] > .to .ch { opacity: 1; transform: none; filter: none; }
      html.s\${k} [data-in="\${k}"] { opacity: 1; transform: none; }
      html.s\${k} [data-out="\${k}"] { opacity: 0; max-height: 0 !important; max-width: 0 !important; margin-top: 0 !important; margin-bottom: 0 !important; padding: 0 !important; border-width: 0 !important; }
    \`;
  });

  function letters(node) {
    let index = 0;
    const walk = (el) => {
      [...el.childNodes].forEach((child) => {
        if (child.nodeType === 3) {
          const frag = document.createDocumentFragment();
          child.textContent.split(/(\\s+)/).forEach((part) => {
            if (!part) return;
            if (/^\\s+$/.test(part)) return frag.appendChild(document.createTextNode(part));
            const word = document.createElement("span");
            word.style.display = "inline-block";
            word.style.whiteSpace = "nowrap";
            [...part].forEach((char) => {
              const span = document.createElement("span");
              span.className = "ch";
              span.style.setProperty("--ci", index++);
              span.textContent = char;
              word.appendChild(span);
            });
            frag.appendChild(word);
          });
          child.replaceWith(frag);
        } else if (child.nodeType === 1 && child.tagName.toLowerCase() !== "svg") {
          walk(child);
        }
      });
    };
    walk(node);
  }

  const conf = window.parent.__stage.conf;
  function layer() {
    return window.parent.document.getElementById("story-layer");
  }

  const box = (el) => el.getBoundingClientRect();
  const sx = (x) => conf.x + x * conf.scale;
  const sy = (y) => conf.y + y * conf.scale;
  function put(className, style, html) {
    const node = window.parent.document.createElement("div");
    node.className = className;
    Object.assign(node.style, style);
    if (html) node.innerHTML = html;
    layer().appendChild(node);
    return node;
  }
  const rect = (left, top, width, height) => ({ left: sx(left) + "px", top: sy(top) + "px", width: width * conf.scale + "px", height: height * conf.scale + "px" });

  const escapeHTML = (text) => String(text).replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
  function audit() {
    document.querySelectorAll("[data-slop]").forEach((el, index) => {
      const b = box(el);
      if (b.width < 4 || b.bottom < 0 || b.top > innerHeight) return;
      const pad = 8 / conf.scale;
      const wrap = put("s-fade", { ...rect(b.left - pad, b.top - pad, b.width + pad * 2, b.height + pad * 2), transitionDelay: index * 70 + "ms" });
      wrap.innerHTML = '<div class="s-box" style="position:absolute;inset:0"></div>' +
        [["left", "top"], ["right", "top"], ["left", "bottom"], ["right", "bottom"]].map(([x, y]) => '<span class="s-corner" style="position:absolute;' + x + ':-4px;' + y + ':-4px"></span>').join("") +
        '<span class="s-tag" style="position:absolute;left:0;top:-40px">' + escapeHTML(el.dataset.slop) + "</span>";
    });
  }

  function spacing() {
    const groups = new Map();
    document.querySelectorAll("[data-gap]").forEach((el) => {
      const key = el.dataset.gap || "main";
      if (!groups.has(key)) groups.set(key, []);
      groups.get(key).push(el);
    });
    const stageWidth = window.parent.innerWidth;
    const several = groups.size > 1;
    const pairs = [];
    groups.forEach((list) => {
      const items = list.filter((el) => box(el).height > 0 && box(el).top < innerHeight).sort((a, b) => box(a).top - box(b).top);
      for (let i = 1; i < items.length; i++) {
        if (box(items[i]).top - box(items[i - 1]).bottom <= 2) continue;
        pairs.push({ group: items, above: items[i - 1], below: items[i], nodes: {
          fill: put("s-fill s-x", {}), top: put("s-hair s-x", {}), bottom: put("s-hair s-x", {}),
          ruler: put("s-ink s-y", {}), capTop: put("s-ink s-x", {}), capBottom: put("s-ink s-x", {}),
          tag: put("s-tag s-fade", {}),
        } });
      }
    });
    return () => {
      for (const { group, above, below, nodes } of pairs) {
        const a = box(above);
        const b = box(below);
        const left = sx(Math.min(...group.map((el) => box(el).left)));
        const ruler = Math.max(14, left - 20);
        const top = sy(a.bottom);
        const size = Math.max(0, (b.top - a.bottom) * conf.scale);
        const value = Math.round(b.top - a.bottom);
        const right = several ? sx(Math.max(...group.map((el) => box(el).right))) + 24 : stageWidth;
        const start = several ? ruler - 8 : 0;
        const band = { left: start + "px", width: right - start + "px", transformOrigin: ruler - start + "px 50%" };
        Object.assign(nodes.fill.style, band, { top: top + "px", height: size + "px" });
        Object.assign(nodes.top.style, band, { top: top + "px", height: "1px" });
        Object.assign(nodes.bottom.style, band, { top: top + size - 1 + "px", height: "1px" });
        Object.assign(nodes.ruler.style, { left: ruler + "px", top: top + "px", width: "1.5px", height: size + "px", transformOrigin: "50% 0" });
        Object.assign(nodes.capTop.style, { left: ruler - 4 + "px", top: top + "px", width: "9px", height: "1.5px" });
        Object.assign(nodes.capBottom.style, { left: ruler - 4 + "px", top: top + size - 1.5 + "px", width: "9px", height: "1.5px" });
        const room = ruler - 10 > 64;
        Object.assign(nodes.tag.style, { left: (room ? ruler - 10 : ruler + 12) + "px", top: top + size / 2 - 15 + "px", translate: room ? "-100% 0" : "0 0" });
        const text = value + "px";
        if (nodes.tag.textContent !== text) nodes.tag.textContent = text;
        const hidden = value < 4 ? "0" : "";
        Object.values(nodes).forEach((node) => {
          if (node.style.visibility !== (hidden ? "hidden" : "")) node.style.visibility = hidden ? "hidden" : "";
        });
      }
    };
  }

  function details() {
    const items = [...document.querySelectorAll("[data-radius]")].filter((el) => box(el).bottom > 0 && box(el).top < innerHeight).map((el) => {
      const wrap = put("s-fade", {}, '<div class="s-box" style="position:absolute;inset:0"></div>');
      return { el, wrap, outline: wrap.firstChild, tag: put("s-tag s-fade", {}) };
    });
    return () => {
      for (const { el, wrap, outline, tag } of items) {
        const b = box(el);
        const radius = Math.round(Math.min(parseFloat(getComputedStyle(el).borderTopLeftRadius) || 0, b.width / 2, b.height / 2));
        const pad = 5 / conf.scale;
        Object.assign(wrap.style, rect(b.left - pad, b.top - pad, b.width + pad * 2, b.height + pad * 2));
        outline.style.borderRadius = radius * conf.scale + 5 + "px";
        Object.assign(tag.style, { left: sx(b.left) + "px", top: sy(b.bottom) + 12 + "px" });
        const text = "r " + radius;
        if (tag.textContent !== text) tag.textContent = text;
      }
    };
  }

  const kinds = { audit, spacing, details };
  const managed = new WeakMap();
  let current = null;
  let stepping = false;

  window.__story = {
    install() {
      const style = document.createElement("style");
      style.id = "story-style";
      style.textContent = css;
      document.head.appendChild(style);
      document.querySelectorAll(".swap > .to").forEach(letters);
      document.querySelectorAll("[data-out]").forEach((el) => {
        const b = box(el);
        if (getComputedStyle(el).display === "inline") el.style.display = "inline-block";
        el.style.overflow = "hidden";
        el.style.maxHeight = Math.ceil(b.height) + "px";
        el.style.maxWidth = Math.ceil(b.width) + "px";
      });
      document.querySelectorAll("body *").forEach((el) => {
        const b = box(el);
        const wave = Math.round(Math.min(420, Math.max(0, b.top) / innerHeight * 320 + Math.max(0, b.left) / innerWidth * 100));
        el.style.setProperty("--wave", wave + "ms");
      });
      document.querySelectorAll("*").forEach((el) => {
        if (getComputedStyle(el).animationName !== "none") el.style.animationPlayState = "paused";
      });
      document.documentElement.offsetHeight;
      document.documentElement.classList.add("story-live");
      const follow = () => {
        if (current && !stepping) current();
        requestAnimationFrame(follow);
      };
      requestAnimationFrame(follow);
    },
    reset() {
      const root = document.documentElement;
      root.classList.remove("story-live", ...steps.map((_, index) => "s" + (index + 1)));
      layer().className = "";
      layer().innerHTML = "";
      current = null;
      root.offsetHeight;
      root.classList.add("story-live");
    },
    tick(ms) {
      stepping = true;
      for (const animation of [...document.getAnimations(), ...window.parent.document.getAnimations()]) {
        if (!managed.has(animation)) {
          if (animation.playState !== "running") continue;
          managed.set(animation, ms);
          animation.pause();
        }
        const time = ms - managed.get(animation);
        const end = animation.effect ? animation.effect.getComputedTiming().endTime : Infinity;
        if (Number.isFinite(end) && time >= end) animation.finish();
        else animation.currentTime = time;
      }
      if (current) current();
    },
    step(k) {
      document.documentElement.classList.add("s" + k);
    },
    show(kind) {
      const node = layer();
      node.className = "";
      node.innerHTML = "";
      const update = (kinds[kind] || (() => {}))();
      current = typeof update === "function" ? update : null;
      if (current) current();
      node.offsetHeight;
      node.classList.add("s-on");
    },
    settle() {
      layer().classList.add("s-on", "s-fixed");
    },
    clear() {
      layer().classList.remove("s-on");
    },
  };
})();
`;

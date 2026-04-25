with open('index.html', encoding='utf-8') as f:
    c = f.read()

# Localizar e substituir toda a secao scroll-vid
start = c.find('<!-- =========================================== -->\n<!-- SCROLL VIDEO')
end = c.find('</script>\n\n', start) + len('</script>\n\n')

frames_js = ',\n    '.join([f"'assets/scroll-video/frame_{str(i).zfill(3)}.jpg'" for i in range(1, 65)])

new_section = """<!-- =========================================== -->
<!-- SCROLL VIDEO — Buque em movimento           -->
<!-- =========================================== -->
<section class="scroll-vid" id="scroll-vid">
  <div class="scroll-vid__sticky">
    <!-- Loading indicator -->
    <div class="scroll-vid__loader" id="scrollLoader">
      <div class="scroll-vid__loader-bar"></div>
    </div>
    <canvas class="scroll-vid__canvas" id="scrollCanvas"></canvas>
    <!-- Texto ABAIXO do buque, fundo continua do canvas -->
    <div class="scroll-vid__bottom" id="scrollBottom">
      <span class="scroll-vid__eyebrow">Cada detalhe importa</span>
      <h2>Do buque ao <em>ultimo confete</em></h2>
      <p>Mais de 400 casamentos planejados com o mesmo cuidado que voce merece.</p>
    </div>
  </div>
</section>

<style>
.scroll-vid {
  height: 350vh;
  position: relative;
}
.scroll-vid__sticky {
  position: sticky;
  top: 0;
  height: 100vh;
  overflow: hidden;
  background: #fff;
  display: flex;
  flex-direction: column;
}
.scroll-vid__canvas {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  display: block;
}
/* Loader */
.scroll-vid__loader {
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: rgba(107,166,161,0.2);
  z-index: 10;
  transition: opacity 600ms;
}
.scroll-vid__loader.is-done { opacity: 0; pointer-events: none; }
.scroll-vid__loader-bar {
  height: 100%;
  background: var(--cc-teal);
  width: 0%;
  transition: width 200ms linear;
}
/* Texto na parte inferior */
.scroll-vid__bottom {
  position: absolute;
  bottom: 0; left: 0; right: 0;
  padding: 48px var(--container-pad) 64px;
  text-align: center;
  background: linear-gradient(to top, rgba(255,255,255,0.92) 0%, rgba(255,255,255,0.6) 60%, transparent 100%);
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 700ms var(--ease-out), transform 700ms var(--ease-out);
  z-index: 5;
}
.scroll-vid__bottom.is-visible {
  opacity: 1;
  transform: none;
}
.scroll-vid__eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  font-family: var(--ff-sans);
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--cc-teal-deep);
  margin-bottom: 12px;
}
.scroll-vid__eyebrow::before,
.scroll-vid__eyebrow::after {
  content: "";
  width: 24px; height: 1px;
  background: var(--cc-teal);
  display: inline-block;
}
.scroll-vid__bottom h2 {
  font-family: var(--ff-display);
  font-weight: 300;
  font-size: clamp(32px, 4.5vw, 68px);
  line-height: 1.05;
  color: var(--cc-ink);
  margin-bottom: 12px;
}
.scroll-vid__bottom h2 em {
  font-style: italic;
  color: var(--cc-lavender-deep);
}
.scroll-vid__bottom p {
  font-family: var(--ff-display);
  font-style: italic;
  font-size: clamp(16px, 1.3vw, 20px);
  color: var(--cc-ink-soft);
}
@media (max-width: 768px) {
  .scroll-vid { height: 280vh; }
  .scroll-vid__bottom {
    padding: 32px 24px 48px;
  }
  .scroll-vid__bottom h2 { font-size: clamp(26px, 7vw, 40px); }
}
@media (max-width: 480px) {
  .scroll-vid { height: 250vh; }
  .scroll-vid__bottom { padding: 24px 20px 36px; }
}
</style>

<script>
(function() {
  var canvas = document.getElementById('scrollCanvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  var section = document.getElementById('scroll-vid');
  var bottomEl = document.getElementById('scrollBottom');
  var loader = document.getElementById('scrollLoader');
  var loaderBar = loader ? loader.querySelector('.scroll-vid__loader-bar') : null;

  var frameCount = 64;
  var frames = [
    """ + frames_js + """
  ];

  var images = new Array(frameCount);
  var loaded = 0;
  var currentFrame = 0;
  var isMobile = window.innerWidth <= 768;

  function setCanvasSize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    isMobile = window.innerWidth <= 768;
  }

  function drawFrame(idx) {
    var img = images[idx];
    if (!img || !img.complete || !img.naturalWidth) return;
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    var iw = img.naturalWidth;
    var ih = img.naturalHeight;
    var cw = canvas.width;
    var ch = canvas.height;

    if (isMobile) {
      // CONTAIN no mobile: buque inteiro visivel, fundo branco
      var scale = Math.min(cw / iw, ch / ih);
      var w = iw * scale;
      var h = ih * scale;
      var x = (cw - w) / 2;
      var y = (ch - h) / 2;
      ctx.fillStyle = '#ffffff';
      ctx.fillRect(0, 0, cw, ch);
      ctx.drawImage(img, x, y, w, h);
    } else {
      // COVER no desktop: preenche tela toda
      var scale = Math.max(cw / iw, ch / ih);
      var w = iw * scale;
      var h = ih * scale;
      var x = (cw - w) / 2;
      var y = (ch - h) / 2;
      ctx.drawImage(img, x, y, w, h);
    }
  }

  function onScroll() {
    var rect = section.getBoundingClientRect();
    var sectionH = section.offsetHeight - window.innerHeight;
    var scrolled = -rect.top;
    var progress = Math.max(0, Math.min(1, scrolled / sectionH));
    var frameIdx = Math.min(frameCount - 1, Math.floor(progress * (frameCount - 1)));

    if (frameIdx !== currentFrame) {
      currentFrame = frameIdx;
      drawFrame(currentFrame);
    }

    // Texto aparece nos ultimos 30% do scroll
    if (bottomEl) {
      if (progress > 0.65) {
        bottomEl.classList.add('is-visible');
      } else {
        bottomEl.classList.remove('is-visible');
      }
    }
  }

  function preload() {
    frames.forEach(function(src, i) {
      var img = new Image();
      img.onload = function() {
        loaded++;
        // Atualizar barra de loading
        if (loaderBar) {
          loaderBar.style.width = (loaded / frameCount * 100) + '%';
        }
        if (loaded === 1) {
          setCanvasSize();
          drawFrame(0);
        }
        if (loaded === frameCount) {
          if (loader) {
            setTimeout(function() { loader.classList.add('is-done'); }, 400);
          }
          drawFrame(currentFrame);
        }
      };
      img.src = src;
      images[i] = img;
    });
  }

  setCanvasSize();
  preload();

  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', function() {
    setCanvasSize();
    drawFrame(currentFrame);
  });
})();
</script>

"""

c = c[:start] + new_section + c[end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('done, len:', len(c))

# 🔧 CORREÇÕES PRÉ-DEPLOY - CLARISSA CUNHA

## Correções Críticas Identificadas na Análise

---

## 1. ⚠️ VENDOR PREFIXES - BACKDROP-FILTER

### Problema:
A ordem dos vendor prefixes está incorreta em vários arquivos. O `-webkit-` deve vir ANTES da propriedade padrão.

### Arquivos Afetados:
- `styles/tokens.css`
- `styles/site.css`
- `styles/mobile-fixes.css`
- `styles/wedding-likes.css`
- `login.html`
- `membros.html`

### Correção Necessária:

**ANTES (Incorreto):**
```css
backdrop-filter: blur(20px);
-webkit-backdrop-filter: blur(20px);
```

**DEPOIS (Correto):**
```css
-webkit-backdrop-filter: blur(20px);
backdrop-filter: blur(20px);
```

### Impacto:
- **Severidade:** Baixa
- **Browsers Afetados:** Safari, Safari iOS
- **Funcionalidade:** Glassmorphism pode não funcionar corretamente

---

## 2. 📝 ARQUIVOS FALTANDO

### 2.1 sitemap.xml

**Criar arquivo:** `sitemap.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://www.clarissacunha.com.br/</loc>
    <lastmod>2026-04-24</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://www.clarissacunha.com.br/sobre.html</loc>
    <lastmod>2026-04-24</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://www.clarissacunha.com.br/casamentos.html</loc>
    <lastmod>2026-04-24</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://www.clarissacunha.com.br/infantil.html</loc>
    <lastmod>2026-04-24</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://www.clarissacunha.com.br/assessoria-online.html</loc>
    <lastmod>2026-04-24</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://www.clarissacunha.com.br/revista.html</loc>
    <lastmod>2026-04-24</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://www.clarissacunha.com.br/blog.html</loc>
    <lastmod>2026-04-24</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://www.clarissacunha.com.br/midia.html</loc>
    <lastmod>2026-04-24</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://www.clarissacunha.com.br/orcamento.html</loc>
    <lastmod>2026-04-24</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>
```

### 2.2 robots.txt

**Criar arquivo:** `robots.txt`

```txt
User-agent: *
Allow: /

# Sitemap
Sitemap: https://www.clarissacunha.com.br/sitemap.xml

# Disallow admin areas
Disallow: /membros.html
Disallow: /login.html

# Disallow test files
Disallow: /test-
Disallow: /CHECKLIST
Disallow: /DIAGNOSTIC
Disallow: /*.md$
```

---

## 3. 📊 GOOGLE ANALYTICS

### Adicionar no `<head>` de todas as páginas:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

**Substituir:** `G-XXXXXXXXXX` pelo ID real do Google Analytics

---

## 4. 🖼️ OTIMIZAÇÃO DE IMAGENS

### Recomendações:

1. **Converter para WebP:**
```bash
# Instalar cwebp
brew install webp  # macOS
apt-get install webp  # Linux

# Converter imagens
cwebp -q 85 input.jpg -o output.webp
```

2. **Adicionar srcset:**
```html
<picture>
  <source srcset="image.webp" type="image/webp">
  <source srcset="image.jpg" type="image/jpeg">
  <img src="image.jpg" alt="Description" loading="lazy">
</picture>
```

3. **Criar versões @2x para retina:**
```
image.jpg      (1x - 800px)
image@2x.jpg   (2x - 1600px)
```

---

## 5. 🔒 SEGURANÇA

### 5.1 Adicionar Headers de Segurança

**Criar arquivo:** `.htaccess` (Apache) ou configurar no servidor

```apache
# Security Headers
Header set X-Content-Type-Options "nosniff"
Header set X-Frame-Options "SAMEORIGIN"
Header set X-XSS-Protection "1; mode=block"
Header set Referrer-Policy "strict-origin-when-cross-origin"

# Content Security Policy
Header set Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://www.youtube.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: https:; frame-src https://www.youtube.com;"

# HTTPS Redirect
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

### 5.2 Configurar HTTPS

- ✅ Obter certificado SSL (Let's Encrypt gratuito)
- ✅ Forçar HTTPS em todas as páginas
- ✅ Atualizar URLs absolutas para HTTPS

---

## 6. 🚀 PERFORMANCE

### 6.1 Minificar CSS e JS

**Ferramentas:**
- CSS: `cssnano` ou `clean-css`
- JS: `terser` ou `uglify-js`

```bash
# Instalar
npm install -g cssnano-cli terser

# Minificar CSS
cssnano styles/site.css styles/site.min.css

# Minificar JS
terser js/site.js -o js/site.min.js -c -m
```

### 6.2 Configurar Cache

**Adicionar no `.htaccess`:**

```apache
# Cache Control
<IfModule mod_expires.c>
  ExpiresActive On
  
  # Images
  ExpiresByType image/jpeg "access plus 1 year"
  ExpiresByType image/png "access plus 1 year"
  ExpiresByType image/webp "access plus 1 year"
  ExpiresByType image/svg+xml "access plus 1 year"
  
  # CSS and JavaScript
  ExpiresByType text/css "access plus 1 month"
  ExpiresByType application/javascript "access plus 1 month"
  
  # Fonts
  ExpiresByType font/woff2 "access plus 1 year"
  ExpiresByType font/woff "access plus 1 year"
  
  # HTML
  ExpiresByType text/html "access plus 0 seconds"
</IfModule>
```

---

## 7. 📱 TESTES FINAIS

### 7.1 Browsers para Testar:

- ✅ Chrome (Desktop + Mobile)
- ✅ Safari (Desktop + iOS)
- ✅ Firefox (Desktop + Mobile)
- ✅ Edge (Desktop)
- ✅ Samsung Internet (Mobile)

### 7.2 Dispositivos para Testar:

- ✅ iPhone (Safari iOS)
- ✅ Android (Chrome)
- ✅ iPad (Safari)
- ✅ Desktop (1920x1080)
- ✅ Laptop (1366x768)

### 7.3 Ferramentas de Teste:

1. **Google PageSpeed Insights**
   - https://pagespeed.web.dev/
   - Meta: Score > 90

2. **GTmetrix**
   - https://gtmetrix.com/
   - Meta: Grade A

3. **WebPageTest**
   - https://www.webpagetest.org/
   - Meta: First Contentful Paint < 1.5s

4. **Lighthouse (Chrome DevTools)**
   - Performance: > 90
   - Accessibility: > 95
   - Best Practices: > 90
   - SEO: > 90

---

## 8. ✅ CHECKLIST PRÉ-DEPLOY

### Crítico (Fazer Antes):
- [ ] Corrigir vendor prefixes (backdrop-filter)
- [ ] Criar sitemap.xml
- [ ] Criar robots.txt
- [ ] Adicionar Google Analytics
- [ ] Configurar HTTPS
- [ ] Testar em Safari iOS
- [ ] Testar formulário de orçamento
- [ ] Verificar todos os links
- [ ] Testar área de membros (login)

### Importante (Fazer Logo Após):
- [ ] Otimizar imagens para WebP
- [ ] Minificar CSS e JS
- [ ] Configurar cache headers
- [ ] Configurar CDN (Cloudflare)
- [ ] Monitorar Core Web Vitals
- [ ] Configurar backup automático

### Opcional (Melhorias Futuras):
- [ ] PWA (Service Worker)
- [ ] Dark mode
- [ ] Internacionalização
- [ ] Blog CMS integration
- [ ] A/B testing
- [ ] Heatmaps (Hotjar)

---

## 9. 🎯 COMANDOS ÚTEIS

### Testar Localmente:
```bash
# Iniciar servidor
python -m http.server 3000

# Acessar
http://localhost:3000
```

### Deploy (Exemplo com Netlify):
```bash
# Instalar Netlify CLI
npm install -g netlify-cli

# Login
netlify login

# Deploy
netlify deploy --prod
```

### Verificar Links Quebrados:
```bash
# Instalar
npm install -g broken-link-checker

# Verificar
blc http://localhost:3000 -ro
```

---

## 10. 📞 SUPORTE PÓS-DEPLOY

### Monitoramento:
1. **Google Search Console** - Indexação e erros
2. **Google Analytics** - Tráfego e conversões
3. **Uptime Robot** - Disponibilidade (gratuito)
4. **Sentry** - Erros JavaScript (opcional)

### Backup:
1. **Git** - Código versionado
2. **Servidor** - Backup diário automático
3. **Banco de dados** - Se houver (futuro)

---

## ✅ CONCLUSÃO

**Status Atual:** 95% Pronto

**Ações Necessárias:**
1. Corrigir vendor prefixes (15 minutos)
2. Criar sitemap.xml e robots.txt (10 minutos)
3. Adicionar Google Analytics (5 minutos)
4. Testar em Safari iOS (30 minutos)

**Tempo Total Estimado:** 1 hora

**Após essas correções:** ✅ **100% PRONTO PARA DEPLOY!**

---

**Última Atualização:** 24/04/2026  
**Próxima Revisão:** Após deploy inicial

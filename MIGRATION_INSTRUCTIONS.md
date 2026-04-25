# Instruções para Migração React + Vite 22.x

## 📋 Para a IA do VS Code

Você foi designada para completar a migração do site Clarissa Cunha Assessoria de Casamentos de HTML estático para React + Vite 22.x.

## 📚 Documentação Completa Disponível

**LEIA ESTES ARQUIVOS PRIMEIRO:**

1. **`.kiro/specs/react-vite-migration/requirements.md`**
   - 20 requisitos completos da migração
   - User stories e acceptance criteria
   - Todos os requisitos técnicos e funcionais

2. **`.kiro/specs/react-vite-migration/design.md`**
   - Arquitetura técnica completa
   - Estrutura de componentes React
   - Implementação de hooks customizados
   - Data models e interfaces
   - Diagramas de arquitetura

3. **`.kiro/specs/react-vite-migration/tasks.md`**
   - 20 tarefas organizadas sequencialmente
   - Cada task com sub-tarefas detalhadas
   - Referências aos requirements
   - Checkpoints de validação

## 🎯 Seu Objetivo

Implementar **TODAS as 20 tasks** do arquivo `tasks.md` para criar uma aplicação React completa que substitui o site HTML atual.

## 📁 Arquivos do Site Atual para Referência

**HTML Pages:**
- `index.html` - Homepage
- `casamentos.html` - Portfólio de casamentos
- `infantil.html` - Portfólio infantil
- `ensaios.html` - Ensaios fotográficos
- `sobre.html` - Sobre a empresa
- `revista.html` - Revista digital
- `blog.html` - Blog
- `midia.html` - Mídia e imprensa
- `orcamento.html` - Formulário de orçamento
- `contato.html` - Formulário de contato
- `assessoria-online.html` - Serviço online
- `monte-sua-festa.html` - Planejador de festas

**Assets:**
- `/assets/` - TODAS as imagens (preservar estrutura)
  - `/assets/brand/` - Logo e marca
  - `/assets/casamentos/` - Fotos de casamentos
  - `/assets/infantil/` - Fotos de festas infantis
  - `/assets/ensaios/` - Fotos de ensaios

**Styles:**
- `styles/tokens.css` - Design tokens (cores, espaçamentos, fontes)
- `styles/site.css` - Estilos globais e base
- `styles/mobile-fixes.css` - Otimizações mobile

**JavaScript:**
- `js/site.js` - Lógica atual (header, menu, cursor, animações)

## 🚀 Fluxo de Implementação

### FASE 1: Setup (Tasks 1-3)
1. Criar projeto Vite em pasta separada `react-app/`
2. Copiar assets e estilos
3. Criar constantes e data models

### FASE 2: Foundation (Tasks 4-6)
4. Implementar custom hooks (useScrollReveal, useParallax, useScrollState)
5. Criar shared components (CustomCursor, WhatsAppFloat, SEO, Button)
6. Criar layout components (Header, Footer, MobileMenu, Layout)

### FASE 3: Main Pages (Tasks 7-14)
7. Checkpoint - Validar layout
8. Criar seções da HomePage
9. Montar HomePage completa
10. Criar seções da CasamentosPage
11. Montar CasamentosPage completa
12. Criar seções da InfantilPage
13. Montar InfantilPage completa
14. Checkpoint - Validar páginas principais

### FASE 4: Completion (Tasks 15-20)
15. Criar páginas restantes (9 páginas + 404)
16. Configurar React Router com todas as rotas
17. Implementar features de acessibilidade
18. Otimizar performance (code splitting, lazy loading)
19. Configurar build e deployment
20. Checkpoint final - Testes completos

## 📝 Estrutura do Projeto React

```
react-app/
├── public/
│   ├── assets/              # Copiar de /assets/
│   │   ├── brand/
│   │   ├── casamentos/
│   │   ├── infantil/
│   │   └── ensaios/
│   └── _redirects           # Para client-side routing
├── src/
│   ├── components/
│   │   ├── layout/
│   │   │   ├── Header.jsx
│   │   │   ├── Footer.jsx
│   │   │   ├── MobileMenu.jsx
│   │   │   └── Layout.jsx
│   │   ├── shared/
│   │   │   ├── CustomCursor.jsx
│   │   │   ├── WhatsAppFloat.jsx
│   │   │   ├── SEO.jsx
│   │   │   └── Button.jsx
│   │   ├── home/
│   │   │   ├── Hero.jsx
│   │   │   ├── Manifesto.jsx
│   │   │   ├── Portfolio.jsx
│   │   │   ├── Services.jsx
│   │   │   ├── Testimonials.jsx
│   │   │   ├── Revista.jsx
│   │   │   ├── PressStrip.jsx
│   │   │   └── CTA.jsx
│   │   ├── casamentos/
│   │   │   ├── PageHero.jsx
│   │   │   ├── FilterBar.jsx
│   │   │   ├── FeaturedWedding.jsx
│   │   │   ├── PortfolioGrid.jsx
│   │   │   ├── DestinationWeddings.jsx
│   │   │   └── ThumbnailsStrip.jsx
│   │   └── infantil/
│   │       ├── StatsRow.jsx
│   │       ├── MagazineGrid.jsx
│   │       ├── Abordagem.jsx
│   │       └── TiposCelebracao.jsx
│   ├── pages/
│   │   ├── HomePage.jsx
│   │   ├── CasamentosPage.jsx
│   │   ├── InfantilPage.jsx
│   │   ├── EnsaiosPage.jsx
│   │   ├── SobrePage.jsx
│   │   ├── RevistaPage.jsx
│   │   ├── BlogPage.jsx
│   │   ├── MidiaPage.jsx
│   │   ├── OrcamentoPage.jsx
│   │   ├── ContatoPage.jsx
│   │   ├── AssessoriaOnlinePage.jsx
│   │   ├── MonteSuaFestaPage.jsx
│   │   └── NotFoundPage.jsx
│   ├── hooks/
│   │   ├── useScrollReveal.js
│   │   ├── useParallax.js
│   │   └── useScrollState.js
│   ├── utils/
│   │   └── constants.js
│   ├── styles/
│   │   ├── tokens.css
│   │   ├── site.css
│   │   └── mobile-fixes.css
│   ├── App.jsx
│   └── main.jsx
├── index.html
├── vite.config.js
├── package.json
└── README.md
```

## ⚙️ Comandos Iniciais

```bash
# 1. Criar projeto Vite
npm create vite@latest react-app -- --template react

# 2. Entrar na pasta
cd react-app

# 3. Instalar dependências
npm install

# 4. Instalar bibliotecas adicionais
npm install react-router-dom react-helmet-async

# 5. Iniciar dev server
npm run dev

# 6. Build para produção
npm run build

# 7. Preview do build
npm run preview
```

## 🎨 Pontos Críticos - NÃO ESQUECER

### 1. Assets
- ✅ Copiar TODA a pasta `/assets/` para `react-app/public/assets/`
- ✅ Usar caminhos absolutos: `/assets/...` (NÃO usar import)
- ✅ Preservar estrutura de pastas exata

### 2. Estilos CSS
- ✅ Copiar os 3 arquivos CSS para `src/styles/`
- ✅ Importar em `main.jsx` na ordem: tokens → site → mobile-fixes
- ✅ Preservar TODOS os estilos (glassmorphism, animações)
- ✅ Manter custom properties CSS (--cc-teal, --cc-cream, etc)

### 3. Design Premium
- ✅ Glassmorphism: `backdrop-filter: blur(20px)`
- ✅ Animações suaves: `cubic-bezier(0.22, 1, 0.36, 1)`
- ✅ Cursor customizado (desktop only)
- ✅ Parallax effects (desktop only)
- ✅ Scroll reveal animations (Intersection Observer)

### 4. Mobile Optimizations
- ✅ Touch targets mínimo 44x44px
- ✅ Menu fullscreen mobile
- ✅ Safe area insets (notch devices)
- ✅ Responsive breakpoints: 600px, 900px, 1000px, 1100px
- ✅ Typography com clamp()

### 5. Performance
- ✅ Code splitting: `React.lazy()` para páginas
- ✅ Lazy loading: `loading="lazy"` em imagens
- ✅ Passive scroll listeners: `{ passive: true }`
- ✅ GPU acceleration: `transform` e `opacity`
- ✅ Bundle < 500KB gzipped

### 6. Acessibilidade
- ✅ Skip link para conteúdo principal
- ✅ Alt text em todas as imagens
- ✅ Labels em inputs de formulário
- ✅ Focus states visíveis (3px outline)
- ✅ Hierarquia semântica (h1, h2, h3)
- ✅ Aria-labels em navegação e botões
- ✅ Contraste WCAG AA (4.5:1)

### 7. SEO
- ✅ react-helmet-async para meta tags
- ✅ Title e description únicos por página
- ✅ Open Graph tags
- ✅ Twitter Card tags
- ✅ Canonical URLs
- ✅ lang="pt-BR"

### 8. React Router
- ✅ BrowserRouter (não HashRouter)
- ✅ Scroll to top on route change
- ✅ 404 catch-all route
- ✅ Active link highlighting
- ✅ Client-side routing com `_redirects`

### 9. Build & Deploy
- ✅ Criar `public/_redirects` com: `/* /index.html 200`
- ✅ Testar `npm run build`
- ✅ Testar `npm run preview`
- ✅ Verificar dist/ contém todos os assets
- ✅ Documentar deployment no README

## 📊 Data Models Importantes

### Navigation Items
```javascript
export const NAV_ITEMS = [
  { id: 'index', href: '/', label: 'Início', num: '01' },
  { id: 'casamentos', href: '/casamentos', label: 'Casamentos', num: '02' },
  { id: 'infantil', href: '/infantil', label: 'Infantil', num: '03' },
  { id: 'ensaios', href: '/ensaios', label: 'Ensaios', num: '04' },
  { id: 'sobre', href: '/sobre', label: 'Sobre', num: '05' },
  { id: 'revista', href: '/revista', label: 'Revista', num: '06' },
  { id: 'blog', href: '/blog', label: 'Blog', num: '07' },
  { id: 'midia', href: '/midia', label: 'Mídia', num: '08' },
  { id: 'contato', href: '/contato', label: 'Contato', num: '09' }
];
```

### WhatsApp Contact
```javascript
const WHATSAPP_NUMBER = '+5581996613555';
const WHATSAPP_MESSAGE = 'Olá! Gostaria de saber mais sobre os serviços.';
```

## 🔍 Referências de Implementação

### Custom Hooks - Exemplos

**useScrollReveal.js:**
```javascript
import { useEffect, useRef } from 'react';

export function useScrollReveal(options = {}) {
  const ref = useRef(null);
  
  useEffect(() => {
    const element = ref.current;
    if (!element || !('IntersectionObserver' in window)) {
      element?.classList.add('is-visible');
      return;
    }
    
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      },
      { rootMargin: '0px 0px -10% 0px', threshold: 0.08, ...options }
    );
    
    observer.observe(element);
    return () => observer.disconnect();
  }, []);
  
  return ref;
}
```

**useScrollState.js:**
```javascript
import { useState, useEffect } from 'react';

export function useScrollState(threshold = 40) {
  const [state, setState] = useState({ isScrolled: false, scrollY: 0 });
  
  useEffect(() => {
    const handleScroll = () => {
      const scrollY = window.scrollY;
      setState({ isScrolled: scrollY > threshold, scrollY });
    };
    
    handleScroll();
    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, [threshold]);
  
  return state;
}
```

### App.jsx - Estrutura Base

```javascript
import { BrowserRouter, Routes, Route, useLocation } from 'react-router-dom';
import { HelmetProvider } from 'react-helmet-async';
import { useEffect } from 'react';
import Layout from './components/layout/Layout';
import HomePage from './pages/HomePage';
import CasamentosPage from './pages/CasamentosPage';
import InfantilPage from './pages/InfantilPage';
// ... importar todas as páginas

function ScrollToTop() {
  const { pathname } = useLocation();
  
  useEffect(() => {
    window.scrollTo(0, 0);
  }, [pathname]);
  
  return null;
}

function App() {
  return (
    <HelmetProvider>
      <BrowserRouter>
        <ScrollToTop />
        <Layout>
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/casamentos" element={<CasamentosPage />} />
            <Route path="/infantil" element={<InfantilPage />} />
            <Route path="/ensaios" element={<EnsaiosPage />} />
            <Route path="/sobre" element={<SobrePage />} />
            <Route path="/revista" element={<RevistaPage />} />
            <Route path="/blog" element={<BlogPage />} />
            <Route path="/midia" element={<MidiaPage />} />
            <Route path="/orcamento" element={<OrcamentoPage />} />
            <Route path="/contato" element={<ContatoPage />} />
            <Route path="/assessoria-online" element={<AssessoriaOnlinePage />} />
            <Route path="/monte-sua-festa" element={<MonteSuaFestaPage />} />
            <Route path="*" element={<NotFoundPage />} />
          </Routes>
        </Layout>
      </BrowserRouter>
    </HelmetProvider>
  );
}

export default App;
```

## ✅ Checklist de Validação

Ao completar a implementação, verifique:

- [ ] Projeto Vite criado e rodando (`npm run dev`)
- [ ] Todos os assets copiados para `public/assets/`
- [ ] Todos os estilos CSS importados e funcionando
- [ ] 3 custom hooks implementados
- [ ] 4 shared components criados
- [ ] 4 layout components criados
- [ ] HomePage completa com 8 seções
- [ ] CasamentosPage completa com filtros
- [ ] InfantilPage completa
- [ ] 9 páginas restantes + 404 criadas
- [ ] React Router configurado com todas as rotas
- [ ] Navegação funcionando sem reload
- [ ] Scroll to top em mudança de rota
- [ ] Active link highlighting no header
- [ ] Menu mobile funcionando
- [ ] Cursor customizado (desktop)
- [ ] WhatsApp button funcionando
- [ ] Scroll reveal animations funcionando
- [ ] Parallax effects funcionando (desktop)
- [ ] Glassmorphism preservado
- [ ] Mobile responsive
- [ ] Formulários com validação
- [ ] SEO meta tags em todas as páginas
- [ ] Acessibilidade (skip link, aria-labels, alt text)
- [ ] Build de produção funcionando (`npm run build`)
- [ ] Preview funcionando (`npm run preview`)
- [ ] `_redirects` criado para client-side routing
- [ ] README.md documentado

## 🎯 Resultado Final Esperado

Ao final da implementação, você terá:

✅ **Aplicação React completa** em `/react-app/`  
✅ **Todas as 12 páginas** funcionando  
✅ **Navegação client-side** com React Router  
✅ **Design premium preservado** (glassmorphism, animações suaves)  
✅ **Mobile-first** e totalmente responsivo  
✅ **Performance otimizada** (code splitting, lazy loading)  
✅ **Acessível** (WCAG AA compliance)  
✅ **SEO-friendly** (meta tags dinâmicas)  
✅ **Build pronto** para deploy na Hostinger  

## 📞 Informações de Contato

- **WhatsApp**: +5581996613555
- **Site**: clarissacunha.com.br

## 🚀 Começar Agora

1. Leia os 3 arquivos de spec (requirements, design, tasks)
2. Execute os comandos iniciais para criar o projeto
3. Siga as tasks sequencialmente (1 → 20)
4. Valide nos checkpoints (tasks 7, 14, 20)
5. Teste o build final

**BOA SORTE! 🎉**

# Clarissa Cunha · Design System

## Theme

Light mode sempre. Cena física: noiva rolando o feed de manhã ao lado do café, luz natural entrando pela janela, ou à noite no sofá procurando assessora depois do pedido. Ambos momentos pedem atmosfera quente, papel, fotografia que brilha. Dark mode contradiz a marca (casamento é LUZ).

## Color Strategy

**Committed** — teal #6BA6A1 carrega a identidade (~35% da superfície via acentos, detalhes, ornamentos, tipografia italic); cremes tintados são a base; lavanda é secundária de emoção (italic em h1 em, eyebrows). Nunca #fff nem #000 puros.

### Tokens (com equivalentes OKLCH implícitos — hex mantido por compatibilidade com CSS atual)

```
--cc-teal:         #6BA6A1  /* oklch(70% 0.05 185) */
--cc-teal-deep:    #3E6F6B  /* oklch(50% 0.04 185) */
--cc-lavender:     #9E85B8  /* oklch(62% 0.07 295) */
--cc-lavender-deep:#6B4F8A  /* oklch(45% 0.10 290) */
--cc-lavender-soft:#C5B3D8

--cc-cream:        #FBF7F1  /* tinted paper, NOT white */
--cc-cream-warm:   #F5EFE4
--cc-paper:        #EFE8DA

--cc-ink:          #2A2F3A  /* tinted toward brand, NOT #000 */
--cc-ink-soft:     #52566A
--cc-ink-muted:    #8088A0
--cc-line:         rgba(42,47,58,0.08)
```

## Typography

- **Display**: Cormorant Garamond (300/400/500 + italics) — h1, h2, blockquotes, depoimentos, nomes. Light italic é a voz da marca.
- **Sans**: Jost (300/400/500/600) — body, labels, UI.
- **Script**: Allura — uso RARÍSSIMO. Apenas assinatura manuscrita (Clarissa Cunha). Nunca em botões.
- **Mono**: JetBrains Mono — números de seção, eyebrows técnicos, meta.

### Scale (fluid)

```
h1:    clamp(36px, 4.5vw, 64px)  line-height 0.95 letter-spacing -0.025em
h2:    clamp(26px, 2.5vw, 40px)  line-height 1.00
h3:    clamp(24px, 2.2vw, 34px)
lede:  clamp(16px, 1.2vw, 20px)  italic display
body:  15-16px  line-height 1.55-1.6
eyebrow: 10-11px  uppercase  letter-spacing 0.28-0.32em
```

Ratio ≥1.25 garantido entre passos. Body line-length travado em ~65ch nos parágrafos longos.

## Spacing & Rhythm

Varia por seção — ritmo sobre monotonia:
- Hero: padding 130px top, 80px bottom
- Seções internas: var(--sp-10) / --sp-11 (80-120px)
- Cards: padding assimétrico (40px 32px 36px vs 36px 32px 40px)
- Grid portfolio: gap 20px desktop, 14px mobile
- Grid services: gap 20px (era 2px "divider" — corrigido para floating cards)

## Elevation

3 níveis, todos tintados em direção ao ink da marca (não cinza genérico):
- Soft: `0 2px 10px -4px rgba(42,47,58,0.08)` — cards em repouso
- Card: `0 20px 40px -16px rgba(42,47,58,0.18)` — hover
- Float: `0 30px 60px -20px rgba(42,47,58,0.35)` — destaques

## Borders

Asymmetric radii como assinatura da marca:
- `4px 32px 4px 32px` e `32px 4px 32px 4px` alternados
- Invertem no hover (transição 600-700ms var(--ease-out))
- Nunca border-radius uniforme redondo em cards principais
- Border-width máxima 1px, cor `rgba(42,47,58,0.04-0.08)`

## Motion

- Ease base: `cubic-bezier(0.16, 1, 0.3, 1)` (ease-out-quart)
- Spring leve (só em arrows/pequenos): `cubic-bezier(0.34, 1.56, 0.64, 1)`
- Durações: micro 250-400ms, component 500-700ms, section reveal 900ms
- Reveal: IntersectionObserver, translateY(40px) + opacity
- Scroll-video: 64 frames cover mode, caption com glassmorphism (uso justificado — flutua sobre foto escura)
- Marquee: 40s linear infinite

## Components

### Cards
- Portfolio: grid editorial 12 colunas, 6 placements com tamanhos distintos, asymmetric radii inversíveis
- Serviços: floating cards com barra gradient (teal→lavender) no hover + blob radial, radii distintos por filho
- Depoimentos: 3 cards com card do meio deslocado +20px, backgrounds alternados (paper / cream-warm)

### Buttons
- Primary: ink background, cream text, hover sobe 2px + shadow
- Ghost: transparent, 1px teal border, hover vira ink
- Nenhum button em gradient, nenhum em script font

### Hero
- Grid 1.1fr 1fr assimétrico
- Media com radius `4px 80px 4px 80px` (mais dramático que cards)
- Accent rotacionado 2deg, radius invertido, hover volta ao 0
- Selo circular animado (float 6s), italic, off-grid à esquerda

## Accessibility

- Contraste AAA no ink sobre cream
- Skip-link no topo
- `prefers-reduced-motion` respeitado em stamp flutuante, scroll-video e reveals
- Focus-visible com outline teal

## Responsive

- Desktop ≥1200: grid completo
- Tablet 1001-1200: gaps reduzidos, hero stamp reposicionado
- Tablet 768-1000: grid hero vira 1 coluna, services 2 colunas
- Mobile ≤600: services 1 coluna, padding reduzido, scroll-video caption em full-width bottom

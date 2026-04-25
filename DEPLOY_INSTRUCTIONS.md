# 🚀 INSTRUÇÕES DE DEPLOY - Site Clarissa Cunha

## ✅ DECISÃO: Deploy do HTML Atual

Você decidiu fazer deploy do site HTML que já está funcionando perfeitamente. **Excelente escolha!**

A pasta `react-app/` ficará guardada para o futuro, quando houver necessidade real de migração.

---

## 📦 ARQUIVOS PARA FAZER UPLOAD NA HOSTINGER

### ✅ Arquivos HTML (raiz do projeto):
```
index.html
casamentos.html
infantil.html
sobre.html
revista.html
blog.html
midia.html
orcamento.html
assessoria-online.html
monte-sua-festa.html
casamento-castelinho.html (se existir)
```

### ✅ Pastas completas:
```
/assets/          (TODA a pasta - imagens, logos, fotos)
/styles/          (TODA a pasta - CSS)
/js/              (TODA a pasta - JavaScript)
/casamentos/      (TODA a pasta - páginas internas)
/infantil/        (TODA a pasta - páginas internas)
```

### ❌ NÃO fazer upload:
```
/react-app/       (deixar para o futuro)
/.kiro/           (arquivos de desenvolvimento)
/.vscode/         (configurações do editor)
/.git/            (controle de versão)
/node_modules/    (se existir)
*.md              (documentação)
*.py              (scripts)
```

---

## 🌐 PASSO A PASSO - HOSTINGER

### 1️⃣ Preparar Arquivos

**No seu computador:**

1. Crie uma pasta chamada `site-para-upload`
2. Copie para dentro dela:
   - Todos os arquivos `.html` da raiz
   - A pasta `/assets/` completa
   - A pasta `/styles/` completa
   - A pasta `/js/` completa
   - A pasta `/casamentos/` completa
   - A pasta `/infantil/` completa

3. Compacte tudo em um arquivo `.zip`:
   - Selecione TUDO dentro de `site-para-upload`
   - Clique com botão direito > "Enviar para" > "Pasta compactada"
   - Nomeie: `clarissa-cunha-site.zip`

---

### 2️⃣ Acessar Hostinger

1. Entre em: **https://hpanel.hostinger.com**
2. Faça login com suas credenciais
3. Selecione seu domínio/hospedagem

---

### 3️⃣ Gerenciador de Arquivos

1. No painel, clique em **"Gerenciador de Arquivos"** ou **"File Manager"**
2. Navegue até a pasta **`public_html/`** (ou `www/`)
3. **IMPORTANTE:** Se houver arquivos de exemplo, delete-os:
   - Selecione todos
   - Clique em "Delete" ou "Excluir"
   - Confirme

---

### 4️⃣ Upload do Site

**Opção A - Upload do ZIP (Mais Rápido):**

1. Clique em **"Upload"** ou **"Enviar"**
2. Selecione o arquivo `clarissa-cunha-site.zip`
3. Aguarde o upload completar (pode demorar alguns minutos)
4. Após upload, clique com botão direito no arquivo `.zip`
5. Selecione **"Extract"** ou **"Extrair"**
6. Confirme a extração
7. Delete o arquivo `.zip` após extrair

**Opção B - Upload Manual (Mais Lento):**

1. Clique em **"Upload"**
2. Selecione todos os arquivos `.html`
3. Aguarde upload
4. Repita para cada pasta (assets, styles, js, casamentos, infantil)

---

### 5️⃣ Verificar Estrutura

Após upload, a estrutura em `public_html/` deve estar assim:

```
public_html/
├── index.html
├── casamentos.html
├── infantil.html
├── sobre.html
├── revista.html
├── blog.html
├── midia.html
├── orcamento.html
├── assessoria-online.html
├── monte-sua-festa.html
├── assets/
│   ├── brand/
│   │   └── logo.png
│   ├── casamentos/
│   ├── infantil/
│   ├── home/
│   └── ...
├── styles/
│   ├── tokens.css
│   ├── site.css
│   ├── mobile-fixes.css
│   └── page.css
├── js/
│   └── site.js
├── casamentos/
│   ├── casamento-na-praia.html
│   ├── casamento-pe-na-areia.html
│   └── ...
└── infantil/
    ├── aeroporto.html
    ├── grand-prix-gael.html
    └── ...
```

---

### 6️⃣ Testar o Site

1. **Abra seu domínio no navegador:**
   - `https://seudominio.com` ou `https://seudominio.com.br`

2. **Teste todas as páginas:**
   - ✅ Homepage
   - ✅ Casamentos
   - ✅ Infantil
   - ✅ Sobre
   - ✅ Revista
   - ✅ Blog
   - ✅ Mídia
   - ✅ Orçamento
   - ✅ Contato
   - ✅ Assessoria Online
   - ✅ Monte Sua Festa

3. **Teste funcionalidades:**
   - ✅ Menu de navegação
   - ✅ Menu mobile (burger)
   - ✅ Links internos
   - ✅ Imagens carregam
   - ✅ Logo aparece
   - ✅ Botão WhatsApp funciona
   - ✅ Formulários funcionam
   - ✅ Animações funcionam
   - ✅ Cursor customizado (desktop)

4. **Teste no mobile:**
   - Abra no celular
   - Teste menu mobile
   - Teste responsividade
   - Teste touch targets

---

## 🔒 CONFIGURAR SSL (HTTPS)

**Importante para segurança e SEO!**

1. No painel Hostinger, vá em **"SSL"**
2. Clique em **"Instalar SSL"** ou **"Ativar SSL"**
3. Selecione **"Let's Encrypt"** (gratuito)
4. Clique em **"Instalar"**
5. Aguarde 5-10 minutos para ativar
6. Teste: `https://seudominio.com`

---

## 🎨 CONFIGURAÇÕES OPCIONAIS

### URLs Amigáveis (Remover .html)

Se quiser URLs sem `.html`:
- `seudominio.com/casamentos` em vez de `seudominio.com/casamentos.html`

**Como fazer:**

1. No Gerenciador de Arquivos, crie um arquivo chamado `.htaccess`
2. Adicione este conteúdo:

```apache
# Remover .html das URLs
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^([^\.]+)$ $1.html [NC,L]

# Forçar HTTPS
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

# Redirecionar www para não-www
RewriteCond %{HTTP_HOST} ^www\.(.*)$ [NC]
RewriteRule ^(.*)$ https://%1/$1 [R=301,L]
```

3. Salve o arquivo na raiz de `public_html/`

---

## ✅ CHECKLIST PÓS-DEPLOY

Após fazer o deploy, verifique:

### Funcionalidades:
- [ ] Homepage carrega
- [ ] Todas as páginas acessíveis
- [ ] Menu funciona
- [ ] Menu mobile funciona
- [ ] Links funcionam
- [ ] Imagens carregam
- [ ] Logo aparece
- [ ] WhatsApp funciona
- [ ] Formulários funcionam
- [ ] Animações funcionam

### Design:
- [ ] Cores corretas
- [ ] Fontes corretas
- [ ] Glassmorphism effects
- [ ] Animações suaves

### Mobile:
- [ ] Responsivo
- [ ] Menu mobile
- [ ] Touch targets
- [ ] Performance

### SEO:
- [ ] Título correto
- [ ] Meta description
- [ ] SSL ativo (HTTPS)
- [ ] Favicon

---

## 🐛 PROBLEMAS COMUNS

### Imagens não carregam
**Solução:**
- Verifique se `/assets/` foi enviada completamente
- Limpe cache: Ctrl+F5
- Verifique permissões: 755

### CSS não aplica
**Solução:**
- Verifique se `/styles/` foi enviada
- Limpe cache: Ctrl+F5
- Verifique links no HTML

### Links quebrados
**Solução:**
- Verifique se todos `.html` foram enviados
- Use caminhos relativos

### Site não abre
**Solução:**
- Verifique se `index.html` está na raiz
- Aguarde propagação DNS (até 24h)
- Verifique apontamento do domínio

---

## 📞 SUPORTE

**Hostinger:**
- Chat: https://www.hostinger.com.br/
- Email: suporte@hostinger.com.br

---

## 🎉 PRONTO!

Após seguir este guia:
- ✅ Site no ar
- ✅ Funcionando 100%
- ✅ Profissional
- ✅ Rápido
- ✅ Responsivo
- ✅ Sem bugs

**Parabéns! Seu site está online! 🎊**

---

## 📂 SOBRE A PASTA REACT

A pasta `react-app/` ficará no seu computador para o futuro.

**Quando migrar para React?**
- Quando houver necessidade real (formulários complexos, área de cliente, etc)
- Quando houver orçamento para desenvolvedor React experiente
- Quando houver tempo para fazer corretamente

**Por enquanto:**
- Site HTML funciona perfeitamente
- Fácil de manter
- Fácil de atualizar
- Performance excelente

---

## ⏱️ TEMPO ESTIMADO

- Preparar arquivos: **5 minutos**
- Upload: **10-20 minutos**
- Configurar SSL: **5 minutos**
- Testar: **10 minutos**

**TOTAL: 30-40 minutos**

---

## 💡 DICA FINAL

**Mantenha simples!**

O site HTML é:
- ✅ Profissional
- ✅ Rápido
- ✅ Fácil de manter
- ✅ Perfeito para seu negócio

**Foque no que importa: seus clientes! 🎊**

# 🚀 Guia de Deploy - Site HTML na Hostinger

## ✅ SITUAÇÃO ATUAL

Você tem um site HTML **PERFEITO E FUNCIONANDO** que precisa ir para produção.

**Não use o React bugado. Use o HTML que já funciona!**

---

## 📦 ARQUIVOS PARA FAZER UPLOAD

### Arquivos na raiz:
```
✅ index.html
✅ casamentos.html
✅ infantil.html
✅ ensaios.html (se existir)
✅ sobre.html
✅ revista.html
✅ blog.html
✅ midia.html
✅ orcamento.html
✅ contato.html (se existir)
✅ assessoria-online.html
✅ monte-sua-festa.html
✅ casamento-castelinho.html (se existir)
```

### Pastas completas:
```
✅ /assets/          (TODA a pasta com subpastas)
✅ /styles/          (TODA a pasta)
✅ /js/              (TODA a pasta)
✅ /casamentos/      (TODA a pasta)
✅ /infantil/        (TODA a pasta)
```

### NÃO fazer upload:
```
❌ /react-app/       (ignorar completamente)
❌ /node_modules/    (se existir)
❌ /.git/            (se existir)
❌ /.kiro/           (arquivos de desenvolvimento)
❌ /.vscode/         (configurações do editor)
❌ MIGRATION_*.md    (documentação)
❌ *.py              (scripts Python)
```

---

## 🌐 PASSO A PASSO - DEPLOY NA HOSTINGER

### Método 1: Via Painel Hostinger (Mais Fácil)

#### 1. Acessar Painel
1. Entre em: https://hpanel.hostinger.com
2. Faça login com suas credenciais
3. Selecione seu domínio/hospedagem

#### 2. Acessar Gerenciador de Arquivos
1. No painel, clique em "Gerenciador de Arquivos"
2. Navegue até a pasta `public_html/` (ou `www/`)
3. **IMPORTANTE:** Limpe a pasta (delete arquivos de exemplo)

#### 3. Upload dos Arquivos
1. Clique em "Upload" ou "Enviar Arquivos"
2. Selecione TODOS os arquivos HTML da raiz
3. Aguarde o upload completar
4. Repita para cada pasta (assets, styles, js, casamentos, infantil)

**OU** (mais rápido):

1. Compacte tudo em um arquivo .zip no seu computador:
   ```
   - Selecione todos os arquivos e pastas necessários
   - Clique com botão direito > "Enviar para" > "Pasta compactada"
   - Nomeie: site-clarissa-cunha.zip
   ```

2. No Gerenciador de Arquivos da Hostinger:
   - Clique em "Upload"
   - Envie o arquivo .zip
   - Clique com botão direito no .zip > "Extrair"
   - Delete o arquivo .zip após extrair

#### 4. Verificar Estrutura
Após upload, a estrutura deve estar assim:
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
│   ├── casamentos/
│   ├── infantil/
│   └── ...
├── styles/
│   ├── tokens.css
│   ├── site.css
│   └── mobile-fixes.css
├── js/
│   └── site.js
├── casamentos/
│   ├── casamento-na-praia.html
│   └── ...
└── infantil/
    ├── aeroporto.html
    └── ...
```

#### 5. Testar
1. Abra seu domínio no navegador
2. Teste TODAS as páginas:
   - Homepage: `seudominio.com`
   - Casamentos: `seudominio.com/casamentos.html`
   - Infantil: `seudominio.com/infantil.html`
   - Etc.

3. Teste no mobile (abra no celular)

4. Teste navegação:
   - Clique em todos os links do menu
   - Teste menu mobile (burger)
   - Teste formulários
   - Teste WhatsApp button

---

### Método 2: Via FTP (Para Usuários Avançados)

#### 1. Obter Credenciais FTP
1. No painel Hostinger, vá em "FTP"
2. Anote:
   - Host/Servidor: `ftp.seudominio.com`
   - Usuário: `seu-usuario`
   - Senha: `sua-senha`
   - Porta: `21`

#### 2. Instalar Cliente FTP
- **Windows:** FileZilla (https://filezilla-project.org/)
- **Mac:** Cyberduck (https://cyberduck.io/)

#### 3. Conectar via FTP
1. Abra o FileZilla
2. Preencha:
   - Host: `ftp.seudominio.com`
   - Usuário: (do passo 1)
   - Senha: (do passo 1)
   - Porta: `21`
3. Clique em "Conexão Rápida"

#### 4. Upload
1. No painel esquerdo (seu computador):
   - Navegue até a pasta do projeto
2. No painel direito (servidor):
   - Navegue até `public_html/`
3. Arraste e solte:
   - Todos os arquivos .html
   - Todas as pastas (assets, styles, js, casamentos, infantil)
4. Aguarde o upload completar

#### 5. Verificar e Testar
- Mesmos passos do Método 1, item 4 e 5

---

## 🔧 CONFIGURAÇÕES ADICIONAIS (Opcional)

### URLs Amigáveis (Remover .html)

Se quiser URLs sem .html (ex: `seudominio.com/casamentos` em vez de `seudominio.com/casamentos.html`):

1. Crie arquivo `.htaccess` na raiz do site
2. Adicione este conteúdo:

```apache
# Remover .html das URLs
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^([^\.]+)$ $1.html [NC,L]

# Redirecionar www para não-www (ou vice-versa)
RewriteCond %{HTTP_HOST} ^www\.(.*)$ [NC]
RewriteRule ^(.*)$ https://%1/$1 [R=301,L]

# Forçar HTTPS
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

3. Salve e faça upload do `.htaccess`

### Certificado SSL (HTTPS)

1. No painel Hostinger, vá em "SSL"
2. Ative o certificado SSL gratuito (Let's Encrypt)
3. Aguarde 5-10 minutos para ativar
4. Teste: `https://seudominio.com`

---

## ✅ CHECKLIST PÓS-DEPLOY

Após fazer o deploy, verifique:

### Funcionalidades:
- [ ] Homepage carrega corretamente
- [ ] Todas as páginas acessíveis
- [ ] Menu de navegação funciona
- [ ] Menu mobile funciona (burger)
- [ ] Links internos funcionam
- [ ] Links externos funcionam
- [ ] Imagens carregam
- [ ] Logo aparece
- [ ] Botão WhatsApp funciona
- [ ] Formulários funcionam
- [ ] Animações funcionam
- [ ] Cursor customizado funciona (desktop)

### Design:
- [ ] Cores corretas
- [ ] Fontes corretas
- [ ] Espaçamentos corretos
- [ ] Glassmorphism effects funcionando
- [ ] Animações suaves

### Mobile:
- [ ] Site responsivo
- [ ] Menu mobile funciona
- [ ] Touch targets adequados
- [ ] Imagens carregam
- [ ] Performance boa

### SEO:
- [ ] Título da página correto
- [ ] Meta description presente
- [ ] Open Graph tags
- [ ] Favicon aparece

### Performance:
- [ ] Site carrega rápido (< 3 segundos)
- [ ] Imagens otimizadas
- [ ] CSS e JS carregam

---

## 🐛 TROUBLESHOOTING

### Problema: Imagens não carregam
**Solução:**
- Verifique se a pasta `/assets/` foi enviada completamente
- Verifique se os caminhos no HTML estão corretos
- Verifique permissões da pasta (755)

### Problema: CSS não aplica
**Solução:**
- Verifique se a pasta `/styles/` foi enviada
- Limpe cache do navegador (Ctrl+F5)
- Verifique se os links no HTML estão corretos

### Problema: Links quebrados
**Solução:**
- Verifique se todos os arquivos .html foram enviados
- Verifique se os caminhos estão corretos
- Use caminhos relativos (ex: `casamentos.html` não `/casamentos.html`)

### Problema: Site não abre
**Solução:**
- Verifique se o arquivo `index.html` está na raiz de `public_html/`
- Verifique se o domínio está apontando corretamente
- Aguarde propagação DNS (até 24h)

---

## 📞 SUPORTE HOSTINGER

Se tiver problemas:
1. Chat ao vivo: https://www.hostinger.com.br/
2. Email: suporte@hostinger.com.br
3. Telefone: Verifique no painel

---

## 🎉 PRONTO!

Após seguir este guia, seu site estará:
- ✅ No ar
- ✅ Funcionando 100%
- ✅ Profissional
- ✅ Rápido
- ✅ Responsivo
- ✅ Sem bugs

**Parabéns! Seu site está online! 🎊**

---

## 📊 TEMPO ESTIMADO

- Upload via Painel: **15-30 minutos**
- Upload via FTP: **10-20 minutos**
- Configurações adicionais: **5-10 minutos**
- Testes: **10-15 minutos**

**TOTAL: 30-60 minutos**

---

## 💡 DICA FINAL

**Não complique!** 

O site HTML já está perfeito. Faça o deploy e coloque no ar.

React pode esperar para uma próxima versão, quando houver necessidade real e orçamento para um desenvolvedor profissional.

**Seu negócio precisa estar online AGORA, não daqui a semanas! 🚀**

# 🤖 Guide Complet - Configuration Discord Bot

Ce guide détaillé t'explique **comment créer et configurer un bot Discord de A à Z**.

---

## 📋 Étapes de Configuration

### 1️⃣ Créer une Application Discord

1. Va sur https://discord.com/developers/applications
2. Clique sur **"New Application"** (en haut à droite)
3. Donne un nom à ton application (ex: "Workly Demo Bot")
4. Accepte les conditions et clique sur **"Create"**

### 2️⃣ Créer le Bot

1. Dans le menu de gauche, clique sur **"Bot"**
2. Clique sur **"Add Bot"** → Confirme avec **"Yes, do it!"**
3. 🎉 Ton bot est créé !

### 3️⃣ Obtenir le Token

1. Dans la section "Bot", trouve **"TOKEN"**
2. Clique sur **"Reset Token"** (si première fois) ou **"Copy"**
3. ⚠️ **GARDE CE TOKEN SECRET !** Ne le partage JAMAIS publiquement
4. Copie-le dans ton `config.json` :
   ```json
   {
     "discord_token": "TON_TOKEN_ICI"
   }
   ```

### 4️⃣ Activer les Intents (CRITIQUE !)

**C'est l'étape la plus importante !**

1. Reste dans l'onglet **"Bot"**
2. Descend jusqu'à **"Privileged Gateway Intents"**
3. Active ces intents :
   - ✅ **PRESENCE INTENT** (optionnel)
   - ✅ **SERVER MEMBERS INTENT** (optionnel)
   - ✅ **MESSAGE CONTENT INTENT** ⚠️ **OBLIGATOIRE !**

4. Clique sur **"Save Changes"** en bas

**❌ Si tu oublies ça, le bot ne pourra PAS lire les messages !**

### 5️⃣ Inviter le Bot sur ton Serveur

1. Dans le menu de gauche, clique sur **"OAuth2"** → **"URL Generator"**

2. **Sélectionne les scopes :**
   - ✅ `bot`
   - ✅ `applications.commands` (optionnel)

3. **Sélectionne les permissions du bot :**
   - ✅ `Read Messages/View Channels`
   - ✅ `Send Messages`
   - ✅ `Send Messages in Threads` (optionnel)
   - ✅ `Embed Links` (optionnel)
   - ✅ `Attach Files` (optionnel)
   - ✅ `Read Message History`
   - ✅ `Use External Emojis` (optionnel)
   - ✅ `Add Reactions` (optionnel)

4. **Copie l'URL générée** en bas de la page

5. **Ouvre l'URL dans ton navigateur**

6. Sélectionne le serveur Discord où tu veux ajouter le bot

7. Clique sur **"Authorize"** (Autoriser)

8. 🎉 Le bot est maintenant sur ton serveur !

---

## 🧪 Test du Bot

### Vérifier que le bot est en ligne

1. Lance le bot : `python bot.py`
2. Dans Discord, vérifie que le bot apparaît **en ligne** (point vert)
3. Si le bot est **hors ligne**, vérifie ton token

### Tester les commandes

Dans un salon Discord où le bot a accès :

```
!workly hello
```

**✅ Si le bot répond :**
→ Tout fonctionne ! 🎉

**❌ Si le bot ne répond pas :**
→ Va à la section "Troubleshooting" ci-dessous

---

## 🐛 Troubleshooting

### Bot en ligne mais ne répond pas

**Causes possibles :**

1. **Message Content Intent désactivé** (le plus fréquent)
   - Retourne dans Developer Portal → Bot → Privileged Gateway Intents
   - Active **"MESSAGE CONTENT INTENT"** ✅
   - **IMPORTANT :** Redémarre le bot après avoir activé cet intent !

2. **Mauvais préfixe de commande**
   - Vérifie que tu tapes bien `!workly hello` (avec espace après "workly")
   - Vérifie le `command_prefix` dans `config.json`

3. **Permissions insuffisantes**
   - Dans Discord → Paramètres du serveur → Rôles
   - Vérifie que le rôle du bot a "Envoyer des messages"

### Bot ne se connecte pas

**"401: Unauthorized"**
→ Token invalide. Copie-le à nouveau depuis Developer Portal.

**"Connection reset" / "Gateway unavailable"**
→ Problème réseau ou Discord a des problèmes. Réessaie plus tard.

### Commandes ne fonctionnent que pour toi

→ Le bot répond uniquement à son créateur ? Vérifie qu'il n'y a pas de filtre dans le code.

---

## 📊 Vérification Complète

Checklist avant de lancer le bot :

```
Configuration Discord Developer Portal :
□ Application créée
□ Bot ajouté à l'application
□ Token copié
□ MESSAGE CONTENT INTENT activé ✅ (CRITIQUE !)
□ Bot invité sur le serveur avec bonnes permissions

Configuration Locale :
□ discord.py installé (pip install discord.py)
□ config.json créé avec le bon token
□ command_prefix configuré (par défaut "!workly ")

Test :
□ Bot lancé (python bot.py)
□ Bot apparaît en ligne dans Discord
□ Test avec : !workly hello
□ Bot répond ✅
```

---

## 🎯 Résumé Visuel

```
Developer Portal
      ↓
1. Create Application
      ↓
2. Add Bot
      ↓
3. Get Token → config.json
      ↓
4. Enable MESSAGE CONTENT INTENT ⚠️ CRITIQUE !
      ↓
5. Generate OAuth2 URL
      ↓
6. Invite Bot to Server
      ↓
Launch: python bot.py
      ↓
Test: !workly hello
      ↓
✅ Bot répond !
```

---

## 📚 Ressources

- **Discord Developer Portal :** https://discord.com/developers/applications
- **discord.py Documentation :** https://discordpy.readthedocs.io/
- **Discord Intents Guide :** https://discord.com/developers/docs/topics/gateway#gateway-intents

---

**🎉 Si tu suis ce guide, ton bot fonctionnera à coup sûr !**

*Workly Public Edition • WorklyHQ*

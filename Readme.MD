# API Resource

Cette API permet de gérer des ressources (documents, fichiers, etc.) avec des fonctionnalités de création, mise à jour et suppression.

## 🔐 Authentification
L'authentification est gérée via un microservice accessible à l'URL :
```
https://rajapi-cop-auth-api.onrender.com/auth/token/
```
L'API utilise un système d'authentification basé sur des tokens (`Bearer Token`).

### 🔹 Connexion
**URL:** `/auth/login/`  
**Méthode:** `POST`

#### Exemple de requête :
```bash
curl -X POST https://rajapi-cop-auth-api.onrender.com/auth/token/ \
     -H "Content-Type: application/json" \
     -d '{"email": "user@example.com", "password": "password123"}'
```
#### Réponse :
```json
{
  "token": "jwt_token_here",
  "user": {
    "email": "user@example.com",
    "username": "user123"
  }
}

## Points de terminaison (Endpoints)

### 1. Création d'une ressource

- **URL**: `/api/resources/`
- **Méthode**: `POST`
- **Authentification**: Requise (Token Microservice)
- **Permissions**: Utilisateur authentifié

**Corps de la requête**:

```json
{
    "title": "Guide d'utilisation",
    "description": "Guide complet pour l'utilisation de l'application",
    "type": "document",
    "published_date": "2025-03-01",
    "status": "published",
    "file": [FICHIER_BINAIRE]
}
```

**Réponse réussie (201 Created)**:

```json
{
    "id": 1,
    "title": "Guide d'utilisation",
    "description": "Guide complet pour l'utilisation de l'application",
    "type": "document",
    "file": "/media/resources/guide.pdf",
    "file_link": "http://example.com/media/resources/guide.pdf",
    "published_date": "2025-03-01",
    "status": "published"
}
```

**Exemple avec curl**:

```bash
curl -X POST \
  http://localhost:8000/api/resources/ \
  -H 'Authorization: Token your_auth_token' \
  -F 'title=Guide d'utilisation' \
  -F 'description=Guide complet pour l'utilisation de l'application' \
  -F 'type=document' \
  -F 'published_date=2025-03-01' \
  -F 'status=published' \
  -F 'file=@/chemin/vers/fichier.pdf'
```

### 2. Consultation d'une ressource

- **URL**: `/api/resources/{resource_id}/`
- **Méthode**: `GET`
- **Authentification**: Requise (Token Microservice)
- **Permissions**: Utilisateur authentifié (auteur de la ressource)

**Réponse réussie (200 OK)**:

```json
{
    "id": 1,
    "title": "Guide d'utilisation",
    "description": "Guide complet pour l'utilisation de l'application",
    "type": "document",
    "file": "/media/resources/guide.pdf",
    "file_link": "http://example.com/media/resources/guide.pdf",
    "published_date": "2025-03-01",
    "status": "published"
}
```

**Exemple avec curl**:

```bash
curl -X GET \
  http://localhost:8000/api/resources/1/ \
  -H 'Authorization: Token your_auth_token'
```

### 3. Mise à jour complète d'une ressource

- **URL**: `/api/resources/{resource_id}/`
- **Méthode**: `PUT`
- **Authentification**: Requise (Token Microservice)
- **Permissions**: Utilisateur authentifié (auteur de la ressource)

**Corps de la requête**:

```json
{
    "title": "Guide d'utilisation mis à jour",
    "description": "Guide complet pour l'utilisation de l'application - Version 2",
    "type": "document",
    "published_date": "2025-03-02",
    "status": "published",
    "file": [FICHIER_BINAIRE_OPTIONNEL]
}
```

**Réponse réussie (200 OK)**:

```json
{
    "id": 1,
    "title": "Guide d'utilisation mis à jour",
    "description": "Guide complet pour l'utilisation de l'application - Version 2",
    "type": "document",
    "file": "/media/resources/guide_v2.pdf",
    "file_link": "http://example.com/media/resources/guide_v2.pdf",
    "published_date": "2025-03-02",
    "status": "published"
}
```

**Exemple avec curl**:

```bash
curl -X PUT \
  http://localhost:8000/api/resources/1/ \
  -H 'Authorization: Token your_auth_token' \
  -F 'title=Guide d'utilisation mis à jour' \
  -F 'description=Guide complet pour l'utilisation de l'application - Version 2' \
  -F 'type=document' \
  -F 'published_date=2025-03-02' \
  -F 'status=published' \
  -F 'file=@/chemin/vers/fichier_v2.pdf'
```

### 4. Mise à jour partielle d'une ressource

- **URL**: `/api/resources/{resource_id}/`
- **Méthode**: `PATCH`
- **Authentification**: Requise (Token Microservice)
- **Permissions**: Utilisateur authentifié (auteur de la ressource)

**Corps de la requête** (exemple de mise à jour partielle):

```json
{
    "title": "Guide d'utilisation mis à jour",
    "status": "draft"
}
```

**Réponse réussie (200 OK)**:

```json
{
    "id": 1,
    "title": "Guide d'utilisation mis à jour",
    "description": "Guide complet pour l'utilisation de l'application - Version 2",
    "type": "document",
    "file": "/media/resources/guide_v2.pdf",
    "file_link": "http://example.com/media/resources/guide_v2.pdf",
    "published_date": "2025-03-02",
    "status": "draft"
}
```

**Exemple avec curl**:

```bash
curl -X PATCH \
  http://localhost:8000/api/resources/1/ \
  -H 'Authorization: Token your_auth_token' \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "Guide d'utilisation mis à jour",
    "status": "draft"
  }'
```

### 5. Suppression d'une ressource

- **URL**: `/api/resources/{resource_id}/`
- **Méthode**: `DELETE`
- **Authentification**: Requise (Token Microservice)
- **Permissions**: Utilisateur authentifié (auteur de la ressource)

**Réponse réussie (204 No Content)**:
Pas de contenu retourné

**Exemple avec curl**:

```bash
curl -X DELETE \
  http://localhost:8000/api/resources/1/ \
  -H 'Authorization: Token your_auth_token'
```

## Modèle de données

Le modèle `Resource` comprend les champs suivants:

| Champ | Type | Description |
|-------|------|-------------|
| id | Integer | Identifiant unique (généré automatiquement) |
| title | CharField | Titre de la ressource (max 100 caractères) |
| description | TextField | Description détaillée de la ressource |
| type | CharField | Type de ressource (document, image, etc.) |
| file | FileField | Fichier uploadé |
| published_date | DateField | Date de publication |
| author | ForeignKey | Auteur (utilisateur Django) |
| status | CharField | Statut ('draft' ou 'published') |
| created_at | DateTimeField | Date de création (automatique) |
| updated_at | DateTimeField | Date de dernière mise à jour (automatique) |


## Notes d'utilisation

- Les fichiers uploadés sont stockés dans le dossier `MEDIA_ROOT/resources/`.
- Seul l'auteur d'une ressource peut la consulter, modifier ou la supprimer.
- L'authentification se fait via un token de microservice.
- Pour les mises à jour partielles, utilisez la méthode PATCH au lieu de PUT.
- Pour obtenir l'URL complète d'un fichier uploadé, utilisez le champ `file_link` dans la réponse.
# Infrastructure Health Checker

Bot de vérification d'infrastructure déclaratif. Les checks sont définis en YAML, les rapports générés en JSON et Markdown, l'exécution automatisée via GitHub Actions (schedule toutes les 6h).

Inspiré de workflows de monitoring réalisés en production (cybersécurité).

## Checks supportés

| Type | Vérifie | Exemple |
|---|---|---|
| HTTP | Code retour + temps de réponse | `https://github.com` → 200 en < 10s |
| TLS | Expiration certificat | `github.com:443` → expire dans > 30 jours |
| TCP | Port ouvert + latence | `github.com:22` → accessible |
| DNS | Résolution de domaine | `github.com` → résout correctement |

## Dernier rapport

Consultable dans [`reports/latest.md`](reports/latest.md), mis à jour automatiquement par GitHub Actions.

## Configuration

Les checks sont déclarés dans `config.yml` :

```yaml
checks:
  http:
    - name: GitHub
      url: https://github.com
      expected_status: 200
      timeout: 10

  tls:
    - name: GitHub TLS
      host: github.com
      port: 443
      warn_days: 30

  tcp:
    - name: GitHub SSH
      host: github.com
      port: 22
      timeout: 5

  dns:
    - name: GitHub DNS
      domain: github.com
      nameserver: 8.8.8.8
```

## Utilisation locale

```bash
pip install -r requirements.txt
python checker.py
cat reports/latest.md
```

## Docker

```bash
docker build -t infra-health-checker .
docker run -v $(pwd)/reports:/app/reports infra-health-checker
```

## Pipeline GitHub Actions

Le workflow `.github/workflows/check.yml` :

- S'exécute toutes les 6h (`cron`) ou manuellement (`workflow_dispatch`)
- Lance les checks
- Commit automatiquement les rapports dans `reports/`

## Ce que ce projet démontre

- Monitoring déclaratif (config YAML → checks → rapports)
- Vérifications multi-protocoles (HTTP, TLS, TCP, DNS)
- CI/CD schedule (GitHub Actions cron)
- Auto-commit de rapports (git ops)
- Conteneurisation (Docker)
# Infrastructure Health Report

**Date** : 2026-11-21T14:09:34.884187+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.105s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.164s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.102s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 67 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 70 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.014s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.014s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 48.202.91.176 |

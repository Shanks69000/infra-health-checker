# Infrastructure Health Report

**Date** : 2026-07-12T19:00:53.037458+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.15s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.105s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.06s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 80 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 84 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.016s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.002s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.113.3 |

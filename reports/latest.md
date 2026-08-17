# Infrastructure Health Report

**Date** : 2026-08-17T18:33:41.648625+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.054s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.09s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.043s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 44 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 85 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.002s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.002s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.112.4 |

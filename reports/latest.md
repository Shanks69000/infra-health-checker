# Infrastructure Health Report

**Date** : 2026-11-18T00:28:22.208942+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.051s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.136s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.041s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 70 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 73 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.013s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.006s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.112.3 |

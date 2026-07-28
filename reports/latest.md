# Infrastructure Health Report

**Date** : 2026-07-28T08:28:33.302717+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.197s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.197s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.112s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 64 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 68 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.04s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.02s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.3 |

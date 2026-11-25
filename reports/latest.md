# Infrastructure Health Report

**Date** : 2026-11-25T16:44:33.406202+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.371s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.191s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.112s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 63 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 66 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.055s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.002s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.113.4 |

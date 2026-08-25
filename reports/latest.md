# Infrastructure Health Report

**Date** : 2026-08-25T12:40:09.604030+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.342s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.412s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.291s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 36 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 78 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.052s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.033s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.113.3 |

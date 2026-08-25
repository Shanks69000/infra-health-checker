# Infrastructure Health Report

**Date** : 2026-08-25T06:39:56.912656+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.137s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.169s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.1s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 36 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 78 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.018s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.002s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.116.3 |

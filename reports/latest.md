# Infrastructure Health Report

**Date** : 2026-07-03T13:56:41.007922+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.164s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.265s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.115s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 89 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 72 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.024s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.014s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.113.4 |

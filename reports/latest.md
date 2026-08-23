# Infrastructure Health Report

**Date** : 2026-08-23T12:32:41.622506+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.165s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.176s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.116s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 38 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 80 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.035s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.018s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.3 |

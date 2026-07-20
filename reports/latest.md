# Infrastructure Health Report

**Date** : 2026-07-20T13:58:53.819459+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.177s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.667s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.147s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 72 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 76 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.026s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.018s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.113.4 |

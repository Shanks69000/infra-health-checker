# Infrastructure Health Report

**Date** : 2026-09-21T21:40:50.912327+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.166s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.214s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.131s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 69 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 71 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.032s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.021s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.4 |

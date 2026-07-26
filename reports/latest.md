# Infrastructure Health Report

**Date** : 2026-07-26T08:21:35.682989+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.332s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.241s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.289s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 66 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 70 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.051s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.011s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.113.3 |

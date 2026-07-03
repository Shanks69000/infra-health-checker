# Infrastructure Health Report

**Date** : 2026-07-03T19:16:13.520995+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.04s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.202s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.111s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 89 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 71 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.002s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.002s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.113.3 |

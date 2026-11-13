# Infrastructure Health Report

**Date** : 2026-11-13T04:56:03.312484+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.046s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.218s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.084s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 75 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 78 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.006s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.007s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.3 |

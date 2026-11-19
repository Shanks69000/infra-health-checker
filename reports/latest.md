# Infrastructure Health Report

**Date** : 2026-11-19T15:11:55.965834+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.021s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.057s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.019s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 69 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 72 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.002s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.007s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.4 |

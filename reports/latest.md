# Infrastructure Health Report

**Date** : 2026-09-21T11:55:19.107882+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.117s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.347s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.063s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 69 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 72 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.02s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.002s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.4 |

# Infrastructure Health Report

**Date** : 2026-10-12T04:11:21.310542+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.328s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.212s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.101s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 48 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 89 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.052s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.005s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.113.3 |

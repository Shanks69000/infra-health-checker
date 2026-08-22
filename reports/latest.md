# Infrastructure Health Report

**Date** : 2026-08-22T06:33:38.939540+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.31s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.251s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.155s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 39 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 81 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.046s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.011s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.112.3 |

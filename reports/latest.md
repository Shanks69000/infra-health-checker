# Infrastructure Health Report

**Date** : 2026-07-16T19:04:34.465633+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.059s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.14s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.072s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 76 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 80 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.006s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.006s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.4 |

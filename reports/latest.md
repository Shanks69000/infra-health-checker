# Infrastructure Health Report

**Date** : 2026-10-25T15:30:03.036816+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.326s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.209s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.14s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 35 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 75 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.05s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.001s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.3 |

# Infrastructure Health Report

**Date** : 2026-07-06T15:25:14.909080+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.18s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.229s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.139s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 86 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 68 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.026s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.014s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.112.4 |

# Infrastructure Health Report

**Date** : 2026-09-18T20:21:13.911445+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.032s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.091s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.052s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 72 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 74 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.002s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.003s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.112.4 |

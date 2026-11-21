# Infrastructure Health Report

**Date** : 2026-11-21T22:44:26.289035+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.175s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.288s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.149s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 67 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 69 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.027s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.014s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.112.3 |

# Infrastructure Health Report

**Date** : 2026-08-14T12:58:25.986183+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.062s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 1.095s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.185s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 47 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 89 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.006s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.005s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.116.3 |

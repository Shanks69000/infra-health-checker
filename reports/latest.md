# Infrastructure Health Report

**Date** : 2026-08-20T06:39:14.486397+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.06s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.206s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.071s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 41 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 83 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.006s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.006s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.112.4 |

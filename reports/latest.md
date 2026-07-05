# Infrastructure Health Report

**Date** : 2026-07-05T08:48:43.105417+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.329s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.254s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.183s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 87 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 70 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.042s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.015s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.112.3 |

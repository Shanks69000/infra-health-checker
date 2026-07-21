# Infrastructure Health Report

**Date** : 2026-07-21T19:16:18.787862+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.176s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.231s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.119s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 71 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 75 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.032s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.023s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.112.3 |

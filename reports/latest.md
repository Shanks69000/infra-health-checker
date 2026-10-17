# Infrastructure Health Report

**Date** : 2026-10-17T20:03:05.045188+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.2s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.186s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.088s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 43 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 83 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.032s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.021s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.112.4 |

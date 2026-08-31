# Infrastructure Health Report

**Date** : 2026-08-31T03:25:56.410261+00:00

**Résultat** : 7/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.062s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.117s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.105s |
| GitHub TLS | tls | github.com:443 | ❌ | Expire dans 30 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 72 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.006s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.006s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.113.3 |

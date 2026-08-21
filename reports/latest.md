# Infrastructure Health Report

**Date** : 2026-08-21T18:31:26.164246+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.318s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.232s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.093s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 40 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 81 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.053s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.003s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.113.4 |

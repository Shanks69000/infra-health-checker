# Infrastructure Health Report

**Date** : 2026-10-14T11:07:11.622986+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.231s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.254s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.141s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 46 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 87 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.034s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.017s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.112.3 |

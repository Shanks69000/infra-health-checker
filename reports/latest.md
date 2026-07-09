# Infrastructure Health Report

**Date** : 2026-07-09T09:33:52.919558+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.325s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.214s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.151s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 83 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 87 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.06s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.002s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.112.3 |

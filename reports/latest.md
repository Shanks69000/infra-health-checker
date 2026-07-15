# Infrastructure Health Report

**Date** : 2026-07-15T13:37:34.944824+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.137s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.157s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.134s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 77 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 81 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.019s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.001s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.116.3 |

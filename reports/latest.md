# Infrastructure Health Report

**Date** : 2026-07-02T19:19:56.109422+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.136s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.145s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.107s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 31 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 72 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.019s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.001s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.116.4 |

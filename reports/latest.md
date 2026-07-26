# Infrastructure Health Report

**Date** : 2026-07-26T19:06:03.720829+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.344s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.22s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.138s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 66 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 70 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.05s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.003s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.113.3 |

# Infrastructure Health Report

**Date** : 2026-10-21T16:33:24.632014+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.319s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.248s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.097s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 39 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 79 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.05s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.003s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.3 |

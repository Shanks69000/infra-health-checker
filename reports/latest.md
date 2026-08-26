# Infrastructure Health Report

**Date** : 2026-08-26T12:43:58.043429+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.338s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.258s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.14s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 35 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 77 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.05s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.002s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.4 |

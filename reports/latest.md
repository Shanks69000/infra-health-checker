# Infrastructure Health Report

**Date** : 2026-09-30T11:52:28.892610+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.056s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.289s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.145s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 60 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 63 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.005s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.005s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.116.3 |

# Infrastructure Health Report

**Date** : 2026-08-09T12:41:50.430045+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.322s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.193s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.147s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 52 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 56 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.054s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.003s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.3 |

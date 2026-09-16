# Infrastructure Health Report

**Date** : 2026-09-16T10:48:02.498105+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.063s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.18s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.067s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 74 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 77 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.006s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.006s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.3 |
